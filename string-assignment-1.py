#Question: Take input from user and print the string of first and last character of the string as well as the length of the string.

user_input = input("Enter a string: ")

first_chr = user_input[0]  # First character
last_chr = user_input[-1]  # Last character

length_of_string = len(user_input)  # Length of the string

print("You entered:", user_input)
print("First character:", first_chr)
print("Last character:", last_chr)
print("Length of the string:", length_of_string)