# Check if a string is a palindrome

text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# Check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Print numbers from 1 to 10

for i in range(1, 11):
    print(i)

# Count vowels in a string

text = input("Enter a sentence: ").lower()
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)