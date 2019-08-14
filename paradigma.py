user_input = raw_input("> ")
user_input = user_input.split(" ")

result_list = []

print(" ".join(["{" * (i+1) + word for i, word in enumerate(user_input)]))

for i, word in enumerate(user_input):
    result_list.append("{" * (i+1) + word)

result = " ".join(result_list)
print(result)