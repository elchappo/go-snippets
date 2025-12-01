# Go Algorithms & Data Structures Reference

🎴 **[View Interactive Flashcards](https://elchappo.github.io/go-snippets/index.html)** - Study these algorithms with an interactive flashcard viewer!

A comprehensive collection of common algorithms and data structures implemented in Go, with complexity analysis, pros/cons, and usage scenarios.

---

## 📋 Documentation Template

When adding new algorithms to this reference, please follow this standardized template to ensure consistency:

### Algorithm Name

**Description**: [2-3 sentences explaining what the algorithm does and how it works. Start with the core concept, then explain the approach.]

**Algorithm Approach**: [Bulleted breakdown of the key steps]
- **Step 1**: Brief explanation
- **Step 2**: Brief explanation
- **Key insight**: The core concept that makes it work

**Time Complexity**: 
- **Best case**: O(?) - [When this occurs]
- **Average case**: O(?) - [Typical scenario]
- **Worst case**: O(?) - [When this occurs]
- **Where n** is [define what n represents]

**Space Complexity**: O(?) - [Explain what uses the space]

**Pros**:
- [Advantage 1]
- [Advantage 2]
- [Advantage 3]
- [Continue as needed]

**Cons**:
- [Limitation 1]
- [Limitation 2]
- [Limitation 3]
- [Continue as needed]

**When to Use**:
- [Specific scenario 1]
- [Specific scenario 2]
- [Specific scenario 3]
- [Real-world application examples]

**When NOT to Use**:
- [Scenario where it's inappropriate 1]
- [Scenario where it's inappropriate 2]
- [Better alternatives for certain cases]

**Usage**: [One-line summary of primary use cases]

**Common Pitfalls** *(optional)*:
- [Common mistake 1]
- [Common mistake 2]

**Related Algorithms**: [Algorithm 1], [Algorithm 2], [Algorithm 3]

```go
func AlgorithmName(input Type) ReturnType {
    // Implementation with clear comments
    // explaining key steps
}
```

**Alternative Implementation** *(if beneficial)*:
```go
func AlternativeApproach(input Type) ReturnType {
    // Different approach to solve same problem
}
```

---

## Table of Contents

- [Go Algorithms \& Data Structures Reference](#go-algorithms--data-structures-reference)
  - [📋 Documentation Template](#-documentation-template)
    - [Algorithm Name](#algorithm-name)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Running Tests](#running-tests)
    - [Project Structure](#project-structure)
    - [Basic Test Structure](#basic-test-structure)
  - [Array \& String Algorithms](#array--string-algorithms)
    - [Remove Duplicates From Sorted Array](#remove-duplicates-from-sorted-array)
    - [Remove Element](#remove-element)
    - [Concatenation of Array](#concatenation-of-array)
  - [Stack \& Queue](#stack--queue)
    - [Valid Parentheses](#valid-parentheses)
    - [Min Stack](#min-stack)
    - [Implement Stack Using Queues](#implement-stack-using-queues)
    - [Design Browser History](#design-browser-history)
    - [Number of Students Unable to Eat Lunch](#number-of-students-unable-to-eat-lunch)
  - [Linked Lists](#linked-lists)
    - [Reverse Linked List](#reverse-linked-list)
    - [Merge Two Sorted Linked Lists](#merge-two-sorted-linked-lists)
    - [Design Linked List](#design-linked-list)
  - [Sorting Algorithms](#sorting-algorithms)
    - [Comparison Table](#comparison-table)
    - [Insertion Sort](#insertion-sort)
    - [Merge Sort](#merge-sort)
    - [Quick Sort](#quick-sort)
    - [Bucket Sort](#bucket-sort)
  - [Search Algorithms](#search-algorithms)
    - [Binary Search](#binary-search)
    - [Koko Eating Bananas (Binary Search Application)](#koko-eating-bananas-binary-search-application)
  - [Binary Search Trees](#binary-search-trees)
    - [Tree Node Definition](#tree-node-definition)
    - [BST Search](#bst-search)
    - [Insert into BST](#insert-into-bst)
    - [Delete Node in BST](#delete-node-in-bst)
  - [Tree Traversal \& Operations](#tree-traversal--operations)
    - [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)
    - [Kth Smallest Element in BST](#kth-smallest-element-in-bst)
    - [Construct Binary Tree from Preorder and Inorder](#construct-binary-tree-from-preorder-and-inorder)
    - [Breadth-First Search (Level Order Traversal)](#breadth-first-search-level-order-traversal)
    - [Design Binary Search Tree (TreeMap)](#design-binary-search-tree-treemap)
  - [Dynamic Programming](#dynamic-programming)
    - [Climbing Stairs (Fibonacci)](#climbing-stairs-fibonacci)
  - [Contributing](#contributing)
  - [Resources](#resources)

---

## Getting Started

### Running Tests
```bash
go test -v
```

### Project Structure
```
go-snippets/
├── README.md           # This comprehensive reference guide
├── index.html          # Interactive flashcard viewer
├── styles.css          # Flashcard styling
└── *_test.go          # Unit tests for each algorithm
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

**Description**: Removes duplicate elements from a sorted array in-place using the two-pointer technique. The algorithm maintains a write pointer that tracks where the next unique element should be placed, while a read pointer scans through the array. Only when a new unique element is found does it get written to the next position.

**Algorithm Approach**: Two-pointer technique
- **Write pointer**: Tracks position for next unique element
- **Read pointer**: Scans through array elements
- **Key insight**: In sorted array, duplicates are adjacent

**Time Complexity**: 
- **Best/Worst/Average**: O(n) - Single pass through array
- **Where n** is the number of elements in the array

**Space Complexity**: O(1) - Only uses two pointer variables

**Pros**:
- In-place modification (no extra space required)
- Single pass through array
- Efficient for sorted arrays
- Simple implementation
- Preserves relative order of unique elements

**Cons**:
- Only works on sorted arrays
- Modifies original array (destructive operation)
- Doesn't actually remove elements, just overwrites

**When to Use**:
- Processing sorted arrays where duplicates should be removed
- Memory-constrained environments requiring in-place operations
- Database query result deduplication
- When you need to preserve the first occurrence of each element

**When NOT to Use**:
- Unsorted arrays (sort first, which takes O(n log n))
- When original array must be preserved
- When you need to count duplicate occurrences

**Usage**: When you need to remove duplicates from a sorted array without using extra space.

**Related Algorithms**: Remove Element, Remove Duplicates from Unsorted Array

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

**Description**: Removes all instances of a specific value from an array in-place using a single-pass filtering approach. The algorithm maintains a write index that only advances when a non-target element is found, effectively compacting the array by overwriting target values.

**Algorithm Approach**: Single-pass filtering with write pointer
- Iterates once through the array
- Copies non-target elements to the front
- Write index tracks the new array length

**Time Complexity**: 
- **Best/Worst/Average**: O(n) - Single pass required
- **Where n** is the number of elements

**Space Complexity**: O(1) - Only uses one index variable

**Pros**:
- In-place modification (minimal memory usage)
- Works on unsorted arrays
- Simple implementation
- Efficient single-pass solution
- Can handle multiple occurrences efficiently

**Cons**:
- Modifies original array
- Order may not be preserved (unstable)
- Doesn't shrink the underlying array capacity

**When to Use**:
- Filtering specific values from arrays in-place
- Memory-constrained scenarios
- Preprocessing data before further operations
- Removing invalid or sentinel values from datasets

**When NOT to Use**:
- When original array must be preserved
- When order must be maintained exactly
- When you need to track removed elements

**Usage**: When you need to filter out specific values from an array without allocating new memory.

**Related Algorithms**: Remove Duplicates, Move Zeroes

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

**Description**: Creates a new array by concatenating the original array with itself, effectively doubling its length. This operation creates a sequence where the original array is repeated twice consecutively.

**Algorithm Approach**: Array duplication using built-in append
- Leverages Go's `append` with spread operator (`...`)
- Creates new underlying array
- Simple one-line operation

**Time Complexity**: 
- **Best/Worst/Average**: O(n) - Must copy all elements
- **Where n** is the number of elements in original array

**Space Complexity**: O(n) - Creates new array of size 2n

**Pros**:
- Simple and readable implementation
- Uses idiomatic Go append function
- Clear intent and purpose
- Efficient built-in implementation

**Cons**:
- Creates new array (memory allocation overhead)
- Not in-place operation
- Doubles memory usage

**When to Use**:
- Creating circular/cyclic patterns
- Preprocessing for sliding window algorithms
- Testing algorithms that need repeated data
- Generating periodic sequences

**When NOT to Use**:
- Very large arrays (memory concerns)
- When in-place modification is preferred
- Real-time systems with strict memory constraints

**Usage**: When you need to duplicate array elements in sequence for pattern generation or algorithm preprocessing.

**Related Algorithms**: Array Rotation, Circular Array Simulation

```go
func getConcatenation(nums []int) []int {
    return append(nums, nums...)
}
```

---

## Stack & Queue

### Valid Parentheses

**Description**: Validates if a string of brackets/parentheses is properly balanced and correctly nested using a stack data structure. The algorithm processes each character, pushing expected closing brackets onto a stack for opening brackets, and verifying that closing brackets match the most recent opening bracket.

**Algorithm Approach**: Stack-based matching
- **Opening brackets**: Push expected closing bracket to stack
- **Closing brackets**: Pop and verify match with current character
- **Final check**: Stack must be empty (all brackets closed)

**Time Complexity**: 
- **Best/Worst/Average**: O(n) - Single pass through string
- **Where n** is the length of the string

**Space Complexity**: 
- **Worst case**: O(n) - All opening brackets (e.g., "((((")
- **Best case**: O(1) - Alternating brackets (e.g., "()()")

**Pros**:
- Handles multiple bracket types `()`, `{}`, `[]`
- Clear and maintainable code
- Efficient single-pass solution
- Catches all invalid patterns (unmatched, wrong order, extra brackets)
- Optimal time complexity

**Cons**:
- Requires extra space for stack
- Cannot identify specific error location
- Only validates, doesn't correct imbalances

**When to Use**:
- Validating mathematical expressions
- Compiler/parser bracket validation
- Code editor syntax checking
- HTML/XML tag matching
- Expression evaluation preprocessing

**When NOT to Use**:
- When you need to identify where the error is
- For non-bracket matching problems
- When memory is extremely constrained

**Usage**: Validating balanced expressions in compilers, parsers, or mathematical expressions.

**Common Pitfalls**:
- Forgetting to check if stack is empty at the end
- Not handling empty strings
- Integer overflow with very long strings

**Related Algorithms**: Expression Evaluation, HTML Tag Matching

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
            // Opening bracket: push expected closing bracket
            stack = append(stack, expected)
        } else {
            // Closing bracket: verify it matches top of stack
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

**Description**: A specialized stack data structure that supports push, pop, top, and retrieving the minimum element in constant O(1) time. This is achieved by maintaining two parallel stacks: one for actual values and one for tracking the minimum at each level.

**Algorithm Approach**: Parallel stack technique
- **Main stack**: Stores all pushed values
- **Min stack**: Stores running minimum at each level
- **Key insight**: Track min as stack grows/shrinks

**Time Complexity**: 
- **All operations**: O(1) - Push, Pop, Top, GetMin
- No iteration required for any operation

**Space Complexity**: O(n) - Two stacks storing n elements

**Pros**:
- Constant time minimum retrieval
- All standard stack operations remain O(1)
- Simple implementation
- No complex data structures needed
- Maintains min even after pop operations

**Cons**:
- Uses double the space (two stacks)
- Increased memory footprint
- Push operation slightly more expensive (two operations)

**When to Use**:
- Stock price tracking (min/max over time)
- Algorithm problems requiring O(1) min access
- Undo/redo with constraint tracking
- Window minimum tracking
- Financial applications (tracking lowest price)

**When NOT to Use**:
- Memory-constrained environments
- When min is rarely needed (cheaper to calculate on demand)
- When you need median or other statistics (use different structure)

**Usage**: When you need to track the minimum value in a stack efficiently (e.g., stock price tracking, sliding window minimums).

**Related Algorithms**: Max Stack, Monotonic Stack

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
    
    // Track minimum at this level
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

**Description**: Implements a Last-In-First-Out (LIFO) stack using First-In-First-Out (FIFO) queue operations. This demonstrates how to transform a FIFO structure into a LIFO structure by reordering elements on each push operation.

**Algorithm Approach**: Queue rotation on push
- **Push operation**: Add element, then rotate queue
- **Rotation**: Move all previous elements to end of queue
- **Result**: Most recent element is at front

**Time Complexity**: 
- **Push**: O(n) - Must rotate all elements
- **Pop**: O(1) - Simple dequeue from front
- **Top**: O(1) - Access front element
- **Where n** is current number of elements

**Space Complexity**: O(n) - Single queue storing n elements

**Pros**:
- Demonstrates data structure conversion
- Educational value for understanding structures
- Simple conceptual approach
- Pop and Top are efficient

**Cons**:
- Push operation is O(n) vs standard O(1) stack
- Less efficient than native stack implementation
- Not practical for production use
- High cost for frequent push operations

**When to Use**:
- Academic purposes or technical interviews
- When only queue operations are available
- Learning data structure relationships
- Demonstrating algorithmic thinking

**When NOT to Use**:
- Production code (use native stack)
- Performance-critical applications
- Frequent push operations
- Real-world applications (unless constrained to queues)

**Usage**: Academic purposes or when only queue operations are available.

**Related Algorithms**: Implement Queue Using Stacks

```go
type MyStack struct {
    q []int
}

func Constructor() MyStack {
    return MyStack{q: []int{}}
}

func (this *MyStack) Push(x int) {
    this.q = append(this.q, x)
    // Rotate all previous elements to back
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

**Description**: Simulates browser navigation with back/forward functionality using an array-based approach. The implementation tracks the current position in a history array and allows navigation backward and forward through visited pages.

**Algorithm Approach**: Array with current index pointer
- **Visit**: Truncate forward history, append new page, move index
- **Back**: Decrease index (bounded by 0)
- **Forward**: Increase index (bounded by history length)

**Time Complexity**: 
- **Visit**: O(1) - Array append and index update
- **Back/Forward**: O(1) - Simple index manipulation

**Space Complexity**: O(n) where n is number of visited pages

**Pros**:
- Simple array-based implementation
- Efficient navigation operations (all O(1))
- Clear state management
- Easy to understand and maintain
- Supports arbitrary back/forward steps

**Cons**:
- Stores all history in memory
- Visiting new page discards forward history
- Memory grows with browsing (no automatic cleanup)
- No maximum history limit

**When to Use**:
- Browser history implementation
- Undo/redo systems with state tracking
- Navigation stacks in applications
- Document version history
- Command history in CLI applications

**When NOT to Use**:
- Extremely long browsing sessions (memory concerns)
- When you need to preserve all forward history after new visits
- Systems requiring persistent storage

**Usage**: Browser history, undo/redo systems, navigation stacks.

**Related Algorithms**: Undo/Redo Stack, Command Pattern

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
    // Truncate forward history
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

**Description**: Calculates the number of students who cannot get their preferred sandwich type using a counting-based approach. Students want either circular (0) or square (1) sandwiches, and will only take sandwiches matching their preference. The algorithm counts student preferences and matches them against the sandwich stack.

**Algorithm Approach**: Counting strategy
- Count preferences (circular vs square)
- Process sandwich stack from top
- Stop when no students want the current sandwich
- Return remaining student count

**Time Complexity**: 
- **Best/Worst/Average**: O(n) - Single pass through both arrays
- **Where n** is the number of students/sandwiches

**Space Complexity**: O(1) - Only uses constant space for counters

**Pros**:
- Efficient counting solution without simulation
- No queue manipulation needed
- Constant extra space
- Simple logic
- Optimal time complexity

**Cons**:
- Less intuitive than direct simulation
- Doesn't track individual student states
- Specific to this problem type

**When to Use**:
- Resource matching problems with binary choices
- Counting-based optimizations
- Queue matching without simulation overhead
- Problems where order doesn't affect final result

**When NOT to Use**:
- When you need to track individual entities
- Problems requiring simulation state
- When the matching process is more complex

**Usage**: Queue matching problems, resource allocation scenarios.

**Related Algorithms**: Time to Buy Tickets, Queue Simulation

```go
func countStudents(students []int, sandwiches []int) int {
    // Count student preferences
    count := []int{0, 0}
    for _, s := range students {
        count[s]++
    }

    // Process sandwiches from top of stack
    for _, sandwich := range sandwiches {
        if count[sandwich] == 0 {
            // No students want this sandwich
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

**Description**: Reverses a singly linked list using recursion, making the last node the new head and reversing all pointers. The recursive approach processes the list from end to beginning, updating pointers as the recursion unwinds.

**Algorithm Approach**: Recursive pointer reversal
- **Base case**: Single node or null
- **Recursive case**: Reverse rest of list, then reverse current link
- **Key insight**: Process from tail to head via recursion

**Time Complexity**: 
- **Best/Worst/Average**: O(n) - Visit each node once
- **Where n** is the number of nodes

**Space Complexity**: O(n) - Recursion call stack depth

**Pros**:
- Clean recursive solution
- Easy to understand conceptually
- Elegant code structure
- Self-contained logic

**Cons**:
- Uses call stack space (O(n))
- Risk of stack overflow for very long lists
- Less efficient than iterative approach
- Not tail-recursive (can't be optimized)

**When to Use**:
- Educational purposes and interviews
- Small to medium sized lists
- When code clarity is prioritized
- Recursive algorithm practice

**When NOT to Use**:
- Very long lists (stack overflow risk)
- Production systems with memory constraints
- When iterative solution is more appropriate

**Usage**: List reversal, interview questions, understanding recursion.

**Common Pitfalls**:
- Forgetting to set head.Next = nil
- Not handling empty list
- Stack overflow on large lists

**Related Algorithms**: Reverse List Iterative, Reverse K Groups

[NeetCode Solution](https://neetcode.io/solutions/reverse-linked-list)

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

**Description**: Merges two sorted linked lists into one sorted list by comparing values and linking nodes in order. The algorithm uses a dummy head node to simplify edge cases and iterates through both lists simultaneously.

**Algorithm Approach**: Two-pointer merge with dummy head
- **Dummy node**: Simplifies edge case handling
- **Compare heads**: Link smaller value
- **Advance pointer**: Move to next in chosen list
- **Append remainder**: Link remaining list

**Time Complexity**: 
- **Best/Worst/Average**: O(n + m) - Visit all nodes once
- **Where n, m** are lengths of the two lists

**Space Complexity**: O(1) - Only uses pointer variables

**Pros**:
- In-place merging (no new nodes created)
- Maintains sorted order
- Efficient single pass
- Optimal time complexity
- Dummy node simplifies code

**Cons**:
- Modifies original lists
- Requires both lists to be sorted
- Not stable if nodes with equal values matter

**When to Use**:
- Merge sort for linked lists
- Combining sorted data streams
- Database result merging
- K-way merge algorithms

**When NOT to Use**:
- Unsorted lists
- When original lists must be preserved
- Array-based data (use array merge instead)

**Usage**: Merge sort for linked lists, combining sorted data streams.

**Related Algorithms**: Merge K Sorted Lists, Merge Sort

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

    // Append remaining nodes
    node.Next = list1
    if list1 == nil {
        node.Next = list2
    }

    return dummy.Next
}
```

### Design Linked List

**Description**: Custom implementation of a singly linked list with common operations including get, add at head/tail/index, and delete at index. Uses a dummy head node and tracks size for efficient validation.

**Algorithm Approach**: Dummy head with size tracking
- **Dummy head**: Simplifies insertion/deletion at beginning
- **Size tracking**: Enables O(1) validation
- **Helper method**: getPrev() finds node before target index

**Time Complexity**: 
- **Get/AddAtIndex/DeleteAtIndex**: O(n) - May traverse list
- **AddAtHead**: O(1) - Constant time insertion
- **AddAtTail**: O(n) - Must traverse to end
- **Where n** is current number of nodes

**Space Complexity**: O(1) per operation - No extra space beyond nodes

**Pros**:
- Full control over implementation
- Efficient head operations
- Tracks size for validation
- Dummy head simplifies edge cases
- Standard linked list operations

**Cons**:
- Linear time for index-based operations
- More complex than built-in structures
- No tail pointer (addAtTail is O(n))
- Manual memory management considerations

**When to Use**:
- Learning data structure implementation
- Interview practice
- Custom requirements not met by standard library
- Educational purposes

**When NOT to Use**:
- Production code (use built-in structures)
- When performance matters (use array-based structures)
- Random access is common (use array/slice)

**Usage**: When you need a custom linked list implementation with specific requirements or for educational purposes.

**Related Algorithms**: Doubly Linked List, Skip List

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

| Algorithm      | Time (Best) | Time (Avg) | Time (Worst) | Space    | Stable | When to Use                        |
| -------------- | ----------- | ---------- | ------------ | -------- | ------ | ---------------------------------- |
| Insertion Sort | O(n)        | O(n²)      | O(n²)        | O(1)     | ✓      | Small/nearly sorted data           |
| Merge Sort     | O(n log n)  | O(n log n) | O(n log n)   | O(n)     | ✓      | Stable sort needed                 |
| Quick Sort     | O(n log n)  | O(n log n) | O(n²)        | O(log n) | ✗      | General purpose, fast average case |
| Bucket Sort    | O(n)        | O(n)       | O(n)         | O(n)     | ✗      | Limited value range                |

### Insertion Sort

![Insertion Sort](https://blog.boot.dev/img/800/insertionsort.gif)

**Description**: Builds a sorted array one element at a time by inserting each element into its correct position within the already-sorted portion. Like sorting playing cards in your hand, it picks each card and places it in the right spot among the cards you've already sorted.

**Algorithm Approach**: Incremental insertion
- **Outer loop**: Iterate through array from second element
- **Inner loop**: Compare current with sorted portion, shift larger elements
- **Insert**: Place current element in correct position

**Time Complexity**: 
- **Best case**: O(n) - Already sorted array
- **Average case**: O(n²) - Random order
- **Worst case**: O(n²) - Reverse sorted array

**Space Complexity**: O(1) - In-place sorting

**Pros**:
- Simple implementation
- Efficient for small datasets (< 50 elements)
- Stable sort (preserves relative order)
- In-place sorting (no extra memory)
- Adaptive (O(n) for nearly sorted data)
- Online algorithm (can sort as it receives data)

**Cons**:
- Quadratic time for large datasets
- Not suitable for large arrays
- Many comparisons and shifts for unsorted data

**When to Use**:
- Small datasets (< 50 elements)
- Nearly sorted data
- Online sorting (streaming data)
- When simplicity is more important than speed
- As part of hybrid algorithms (e.g., Timsort uses it)

**When NOT to Use**:
- Large datasets (use merge sort or quick sort)
- Completely unsorted data
- Performance-critical applications

**Usage**: Small datasets, nearly sorted data, or when simplicity is preferred over performance.

**Related Algorithms**: Selection Sort, Bubble Sort

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

### Merge Sort

![Merge Sort](https://blog.boot.dev/img/800/merge_sort_gif.gif)

**Description**: A divide-and-conquer algorithm that recursively splits the array into halves until single elements remain, then merges them back in sorted order. Guarantees O(n log n) performance regardless of input.

**Algorithm Approach**: Divide and conquer
- **Divide**: Split array into two halves recursively

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

**Description**: A divide-and-conquer sorting algorithm that selects a 'pivot' element and partitions the array around it, recursively sorting the sub-arrays. Elements smaller than the pivot go to the left, larger elements go to the right, and the process repeats until the array is sorted.

**Algorithm Approach**: Divide and conquer with partitioning
- **Select pivot**: Choose an element (typically last element)
- **Partition**: Rearrange array so elements < pivot are left, elements > pivot are right
- **Recursively sort**: Apply same process to left and right sub-arrays
- **Key insight**: Each partition places one element in its final sorted position

**Time Complexity**: 
- **Best case**: O(n log n) - Balanced partitions (pivot near median)
- **Average case**: O(n log n) - Random pivot selection
- **Worst case**: O(n²) - Unbalanced partitions (already sorted array with poor pivot choice)
- **Where n** is the number of elements

**Space Complexity**: O(log n) - Recursion stack for balanced partitions, O(n) worst case

**Pros**:
- Fast average case performance (often fastest in practice)
- In-place sorting (low memory overhead)
- Cache-friendly (good memory locality)
- Often outperforms other O(n log n) algorithms
- Simple to implement

**Cons**:
- Unstable sort (doesn't preserve relative order of equal elements)
- Worst case O(n²) performance (rare with good pivot selection)
- Not ideal for nearly sorted data with naive pivot selection
- Performance sensitive to pivot selection strategy
- Recursive implementation can cause stack overflow on very large arrays

**When to Use**:
- General-purpose sorting for large datasets
- When average-case performance is more important than worst-case
- Memory-constrained environments (in-place sorting)
- When stability is not required
- Sorting primitive types or simple objects

**When NOT to Use**:
- When worst-case O(n log n) is required (use Merge Sort or Heap Sort)
- When stability is needed (use Merge Sort)
- Nearly sorted data with naive pivot (use Insertion Sort or Merge Sort)
- When consistent performance is critical (use Merge Sort)
- Small arrays (use Insertion Sort)

**Usage**: General-purpose sorting when stability isn't required and average-case performance matters.

**Related Algorithms**: Merge Sort, Heap Sort, Intro Sort (hybrid Quick/Heap Sort)

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

**Description**: A distribution-based sorting algorithm that divides elements into a fixed number of buckets, where each bucket represents a range of values. Elements are distributed into appropriate buckets, each bucket is sorted individually, and then all buckets are concatenated to produce the final sorted array.

**Algorithm Approach**: Distribution and counting
- **Create buckets**: Initialize array of counters for each possible value
- **Distribute**: Count occurrences of each value
- **Reconstruct**: Fill original array by iterating through buckets
- **Key insight**: Works efficiently when value range is small and known

**Time Complexity**: 
- **Best case**: O(n + k) - When values are uniformly distributed
- **Average case**: O(n + k) - Linear time for limited range
- **Worst case**: O(n + k) - Where k is the number of distinct values
- **Where n** is the number of elements, **k** is the range of values

**Space Complexity**: O(k) - Additional space for bucket counters

**Pros**:
- Linear time complexity for limited value ranges
- Simple and easy to implement
- Efficient for uniformly distributed data
- Stable (can be made stable with proper implementation)
- No comparison operations needed

**Cons**:
- Only works for limited, known value ranges
- Not general-purpose (requires prior knowledge of data)
- Memory inefficient for large value ranges
- Not suitable for floating-point or complex data types
- Performance depends heavily on value distribution

**When to Use**:
- Sorting integers with small, known range (e.g., 0-9, 0-100)
- Counting sort scenarios (sorting 0s, 1s, 2s)
- When input values are uniformly distributed
- Sorting by category or discrete values
- When O(n) time is critical and constraints are met

**When NOT to Use**:
- Large or unknown value ranges (wastes memory)
- Arbitrary data types (strings, floats, objects)
- When comparison-based sorting is more appropriate
- Sparse data distributions (most buckets empty)
- General-purpose sorting needs (use Quick Sort or Merge Sort)

**Usage**: Sorting data with known, limited range (e.g., sorting 0s, 1s, and 2s), counting sort implementations.

**Related Algorithms**: Counting Sort, Radix Sort, Pigeonhole Sort

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

**Description**: Efficiently searches a sorted array by repeatedly dividing the search interval in half. At each step, it compares the target value with the middle element and eliminates half of the remaining elements based on the comparison. This divide-and-conquer approach makes it one of the most efficient search algorithms for sorted data.

**Time Complexity**: 
- **Best Case**: O(1) - Target is at the middle position
- **Average/Worst Case**: O(log n) - Must divide search space repeatedly
- **Where n** is the number of elements in the array

**Space Complexity**: 
- **Iterative**: O(1) - Only uses a few variables
- **Recursive**: O(log n) - Due to call stack depth

**Big O Notation Explained**:
- **O(log n)**: Each comparison eliminates half the search space
- **Example**: Array of 1,000,000 elements requires only ~20 comparisons (log₂ 1,000,000 ≈ 20)
- **Logarithmic growth**: Doubling array size adds only one more comparison
- **Why log n?**: Search space halves each iteration: n → n/2 → n/4 → ... → 1

**When to Use Binary Search**:
✅ **Best suited for:**
- Searching in large sorted arrays (1000+ elements)
- Finding insertion points in sorted data
- Implementing autocomplete/search suggestions
- Database index lookups
- Finding boundaries (first/last occurrence of value)
- Optimization problems with monotonic functions
- When you need guaranteed O(log n) search time

❌ **Not ideal for:**
- Unsorted data (sorting first takes O(n log n), negating benefits)
- Small arrays (<50 elements, linear search is simpler and often faster)
- Linked lists (no random access, can't efficiently find middle)
- Frequently changing data (maintaining sorted order is expensive)
- When you need to find all occurrences (still O(n) in worst case)

**Comparison with Alternatives**:
- **vs Linear Search**: O(log n) vs O(n) - 1000x faster for million elements
- **vs Hash Table**: Binary search maintains order, hash table doesn't; hash is O(1) average but no range queries
- **vs BST Search**: Array binary search has better cache locality, BST allows O(log n) insertions
- **vs Interpolation Search**: Binary search is O(log n) guaranteed, interpolation is O(log log n) average but O(n) worst case

**Pros**:
- Extremely fast for large sorted datasets
- Simple iterative implementation
- Minimal memory usage (O(1) space)
- Predictable performance (always O(log n))
- Cache-friendly (array-based, good locality)
- No preprocessing needed (if already sorted)

**Cons**:
- Requires sorted array (O(n log n) to sort first)
- Not suitable for unsorted or frequently changing data
- Random access required (not efficient for linked lists)
- Overkill for small datasets
- Can't efficiently handle duplicates (finding all occurrences)
- Integer overflow risk with (L + R) / 2 (use L + (R - L) / 2)

**Usage**: Searching in sorted arrays, finding insertion points, optimization problems, implementing lower_bound/upper_bound, finding peak elements, rotated array searches.

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

**Description**: Searches for a value in a binary search tree by leveraging the BST property where left subtree contains smaller values and right subtree contains larger values. The algorithm recursively navigates left or right based on value comparison, eliminating half of the remaining nodes at each step.

**Time Complexity**: 
- **Best/Average Case**: O(log n) - For balanced trees, height is logarithmic
- **Worst Case**: O(n) - For completely unbalanced trees (essentially a linked list)
- **Where n** is the number of nodes in the tree

**Space Complexity**: 
- **Recursive**: O(h) where h is tree height - Due to call stack
- **Iterative**: O(1) - No extra space needed

**Big O Notation Explained**:
- **O(log n)**: Each comparison eliminates half the search space (like binary search)
- **O(n)**: In worst case (skewed tree), must traverse all nodes linearly
- **Height matters**: Balanced tree height = log n, skewed tree height = n

**When to Use BST Search**:
✅ **Best suited for:**
- Searching in sorted/ordered data that changes frequently (insertions/deletions)
- When you need O(log n) average search time without array reallocation
- Dictionary/map implementations where keys need ordering
- Range queries (find all values between x and y)
- Finding min/max values efficiently
- Maintaining sorted data with dynamic updates

❌ **Not ideal for:**
- Static sorted data (use binary search on array instead - better cache locality)
- Unbalanced trees (consider self-balancing trees like AVL or Red-Black)
- Small datasets (overhead not worth it, use simple array)
- When you don't need ordering (use hash table for O(1) average lookup)

**Comparison with Alternatives**:
- **vs Array Binary Search**: BST allows O(log n) insertion/deletion, array requires O(n)
- **vs Hash Table**: BST maintains order and supports range queries, hash table doesn't
- **vs Linear Search**: BST is O(log n) vs O(n), but requires maintaining tree structure
- **vs Balanced BST (AVL/Red-Black)**: Standard BST can degrade to O(n), balanced trees guarantee O(log n)

**Pros**:
- Efficient O(log n) search for balanced trees
- Simple recursive implementation
- Leverages BST ordering property
- No extra space needed for iterative version
- Naturally supports range queries and ordered traversal

**Cons**:
- Performance degrades to O(n) for unbalanced trees
- Recursion overhead and stack space usage
- Requires maintaining BST property during insertions/deletions
- Not cache-friendly compared to arrays
- Slower than hash tables for exact-match lookups

**Usage**: Finding elements in BST, validating BST structure, implementing ordered maps/sets, range queries, finding successor/predecessor nodes.

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
