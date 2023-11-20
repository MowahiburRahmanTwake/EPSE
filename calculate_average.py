def calculate_average(numbers):

    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average of the list is: {result}")