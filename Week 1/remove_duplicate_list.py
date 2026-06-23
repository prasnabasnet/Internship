user_input = input("Enter items separated by commas (eg: apple,banana,orange): ").split(",")

cleaned_list = [item.strip() for item in user_input]

unique_list = list(dict.fromkeys(cleaned_list))

print("\nYour list with duplicates removed:")
print(unique_list)