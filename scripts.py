# Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 == 1:
        print('Weird') # Print 'Weird' if n is odd
    else:
        if n in range(2,6): # if 2 <= n <= 5
            print('Not Weird') # print 'Not Weird'
        elif n in range(6,21): # if 6 <= n <= 20
            print('Weird') # print 'Weird'
        elif n>20: # if n is larger than 20
            print('Not Weird') # print 'Not Weird'

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# Write a function
def is_leap(year):
    leap = False
    
    if year % 4 == 0: # if divisible by 4
        leap = True # it's a leap year
        if year % 100 == 0: # unless it's divisible by 100
            leap = False # then it's not a leap year
            if year % 400 == 0: # except when it's divisible by 400
                leap = True # in that case it is a leap year
    
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    grid = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n] # Create list of 3D coordinates (i,j,k) on a grid such that i+j+k != n
    print(grid)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr) # initialize list of scores
    winner = max(scores) # maximum score
    while winner in scores: # eliminate all max scores from the list
        scores.remove(winner)
    runner_up = max(scores) # the next highest score is the runner up
    print(runner_up)

# Nested Lists
if __name__ == '__main__':
    records =[] # initialize list of records
    
    # Read student names and scores
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        
    scores = [records[i][1] for i in range(len(records))] # list of student scores
    min_score = min(scores) # min score
    
    # remove all the minimum scores
    while min_score in scores: 
        scores.remove(min_score)
            
    second_to_last = min(scores) # second to last score is the new min score
    second_to_last_students = [] # initialize list of second to last students
        
    # fill list of second to last students
    for k, student in enumerate(records):
        if records[k][1] == second_to_last: # see if student is second to last
            second_to_last_students.append(records[k][0]) # add this student
    
    for student in sorted(second_to_last_students):
        print(student)

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg_grades = sum(student_marks[query_name])/len(student_marks[query_name]) # avg grade of the query student
    formatted_avg = "{:.2f}".format(avg_grades) # format the avg to have 2 places after decimal
    print(formatted_avg)
    

# Lists
if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        command = input().split() # read the command
        # execute the command specified by the input
        if str(command[0]) == 'insert':
            arr.insert(int(command[1]),int(command[2]))
        if str(command[0]) == 'print':
            print(arr)
        if str(command[0]) == 'remove':
            arr.remove(int(command[1]))
        if str(command[0]) == 'append':
            arr.append(int(command[1]))
        if str(command[0]) == 'sort':
            arr.sort()
        if str(command[0]) == 'pop':
            arr.pop()
        if str(command[0]) == 'reverse':
            arr.reverse()
            
# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list) # turn integer list into a tuple
    print(hash(t)) # print the result of hash(t)

# sWAP cASE
def swap_case(s):
    s = s.swapcase()
    return s

# String Split and Join
def split_and_join(line):
    # write your code here
    line = line.split(' ') # Split the line on a " " space
    line = '-'.join(line) # Join the line using - hyphen
    return line

# What's Your Name?
def print_full_name(first, last):
    s = 'Hello {0} {1}! You just delved into python.'.format(first,last)
    print(s)

# Mutations
def mutate_string(string, position, character):
    new_string = string[:position] + character + string[position+1:]
    return new_string

# Find a string
def count_substring(string, sub_string):
    occurrences = 0 # initialize number of occurrences
    index = 0 # initialize starting index for looking for a substring 
    while sub_string in string:
        occurrences += 1 # add this occurrence to the counter
        index = string.find(sub_string)+1 # modify the search index in order not to encounter the same occurrence twice
        string = string[index:] # reassign the string, only keeping the slice that contains potential other occurrences
    return occurrences

# String Validators
if __name__ == '__main__':
    s = input()
    # initialize boolean list that will be True at position i if the associated requirement is satisfied
    specific_char_exists = [False,False,False,False,False]
    for char in s:
        if char.isalnum() and specific_char_exists[0]==False:
            specific_char_exists[0] = True # alphanumeric char exists
        if char.isalpha() and specific_char_exists[1]==False:
            specific_char_exists[1] = True # alphabetical char exists
        if char.isdigit() and specific_char_exists[2]==False:
            specific_char_exists[2] = True # digit exists
        if char.islower() and specific_char_exists[3]==False:
            specific_char_exists[3] = True # lowercase char exists
        if char.isupper() and specific_char_exists[4]==False:
            specific_char_exists[4] = True # uppercase char exists
        
    for el in specific_char_exists:
        print(el)

# Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap
import textwrap

def wrap(string, max_width):
    new_string = textwrap.wrap(string,max_width) # split into list of max width lines
    new_string = '\n'.join(new_string) # join the elements into one string
    return new_string

# Designer Door Mat
N, M = map(int, input().split())
K = (N-1)//2

# first line
print(('.|.').center(M,'-'))

# upper half
for n in range(1,K):
    print(('.'+(2*n)*'|..'+'|.').center(M,'-'))
    
# middle text
print('WELCOME'.center(M,'-'))

# lower half
for n in range(K-1,0,-1):
    print(('.'+(2*n)*'|..'+'|.').center(M,'-'))
    
# last line
print(('.|.').center(M,'-'))

# String Formatting
def print_formatted(number):
    # get length of the binary number for formatting purposes
    width = len(str(bin(number)[2:]))
    
    # print each number from 1 to number in bases 10, 8, 16, 2
    for i in range(1,number+1):
        octal = str(oct(i))[2:] # remove the '0o' of octal numbers
        hexadecimal = str(hex(i)).upper()[2:] # remove the '0x' of hexadecimal numbers
        binary = str(bin(i))[2:] # remove the '0b' of binary numbers
        print('{0:{4}} {1:>{4}} {2:>{4}} {3:>{4}}'.format(i,octal,hexadecimal,binary,width))

# Alphabet Rangoli
import string
def print_rangoli(size):
    # get all the lowercase letters that will be in the Rangoli
    letters = string.ascii_lowercase[0:size] 
    
    # calculate width of the Rangoli
    width = 4 * size - 3
    
    # build the upper half of the Rangoli
    extremities = '{0:-^{1}}'.format(letters[-1],width) # top and bottom rows
    upper_half = extremities +'\n' # 'initialize' upper half string
    lower_half = extremities # 'initialize' lower half string
    for row in range(1,len(letters)):
        row_letters = letters[-row-1:][::-1] + letters[-row:] # letters in this row
        spaced_row = '-'.join(list(row_letters)) # connect the letters with '-' hyphens
        formatted_row = '{0:-^{1}}'.format(spaced_row,width) # format the row
        upper_half = upper_half + formatted_row + '\n' # add the new row to the upper half
    
    # build the lower half ot the Rangoli
    lower_half = upper_half[-width-3::-1]
    
    # unify both halves
    rangoli = upper_half + lower_half
    print(rangoli)
    

# Capitalize!
def solve(s):
    capitalized = [word.capitalize() for word in s.split(' ')]
    return ' '.join(capitalized)

# The Minion Game
def minion_game(string):
    stuart_points = 0
    kevin_points = 0
    
    for pos, letter in enumerate(string):
        if letter in 'AEIOU': # if the letter is a vowel
            kevin_points += len(string[pos:]) # give Kevin a point for every following substring 
        if letter not in 'AEIOU': # if letter is not a vowel
            stuart_points += len(string[pos:]) # give Stuart a point for every following substring
            
    # print the winner and his points, or print 'Draw'
    if stuart_points > kevin_points:
        print(f'Stuart {stuart_points}')
    if kevin_points > stuart_points:
        print(f'Kevin {kevin_points}')
    if stuart_points == kevin_points:
        print('Draw')

# Merge the Tools!
import textwrap
def merge_the_tools(string, k):
    divided_string = textwrap.wrap(string,k) # divide string into n/k parts
    for i in range(len(divided_string)):
        seen_letters = set() # set of already encountered letters
        end_string = [] # list to store new letters in order
        for letter in divided_string[i]:
            if letter not in seen_letters: # if the letter is new
                seen_letters.add(letter) # add it to the seen letters
                end_string.append(letter) # add this letter to the list
                
        print(''.join(end_string)) # print the final word

# Introduction to Sets
def average(array):
    plants = set(array) # turn array into set (no duplicates)
    return '{0:.3f}'.format(sum(plants)/len(plants))

# Symmetric Difference
# Read Input
M = input()
set1 = set(map(int,input().split()))
N = input()
set2 = set(map(int,input().split()))

symm_diff = set1.difference(set2).union(set2.difference(set1)) # Create symmetric diff set
for el in sorted(list(symm_diff)):
    print(el)

# No Idea!
# Store the input
n, m = map(int,input().split())
array = map(int,input().split())
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0 # initialize happiness
for i in array:
    if i in A:
        happiness += 1 # add 1 to happiness if i is in A
    if i in B:
        happiness -= 1 # subtract 1 from happiness if i is in B
print(happiness)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
distinct_stamps = set() # initialize the set of distinct country stamps
for _ in range(N):
    country = input()
    if country not in distinct_stamps:
        distinct_stamps.add(country) # add this country to the distinct stamps
print(len(distinct_stamps))

# Set .discard(), .remove() & .pop()
# Enter your code here. Read input from STDIN. Print output to STDOUT
# read input
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    command = input().split() # split command line into a list
    if command[0] == 'remove' and int(command[1]) in s: # if command is remove and the given element is in the set
        s.remove(int(command[1])) # remove that element
    elif command[0] == 'remove' and int(command[1]) not in s: # otherwise use discard
        s.discard(int(command[1])) 
    if command[0] == 'discard': # if command is discard
        s.discard(int(command[1])) # discard the given element
    if command[0] == 'pop': # if command is pop
        if s: # if set s not empty
            s.pop() # remove an element
print(sum(s))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))
total = english.union(french) # students subscribed to French or English newspapers
print(len(total))

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))
both = french.intersection(english) # students subscribed to both newspapers
print(len(both))

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))
print(len(english.difference(french))) # print set diff between english and french set

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
english = set(map(int,input().split()))
b = int(input())
french = set(map(int,input().split()))
print(len(english.symmetric_difference(french))) # print symm diff set length

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
numA = int(input())
A = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    command = input().split()
    other = set(map(int,input().split()))
    if command[0] == 'update': # if command is 'update'
        A.update(other) # add other set's elements to A (if not already there)
    if command[0] == 'intersection_update': # if commmand is 'intersection_update'
        A.intersection_update(other) # update A and perform intersection with other set
    if command[0] == 'difference_update': # if command is 'difference_update'
        A.difference_update(other) # update A performing set difference on A and the other set
    if command[0] == 'symmetric_difference_update': # if command is 'symmetric_difference_update'
        A.symmetric_difference_update(other) # update A performing symmetric difference on A and the other set
print(sum(A)) # print sum of A's final elements

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
room_list = map(int,input().split())
seen_once = set() # initialize set of room numbers seen once
seen_twice = set() # initialize set of room numbers seen twice
for i in room_list:
    if i not in seen_once: # if the room number hasn't been seen yet, add it to seen_once
        seen_once.add(i)
    else: # otherwise add it to seen_twice to show that the number has been seen before
        seen_twice.add(i)
captain = seen_once.difference(seen_twice) # remove from seen_once all the numbers that have been seen twice
print(captain.pop()) # print the only element in the set captain

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    numA = int(input())
    A = set(map(int, input().split())) # read set A
    numB = int(input()) 
    B = set(map(int, input().split())) # read set B
    
    if A.issubset(B): # check if A is subset of B
        print(True)
    else:
        print(False)

# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read input
A = set(map(int,input().split()))
N = int(input())
is_superset = True # bool variable that becomes wrong if A is not a superset
for _ in range(N):
    s = set(map(int,input().split())) # read the set s
    if not s.issubset(A) or len(s)>=len(A): # if s is not a subset of A or not shorter than A, A cannot be a strict supersubset
        is_superset = False
        break # iterations can stop if A is not a strict superset
        
print(is_superset)

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input()) # number of shoes
shoe_sizes = map(int,input().split()) # list of all shoe sizes
N = int(input()) # number of costumers
available_sizes = Counter(shoe_sizes) # counter of available shoe sizes
earned = 0 # initialize amount of money earned
for _ in range(N):
    costumer = list(map(int,input().split()))
    if costumer[0] in available_sizes:
        earned += costumer[1] # increase money earned
        available_sizes[costumer[0]] -= 1 # decrease counter of this size
        if available_sizes[costumer[0]] == 0: # if this counter reached 0
            del available_sizes[costumer[0]] # remove this shoe size
print(earned)

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = list(map(int,input().split()))
words = defaultdict(list) # initialize defaultdict to store words
for _ in range(n):
    words['A'].append(input()) # add input word to group A
for i in range(m):
    new_word = input()
    words['B'].append(new_word) # add this new word to group B
    indeces = [i+1 for i,word in enumerate(words['A']) if word==new_word]
    if indeces: # if the new word in B appears in A
        print(' '.join((map(str,indeces)))) # print the indeces next to each other
    else: # otherwise print -1
        print(-1)

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
Student = namedtuple('Student',input().split()) # create namedtuple class for students
marks = [] # initialize list of marks
for _ in range(N):
    new_student = Student._make(input().split()) # create a tuple for the student
    marks.append(int(new_student.MARKS)) # access the mark of this student, add to list
avg_marks = sum(marks)/len(marks) # calculate avg grade
print(avg_marks)

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
items_bought = OrderedDict() # create ordered dictionary to store items in order
for i in range(N):
    new_item = input().split() # read item name and net price
    item_name = ' '.join(new_item[:-1]) # retrieve the name
    if item_name not in items_bought: # if the item isn't in the dictionary yet
        items_bought[item_name] = int(new_item[-1]) # add item and its price
    else: 
        items_bought[item_name] += int(new_item[-1]) # add price to existing item
for item in items_bought.items():
    print(item[0],item[1])

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input()) # number of words
words = OrderedDict() # initialize ordered dictionary of words
for _ in range(n):
    word = input() # read word
    if word not in words: # if this word isn't in the dictionary yet
        words[word] = 1 # add it to the dictionary with initialized counter 1
    else:
        words[word] += 1 # if the word is already in the dictionary, increase its counter
print(len(words)) # print the number of distinct words
for word_count in words.values():
    print(word_count, end=' ') # print the number of occurrences of each word
   

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
N = int(input())
d = deque() # create deque object
for _ in range(N):
    command = input().split()
    if command[0] == 'append':
        d.append(int(command[1])) # append an element to the right
    if command[0] == 'pop':
        d.pop() # remove outermost element on the right
    if command[0] == 'popleft':
        d.popleft() # remove outermost element on the left
    if command[0] == 'appendleft':
        d.appendleft(int(command[1])) # append an element to the left
for el in d:
    print(el,end=' ') # print elements

# Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
T = int(input())  # number of test cases
for _ in range(T):
    n = int(input())  # number of cubes
    sideLengths = deque(map(int, input().split()))  # deque with side lengths
    last_cube = float('inf')  # initialize the top of the pile to be infinitely large
    possible = True  # flag to check if it's possible to pile up
    while sideLengths:
        if sideLengths[0] >= sideLengths[-1]: # if the left-most cube is longer than the right
            current_cube = sideLengths.popleft() # this is the next cube to add
        else: # if the right-most cube is longer than the left
            current_cube = sideLengths.pop() # this is the next cube to add
        if current_cube > last_cube: # if the current_cube is longer than the cube on top
            possible = False # you can't stack the cubes
            break
        
        last_cube = current_cube
    if possible:
        print('Yes')
    else:
        print('No')

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    s_list = list(s) # split string s into a list of characters
    counter = Counter(s_list) # turn the list into a counter
    # sort the counter in descending order of occurrence count and then in alphabetical order of letters
    sorted_counter = sorted(counter.items(),key = lambda x: (-x[1],x[0])) 
    for i in range(3): # print the first three letters with their occurrence counters
        print(sorted_counter[i][0],sorted_counter[i][1])

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date = list(map(int,input().split()))
weekdays = {0:'MONDAY',1:'TUESDAY',2:'WEDNESDAY',3:'THURSDAY',4:'FRIDAY',5:'SATURDAY',6:'SUNDAY'}
day = calendar.weekday(date[2],date[0],date[1])
print(weekdays[day])

# Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime, timezone
def time_delta(t1, t2):
    # format datetimes using python docs formats
    time1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    # convert to utc timezone
    utc1 = time1.astimezone(timezone.utc)
    utc2 = time2.astimezone(timezone.utc)
    # calculate time difference
    time_delta = utc1 - utc2
    # Use timedelta.total_seconds
    return str(abs(int(time_delta.total_seconds())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input()) # number of test cases

for _ in range(T):
    a,b = input().split()
    # check if a is an integer, raise ValueError if not
    try:
        a = int(a)
    except ValueError:
        print(f"Error Code: invalid literal for int() with base 10: '{a}'")
        continue
    # check if b is an integer, raise ValueError if not
    try:
        b = int(b)
    except ValueError:
        print(f"Error Code: invalid literal for int() with base 10: '{b}'")
        continue
    # check if integer division is possible, otherwise raise ZeroDivisionError
    try:
        print(a // b)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')

# Incorrect Regex
import re
T = int(input())
for _ in range(T):
    try:
        m = re.compile(input())
        print(True)
    except Exception:
        print(False)

# Zipped!
N, X = list(map(int,input().split()))

students = []

for _ in range(X): # add subject grades
    students += [list(map(float,input().split()))]
# create list of tuples with student grades
students = list(zip(*students))

for i in range(N):
    print(sum(students[i])/X) # avg grade of student i

# Input()
# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = list(map(int,input().split()))
polynomial = input()
result = eval(polynomial) # evaluate polynomial expression
print(result==k) # check if P(x)=k

# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input().strip())
    
    arr.sort(key = lambda x: x[k])
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=' ')
        print('')

# ginortS
s = input()
s_upper = ''
s_lower = ''
s_odd = ''
s_even = ''
for i in range(len(s)):
    if s[i].isupper():
        s_upper = s_upper + s[i]
    elif s[i].islower():
        s_lower = s_lower + s[i]
    elif int(s[i])%2==0:
        s_even = s_even + s[i]
    elif int(s[i])%2==1:
        s_odd = s_odd + s[i]
print(''.join(sorted(s_lower)+sorted(s_upper)+sorted(s_odd)+sorted(s_even)))

# Map and Lambda Function
cube = lambda x: x**3
def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    fib = []
    f1, f2 = 0, 1
    fib.extend([0,1])
    for _ in range(2,n):
        fib.append(f1+f2)
        f1, f2 = f2, f1+f2
    return fib

# Validating Email Addresses With a Filter
def fun(s):
    try:
        split_email = s.split('@')
        username = split_email[0]
        website = split_email[1].split('.')[0]
        extension = split_email[1].split('.')[1]    
    except IndexError:
        return False
    username_requisite = False
    if username.replace('-','').replace('_','').isalnum():
        username_requisite = True
    website_requisite = False
    if website.isalnum():
        website_requisite = True
    extension_requisite = False
    if extension.isalpha() and 0<len(extension)<4:
        extension_requisite = True
    if username_requisite and website_requisite and extension_requisite:
        return True
    else:
        return False
   

# Detect Floating Point Number
T = int(input())
for _ in range(T):
    N = input()
    if (N[0] not in '+-.') and (not N[0].isdigit()):
        print(False)
        continue
    if len(N.split('.'))!=2 or not N.split('.')[1] or not N.split('.')[1].isdigit():
        print(False)
        continue
    if (N.count('+')+N.count('-'))>1 or (N.count('+')==1 and N.index('+')!=0) or (N.count('-')==1 and N.index('-')!=0):
        print(False)
        continue
    try:
        float(N.replace('+','').replace('-',''))
    except TypeError:
        print(False)
        continue
    print(True)

# Re.split()
regex_pattern = r"[,.]"    # Do not delete 'r'.

# Group(), Groups() & Groupdict()
import re
S = input()
m = re.search(r'([A-Za-z0-9])\1+',S)
try:
    print(m.group(1))
except Exception:
    print(-1)

# Re.findall() & Re.finditer()
import re
S = input()
m = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',S)
if m:
    for match in m:
        print(match)
else:
    print(-1)

# Re.start() & Re.end()
import re
S = input()
k = input()
idx = 0
matches = set()
while idx<len(S)-len(k):
    m = re.search(k,S[idx:])
    if m:
        matches.add((m.start()+idx,m.end()+idx-1))
    idx += 1
    
if matches:
    for match in matches:
        print(match)
else:
    print((-1,-1))

# Regex Substitution
import re
N = int(input())
text = ''
for i in range(N):
    if i==0:
        text = input()
    else:
        text = text + '\n' + input()
    
m = re.sub(r'(?<=\s{1})([&]{2})(?=\s{1})','and',text)
n = re.sub(r'(?<=\s{1})([|]{2})(?=\s{1})','or',m)
print(n)

# Validating Roman Numerals
regex_pattern = r"^(M){0,3}(C{1,3}|CD|D|DC{1,3}|CM){0,1}(X{1,3}|XL|L|LX{1,3}|XC){0,1}(I{1,3}|IV|V|VI{1,3}|IX){0,1}$"	# Do not delete 'r'.

# Validating phone numbers
import re
N = int(input())
for _ in range(N):
    number = input()
    m = re.match(r'(7|8|9)(\d{9})$',number)
    if m:
        print('YES')
    else:
        print('NO')

# Validating and Parsing Email Addresses
import re

n = int(input())
for _ in range(n):
    line = input()
    m = re.match(r'([A-Za-z]+) <([A-Za-z]{1})([A-Za-z0-9_.-]*)@([A-Za-z]+)[.]([A-Za-z]{1,3})>$',line)
    if m:
        print(line)

# Hex Color Code
import re
N = int(input())
text = ''
for i in range(N):
    if i==0:
        text = input()
    else:
        text = text + '\n' + input()
        
m = re.findall(r'(#[A-Fa-f0-9]{3,6})(?!\s*[{])', text)
for match in m:
    print(match)

# HTML Parser - Part 1
from html.parser import HTMLParser
class NewHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(f'Start : {tag}')
        for name, value in attrs:
            print(f'-> {name} > {value}')
    def handle_endtag(self,tag):
        print(f'End   : {tag}')
    def handle_startendtag(self,tag,attrs):
        print(f'Empty : {tag}')
        for name, value in attrs:
            print(f'-> {name} > {value}')
N = int(input())
html_code = ''
for i in range(N):
    if i==0:
        html_code = input()
    else:
        html_code = html_code + input()
parser = NewHTMLParser()
parser.feed(html_code)

# HTML Parser - Part 2
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class NewHTMLParser(HTMLParser):
    def handle_comment(self,comment):
        if len(comment.split('\n'))==1:
            print('>>> Single-line Comment')
            print(comment)
        elif len(comment.split('\n'))>1:
            print('>>> Multi-line Comment')
            for el in comment.split('\n'):
                print(el)
    def handle_data(self,data):
        if data!='\n':
            print('>>> Data')
            print(data)
N = int(input())
html_code = ''
for _ in range(N):
    html_code += ('\n' + input())
parser = NewHTMLParser()
parser.feed(html_code)
    

# Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class NewHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print(tag)
        if attrs:
            for name, value in attrs:
                print(f'-> {name} > {value}')
N  = int(input())
html_code = ''
for i in range(N):
    if i==0:
        html_code = input()
    else:
        html_code += ('\n' + input())
parser = NewHTMLParser()
parser.feed(html_code)

# Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
from collections import Counter
T = int(input())
for _ in range(T):
    UID = input()
    
    if max(Counter(UID).values())>1:
        print('Invalid')
        continue
    m = re.findall(r"[A-Z]",UID)
    n = re.findall(r"[0-9]",UID)
    p = re.findall(r"^[A-Za-z0-9]{10}$",UID)
    
    if len(m)<2 or len(n)<3 or not p:
        print('Invalid')
    else:
        print('Valid')
        
        
# Validating Credit Card Numbers
import re
N = int(input())
for _ in range(N):
    
    credit_card = input()
    m = re.findall(r"^[4-6]{1}",credit_card)
    n = re.findall(r"^[0-9]{16}$",credit_card)
    p = re.findall(r"^([0-9]{4})(\-[0-9]{4})(\-[0-9]{4})(\-[0-9]{4})$",credit_card)
    q = re.findall(r"([0-9])\1{3}|([0-9])\-\2\2|([0-9])\3\-\3",credit_card)
    
    if m and (n or p) and (not q):
        print('Valid')
    else:
        print('Invalid')

# Validating Postal Codes
regex_integer_in_range = r"^[1-9]{1}[0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(?=([0-9]{1})[0-9]{1}\1)"

# Matrix Script
#!/bin/python3
import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
chars_in_order = ''.join([matrix[i][j] for j in range(m) for i in range(n)])
m = re.sub(r'(?<=[A-Za-z0-9])[\s!@#$%&]+(?=[A-Za-z0-9])',' ',chars_in_order)
print(m)


# XML 1 - Find the Score
def get_attr_number(node):
    score = 0
    for child in node.iter():
        score += len([attr for attr in child.attrib])
    return score

# XML2 - Find the Maximum Depth
maxdepth = 0
def depth(elem, level):
    global maxdepth
    if not elem:
        pass
    level += 1
    if level>maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)


# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        formatted_nums = []
        for number in l:
            num = number[-10:] # actual number
            formatted_nums.append("+91 {0} {1}".format(num[:5],num[5:]))
        return f(formatted_nums)
    return fun

# Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        people_with_indices = [(person, idx) for idx, person in enumerate(people)]
        people_with_indices.sort(key=lambda x: (int(x[0][2]),x[1]))
        new = [f(person) for person, idx in people_with_indices]
        return new
    return inner

# Arrays
import numpy
def arrays(arr):
    # Reverse the array using two pointers
    first, second = 0, len(arr)-1
    while first<second:
        arr[first],arr[second]=arr[second],arr[first]
        first += 1
        second -= 1
    # convert the array to numpy and print it
    return numpy.array(arr,float)

# Shape and Reshape
import numpy
# read the numbers and turn them into a numpy array
arr = numpy.array(input().strip().split(' '),int)
print(arr.reshape(3,3)) # print the array

# Transpose and Flatten
import numpy
N,M = list(map(int,input().split())) # read matrix dimensions
lines = []
for _ in range(N):
    lines.append(list(map(int,input().split()))) # append new row to the lines list
    
np_array = numpy.array(lines)
print(np_array.transpose(1,0)) # print the transposed the array
print(np_array.flatten()) # print flattened array

# Concatenate
import numpy

N,M,P = list(map(int,input().split())) # read input dimensions
rows1, rows2 = [], []
# Read first array
for _ in range(N):
    rows1.append(list(map(int,input().split())))
# Read second array
for _ in range(M):
    rows2.append(list(map(int,input().split())))
    
array1 = numpy.array(rows1) # first numpy array    
array2 = numpy.array(rows2) # second numpy array
print(numpy.concatenate((array1,array2),axis=0)) # concatenate arrays

# Zeros and Ones
import numpy
dimensions = tuple(map(int,input().split())) # read dimensions
print(numpy.zeros(dimensions,dtype=int)) # print array of zeros
print(numpy.ones(dimensions,dtype=int)) # print array of ones

# Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13') # get the alignment correct
N,M = list(map(int,input().split())) # read dimensions
print(numpy.eye(N,M)) # print identity matrix

# Array Mathematics
import numpy
N, M = list(map(int,input().split()))
rowsA, rowsB = [], []
# read input  arrays
for _ in range(N):
    rowsA.append(list(map(int,input().split())))
for _ in range(N):
    rowsB.append(list(map(int,input().split())))
A = numpy.array(rowsA,dtype=int) # array A
B = numpy.array(rowsB,dtype=int) # array B
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))

# Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13') # set coorect output format
A = numpy.array(list(map(float,input().split()))) # read input array A
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

# Sum and Prod
import numpy
N,M = list(map(int,input().split())) # read input
rows = []
for _ in range(N):
    rows.append(list(map(int,input().split())))
arr = numpy.array(rows) # turn rows into a numpy array
print(numpy.prod(numpy.sum(arr,axis=0))) # print product of the column sums

# Min and Max
import numpy
N, M = list(map(int,input().split())) # read dimensions
rows = []
# read input
for _ in range(N):
    rows.append(list(map(int,input().split())))
arr = numpy.array(rows) # turn rows into a numpy array
print(numpy.max(numpy.min(arr,axis=1))) # print the max among the column mins

# Mean, Var, and Std
import numpy
#numpy.set_printoptions(legacy='1.13') # set coorect output format
# read input
N, M = list(map(int,input().split()))
rows = []
for _ in range(N):
    rows.append(list(map(float,input().split())))
arr = numpy.array(rows) # numpy array
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr,axis=None),11)) # round to 11 decimal places

# Dot and Cross
import numpy
# read input
N = int(input())
rowsA, rowsB = [], []
for _ in range(N):
    rowsA.append(list(map(int,input().split())))
for _ in range(N):
    rowsB.append(list(map(int,input().split())))
A = numpy.array(rowsA) # numpy array A
B = numpy.array(rowsB) # numpy array B
print(A @ B) # print matrix product

# Inner and Outer
import numpy
# read input arrays
A = numpy.array(input().split(),int)
B = numpy.array(input().split(),int)
# print inner and outer products
print(numpy.inner(A,B))
print(numpy.outer(A,B))

# Polynomials
import numpy
P = numpy.array(input().split(),float) # read input array of coefficients
x = float(input()) # read x
print(numpy.polyval(P,x)) # print value of polynomial P at point x

# Linear Algebra
import numpy
# read input
N = int(input())
rows = []
for _ in range(N):
    rows.append(list(map(float,input().split())))
    
A = numpy.array(rows) # numpy array A
print(round(numpy.linalg.det(A),2)) # print determinant of A


# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    return candles.count(max(candles))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v1==v2:
        if x1==x2:
            return 'YES'
        else:
            return 'NO'
    d = (x2-x1)/(v1-v2)
    if d.is_integer() and d>0:
        return 'YES'
    else:
        return 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
day_cache = {1: 2} # new likes on a day (days are keys)
tot_cache = {1: 2} # cumulative likes until a day (days are keys)

def viralAdvertising(n):
    # check if the result for this day is already in the cache
    if n in tot_cache:
        return tot_cache[n]
    # if not, compute values for new days
    for i in range(2, n+1):
        if i not in day_cache:
            day_cache[i] = math.floor((day_cache[i-1]*3)/2)
            tot_cache[i] = tot_cache[i-1] + day_cache[i]
    
    return tot_cache[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

sup_digit_cache = {} # cache that saves past super digits

def superDigit(n, k):
    
    digit_split = lambda x: list(map(int,list(str(x)))) # function that splits digits of a number into a list
    digit_list = digit_split(n) # split number into a digit list
    sup_digit = k*sum(digit_list) # replicate that list k times
        
    # function that sums the digits of a number
    def DigitSum(x):
        if 0<=x<=9: # if there's only one digit
            return x # that's the answer
        else:  # if there's more than one digit
            return DigitSum(sum(digit_split(x))) # recursive digit sum
    
    # if the super digit is already in the cache, return the super digit
    if sup_digit in sup_digit_cache:
        return sup_digit_cache[sup_digit]
    else: # if the super digit isn't in the cache yet, calculate the recursive digit sum
        result = DigitSum(sup_digit)
        sup_digit_cache[sup_digit] = result # add this result to the cache
        return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    if n>1:
        last = arr[n-1] # store the last element of the array
        moving_index = n-2 # initialize moving index
        while moving_index >= 0:
            if arr[moving_index] >= last: # if the element at moving_index is larger than last
                arr[moving_index+1]=arr[moving_index] # update position moving_index+1
                print(' '.join(list(map(str,arr)))) # print current array
                if moving_index == 0: # if we reached the end of the array
                    arr[0]=last # update value at index 0 to last
                    print(' '.join(list(map(str,arr)))) # print current array
            else: # if the element at moving_index is smaller than last
                arr[moving_index+1] = last # update value at moving_index+1 to last
                print(' '.join(list(map(str,arr)))) # print current array
                break # stop the iterations, the array is sorted
            moving_index -= 1 # decrease moving_index

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
# insertionSort1(n,arr) from the previous problem
def insertionSort1(n, arr):
    if n>1:
        last = arr[n-1] # store the last element of the array
        moving_index = n-2 # initialize moving index
        while moving_index >= 0:
            if arr[moving_index] >= last: # if the element at moving_index is larger than last
                arr[moving_index+1]=arr[moving_index] # update position moving_index+1
                if moving_index == 0: # if we reached the end of the array
                    arr[0]=last # update value at index 0 to last
                    print(' '.join(list(map(str,arr)))) # print current array
            else: # if the element at moving_index is smaller than last
                arr[moving_index+1] = last # update value at moving_index+1 to last
                print(' '.join(list(map(str,arr)))) # print current array
                break # stop the iterations, the array is sorted
            moving_index -= 1 # decrease moving_index
# function that sorts the array in ascending order
def insertionSort2(n, arr):
    k = 1
    while k <= n:
        insertionSort1(k,arr) # perform insertionSort1 from left to right
        k += 1
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)
