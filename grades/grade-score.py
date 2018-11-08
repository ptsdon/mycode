#!/usr/bin/env python3
message = 'Numeric Score to Letter Grade Program '
print('Please enter numeric test score')
score = int(input())
if score  >= 90 and score <= 100:
    print("Your letter grade is an A")
elif score  >= 80 and score <= 89:
    print("Your letter grade is an B")
elif score  >= 70 and score <= 79:
    print("Your letter grade is an C")
elif score  >= 60 and score <= 69:
    print("Your letter grade is an D")
elif score  <= 59:
    print("Your letter grade is an F")
print(message)
