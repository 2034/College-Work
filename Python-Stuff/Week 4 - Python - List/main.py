list = []

print("What is your top 3 movies?")
for i in range(3):
    movieInput = input("Enter your movie: ")
    list.append(movieInput)

print("Your top 3 movies are:")
for i in range(3):
    print(list[i])