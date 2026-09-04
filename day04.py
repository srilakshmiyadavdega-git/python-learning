#if
n = 1
if n == 1:
    print(1)
print(2)
print()     #1, 2

#if-else 
n = 10
if n == 10:
    print(1)
else:
    print(2)
print(3)
print()         #1, 3 
if n == 20:
    print(1)
else:
    print(2)
print(3)       #2, 3
print()      

#if-elif-else
n = 3
if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(3)
else:
    print(10)
print(11)
print()      # 3 , 11
n = 5
if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(3)
else:
    print(10)      # 10, 11
print(11)

#nested-if
ch = 'A'  #one char
if ch.isalpha():
    if 65 <= ord(ch) <= 90:
        print('upper case letter')     #upper case letter
    elif 97 <= ord(ch) <= 122:
        print('lower case letter')
else:
    print('not an letter')
print(1)

#match case 
day = 5 
match day:
    case 1: 
        print('Sunday')
    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')      # thursday
    case 6:
        print('Friday') 
    case 7:
        print('Saturday')