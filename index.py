import random
while True:
    try:
        possible_options = ["R", "P", "S"]
        player = str(input(
            f"Select an option between {possible_options}\n Where:\n R is Rock\n P is Paper\n S is Scissors "))
        player = player.upper()
        for i in player:
            if i in possible_options:
                print("You picked", player)
                continue
            else:
                print("Invalid input\nSelect an option between (rock, paper, scissors)")

    except:
        print("Invalid input")
        break

    cpu = random.choice(possible_options)
    print(f"\nYou chose {player}, computer chose {cpu}.")

    if player == cpu:
        print(f"Both players selected {player}. Its a tie!")
        continue

    elif player == "R":
        if cpu == "S":
            print("Player(Rock) : CPU(Scissors)")
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Player(Rock) : CPU(Paper)")
            print("Paper covers rock! You lose. CPU win!")
            break
    elif player == "P":
        if cpu == "R":
            print("Player(Paper) : CPU(Rock)")
            print("Paper covers rock! You win!")
            break
        else:
            print("Player(Paper) : CPU(Scissors)")
            print("Scissors cuts paper! You lose.CPU win!")
            break

    elif player == "S":
        if cpu == "P":
            print("Player(Scissors) : CPU(Paper)")
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Player(Scissors) : CPU(Rock)")
            print("Rock smashes scissors! You lose. CPU win!")
            break
