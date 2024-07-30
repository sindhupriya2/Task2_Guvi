#program 1: write a program to calculate total number of vowels and count each vowels in the string "Guvi Geeks Network Private Limited"

string=input("Enter the String: ")
new_string=string.lower()
l=['a','e','i','o','u']
count=0
for char in new_string:
    if char in l:
        count=count+1
        print(char)
print(count)

# Program 2-Pyramid of numbers from 1-20 using for loop

print("\t\t\t\t\tpyramid of numbers")

for i in range(1 , 21):
    for j in range(21 - i):
        print(" ", end =" ")
    for j in range(1, i):
        print(j, end =" ")
    for i in range(i, 0, -1):
       print(i, end = " ")

    print("\n")


# Program 3 - write a program that takes a string and returns new string after removing the vowels

str=input("Enter String" )
vowels_string="aeiouAEIOU"
print("input string",str)
for char in str:
    if char in vowels_string:
        str=str.replace(char,"")
print("output string without vowels", str)



# Program 4 - write a program that takes a string and returns the number of unique characters in it

s="hello"
u={}
for i in s:
    u[i]=0
for i in s:
    u[i]=u[i]+1
print(u)
for i in s:
    if (u[i]==1):
        print(i)


# Problem 5 - write a program that takes a string and returns true if it is palindrome and false if not.
x = input("Enter here: ")
w = ""
for i in x:
    w += i

if (x == w):
    print("true")
else:
    print("false")


# Problem 6 - write a program that takes a string and returns most frequent character in it.

x = input("Enter any String : ")
d = {}
for c in x:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1
print(d)
print(max(d, key=d.get))


# Program 7 - write a program that takes string and returns True if it is an Anagram of an another string, False  otherwise.

str1 = input("string1:")
str2 = input("string2:")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if sorted_str1 == sorted_str2:
    print("True")
else:
    print("False")


# Program 8 - Write a program that takes string and returns number of words in it.

str = input("Enter your text here: ")
print("you have entered the text:" + str)

list = str.split()
length = len(list)
print("Total number of words are:" + str(length))


# Program 9 - Write a program that takes two strings and retuns the longest common substring in it.
 
def substr(str1 , str2):
    ans = 0
    for i in range(len(str1)):
     for j in range(len(str2)):
         k=0
         while((i+k) < len(str1) and (j+k) < len(str2) and str1[i+k] == str2[j+k]):
             k=k+1
        ans = max(ans,k)
     return ans
     
            


