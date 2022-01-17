from tkinter import *
window = Tk()
window.title("Arcade Games")
window.geometry("600x600")
l1 = Label(window, text = "Welcome to arcade games!\nChoose which game you want to play.")
l1.grid(row = 0, column = 0)
def snake():
  from turtle import Screen
  from snake import Snake
  from food import Food
  from scoreboard import Scoreboard
  import time

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
b1 = Button(window, text = "Snake Game", command = snake)
b1.grid(row=1, column=0)
def hangman():
  def s1():
      print('---------')
      print('    |')


  def s2():
      print('---------')
      print('    |')
      print('    O')


  def s3():
      print('---------')
      print('    |')
      print('    O')
      print('    |')
      print('    |')


  def s4():
      print('---------')
      print('    |')
      print('    O')
      print('  --|')
      print('    |')


  def s5():
      print('---------')
      print('    |')
      print('    O')
      print('  --|--')
      print('    |')


  def s6():
      print('---------')
      print('    |')
      print('    O')
      print('  --|--')
      print('    |')
      print('   | ')
      print('   | ')


  def s7():
      print('---------')
      print('    |')
      print('    O')
      print('  --|--')
      print('    |')
      print('   | |')
      print('   | |')


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
b2 = Button(window, text = "Hangman", command = hangman)
b2.grid(row=2, column=0)
def rps():
  import random
  print("now you  have entered THE stone,paper and scissor game.Enjoy your game ")
  print("STONE:")
  print("""
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
  """)

  print("PAPER:")
  print("""
      _______
  ---'    ____)____
            ______)
            _______)
          _______)
  ---.__________)
  """)

  print("SCISSORS:")
  print("""
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
  ---.__(___)
  """)
  a=input("enter your choice ")
  l=["stone","paper","scissor"]
  b=random.choice(l)
  print(b)
  if a==b:
      print("its a draw as the computer chose",b)
  elif a=="stone" and b=="paper":
      print("defeated as the computer chose ",b)
      print(''' 
                    BETTER LUCK NEXT TIME 
                    .___
                    @...V;
                    P:   :|
              .___"d `~" P.
              .@ .."W     d;
              :P'  "d     j#
              \@`_#f  ~  W.
                " #;    .@.",
                  P.     Pj n|
                  @.     #;  ":
                  n; ~   mZ   :;
                  M.    .#     f.
              ___.f#     .".   .d
            ."    ":     .";    ;f
      .____P     L.      :     jh
      h    "     |      //  ;Y
      "P    |    .nm    -j:     :P.
      W   .n                    .Y
      Z                        #8.
      .P                         'Z
      `f                       fj
        ":                      :d
        :p                    P;
          `v                  -l'
      ''')

  elif a=="stone" and b=="scissor":
      print("won as the computer chose ", b)
      print('''$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$'`$$$$$$$$$$$$$'`$$$
  $$$$$$  $$$$$$$$$$$  $$$$
  $$$$$$$  '$/ `/ `$' .$$$$
  $$$$$$$$. i  i  /! .$$$$$
  $$$$$$$$$.--'--'   $$$$$$
  $$^^$$$$$'        J$$$$$$
  $$$   ~""   `.   .$$$$$$$
  $$$$$e,      ;  .$$$$$$$$
  $$$$$$$$$$$.'   $$$$$$$$$
  $$$$$$$$$$$$.    $$$$$$$$
  $$$$$$$$$$$$$     $$$$$$$''')
  elif a=="paper" and b=="scissor":
      print("defeated as the computer chose ", b)
      print(''' 
                
                BETTER LUCK NEXT TIME 
                .___
                @...V;
                P:   :|
          .___"d `~" P.
          .@ .."W     d;
          :P'  "d     j#
          \@`_#f  ~  W.
            " #;    .@.",
              P.     Pj n|
              @.     #;  ":
              n; ~   mZ   :;
              M.    .#     f.
          ___.f#     .".   .d
        ."    ":     .";    ;f
  .____P     L.      :     jh
  h    "     |      //  ;Y
  "P    |    .nm    -j:     :P.
  W   .n                    .Y
  Z                        #8.
  .P                         'Z
  `f                       fj
    ":                      :d
    :p                    P;
      `v                  -l'
  ''')

  elif a=="paper" and b=="stone":
      print("won as the computer chose ", b)
      print('''$$$$$$$$$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$$$
      $$$$$'`$$$$$$$$$$$$$'`$$$
      $$$$$$  $$$$$$$$$$$  $$$$
      $$$$$$$  '$/ `/ `$' .$$$$
      $$$$$$$$. i  i  /! .$$$$$
      $$$$$$$$$.--'--'   $$$$$$
      $$^^$$$$$'        J$$$$$$
      $$$   ~""   `.   .$$$$$$$
      $$$$$e,      ;  .$$$$$$$$
      $$$$$$$$$$$.'   $$$$$$$$$
      $$$$$$$$$$$$.    $$$$$$$$
      $$$$$$$$$$$$$     $$$$$$$''')
  elif a=="scissor" and b=="stone":
      print("defeated as the computer chose ", b)
      print(''' 
                    BETTER LUCK NEXT TIME 
                    .___
                    @...V;
                    P:   :|
              .___"d `~" P.
              .@ .."W     d;
              :P'  "d     j#
              \@`_#f  ~  W.
                " #;    .@.",
                  P.     Pj n|
                  @.     #;  ":
                  n; ~   mZ   :;
                  M.    .#     f.
              ___.f#     .".   .d
            ."    ":     .";    ;f
      .____P     L.      :     jh
      h    "     |      //  ;Y
      "P    |    .nm    -j:     :P.
      W   .n                    .Y
      Z                        #8.
      .P                         'Z
      `f                       fj
        ":                      :d
        :p                    P;
          `v                  -l'
      ''')

  elif a=="scissor" and b=="paper":
      print("won as the computer chose ", b)
      print('''$$$$$$$$$$$$$$$$$$$$$$$$$
      $$$$$$$$$$$$$$$$$$$$$$$$$
      $$$$$'`$$$$$$$$$$$$$'`$$$
      $$$$$$  $$$$$$$$$$$  $$$$
      $$$$$$$  '$/ `/ `$' .$$$$
      $$$$$$$$. i  i  /! .$$$$$
      $$$$$$$$$.--'--'   $$$$$$
      $$^^$$$$$'        J$$$$$$
      $$$   ~""   `.   .$$$$$$$
      $$$$$e,      ;  .$$$$$$$$
      $$$$$$$$$$$.'   $$$$$$$$$
      $$$$$$$$$$$$.    $$$$$$$$
      $$$$$$$$$$$$$     $$$$$$$''')
  else:
      print("the given input is not recognised by the computer please enter from stone paper and scissor ")
b3 = Button(window, text = "Rock, Paper, Scissors", command = rps)
b3.grid(row=3, column=0)
window.mainloop()
