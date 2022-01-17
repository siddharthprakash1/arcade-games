from tkinter import *
import threading
from multiprocessing import Process
from turtle import Screen
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import random
import os

def snake():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.game_over()

        #Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()
def hangman():
    def s1():
        print('---------+')
        print('    |    |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('===========')


    def s2():
        print('---------+')
        print('    |    |')
        print('    O    |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('===========')


    def s3():
        print('---------+')
        print('    |    |')
        print('    O    |')
        print('    |    |')
        print('    |    |')
        print('         |')
        print('         |')
        print('===========')


    def s4():
        print('---------+')
        print('    |    |')
        print('    O    |')
        print('  --|    |')
        print('    |    |')
        print('         |')
        print('         |')
        print('===========')


    def s5():
        print('---------+')
        print('    |    |')
        print('    O    |')
        print('  --|--  |')
        print('    |    |')
        print('         |')
        print('         |')
        print('===========')


    def s6():
        print('---------+')
        print('    |    |')
        print('    O    |')
        print('  --|--  |')
        print('    |    |')
        print('   /    |')
        print('   |     |')
        print('         |')
        print('===========')


    def s7():
        print('---------+')
        print('    |    |')
        print('    O    |')
        print('  --|--  |')
        print('    |    |')
        print('   / \   |')
        print('   | |   |')
        print('         |')
        print('===========')


    print('''
    _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                      |___/  ''')
    print('\n')
    word = []
    guessed_letters = []
    guess_word = []

    x = input('Enter a word for other player to guess: ')
    print('\n' * 25)
    print('\n' * 25)

    for a in x:
        word.append(a.upper())

    tries = 1
    until = ''
    p = 0
    ind = 0
    for l in range(len(word)):
        guess_word.append('_')
    while p == 0:

        guess = input('Guess a letter or the word: ')

        if len(guess) == 1:
            if guess.upper() in guessed_letters:
                print('you already guessed that letter try again!', '\n')
                continue
                print(until, '\n')
                if tries == 1:
                    s1()
                if tries == 2:
                    s2()
                if tries == 3:
                    s3()
                if tries == 4:
                    s4()
                if tries == 5:
                    s5()
                if tries == 6:
                    s6()
                if tries == 7:
                    s7()

            if guess.upper() in word:
                guessed_letters.append(guess.upper())
                print('CORRECT!', '\n')
                count = word.count(guess.upper())
                for u in range(count):
                    ind = word.index(guess.upper())
                    guess_word[ind] = guess.upper()
                    until = ' '.join(guess_word)
                    word.append('_')
                    word[ind] = ''
                print(until, '\n')
                m = ''.join(guess_word)
                if m == x.upper():
                    print('YESSSS, THAT IS THE CORRECT WORD!', '\n')
                    break
                if tries == 1:
                    s1()
                if tries == 2:
                    s2()
                if tries == 3:
                    s3()
                if tries == 4:
                    s4()
                if tries == 5:
                    s5()
                if tries == 6:
                    s6()
                if tries == 7:
                    s7()


            else:
                tries += 1
                guessed_letters.append(guess.upper())
                print('NOPE!', '\n')
                print(until)
                if tries == 1:
                    s1()
                if tries == 2:
                    s2()
                if tries == 3:
                    s3()
                if tries == 4:
                    s4()
                if tries == 5:
                    s5()
                if tries == 6:
                    s6()
                if tries == 7:
                    s7()
                    print('OH NO THE WORD WAS', x.upper())
                    break

        elif (len(guess) != 1):
            if guess.upper() == x.upper():
                print(x.upper())
                print('YESSSS, THAT IS THE CORRECT WORD!', '\n')
                break

            else:
                print(until.upper())
                tries += 1
                print('NOPE!', '\n')
                print(until)
                if tries == 1:
                    s1()
                if tries == 2:
                    s2()
                if tries == 3:
                    s3()
                if tries == 4:
                    s4()
                if tries == 5:
                    s5()
                if tries == 6:
                    s6()
                if tries == 7:
                    s7()
                    print('Oh no the word was', x)
                    break
def thread_func(func):
    x = threading.Thread(target=func)
    x.start()

def rps():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    ROCK
    
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
            _______)
    ---.__________)
    
    PAPER
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
          __________)
          (____)
    ---.__(___)
    
    SCISSORS
    
    '''

    game_images = [rock, paper, scissors]

    user_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
    if user_chose >= 3 or user_chose < 0: 
      print("You typed an invalid number. You lose.")
    else: 
      print(game_images[user_chose])

      computer_chose = random.randint(0, 2)
      print("Computer chose:")
      print(game_images[computer_chose])


      if user_chose == 0 and computer_chose == 2:
        print("You win!")
      elif computer_chose == 0 and user_chose == 2:
        print("You lose")
      elif computer_chose > user_chose:
        print("You lose")
      elif user_chose > computer_chose:
        print("You win!")
      elif computer_chose == user_chose:
        print("It's a draw.")
def pong():
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("gray")
    wn.setup(width=800, height=600)
    wn.tracer(0)


    score_a = 0
    score_b = 0

    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("#15f4ee")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape("square")
    paddle_b.color("#15f4ee")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)


    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("#15f4ee")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.6
    ball.dy = 0.6 

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    def paddle_a_up():
        y = paddle_a.ycor()
        y += 30
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 30
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 30
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 30
        paddle_b.sety(y)


    wn.listen()
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")

    while True:
        wn.update()
        
        
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            
        
        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            
        if ball.xcor() > 350:
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1 
            
        
        elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
#def destroy(window):
    #window.destroy()
    #clear()


def clear():
    window = Tk()
    window.title("Retro Arcade Games")
    window.configure(bg="#95ADBE")
    window.geometry("600x600") 
    l1 = Label(window, text = "Welcome to arcade games!\nChoose which game you want to play.",bg="#D3DEDC", fg="#1A374D")
    l1.place(x=300, y=35, anchor='center')

    def snake_process():
        p = Process(target=snake)
        p.start()
        p.join()

    b1 = Button(window, text = "Snake Game", command=snake_process, width = 18, bg="#D3DEDC", fg="#1A374D")
    b1.place(x=300, y=100, anchor='center')

    def hangman_thread():
        thread_func(hangman)

    b2 = Button(window, text = "Hangman", command=hangman_thread, width = 18, bg="#D3DEDC", fg="#1A374D")
    b2.place(x=300, y=150, anchor='center')

    def destroy():
        window.destroy()
        clear()

    def rps_thread():
        thread_func(rps)

    b3 = Button(window, text = "Rock, Paper, Scissors", command=rps_thread, width = 18, bg="#D3DEDC", fg="#1A374D")
    b3.place(x=300, y=200, anchor='center')
    b4 = Button(window, text="Click to change game", command=destroy, width = 18, bg="#D3DEDC", fg="#1A374D")
    b4.place(x=300, y=300, anchor='center')

    def pong_process():
        p = Process(target=pong)
        p.start()
        p.join()

    b5 = Button(window, text = "Pong", command = pong_process, width = 18, bg="#D3DEDC", fg="#1A374D")
    b5.place(x=300, y=250, anchor='center')
    def destroyfr():
        window.destroy()
    b6 = Button(window, text = "Quit", command = destroyfr, width = 18, bg="#D3DEDC", fg="#1A374D")
    b6.place(x=300, y=350, anchor='center')
    window.mainloop()

if "__main__" == __name__:
    clear()
