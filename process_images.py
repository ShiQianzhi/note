import os
import re
import shutil
import urllib.request
from datetime import datetime
from pathlib import Path

NOTE_ROOT = "/Users/bytedance/note"
IMAGE_DIR = os.path.join(NOTE_ROOT, "data", "images")
FAILED_LOG = os.path.join(NOTE_ROOT, "image_processing_failed.log")

IMAGE_PATTERN = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)', re.IGNORECASE)


def get_timestamp():
    return datetime.now().strftime("%Y%m%d%H%M%S")


def extract_images_from_markdown(content):
    matches = IMAGE_PATTERN.findall(content)
    return matches


def is_url(path):
    return path.lower().startswith(('http://', 'https://', 'ftp://'))


def get_file_extension(url_or_path):
    if is_url(url_or_path):
        parsed = urllib.parse.urlparse(url_or_path)
        return os.path.splitext(parsed.path)[1] or '.jpg'
    return os.path.splitext(url_or_path)[1] or '.jpg'


def generate_new_filename(article_name, original_ext, index=0):
    timestamp = get_timestamp()
    safe_name = re.sub(r'[\\/:*?"<>|]', '_', article_name)
    safe_name = safe_name.strip()
    if not safe_name:
        safe_name = "unknown"
    if index > 0:
        return f"{safe_name}-{timestamp}-{index}{original_ext}"
    return f"{safe_name}-{timestamp}{original_ext}"


def download_image(url, save_path):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            with open(save_path, 'wb') as f:
                f.write(response.read())
        return True
    except Exception as e:
        print(f"下载失败 {url}: {e}")
        return False


def process_markdown_file(filepath):
    failed_entries = []
    article_name = os.path.splitext(os.path.basename(filepath))[0]
    file_dir = os.path.dirname(filepath)
    image_index = 0

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    images = extract_images_from_markdown(content)
    if not images:
        return failed_entries

    lines = content.split('\n')
    new_lines = []
    line_number = 0

    for line in lines:
        line_number += 1
        matches = list(IMAGE_PATTERN.finditer(line))
        
        if not matches:
            new_lines.append(line)
            continue

        new_line = line
        offset = 0
        
        for match in matches:
            image_index += 1
            alt_text = match.group(1)
            original_path = match.group(2)
            start = match.start() + offset
            end = match.end() + offset

            if is_url(original_path):
                ext = get_file_extension(original_path)
                new_filename = generate_new_filename(article_name, ext, image_index)
                save_path = os.path.join(IMAGE_DIR, new_filename)
                
                if download_image(original_path, save_path):
                    new_path = f"data/images/{new_filename}"
                    new_image_ref = f"![{alt_text}]({new_path})"
                    new_line = new_line[:start] + new_image_ref + new_line[end:]
                    offset += len(new_image_ref) - len(match.group(0))
                else:
                    failed_entries.append({
                        'file_path': filepath,
                        'line_number': line_number,
                        'original_ref': match.group(0)
                    })
                    new_line = new_line[:start] + new_line[end:]
                    offset -= len(match.group(0))
            else:
                local_path = os.path.join(file_dir, original_path)
                local_path = os.path.normpath(local_path)
                
                if os.path.isfile(local_path):
                    ext = get_file_extension(local_path)
                    new_filename = generate_new_filename(article_name, ext, image_index)
                    save_path = os.path.join(IMAGE_DIR, new_filename)
                    
                    if local_path != save_path:
                        shutil.copy2(local_path, save_path)
                    
                    new_path = f"data/images/{new_filename}"
                    new_image_ref = f"![{alt_text}]({new_path})"
                    new_line = new_line[:start] + new_image_ref + new_line[end:]
                    offset += len(new_image_ref) - len(match.group(0))
                else:
                    failed_entries.append({
                        'file_path': filepath,
                        'line_number': line_number,
                        'original_ref': match.group(0)
                    })
                    new_line = new_line[:start] + new_line[end:]
                    offset -= len(match.group(0))

        new_lines.append(new_line)

    new_content = '\n'.join(new_lines)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return failed_entries


def main():
    os.makedirs(IMAGE_DIR, exist_ok=True)
    
    if os.path.exists(FAILED_LOG):
        os.remove(FAILED_LOG)
    
    all_failed = []
    
    for root, dirs, files in os.walk(NOTE_ROOT):
        dirs[:] = [d for d in dirs if d not in ('data', '.git', '__pycache__')]
        
        for file in files:
            if file.lower().endswith('.md'):
                filepath = os.path.join(root, file)
                print(f"处理文件: {filepath}")
                failed = process_markdown_file(filepath)
                all_failed.extend(failed)
    
    if all_failed:
        with open(FAILED_LOG, 'w', encoding='utf-8') as f:
            for entry in all_failed:
                line = f"{entry['file_path']},{entry['line_number']},{entry['original_ref']}\n"
                f.write(line)
        print(f"\n处理完成！共 {len(all_failed)} 个图片处理失败，详情请查看: {FAILED_LOG}")
    else:
        print("\n处理完成！所有图片均已成功处理。")


if __name__ == "__main__":
    main()