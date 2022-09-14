# Doors Challenger

![alt text](https://miro.medium.com/max/700/1*2ypNLAI4KNsWmi68SPmQqg.png)


# Table of Contents
1. [Language](#Deps)
2. [Problem](#Problem)
3. [Simulation with 3 doors](#Simulation)
4. [Solution](#Stats)


# <a name="Deps"></a>Language
This project is using Python3.10

# <a name="The Problem"></a>Problem

There are three boxes, and only one of them contains the long-awaited Apple Watch, which you can win if you guess which one it is.

The boxes are shuffled, and as soon as you choose one of them, the program will show you a different one - which will be empty (the program knows where the reward is!). As a player, it is up to you to change your initial choice. Do you keep your original guess or change the box you chose?

Your task is to write a program that simulates the above-mentioned problem and a function that proves which would be the best choice, change your guess or not! 

And go further - what would you change if it were fifty boxes? 



## Output


* Python (3.10)
```shell
python3 main.py

Doors numbers: ['1', '2', '3']
Pick up a door number: 1
I will show you an empty door: 2
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Would you like to select the third door? Type 'yes' or 'no': yes
The door you will switch to is: 3
Congratulations, you win! The prize was behind of the door: 3
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Let`s check the final result:
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
The prize is behind the door: 3
Your initial selection was: 1 
You decide to change your first choice
You change from 1 door to 3 door and ...
You Won the price =]
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
A problem to choose a door between 3 doors
Initial probability of winning of each door: 33.33%
Probability of win without change: 33.33%
Probability of win change the initial selection: 66.67%
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
A problem to choose a door between 4 doors
Initial probability of winning of each door: 25.0%
Probability of win without change: 25.0%
Probability of win change the initial selection: 37.5%
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
A problem to choose a door between 5 doors
Initial probability of winning of each door: 20.0%
Probability of win without change: 20.0%
Probability of win change the initial selection: 26.67%
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
A problem to choose a door between 10 doors
Initial probability of winning of each door: 10.0%
Probability of win without change: 10.0%
Probability of win change the initial selection: 11.25%
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
A problem to choose a door between 50 doors
Initial probability of winning of each door: 2.0%
Probability of win without change: 2.0%
Probability of win change the initial selection: 2.04%

```
