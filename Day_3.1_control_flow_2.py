# # Loops

# # Repeating statements
# # print("yoshika")

# # i = 1

# # while i <= 3:
# #     print("yoshika")
# #     i = i + 1

# # Task - 1
# # Expected output
# # 🔥
# # 🔥🔥
# # 🔥🔥🔥
# # 🔥🔥🔥🔥
# # 🔥🔥🔥🔥🔥

# i = 1

# while i <= 5:
#     print("🔥" * i)
#     i = i + 1

# # Task - 1.2
# # Get number of rows from user

# row_number = input("Please tell me number")

# i = 1

# while i <= int(row_number):
#     print("🔥" * i)
#     i = i + 1

# Task - 1.3
# sol1
# row_number = input("Please tell me number")

# i = 1

# while i <= int(row_number):

#     print(("  " * (int(row_number) - i)) + "🔥" * (i * 2 - 1))
#     i = i + 1

# sol2
# row_number = int(input("Please tell me number"))

# i = 1

# while i <= int(row_number):

#     print(f"{"  "*{row_number}-i}  {"🔥" * {i * 2 - 1}}")
#     i = i + 1

# teacher answer
# i = 1
# rows = int(input("Please tell the no of rows?: "))
# pattern = input("Please tell the pattern?: ")
# while i <= rows:
#     odd_num = 2 * i - 1
#     spaces = rows - i
#     print(" " * (spaces) + pattern * (odd_num))
#     i = i + 1


# for i in range(3):
#     print(i)


# for i in range(1, 4):
#     print(i)


# Task - Convert below to for loop

# i = 1

# while i <= 5:
#     print("🔥" * i)
#     i = i + 1

# sol1
# i = 1

# for i in range(1, 6):
#     print("🔥" * i)

# sol2
# row_number = int(input("Please tell me number? :"))
# for i in range(1, row_number + 1):
#     print("🔥" * i)


# Task 1.2 - Convert below to for loop

# i = 1
# rows = int(input("Please tell the no of rows?: "))
# pattern = input("Please tell the pattern?: ")
# while i <= rows:
#     print(pattern * i)
#     i = i + 1 # increment

# sol1
# rows = int(input("Please tell the no of rows?: "))
# pattern = input("Please tell the pattern?: ")
# for i in range(1, rows + 1):
#     print(pattern * i)

# Task - 1.3

# 4
# 16
# 36
# 64
# 100
# 144

# sol1
# for i in range(1, 7):
#     print(4 * i**2)

# sol2
# for i in range(2, 13, 2):
#     print(i**2)

# sol3
# num = int(input("Please tell me number? :"))
# for i in range(2, num * 2 + 1, 2):
#     print(i**2)
