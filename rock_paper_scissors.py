import random
me = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if me not in [0,1,2]:
    print("You type an invalid number. You Lose")
else:
    computer = random.randint(0,2)
    if computer == 0:
        print("Computer chose: Rock")

    elif computer == 1:
        print("Computer chose: Paper")

    else:
        print("Computer chose: Scissors")

    table = [["It's a draw","You Lose","You Win"],
             ["You Win","It's a draw","You Lose"],
             ["You Lose","You Win","It's a draw"]]

    print(table[me][computer])
