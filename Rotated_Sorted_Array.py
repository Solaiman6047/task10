def rotated_sorted_array(numbers: list[int]) -> int:
    if numbers[0]<numbers[-1]:
        return "Rotation number= Zero"
    start=0
    end=len(numbers)-1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid]>numbers[mid+1]:
            return mid +1
        if numbers[mid] >= numbers[start]:
            start = mid + 1
        else:
            end = mid - 1

numbers=list(eval(input("Enter the array: ")))
print(rotated_sorted_array(numbers))