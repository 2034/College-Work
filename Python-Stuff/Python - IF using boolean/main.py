# Jonathan (17/12/24)
# Input
pet_type = input("What type of pet insurance are you looking for? (cat/dog/other): ").lower()
# Check Type of Input
if pet_type == "cat" or pet_type == "dog":
    quote = 10
else:
    quote = 25
# Print Message
print(f"The monthly insurance quote for a {pet_type} is £{quote}.")