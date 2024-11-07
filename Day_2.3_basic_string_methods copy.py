# Task 1.1
secret_message = "   Programming in Python is not only powerful but also fun!   "

# Clue:
# Slice operator

# Expected Output
# "PYTHON-POWERFUL"

# sol1
secret_message_shaped = secret_message.strip()
secret_message_quote_1 = secret_message_shaped[15:21]
secret_message_quote_2 = secret_message_shaped[34:42]
secret_message_quote_3 = (secret_message_quote_1 + "-" + secret_message_quote_2)
print(secret_message_quote_3.upper())

# sol2
clean_secret_message = secret_message.strip().upper()
# print(clean_secret_message[15:21]+ "-" +clean_secret_message[34:42])
print(f"{clean_secret_message[15:21]}-{clean_secret_message[34:42]}")



# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

# sol1
print(flipped_message[::-1])

flipped_message_reverse = flipped_message[::-1]
print(flipped_message_reverse[0:6])
print(flipped_message_reverse[12:21])
flipped_message_reverse_quote_1=flipped_message_reverse[0:6]
flipped_message_reverse_quote_2=flipped_message_reverse[12:21]
print(flipped_message_reverse_quote_1.lower()+ " 🗡️  " + flipped_message_reverse_quote_2 +"🌸")

print(f"{flipped_message_reverse_quote_1.lower()} 🗡️  {flipped_message_reverse_quote_2}🌸")

# sol2
flipped_message_shaped = flipped_message[::-1].lower()
flipped_message_reverse_quote_1=flipped_message_shaped[0:6]
flipped_message_reverse_quote_2=flipped_message_shaped[12:21]
print(f"{flipped_message_reverse_quote_1} 🗡️  {flipped_message_reverse_quote_2}🌸")

# sol2
flipped_message_shaped = flipped_message[::-1].lower()
print(f"{flipped_message_shaped[0:6]} 🗡️  {flipped_message_shaped[12:21]}🌸")

