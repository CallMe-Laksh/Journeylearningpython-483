# Today is my first day 5th January 2026
# I already know basic pyhton (if, input, print, mathematical operations, variables and functions)
# Im starting with String operations
# I learnt this from the book "learn python vissualy"* pg 28 - 30
# * - link: https://archive.org/details/learn-python-visually_compress/page/28/mode/2up 

# String Operations

# indexing

# from left to right 0 to n
# from right to left -1 to -(amount of digits in your string) 

name = "My name is laksh"

print(name[0])
print(name[-1])
print(name[-5])

# SLicing - as the name suggest cutting off a certian part of a string

print(name[11:16])

# len calculates the length of a string
print(len(name))

#leaving for today 5-1-26 10:11 PM
#back 6-1-26 7:30 PM

#Concatenation
#joining strings together

print("an exapmle of concatenation is " + "cone " + "cat " + "ten " + "ate")

#Excersizes

#1.There are two strings: one = "John is strong" two = "Tea is not warm".
#  Write Python code to produce a string result = "John is not strong" out of one and two

one = "John is strong"
two = "Tea is not warm"
solution = one[0:7] + two[6:11] + one[8:14]
print(solution)

#2.  Find which of these strings doesn't contain the letter "B": "Foo", "Bar", "Zoo", "Loo".

ans1 = "B" in "Foo"
ans2 ="B" in "Bar"
ans3 = "B" in "Zoo"
ans4 = "B" in "Loo"
print(ans1)
print(ans2)
print(ans3)
print(ans4)
#Thats it for string operations - 6-1-2026, 9:30 PM
