
Question1= ("A _______ is defined as a weakness or flaw in the design, implementation "
            "or behaviors of a system or application.")
Question2= ("An_____ is something such as an action or bahior that utilizes "
            "a nulnerability on system or application. ")

print(Question1)
answer1= input("Enter the answer:")

if answer1=="Vulnerability":
    print("Your answer is right, Do you want to see the same question again?")
    choice=input("Enter YES/NO: ")
    if choice=="yes":
        print(Question1)
        answer1 = input("Enter the answer:")
    elif choice=="No":
        print(Question2)
        answer2 = input("Enter the answer:")

else:
    print("Your answer is Wrong, Do you want to see the same question again?")
    choice = input("Enter YES/NO: ")
    if choice == "yes":
        print(Question1)
        answer1 = input("Enter the answer:")
    else:
        print(Question2)
        answer2 = input("Enter the answer:")
        if answer2=="exploit":
            print("Right answer: Do you want to see the same answer again.")
        choice=input("Enter choice YES/ NO:")
        if choice== "yes":
            print(Question2)
            answer2= input("Enter the answer:")
        else:
            print("Quiz ended")
