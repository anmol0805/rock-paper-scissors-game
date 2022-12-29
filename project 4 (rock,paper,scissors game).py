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

#Write your code below this line 👇

images = [rock, paper, scissors]

user_choice=int(input("what will you choose? type 0 for rock , type 1 for paper and type 2 for scissors. \n"))

if user_choice >= 3 or user_choice < 0:
  print("you typed invalid no. SORRY")
else:
  print(images[user_choice])
  
  computers_choice=random.randint(0, 2)
  print(f"computer choose {computers_choice}")
  print(images[computers_choice])
  
  if user_choice==0 and computers_choice==1:
    print("You Win!")
  elif user_choice==0 and computers_choice==2:
    print("You Win")
  elif user_choice == computers_choice:
    print("It's Draw")
  # elif user_choice < computers_choice:
  # print("You Win!")
  elif user_choice==1 and computers_choice==2:
    print("Computer Win!")
  elif user_choice==2 and computers_choice==1:
    print("You Win!")  
  else:
    print("Computer Win!")