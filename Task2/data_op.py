def data_operations():
    numbers = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num.lower() == 'done':
            break
        try:
            numbers.append(float(num))
        except ValueError:
            print("Please enter a valid number.")
    
    if not numbers:
        print("No numbers entered.")
        return
    
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    
    sorted_numbers = sorted(unique_numbers)
    
    max_num = max(unique_numbers)
    min_num = min(unique_numbers)
    average = sum(unique_numbers) / len(unique_numbers)
    
    print(f"\nOriginal: {numbers}")
    print(f"Unique Numbers: {unique_numbers}")
    print(f"Sorted: {sorted_numbers}")
    print(f"Max: {max_num}")
    print(f"Min: {min_num}")
    print(f"Average: {round(average, 2)}")

data_operations()