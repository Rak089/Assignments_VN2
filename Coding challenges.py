# 1. Implement palindrome using iterator(for loop) and generator mechanism.
# Using generator mechanism


def palindrome_generator():
    """Generates palindromic numbers."""

    palindromes = []

    for count in range(1000):
        n = str(count) # typecasting the count variable from int to a string
        if n == n[::-1]: # checking for slice condition
            palindromes.append(n)

    yield palindromes


x = palindrome_generator()
print(next(x))


# using for loop to check a given number to a palindrome

num = input("Enter any number :")

i = 0

for i in range(len(num)):

    if num[i] != num[-1 - i]:
        print('It is not a palindrome')
        break

    else:
        print('It is a palindrome')
        break


# string checking for palindrome

word = input("Enter any word :")

rev = reversed(word)

if list(word) == list(rev):
    print('It is a palindrome')

else:
    print('It is not a palindrome')


# 2. Sum of 2 digits into output

n1 = input("Enter your first 4 digit number: ")
n2 = input("Enter your second 4 digit number: ")

a, b, c, d = n1[0], n1[1], n1[2], n1[3]
e, f, g, h = n2[0], n2[1], n2[2], n2[3]

a1 = int(a) + int(e)
a2 = int(b) + int(f)
a3 = int(c) + int(g)
a4 = int(d) + int(h)

output = a1 + a2 + a3 + a4
print(f"The required output is {output}")

# 4. #findout elements duplicate count output in  dict format

def sumList(l1):
    dic = {}
    for i in l1:
        if i in l1:
            dic[i] = dic.get(i, 0)+1
            pass
        else:
            dic[i] = dic.count(i)
    return dic


some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
l2 = sumList(some_list)
print("The given list is :", some_list)
print("The Output of Dictionary is :", l2)
print()

# 5. Combine of two lists

def combine_list(t1, t2):
    t3 = []
    for i in t1:

        for j in range(len(t2)):

            if(type(i) is type(t2[j])):

                t3.append(i+t2[j])
                t2.remove(t2[j])

                break
    return t3


t1 = [1, 2, 3, "a", "c"]
t2 = ["b", "d", 9, 8, 7]
print(combine_list(t1, t2))

# 6.ip address program


def ip_addr(str1):
    str2 = ""
    for i in str1:
        if i != "0":
            str2 += i
    return str2


ip = input("Enter the ip address: ")
print(ip_addr(ip))

# 7. Nested list to flat list


def single_list(l1):
    l2 = []

    for i in l1:
        if type(i) is list:
            l2.extend(single_list(i))
        else:
            l2.append(i)
    return l2


l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(single_list(l))