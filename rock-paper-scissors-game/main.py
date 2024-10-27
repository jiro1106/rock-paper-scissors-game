import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#rules


random_choice_for_computer = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice == 0:
    print(rock)
    print("Computer chose:")
    computer_choice = (random.choice(random_choice_for_computer))
    print(computer_choice)

    if computer_choice == random_choice_for_computer[0]:
        print("It's a draw")
    elif computer_choice == random_choice_for_computer[1]:
        print("You lose!")
    elif computer_choice == random_choice_for_computer[2]:
        print("You win!")
elif user_choice == 1:
    print(paper)
    print("Computer chose:")
    computer_choice = (random.choice(random_choice_for_computer))
    print(computer_choice)

    if computer_choice == random_choice_for_computer[0]:
        print("You win!")
    elif computer_choice == random_choice_for_computer[1]:
        print("It's a draw")
    elif computer_choice == random_choice_for_computer[2]:
        print("You lose!")
elif user_choice == 2:
    print(scissors)
    print("Computer chose:")
    computer_choice = (random.choice(random_choice_for_computer))
    print(computer_choice)

    if computer_choice == random_choice_for_computer[0]:
        print("You lose!")
    elif computer_choice == random_choice_for_computer[1]:
        print("You win!")
    elif computer_choice == random_choice_for_computer[2]:
        print("Its a draw!")
else:
    print("Wrong input!")

