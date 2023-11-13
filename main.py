import time
game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]
player1="X"
player2="Y"

score_player1=0
score_player2=0
seconds = 5





quit = True
def countdown(t):
    while t>=0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print(f'\r{timer}', end='')
        time.sleep(1)
        t -= 1



def chance():
    global quit

    while quit:
        current = True
        if current is True:

            print("\nIts player1 chance: ")
            a=int(input("Choose a number from 1-9: "))


            if a in range(0,10):
                a=a-1
                game_board[a]="X"
                display(game_board)
                quit= result()
                if quit is False:
                    break


            else:
                print("Enter valid input")

        current= False

        if current is False and quit is True:

            print("\nIts player2 chance: ")
            b = int(input("Choose a number from 1-9: "))


            if b in range(0,10):
                b=b-1
                game_board[b] = "Y"
                display(game_board)

                quit=resplayer2()
                if quit is False:
                    break


            else:
                print("Enter valid input")





def player1_result():
    global score_player1
    global score_player2
    print("Player 1 won ")
    score_player1 = score_player1 + 1
    print("Player 1 Score is: ", score_player1)
    print("Player 2 Score is: ", score_player2)
    quit = False
    return quit

def player2_result():
    global score_player1
    global score_player2
    print("Player 2 won")
    score_player2 = score_player2 + 1
    print("Player 2 Score is: ", score_player2)
    print("Player 1 Score is: ", score_player1)
    quit = False
    return quit


def draw():
    count = 0
    for i in range(0, 9):
        if (game_board[i] != "-"):
            count = count + 1
            if (count == 9):
                print("Player 1 Score is: ", score_player1)
                print("Player 2 Score is: ", score_player2)
                return False
        else:
            quit = True
            return quit



def result():
    global score_player1
    global quit
    if(game_board[0]=="X" and game_board[1]=="X" and game_board[2] == "X"):
        return player1_result()




    elif(game_board[3]=="X" and game_board[4]=="X" and game_board[5] == "X"):
        return player1_result()


    elif(game_board[6]=="X" and game_board[7]=="X" and game_board[8] == "X"):
        return player1_result()

    elif(game_board[0]=="X" and game_board[3]=="X" and game_board[6] == "X"):
        return player1_result()
    elif(game_board[1]=="X" and game_board[4]=="X" and game_board[7] == "X"):
        return player1_result()
    elif(game_board[2]=="X" and game_board[5]=="X" and game_board[8] == "X"):
        return player1_result()
    elif(game_board[0]=="X" and game_board[4]=="X" and game_board[8] == "X"):
        return player1_result()
    elif(game_board[2]=="X" and game_board[4]=="X" and game_board[6] == "X"):
        return player1_result()


    else:
        return draw()


def resplayer2():
    global score_player2
    global quit
    if (game_board[0]== "Y" and game_board[1]== "Y" and game_board[2] == "Y"):
           return player2_result()
    elif (game_board[3]== "Y" and game_board[4]== "Y" and game_board[5] == "Y"):
           return player2_result()
    elif (game_board[6]== "Y" and game_board[7]== "Y" and game_board[8] == "Y"):

        return player2_result()
    elif (game_board[0]== "Y" and game_board[3]== "Y" and game_board[6] == "Y"):
        return player2_result()
    elif (game_board[1]== "Y" and game_board[4]== "Y" and game_board[7] == "Y"):
        return player2_result()
    elif (game_board[2]== "Y" and game_board[5]== "Y" and game_board[8] == "Y"):
        return player2_result()
    elif (game_board[0]== "Y" and game_board[4]== "Y" and game_board[8] == "Y"):
        return player2_result()
    elif (game_board[2]== "Y" and game_board[4]== "Y" and game_board[6] == "Y"):
        return player2_result()
    else:
        return draw()



def display(game_board):
    print("\n")
    print("|"+game_board[0]+"|"+game_board[1]+"|"+game_board[2]+"|")
    print("|"+game_board[3] + "|" + game_board[4] + "|" + game_board[5] + "|")
    print("|"+game_board[6] + "|" + game_board[7] + "|" + game_board[8] + "|")
    print("\n")


def resetgameboard(gameboard):
    for i in range(0,9):
        gameboard[i]="-"


display(game_board)


chance()
print("finished")
stop=True
while stop:
    print("Do you want to play again. ")
    restart = input("Enter Yes or No:").upper()
    if restart=="YES":
        resetgameboard(game_board)
        display(game_board)
        quit=True
        chance()
    else:
        print("Thankyou")
        stop=False



