## 1. 如何控制 sync.WaitGroup 的并发数
通常我们要批量批量并发处理某些任务的时候，我们大部分情况都是通过 sync.WaitGroup 来实现的。例如：
```go
func main() {
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			// 处理任务
		}(i)
	}
	wg.Wait()
}
```
但是这样会存在一个问题，就是如果并发的任务数量很多，会导致内存占用过高，甚至导致内存溢出。为此，我们可以通过控制并发数的方式来解决这个问题。例如：
```go
func main() {
	var wg sync.WaitGroup
    //  最大并发10个任务
	sem := make(chan struct{}, 10)

	for i := 0; i < 100; i++ {
		wg.Add(1)
        // 等待semaphore信号量
        sem <- struct{}{}

		go func(i int) {
			defer wg.Done()
            defer func() { <-sem }()
			// 处理任务
		}(i)
	}
	wg.Wait()
}
```