# Footballers Hangman
<br>
Welcome to Footballers Hangman!
<br>

Footballers hangman is a python terminal game which runs through Heroku and is based on the classic game, Hangman.

Will you succeed in guessing before your guesses run out or will you be dangling from above.

![Responsivness](./readme-images/spc-responsive.webp)

How to play:

Here your knowledge will be tested on famous footballers.

A random footballer will be generated for you to guess. As with the classic hangman game, you will have oppotunites to guess letters in which to guess the correct footballer. If you guess the correct letter the blank will be filled in, however get it worng and you will be one step closer to being hanged.

# Table of contents

- [1. Live Game](#1-live-game)
- [2. Goals](#2-goals)
- [3. Features](#3-features)
- [4. Technologies Used](#4-technologies-used)
- [5. Testing](#5-testing)
- [6. Deployment](#6-deployment)
- [7. Acknowledgements and Credits](#7-acknowledgements-and-credits)

<br>

## 1. Live Game:
Please see the live version here: Footballers Hangman. (https://footballers-hangman-cf411def0ec1.herokuapp.com/)

## 2. Goals:

### Developer Goals:

- I would like the game to be fun but testing.
- I wanted the game to be easy to use and navigate through.

### User stories /Goals:

- As a user I would like to be able to play the game in the command line.
- As a user I would like ot see when I guess correctly.
- As a user I would like to see how many guesses I have left if I guess wrong.
- As a user I would like to see the answer if I dont get it in time.
- As a user I would like to be asked to play again at the end of the game.


<br>

## 3. Features:

### The Welcome Screen:

- When you run the game you will have a welcome screen loaded which shows the game and rules.

![Welcome Screen](./readme-images/welcome-screen.webp)


### Random Footballer

- The game will choose a random footballer for you to try and guess. Each time you play there should be a different footballer chosen from within 20 footballers.

### Choosing an answer / invalid answer:

- Once you enter a letter the game will tell you if you are right or wrong. If you enter a number or more than one letter you will get a message asking you to input the correct data.

![Choosing an answer](./readme-images/choose.webp)

### The correct answer:

- If correct you will be advised you are right and all blank spaces in which that letter is correct will fill in to give you a better idea of who the footballer may be.

![Correct answer](./readme-images/correct-answer.webp)

### The wrong answer:

- However, if you enter a letter which is not one of the chosen fottballer you will be told you are wrong and shown how many guesses you have left.

![Wrong answer](./readme-images/incorrect-answer.webp)

### Future Features:
- I would have liked to have implemented an enter name function where your score could then be stored on a leaderboard at the end of the game but ran out of time.

