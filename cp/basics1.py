for i in range(1,10+1):
    print(i)

# how use reverse slicing
name = "Amarjit Singh"
print("\n"+ name[-5:]) # print the surname

# use for loop to see chars
value = "We win"
for i in value:
    print(str(i)) # print all the chars

# Add the string chars to a list
valueTwo = "second line"
print([str(x) for x in valueTwo])

alpha = 'abcdefghijklmnopqrstuvwxyz'
print("reversed string =" + alpha[::-1])
print(alpha[-10:-13])       # won't print as end <  begining
print(alpha[-1:-4:-1])      # zyx
print(alpha[4::-1])         # edcba
print(alpha[-1:-9:-1])      # last 8 chars

students = ['alpha', 'beta', 'gamma']
print("\n" + students[1][1:]) # will print all chars from index 1 of beta [eta]

# use of apostophe
print("""He's is trying to write an journal""")

print("this can " 'be ' 'written ' "without using the + operator")

print("this can " ,'be ', 'written ', students[1])

print('hello ' * 5) # will repeat it 5 times


today = 'Friday'
print("day is present in 'today'" if 'day' in today else "day is not present in 'today'")
print("Day is present in 'today'" if 'day' in today else "Day is not present in 'today'")

# string replacements

# using the format
age = 27
joinedYear = 2
print("My age is {0} years and I joined the Saba {1} years ago".format(age, joinedYear))

print("There are 31 days in {1}, {3}, {0}, and {2}".format("Jan", "March","May","July"))

# using the width in format
for i in range(1,13):
    print("the square of {0:2} is {1:<3} and division by 3 is {2:4.4}".format(i, i **2, i/3))


company_name = "saba software"
print(list(company_name)) # convert an string into an list

salaries_list = [-32,1523,13131,313,1,13131,13,453,535,232,103,100,101,102,102]
print(sorted(set(salaries_list))) # set will take unique values and sorted will create a new list


males = ['amar', 'ammy', 'vicky', 'jazz']
females = ['alice', 'brenda', 'stef', 'nan']

males.append('vishal')

added_list = males+ females # this will add them to one list
persons = [males, females]  # this will add 2 lists as a part of a bigger sublist

print("\nAdded list = ", added_list)
print("Container list = ",  persons)

for persons_list in persons:
    for x in persons_list:
        if x not in ["amar", "vicky"]: # filter amar and vicky
            print(x , end= " ")


#  using iterator
names_iter = iter(persons)
print('\n\nprinting iterator values')
print(next(names_iter)[2:])     # will print the second onwards sub-items in iterator
print(next(names_iter))         # will print the second item in iter

# print all values using iter and len()
days = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
days_iter = iter(days) # make an iterator

print('\nprint all values using iter and len()')
for i in range(0,len(days)):
    print(next(days_iter), end="\n")

# create a list of even numbers till 20
print(list(range(0,20,2)))








