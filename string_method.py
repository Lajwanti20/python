#Question : Take input from user
#convert it into lowercase
#replaces all " " with "_"
#print the new string

string_input = input("Enter a string: ")
convert_into_locwercase = string_input.lower()  # Convert to lowercase
replace_space_with_underscore = string_input.replace(" ", "_")  # Replace spaces with underscores

print("You entered:", string_input)
print("Converted to lowercase:", convert_into_locwercase)
print("Replaced spaces with underscores:", replace_space_with_underscore)

print("New string Title:",convert_into_locwercase.title())  # Convert to title case 
print("New string first character :",convert_into_locwercase.find("pro"))  # find first character of string