quote = "I love python"

print(quote[2])
print(quote[3])

# Slice operetor
# print(quote[start:end]) end index not included
print(quote[2:6])
print(quote[2:])
print(quote[2:10])
print(quote[2:10:1])
print(quote[2:10:2])

# Copy the string
print(quote[0:])
print(quote[:])
# skip < 0, start from last
# Reverse the string
print(quote[::-1])

# Negative index
print(quote[-1])

# Repetition operator (*)
print("Hi" * 3)

name = "   Taisei   "

# 3. upper

print(name.upper())

# 4. lower

print(name.lower())

# 5. strip _ Remove space
print(name.strip())