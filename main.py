message = "Hello World"
print(message)

first_Name = "Tengiz"
last_Name = "Gachechiladze"
print(f"{first_Name} {last_Name.upper()} is {10*2+2} years old")

a,b,c = 1,2,3

numbers = [a, b, c, 4, 5, 6.0, 7, 8, 3 ]
print(numbers)
print(f'\n{numbers[0]}')

numbers.append(7)
numbers[len(numbers)-4] = 9
print(numbers)
removed_elem = numbers.pop() #can pass index or value as well
print(numbers)
numbers.sort() #sorted() will just print if list is sorted
print(numbers)
print(numbers[-1])

for number in numbers:
    print(number)

for value in range(10,20):
        print(value)

even_numbers = list(range(2,11,2))
print(even_numbers)

print((even_numbers[0:3]))

even_numbers_copy = even_numbers[:]
print(even_numbers_copy)

print((2,4)) #tuple is immutable

for number in numbers:
    if number == 6.0:
        print(number)
    else:
        pass

for number in numbers:
    if number > 2 and number < 5:
        print(number)
    else:
        pass

if numbers[0] > 5:
    print(numbers[0])
elif numbers[0] < 2:
    print("Hello")
else:
    print("Bye")

message = input("Enter the message ")
print(message)

age = input("Enter the age ")
print(int(age))

while 3 in numbers:
    numbers.remove(3)
print(numbers)

my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])

my_dict["DateOfBirth"] = '1999-03-07'

print(my_dict)

def example_function(*args):
    for arg in args:
        print(arg)

example_function(1, 2, 3)
example_function('a', 'b', 'c', 'd')