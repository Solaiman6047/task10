def missing_number(numbers: list) -> int:
    list.sort
    sum_numbers=sum(numbers) 
    real_sum=(max(numbers) + min(numbers)) * (max(numbers) - min(numbers) + 1) // 2
    if real_sum-sum_numbers==0:
        return "No missing number"
    else:
        return real_sum-sum_numbers

numbers=list(eval(input("Enter numbers: ")))
set_numbers=set(numbers)
if len(numbers)!=len(set_numbers):
    print("Duplication not allowed")
else:
    print(missing_number(numbers))