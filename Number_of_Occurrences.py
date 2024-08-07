def number_of_occurrences(numbers: list[int], target: int) -> int:
    return numbers.index(target),len(numbers) - 1 - numbers[::-1].index(target),numbers.count(target)
    
numbers=list(eval(input("Enter numbers: ")))
target=int(input("Enter target number: "))
first,last,count=number_of_occurrences(numbers,target)
print(f"First index: {first}, Last index: {last}, occurrences: {count}")