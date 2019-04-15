#A Rock,Paper,Scissor game

from random import randint
#Let the player choose rock,paper,scissors
player = input('rock(r),paper(p),scissors(s)? ')
print(player, 'vs', end=' ')
#computer's turn to chose
chosen = randint(1,3)
#print(chosen)
if chosen == 1:
  computer = 'r'
elif chosen == 2:
  computer = 'p'
else:
  computer = 's'
print(computer)

if player == computer:
  print("DRAW!")
elif player == 'r' and computer == 's':
  print("You win!")
elif player == 'r' and computer == 'p':
  print("Computer wins!")
elif player == 'p' and computer == 's':
  print("Computer wins!")
elif player == 'p' and computer == 'r':
  print("You win!")
elif player == 's' and computer == 'r':
  print("Computer wins")
elif player == 's' and computer == 'p':
  print("You win!")