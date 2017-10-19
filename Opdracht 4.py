import sys
import random


def checkInputText(text):
    if (text in ["q", "quit"]):
        print("Ciao!")
        exit(0)

if __name__ == '__main__':
    print(input("Lets play rock-paper-scissors!"))
    print(input("If you want to quit, press 'q' or 'quit' anytime!"))

while True:
    inputText = input("Choose rock, paper or scissors! ")
    checkInputText(inputText)

    ans = random.choice(["rock", "paper", "scissors"])


    if inputText == "rock":
        print(ans)
        if inputText == "rock" and ans == "rock":
            print("Draw!")
            print(" ")
        if inputText == "rock" and ans == "paper":
            print("Haha i win, u lose!")
            print(" ")
        if inputText == "rock" and ans == "scissors":
            print("Aw shit! U win!")
            print(" ")
    if inputText == "paper":
        print(ans)
        if inputText == "paper" and ans == "rock":
            print("Shit! U've won!")
            print(" ")
        if inputText == "paper" and ans == "paper":
            print("Draw!")
            print(" ")
        if inputText == "paper" and ans == "scissors":
            print("Hah i win!")
            print(" ")
    if inputText == "scissors":
        print(ans)
        if inputText == "scissors" and ans == "rock":
            print("Yee, i win!")
            print(" ")
        if inputText == "scissors" and ans == "paper":
            print("Oh no! I lost!")
            print(" ")
        if inputText == "scissors" and ans == "scissors":
            print("Thats a draw!")
            print(" ")