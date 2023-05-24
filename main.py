from pictures import flasher, man, woman, heart, game_over, game_over1, poop

print("Welcome to The Game of Finding Your Princess!")

first_question = input("You are in a dark forest and do not have any lights. You need to find the way out.\nWhere do you want to go? Left\nRight\nStraight?\n").lower()
print(" ")
if first_question == "straight":
  second_question = input("Correct! You walk out the dark forest and see 3 glasses with liquids. Which would you choose:\nTransparent\nRed\nBlack?\n").lower()
  print(" ")
  if second_question == "red":
    third_question = input("Congratulations! It was wine! You got more relaxed and see now the castle in front of you.\nYou need to call your princess.\nWhat you choose?\nMy love!\nHello! Woman!\nHey you!\n").upper()
    print(" ")
    if third_question == "MY LOVE!":
      print("You win!")
      print(heart)
    elif third_question == "HELLO! WOMAN!":
      print("Some prostitute comes out.\nYou lose.")
      print(woman)
    else:
      print("That was rude. The princess will not come out.\nYou loose.")
      print(poop)
      print(game_over1)
  elif second_question == "transparent":
    print("Oh no! It was poison!\nGame over.")
    print(game_over)
  else:
    print("It was coffee and you are having a heart attack.\You loose.\nGame over.")
    print(game_over)
elif first_question == "left":
  print("Oops! You ran into a pervert and got flashed!\nGame over.")
  print(flasher)
  print(game_over1)
else:
  print("Mistake! There is a knight showering you stepped on his soap and he catches you.\nYou loose.\nGame over")
  print(man)
  print(game_over1)
