# Go Algorithms & Data Structures Reference

🎴 **[View Interactive Flashcards](https://elchappo.github.io/go-snippets/)** - Study these algorithms with an interactive flashcard viewer!

A comprehensive collection of common algorithms and data structures implemented in Go, with complexity analysis, pros/cons, and usage scenarios.

## Table of Contents

- [Getting Started](#getting-started)
- [Array & String Algorithms](#array--string-algorithms)
- [Stack & Queue](#stack--queue)
- [Linked Lists](#linked-lists)
- [Sorting Algorithms](#sorting-algorithms)
- [Search Algorithms](#search-algorithms)
- [Binary Search Trees](#binary-search-trees)
- [Tree Traversal & Operations](#tree-traversal--operations)
- [Dynamic Programming](#dynamic-programming)

---

## Getting Started

### Running Tests
```bash
go test -v
```

### Basic Test Structure
```go
package main

import "testing"

func TestAdd(t *testing.T) {
    tests := []struct {
        name     string
        a        int
        b        int
        expected int
    }{
        {"Add positive numbers", 2, 3, 5},
        {"Add with zero", 10, 0, 10},
        {"Add negative numbers", -5, -3, -8},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := Add(tt.a, tt.b)
            if result != tt.expected {
                t.Errorf("Add(%d, %d) = %d; expected %d", tt.a, tt.b, result, tt.expected)
            }
        })
    }
}
```

---

## Array & String Algorithms

### Remove Duplicates From Sorted Array

**Description**: Removes duplicate elements from a sorted array in-place using two-pointer technique.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

**Pros**:
- In-place modification (no extra space)
- Single pass through array
- Efficient for sorted arrays

**Cons**:
- Only works on sorted arrays
- Modifies original array

**Usage**: When you need to remove duplicates from a sorted array without using extra space.

```go
func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
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

**Description**: Removes all instances of a specific value from an array in-place.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

**Pros**:
- In-place modification
- Works on unsorted arrays
- Simple implementation

**Cons**:
- Modifies original array
- Order may not be preserved

**Usage**: When you need to filter out specific values from an array without allocating new memory.

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

**Description**: Creates a new array by concatenating the original array with itself.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

**Pros**:
- Simple and readable
- Built-in Go append function

**Cons**:
- Creates new array (memory allocation)

**Usage**: When you need to duplicate array elements in sequence.

```go
func getConcatenation(nums []int) []int {
    return append(nums, nums...)
}
```

---

## Stack & Queue

### Valid Parentheses

**Description**: Validates if a string of brackets is properly balanced using a stack.

**Time Complexity**: O(n)  
**Space Complexity**: O(n)

**Pros**:
- Handles multiple bracket types
- Clear and maintainable
- Efficient single-pass solution

**Cons**:
- Requires extra space for stack

**Usage**: Validating balanced expressions in compilers, parsers, or mathematical expressions.

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
            stack = append(stack, expected)
        } else {
            if len(stack) == 0 || stack[len(stack)-1] != ch {
                return false
            }
            stack = stack[:len(stack)-1]
        }
    }

    return len(stack) == 0
}
```

### Min Stack

**Description**: Stack that supports push, pop, top, and retrieving minimum element in O(1) time.

**Time Complexity**: O(1) for all operations  
**Space Complexity**: O(n)

**Pros**:
- Constant time minimum retrieval
- All standard stack operations remain O(1)

**Cons**:
- Uses double the space (two stacks)

**Usage**: When you need to track the minimum value in a stack efficiently (e.g., stock price tracking).

```go
type MinStack struct {
    stack []int
    min   []int
}

func Constructor() MinStack {
    return MinStack{}
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

### Implement Stack Using Queues

**Description**: Implements a LIFO stack using FIFO queue operations.

**Time Complexity**: O(n) for push, O(1) for pop/top  
**Space Complexity**: O(n)

**Pros**:
- Demonstrates data structure conversion
- Educational value

**Cons**:
- Push operation is O(n)
- Less efficient than native stack

**Usage**: Academic purposes or when only queue operations are available.

```go
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

### Design Browser History

**Description**: Simulates browser navigation with back/forward functionality.

**Time Complexity**: O(1) for all operations  
**Space Complexity**: O(n) where n is number of visited pages

**Pros**:
- Simple array-based implementation
- Efficient navigation operations
- Clear state management

**Cons**:
- Stores all history in memory

**Usage**: Browser history, undo/redo systems, navigation stacks.

```go
type BrowserHistory struct {
    history []string
    index   int
}

func Constructor(homepage string) BrowserHistory {
    return BrowserHistory{
        history: []string{homepage},
        index:   0,
    }
}

func (this *BrowserHistory) Visit(url string) {
    this.history = this.history[:this.index+1]
    this.history = append(this.history, url)
    this.index++
}

func (this *BrowserHistory) Back(steps int) string {
    if this.index-steps < 0 {
        this.index = 0
    } else {
        this.index -= steps
    }
    return this.history[this.index]
}

func (this *BrowserHistory) Forward(steps int) string {
    if this.index+steps >= len(this.history) {
        this.index = len(this.history) - 1
    } else {
        this.index += steps
    }
    return this.history[this.index]
}
```

### Number of Students Unable to Eat Lunch

**Description**: Counts students who cannot get their preferred sandwich using counting approach.

**Time Complexity**: O(n)  
**Space Complexity**: O(1)

**Pros**:
- Efficient counting solution
- No simulation needed
- Constant extra space

**Cons**:
- Less intuitive than simulation

**Usage**: Queue matching problems, resource allocation scenarios.

```go
func countStudents(students []int, sandwiches []int) int {
    count := []int{0, 0}
    for _, s := range students {
        count[s]++
    }

    for _, sandwich := range sandwiches {
        if count[sandwich] == 0 {
            break
        }
        count[sandwich]--
    }
    return count[0] + count[1]
}
```

---

## Linked Lists

### Reverse Linked List

**Description**: Reverses a singly linked list using recursion.

**Time Complexity**: O(n)  
**Space Complexity**: O(n) due to recursion stack

**Pros**:
- Clean recursive solution
- Easy to understand

**Cons**:
- Uses call stack space
- Risk of stack overflow for very long lists

**Usage**: List reversal, interview questions. [NeetCode Solution](https://neetcode.io/solutions/reverse-linked-list)

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

**Description**: Merges two sorted linked lists into one sorted list.

**Time Complexity**: O(n + m)  
**Space Complexity**: O(1)

**Pros**:
- In-place merging
- Maintains sorted order
- Efficient single pass

**Cons**:
- Modifies original lists

**Usage**: Merge sort for linked lists, combining sorted data streams.

```go
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

**Description**: Custom implementation of a singly linked list with common operations.

**Time Complexity**: O(n) for get/add/delete at index, O(1) for add at head  
**Space Complexity**: O(1) per operation

**Pros**:
- Full control over implementation
- Efficient head operations
- Tracks size for validation

**Cons**:
- Linear time for index-based operations
- More complex than using built-in structures

**Usage**: When you need a custom linked list implementation with specific requirements.

```go
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

---

## Sorting Algorithms

### Comparison Table

| Algorithm      | Time (Best) | Time (Avg) | Time (Worst) | Space    | Stable |
| -------------- | ----------- | ---------- | ------------ | -------- | ------ |
| Insertion Sort | O(n)        | O(n²)      | O(n²)        | O(1)     | ✓      |
| Merge Sort     | O(n log n)  | O(n log n) | O(n log n)   | O(n)     | ✓      |
| Quick Sort     | O(n log n)  | O(n log n) | O(n²)        | O(log n) | ✗      |
| Bucket Sort    | O(n)        | O(n)       | O(n)         | O(n)     | ✗      |

### Insertion Sort

![Insertion Sort](https://blog.boot.dev/img/800/insertionsort.gif)

**Description**: Builds sorted array one element at a time by inserting elements into their correct position.

**Time Complexity**: O(n²) average, O(n) best case  
**Space Complexity**: O(1)

**Pros**:
- Simple implementation
- Efficient for small datasets
- Stable sort
- In-place sorting
- Adaptive (efficient for nearly sorted data)

**Cons**:
- Quadratic time for large datasets
- Not suitable for large arrays

**Usage**: Small datasets, nearly sorted data, or when simplicity is preferred over performance.

```go
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

**With Snapshots** (for visualization):
```go
func insertionSort(pairs []Pair) [][]Pair {
    result := make([][]Pair, 0, len(pairs))
    arr := make([]Pair, len(pairs))
    copy(arr, pairs)

    for i := 0; i < len(arr); i++ {
        j := i
        for j > 0 && arr[j-1].Key > arr[j].Key {
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j--
        }
        snapshot := make([]Pair, len(arr))
        copy(snapshot, arr)
        result = append(result, snapshot)
    }
    return result
}
```

### Merge Sort

![Merge Sort](https://blog.boot.dev/img/800/merge_sort_gif.gif)

**Description**: Divide-and-conquer algorithm that recursively splits array, sorts halves, and merges them.

**Time Complexity**: O(n log n) in all cases  
**Space Complexity**: O(n)

**Pros**:
- Guaranteed O(n log n) performance
- Stable sort
- Predictable performance
- Good for linked lists

**Cons**:
- Requires O(n) extra space
- Not in-place
- Slower than quicksort in practice for arrays

**Usage**: When stable sort is required, sorting linked lists, or when consistent performance is critical.

```go
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

**Merge K Sorted Lists** (using merge sort approach):
```go
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

### Quick Sort

![Quick Sort](https://upload.wikimedia.org/wikipedia/commons/f/fe/Quicksort.gif)

**Description**: Divide-and-conquer algorithm using pivot partitioning for in-place sorting.

**Time Complexity**: O(n log n) average, O(n²) worst case  
**Space Complexity**: O(log n) for recursion stack

**Pros**:
- Fast average case performance
- In-place sorting (low memory)
- Cache-friendly
- Often fastest in practice

**Cons**:
- Unstable sort
- Worst case O(n²) (rare with good pivot selection)
- Not ideal for nearly sorted data

**Usage**: General-purpose sorting when stability isn't required and average-case performance matters.

```go
func partition(arr []int, low, high int) ([]int, int) {
    pivot := arr[high]
    i := low
    for j := low; j < high; j++ {
        if arr[j] < pivot {
            arr[i], arr[j] = arr[j], arr[i]
            i++
        }
    }
    arr[i], arr[high] = arr[high], arr[i]
    return arr, i
}

func quickSort(arr []int, low, high int) []int {
    if low < high {
        var p int
        arr, p = partition(arr, low, high)
        arr = quickSort(arr, low, p-1)
        arr = quickSort(arr, p+1, high)
    }
    return arr
}

func quickSortStart(arr []int) []int {
    return quickSort(arr, 0, len(arr)-1)
}
```

**Alternative Implementation**:
```go
func QuickSort(arr []int, start, end int) {
    if start >= end {
        return
    }

    pivotValue := arr[end]
    smallerIndex := start

    for currentIndex := start; currentIndex < end; currentIndex++ {
        if arr[currentIndex] < pivotValue {
            arr[smallerIndex], arr[currentIndex] = arr[currentIndex], arr[smallerIndex]
            smallerIndex++
        }
    }

    arr[smallerIndex], arr[end] = arr[end], arr[smallerIndex]

    QuickSort(arr, start, smallerIndex-1)
    QuickSort(arr, smallerIndex+1, end)
}
```

### Bucket Sort

**Description**: Distributes elements into buckets, then sorts each bucket (works for limited value ranges).

**Time Complexity**: O(n) when values are uniformly distributed  
**Space Complexity**: O(n)

**Pros**:
- Linear time for specific use cases
- Simple implementation for limited ranges
- Efficient for uniformly distributed data

**Cons**:
- Only works for limited value ranges
- Not general-purpose
- Unstable
- Requires knowing value range beforehand

**Usage**: Sorting data with known, limited range (e.g., sorting 0s, 1s, and 2s).

```go
func bucketSort(arr []int) []int {
    // Assuming arr only contains 0, 1 or 2
    counts := [3]int{0, 0, 0}

    // Count the quantity of each val in arr
    for _, num := range arr {
        counts[num]++
    }

    // Fill each bucket in the original array
    i := 0
    for n, count := range counts {
        for j := 0; j < count; j++ {
            arr[i] = n
            i++
        }
    }
    return arr
}
```

---

## Search Algorithms

### Binary Search

**Description**: Efficiently searches sorted array by repeatedly dividing search interval in half.

**Time Complexity**: O(log n)  
**Space Complexity**: O(1)

**Pros**:
- Very fast for large datasets
- Simple implementation
- Minimal memory usage

**Cons**:
- Requires sorted array
- Not suitable for unsorted data
- Random access required (not good for linked lists)

**Usage**: Searching in sorted arrays, finding insertion points, optimization problems.

[GeeksforGeeks Reference](https://www.geeksforgeeks.org/dsa/binary-search/)

```go
func binarySearch(arr []int, target int) int {
    L, R := 0, len(arr)-1
    var mid int

    for L <= R {
        mid = (L + R) / 2
        if target > arr[mid] {
            L = mid + 1
        } else if target < arr[mid] {
            R = mid - 1
        } else {
            return mid
        }
    }
    return -1
}
```

### Koko Eating Bananas (Binary Search Application)

**Description**: Uses binary search to find minimum eating speed to finish bananas in time.

**Time Complexity**: O(n log m) where m is max pile size  
**Space Complexity**: O(1)

**Pros**:
- Efficient optimization
- Avoids brute force
- Logarithmic search space reduction

**Cons**:
- Requires understanding of binary search on answer space

**Usage**: Optimization problems where you can verify a solution but need to find the minimum/maximum.

```go
func minEatingSpeed(piles []int, h int) int {
    canFinish := func(k int) bool {
        hours := 0
        for _, pile := range piles {
            hours += (pile + k - 1) / k // ceiling division
            if hours > h {
                return false
            }
        }
        return hours <= h
    }

    low, high := 1, 0
    for _, pile := range piles {
        if pile > high {
            high = pile
        }
    }

    // Binary search for minimum k
    for low < high {
        mid := low + (high-low)/2
        if canFinish(mid) {
            high = mid
        } else {
            low = mid + 1
        }
    }

    return low
}
```

**Brute Force Alternative** (for comparison):
```go
func minEatingSpeed(piles []int, h int) int {
    speed := 1
    for {
        totalTime := 0
        for _, pile := range piles {
            totalTime += int(math.Ceil(float64(pile) / float64(speed)))
        }

        if totalTime <= h {
            return speed
        }
        speed += 1
    }
}
```

---

## Binary Search Trees

### Tree Node Definition

```go
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func NewTreeNode(val int) *TreeNode {
    return &TreeNode{
        Val:   val,
        Left:  nil,
        Right: nil,
    }
}
```

### BST Search

**Description**: Searches for a value in a binary search tree using BST property.

**Time Complexity**: O(log n) for balanced tree, O(n) worst case  
**Space Complexity**: O(log n) for recursion stack

**Pros**:
- Efficient for balanced trees
- Simple recursive implementation
- Leverages BST property

**Cons**:
- Degrades to O(n) for unbalanced trees
- Recursion overhead

**Usage**: Finding elements in BST, validating BST structure.

```go
type Search struct{}

func (s *Search) Search(root *TreeNode, target int) bool {
    if root == nil {
        return false
    }

    if target > root.Val {
        return s.Search(root.Right, target)
    } else if target < root.Val {
        return s.Search(root.Left, target)
    } else {
        return true
    }
}
```

**Alternative Implementation**:
```go
func searchBST(root *TreeNode, val int) *TreeNode {
    if root == nil || root.Val == val {
        return root
    }
    if val < root.Val {
        return searchBST(root.Left, val)
    }
    return searchBST(root.Right, val)
}
```

### Insert into BST

**Description**: Inserts a new value into a binary search tree maintaining BST property.

**Time Complexity**: O(log n) average, O(n) worst case  
**Space Complexity**: O(log n) for recursion

**Pros**:
- Maintains BST property
- Simple recursive logic
- No rebalancing needed

**Cons**:
- Can create unbalanced tree
- Performance degrades with unbalanced trees

**Usage**: Building BSTs, maintaining sorted data structure.

```go
func insertIntoBST(root *TreeNode, val int) *TreeNode {
    if root == nil {
        return &TreeNode{Val: val}
    }

    if val < root.Val {
        root.Left = insertIntoBST(root.Left, val)
    } else {
        root.Right = insertIntoBST(root.Right, val)
    }
    return root
}
```

### Delete Node in BST

**Description**: Removes a node from BST while maintaining BST property.

**Time Complexity**: O(log n) average, O(n) worst case  
**Space Complexity**: O(log n) for recursion

**Pros**:
- Maintains BST property
- Handles all three deletion cases

**Cons**:
- Complex logic for node with two children
- Can unbalance tree

**Usage**: Removing elements from BST while preserving structure.

```go
func getMin(node *TreeNode) *TreeNode {
    current := node
    for current.Left != nil {
        current = current.Left
    }
    return current
}

func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
        return nil
    }

    if key < root.Val {
        root.Left = deleteNode(root.Left, key)
    } else if key > root.Val {
        root.Right = deleteNode(root.Right, key)
    } else {
        if root.Left == nil {
            return root.Right
        } else if root.Right == nil {
            return root.Left
        }
        minNode := getMin(root.Right)
        root.Val = minNode.Val
        root.Right = deleteNode(root.Right, root.Val)
    }
    return root
}
```

---

## Tree Traversal & Operations

### Binary Tree Inorder Traversal

**Description**: Traverses tree in left-root-right order (produces sorted sequence for BST).

**Time Complexity**: O(n)  
**Space Complexity**: O(n) for recursion stack

**Pros**:
- Produces sorted output for BST
- Simple recursive implementation
- Visits all nodes

**Cons**:
- Recursion overhead
- Stack space usage

**Usage**: Getting sorted values from BST, tree validation, expression evaluation.

```go
func traverse(node *TreeNode, result *[]int) {
    if node != nil {
        traverse(node.Left, result)
        *result = append(*result, node.Val)
        traverse(node.Right, result)
    }
}

func inorderTraversal(root *TreeNode) []int {
    result := []int{}
    traverse(root, &result)
    return result
}
```

### Kth Smallest Element in BST

**Description**: Finds the kth smallest element using inorder traversal.

**Time Complexity**: O(k) to O(n)  
**Space Complexity**: O(h) where h is tree height

**Pros**:
- Efficient early termination
- Leverages BST inorder property
- Iterative approach avoids recursion overhead

**Cons**:
- Requires stack for iterative approach

**Usage**: Finding kth statistics in BST, range queries.

```go
func kthSmallest(root *TreeNode, k int) int {
    stack := []*TreeNode{}
    current := root

    for current != nil || len(stack) > 0 {
        for current != nil {
            stack = append(stack, current)
            current = current.Left
        }

        current = stack[len(stack)-1]
        stack = stack[:len(stack)-1]

        k--
        if k == 0 {
            return current.Val
        }

        current = current.Right
    }
    return -1
}
```

### Construct Binary Tree from Preorder and Inorder

**Description**: Reconstructs binary tree from preorder and inorder traversal arrays.

**Time Complexity**: O(n²) due to linear search, O(n) with hashmap  
**Space Complexity**: O(n)

**Pros**:
- Unique reconstruction possible
- Demonstrates tree properties

**Cons**:
- Requires both traversals
- Can be optimized with hashmap

**Usage**: Tree serialization/deserialization, understanding tree traversals.

```go
func buildTree(preorder []int, inorder []int) *TreeNode {
    if len(preorder) == 0 || len(inorder) == 0 {
        return nil
    }

    rootVal := preorder[0]
    root := &TreeNode{Val: rootVal}

    var rootIndex int
    for i, val := range inorder {
        if val == rootVal {
            rootIndex = i
            break
        }
    }

    root.Left = buildTree(preorder[1:rootIndex+1], inorder[:rootIndex])
    root.Right = buildTree(preorder[rootIndex+1:], inorder[rootIndex+1:])
    return root
}
```

### Breadth-First Search (Level Order Traversal)

**Description**: Traverses tree level by level using a queue.

**Time Complexity**: O(n)  
**Space Complexity**: O(w) where w is maximum width of tree

**Pros**:
- Visits nodes level by level
- Useful for finding shortest path
- Iterative (no recursion overhead)

**Cons**:
- Requires queue data structure
- More memory than DFS for wide trees

**Usage**: Level-order processing, finding tree width, shortest path problems.

```go
func levelOrder(root *TreeNode) [][]int {
    var result [][]int
    if root == nil {
        return result
    }

    queue := []*TreeNode{root}

    for len(queue) > 0 {
        var level []int
        qLen := len(queue)

        for i := 0; i < qLen; i++ {
            node := queue[0]
            queue = queue[1:]

            level = append(level, node.Val)

            if node.Left != nil {
                queue = append(queue, node.Left)
            }

            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }

        result = append(result, level)
    }

    return result
}
```

### Design Binary Search Tree (TreeMap)

**Description**: Complete BST implementation with insert, get, min/max, remove, and traversal operations.

**Time Complexity**: O(log n) average for balanced tree, O(n) worst case  
**Space Complexity**: O(n)

**Pros**:
- Full-featured BST implementation
- Supports all common operations
- Maintains sorted order

**Cons**:
- No self-balancing
- Can degrade to O(n) operations

**Usage**: Implementing ordered maps, maintaining sorted data with efficient operations.

```go
type TreeNode struct {
    Key   int
    Value int
    Left  *TreeNode
    Right *TreeNode
}

type TreeMap struct {
    Root *TreeNode
}

func NewTreeMap() *TreeMap {
    return &TreeMap{}
}

func (t *TreeMap) Insert(key, val int) {
    t.Root = t.insert(t.Root, key, val)
}

func (t *TreeMap) insert(node *TreeNode, key, val int) *TreeNode {
    if node == nil {
        return &TreeNode{Key: key, Value: val}
    }
    if key < node.Key {
        node.Left = t.insert(node.Left, key, val)
    } else if key > node.Key {
        node.Right = t.insert(node.Right, key, val)
    } else {
        node.Value = val
    }
    return node
}

func (t *TreeMap) Get(key int) int {
    node := t.get(t.Root, key)
    if node == nil {
        return -1
    }
    return node.Value
}

func (t *TreeMap) get(node *TreeNode, key int) *TreeNode {
    if node == nil {
        return nil
    }
    if key < node.Key {
        return t.get(node.Left, key)
    } else if key > node.Key {
        return t.get(node.Right, key)
    }
    return node
}

func (t *TreeMap) GetMin() int {
    node := t.getMin(t.Root)
    if node == nil {
        return -1
    }
    return node.Value
}

func (t *TreeMap) getMin(node *TreeNode) *TreeNode {
    if node.Left == nil {
        return node
    }
    return t.getMin(node.Left)
}

func (t *TreeMap) GetMax() int {
    node := t.getMax(t.Root)
    if node == nil {
        return -1
    }
    return node.Value
}

func (t *TreeMap) getMax(node *TreeNode) *TreeNode {
    if node.Right == nil {
        return node
    }
    return t.getMax(node.Right)
}

func (t *TreeMap) Remove(key int) {
    t.Root = t.remove(t.Root, key)
}

func (t *TreeMap) remove(node *TreeNode, key int) *TreeNode {
    if node == nil {
        return nil
    }
    if key < node.Key {
        node.Left = t.remove(node.Left, key)
    } else if key > node.Key {
        node.Right = t.remove(node.Right, key)
    } else {
        if node.Left == nil {
            return node.Right
        }
        if node.Right == nil {
            return node.Left
        }
        temp := t.getMin(node.Right)
        node.Key = temp.Key
        node.Value = temp.Value
        node.Right = t.remove(node.Right, temp.Key)
    }
    return node
}

func (t *TreeMap) GetInorderKeys() []int {
    return t.getInorderKeys(t.Root)
}

func (t *TreeMap) getInorderKeys(node *TreeNode) []int {
    if node == nil {
        return []int{}
    }
    keys := t.getInorderKeys(node.Left)
    keys = append(keys, node.Key)
    keys = append(keys, t.getInorderKeys(node.Right)...)
    return keys
}
```

---

## Dynamic Programming

### Climbing Stairs (Fibonacci)

**Description**: Calculates number of ways to climb n stairs (1 or 2 steps at a time).

**Time Complexity**: O(n)  
**Space Complexity**: O(1) for iterative, O(n) for recursive

**Pros**:
- Classic DP problem
- Multiple solution approaches
- Demonstrates optimization techniques

**Cons**:
- Recursive solution can be slow without memoization

**Usage**: Understanding DP concepts, counting problems, Fibonacci-like sequences.

**Iterative Solution** (Optimal):
```go
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

**Recursive DFS Solution** (Educational):
```go
func climbStairs(n int) int {
    var dfs func(i int) int
    dfs = func(i int) int {
        if i >= n {
            if i == n {
                return 1
            }
            return 0
        }
        return dfs(i+1) + dfs(i+2)
    }
    return dfs(0)
}
```

**Comparison**:
- **Iterative**: O(n) time, O(1) space - Best for production
- **Recursive**: O(2^n) time without memoization - Good for understanding recursion
- **With Memoization**: O(n) time, O(n) space - Balance between clarity and efficiency

---

## Contributing

Feel free to add more algorithms and data structures! When contributing:

1. Include clear description
2. Add time/space complexity analysis
3. List pros and cons
4. Provide usage scenarios
5. Include well-commented code
6. Add visual aids where helpful

## Resources

- [NeetCode](https://neetcode.io/) - Algorithm practice and solutions
- [GeeksforGeeks DSA](https://www.geeksforgeeks.org/data-structures/) - Comprehensive tutorials
- [Boot.dev](https://blog.boot.dev/) - Algorithm visualizations
- [Go Documentation](https://go.dev/doc/) - Official Go language docs

---

**Last Updated**: 2025  
**Language**: Go 1.x+
