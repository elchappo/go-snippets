# go-snippets

## Static Arrays
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