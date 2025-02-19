#SOLUTION_1
START = int(input("Enter start: "))
END = int(input("Enter end: "))

current_number = START
while current_number <= END:
    if current_number % 5 == 0 and current_number % 7 == 0:
        print(current_number)
    current_number += 1

######################################################################

#SOLUTION_2
START = int(input("Enter start: "))
END = int(input("Enter end: "))
lcm = 5 * 7
first_multiple = (START // lcm + 1) * lcm
number = first_multiple

while number <= END:
    print(number)
    number += lcm

