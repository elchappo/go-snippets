# go-snippets

### Remove Duplicates From Sorted Array
```go
func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return  0
    }

    writeIndex := 1
    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[i-1] {
            nums[writeIndex] = nums[i]
            writeIndex++
        } 
    }
    return writeIndex
}
```

### Remove Element
```go
func removeElement(nums []int, val int) int {
    if len(nums) == 0 {
        return 0
    }

    nIndex := 0
    for _, num := range nums {
        if num != val {
            nums[nIndex] = num
            nIndex++
        }
    }
    return nIndex
}
```
### Concatenation of Array
```go
func getConcatenation(nums []int) []int {
    return append(nums, nums...)
}
```
### Valid Parentheses
```go
func isValid(s string) bool {
    stack := []rune{}
    pairs := map[rune]rune{
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for _, ch := range s {
        if expected, isOpen := pairs[ch]; isOpen {
            // opening → push expected closing
            stack = append(stack, expected)
        } else {
            // closing → must match stack top
            if len(stack) == 0 || stack[len(stack)-1] != ch {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack) == 0
}
```
### Minimum Stack
```go
type MinStack struct {
    stack []int
    min []int
}

func Constructor() MinStack {
    return MinStack{
    }
}

func (this *MinStack) Push(val int) {
    this.stack = append(this.stack, val)
    
    if len(this.min) == 0 || val <= this.min[len(this.min)-1] {
        this.min = append(this.min, val)
    } else {
        this.min = append(this.min, this.min[len(this.min)-1])
    }
}

func (this *MinStack) Pop() {
    if len(this.stack) == 0 {
        return
    }
    this.stack = this.stack[:len(this.stack)-1]
    this.min = this.min[:len(this.min)-1]
}

func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
    return this.min[len(this.min)-1]
}
```
### Reverse Linked List !
https://neetcode.io/solutions/reverse-linked-list
```go
func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }

    newHead := head
    if head.Next != nil {
        newHead = reverseList(head.Next)
        head.Next.Next = head
    }
    head.Next = nil

    return newHead
}
```
### Merge Two Sorted Linked Lists
```go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
    dummy := &ListNode{}
    node := dummy

    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            node.Next = list1
            list1 = list1.Next
        } else {
            node.Next = list2
            list2 = list2.Next
        }
        node = node.Next
    }

    node.Next = list1
    if list1 == nil {
        node.Next = list2
    }

    return dummy.Next
}

```
### Design Linked List
```Go
package main

type ListNode struct {
    Val  int
    Next *ListNode
}

type MyLinkedList struct {
    head *ListNode
    size int
}

func Constructor() MyLinkedList {
    return MyLinkedList{
        head: &ListNode{Next: nil},
        size: 0,
    }
}

func (this *MyLinkedList) getPrev(index int) *ListNode {
    cur := this.head
    for i := 0; i < index; i++ {
        cur = cur.Next
    }
    return cur
}

func (this *MyLinkedList) Get(index int) int {
    if index < 0 || index >= this.size {
        return -1
    }
    return this.getPrev(index).Next.Val
}

func (this *MyLinkedList) AddAtHead(val int) {
    this.AddAtIndex(0, val)
}

func (this *MyLinkedList) AddAtTail(val int) {
    this.AddAtIndex(this.size, val)
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
    if index < 0 || index > this.size {
        return
    }
    prev := this.getPrev(index)
    node := &ListNode{Val: val, Next: prev.Next}
    prev.Next = node
    this.size++
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
    if index < 0 || index >= this.size {
        return
    }
    prev := this.getPrev(index)
    prev.Next = prev.Next.Next
    this.size--
}

```
### Design Browser History
```Go
type BrowserHistory struct {
    history[]string
    index int
}


func Constructor(homepage string) BrowserHistory {
    return BrowserHistory {
        history: []string{homepage},
        index: 0,
    }
}


func (this *BrowserHistory) Visit(url string)  {
    this.history = this.history[:this.index+1]
    this.history = append(this.history, url)
    this.index++
}


func (this *BrowserHistory) Back(steps int) string {
    if this.index - steps < 0 {
        this.index = 0 
    }else{
        this.index -= steps
    }
    return this.history[this.index]
}


func (this *BrowserHistory) Forward(steps int) string {
    if this.index + steps >= len(this.history) {
        this.index = len(this.history)-1
    } else{
        this.index += steps
    }
    return this.history[this.index]
}

```
### Number of Students Unable to Eat Lunch
```Go
func countStudents(students []int, sandwiches []int) int {
    count := []int{0,0 }
    for _, s := range students {
        count[s]++
    }

    for _, sandwitch := range sandwiches {
        if count[sandwitch] ==0 {
            break
        }
        count[sandwitch]--
    }
    return count[0] + count[1]
}
```

### Implement Stack Using Queues
```Go
type MyStack struct {
    q []int
}

func Constructor() MyStack {
    return MyStack{q: []int{}}
}

func (this *MyStack) Push(x int) {
    this.q = append(this.q, x)
    for i := 0; i < len(this.q)-1; i++ {
        this.q = append(this.q, this.q[0])
        this.q = this.q[1:]
    }
}

func (this *MyStack) Pop() int {
    top := this.q[0]
    this.q = this.q[1:]
    return top
}

func (this *MyStack) Top() int {
    return this.q[0]
}

func (this *MyStack) Empty() bool {
    return len(this.q) == 0
}
```

### Climbing Stairs - Fibonaci - DFS - Depth First Search
```GO
func climbStairs(n int) int {
    if n <= 2 {
        return n
    }
    first, second := 1, 2
    for i := 3; i <= n; i++ {
        first, second = second, first+second
    }
    return second
}
```
```Go
func climbStairs(n int) int {
    var dfs func(i int) int
    dfs = func(i int) int {
        if i >= n {
            if i == n {
                return 1
            }
            return 0
        }
        return dfs(i + 1) + dfs(i + 2)
    }
    return dfs(0)
}
```

### Insertion Sort - stable sorting O(n2)

![Insertion Sort](https://blog.boot.dev/img/800/insertionsort.gif)

```Go
func InsertionSort(arr []int) []int {
    for i := 1; i < len(arr); i++ {
        j := i
        for j > 0 && arr[j] < arr[j-1] {
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j--
        }
    }
    return arr
}
```
```Go
func insertionSort(pairs []Pair) [][]Pair {
	// Result holds snapshots after each insertion
	result := make([][]Pair, 0, len(pairs))

	// Work on a copy so original isn't modified
	arr := make([]Pair, len(pairs))
	copy(arr, pairs)

	for i := 0; i < len(arr); i++ {
		// Perform insertion step
		j := i
		for j > 0 && arr[j-1].Key > arr[j].Key {
			// Swap (stable because we only swap when strictly greater)
			arr[j], arr[j-1] = arr[j-1], arr[j]
			j--
		}

		// Record snapshot (copy slice to avoid later overwrite)
		snapshot := make([]Pair, len(arr))
		copy(snapshot, arr)
		result = append(result, snapshot)
	}

	return result
}
```
### Merge Sort - Divide & Conquer O(nlog n)

![Merge Sort](https://blog.boot.dev/img/800/merge_sort_gif.gif)

```Go
package main

func mergeSort(items []int) []int {
    if len(items) < 2 {
        return items
    }
    first := mergeSort(items[:len(items)/2])
    second := mergeSort(items[len(items)/2:])
    return merge(first, second)
}

func merge(a []int, b []int) []int {
    final := []int{}
    i := 0
    j := 0
    for i < len(a) && j < len(b) {
        if a[i] < b[j] {
            final = append(final, a[i])
            i++
        } else {
            final = append(final, b[j])
            j++
        }
    }
    for ; i < len(a); i++ {
        final = append(final, a[i])
    }
    for ; j < len(b); j++ {
        final = append(final, b[j])
    }
    return final
}
```
```Go
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    nodes := make([]int, 0)

    for _, list := range lists {
        curr := list
        for curr != nil {
            nodes = append(nodes, curr.Val)
            curr = curr.Next
        }
    }

    sort.Ints(nodes)

    dummy := &ListNode{Val: 0}
    curr := dummy

    for _, val := range nodes {
        curr.Next = &ListNode{Val: val}
        curr = curr.Next
    }

    return dummy.Next
}
```