def second_largest(numbers) -> int:
    if len(numbers)<2:
        return None
    else:
        numbers.sort()
        return(numbers[-2])

numbers=list(eval(input("Enter numbers: ")))
print(second_largest(numbers))