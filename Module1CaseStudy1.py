# find factors of given number

num = int(input("Finding Factors of a number. Enter a number: "))

print("The factors of ", num, " are: ")
for i in range(1, num+1):
    if num % i == 0:
        if i % 2 == 0:
            print(i, "EVEN")
        else:
            print(i, "ODD")

# sorting sequence of words alphabetically
print("\n")
myStr = input("Sorting words alphabetically. Enter a string: ")

allWords = [word.lower() for word in myStr.split()]
allWords.sort()

print("Sorted words: ")
for word in allWords:
    print(word)

# find all the numbers between 1000 and 3000 such
# that each digit of a number is an even number
print("\n")
print("Printing numbers between 1000 and 3000 where all digits are even")
items = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        items.append(s)

print(items)

# Enter a sentence and calculate the number of letters and digits
print("\n")
sentence = input("Counting letters and digits in a string. Enter a string: ")
digitCount = letterCount = 0
for c in sentence:
    if c.isdigit():
        digitCount += 1
    elif c.isalpha():
        letterCount += 1
    else:
        pass
print("Letters: ", letterCount)
print("Digits: ", digitCount)

#  find the given number is Palindrome number or not
print("\n")
myNum = int(input("Finding if a number is Palindrome. Enter a number:"))
temp = myNum
rev = 0
while myNum > 0:
    dig = myNum % 10
    rev = rev * 10 + dig
    myNum = myNum // 10
if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")