import random
computer_number=random.randint(0,20)
count=0
for i in range(10):
    user_number=int(input())
    count=count+1
    if user_number==computer_number:
        print("successful")
        print(count)
        break
    elif user_number>computer_number:
        print("Go down")

    elif user_number<computer_number:
        print("Go up")