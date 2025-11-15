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
### Reverse Linked List
https://neetcode.io/solutions/reverse-linked-list
```go
func reverseList(head *ListNode) *ListNode {
    var prev *ListNode
    current := head 

    for current != nil {
        next := current.Next
        current.Next = prev 
        prev = current 
        current = next
    } 

    return prev
}
```