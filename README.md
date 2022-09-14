# Doors Challenger

![alt text](https://github.com/luigus/doors_challenger/blob/main/images/doors_99.png)


# Table of Contents
1. [Language](#Deps)
2. [Problem](#Problem)
3. [Simulation with 3 doors](#Simulation)
4. [Solution](#Stats)
5. [Conclusion](#Conclusion)
5. [Exemple](#Exemple)

# <a name="Deps"></a>Language
This project is using Python3.10

# <a name="The Problem"></a>Problem

There are three boxes, and only one of them contains the long-awaited Apple Watch, which you can win if you guess which one it is.

The boxes are shuffled, and as soon as you choose one of them, the program will show you a different one - which will be empty (the program knows where the reward is!). As a player, it is up to you to change your initial choice. Do you keep your original guess or change the box you chose?

Your task is to write a program that simulates the above-mentioned problem and a function that proves which would be the best choice, change your guess or not! 

And go further - what would you change if it were fifty boxes? 



## Simulation with 3 doors


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
Lets check the final result:
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
The prize is behind the door: 3
Your initial selection was: 1 
You decide to change your first choice
You change from 1 door to 3 door and ...
You Won the price =)
```

## Solution 
The best option as we can see in the statistical results will always occur when we decide to switch ports, because when we do that, we are choosing a port that has a higher probability of having the prize.
What !??????
Come on, when there is no open door yet, the probability of the prize being in some door is the same for all doors. But once any empty port is revealed, then the probability that it was for that port is distributed to all other remaining ports except the one you initially chose. In other words, the port that was revealed has a 0% chance of getting the prize as it was revealed, your port chosen initially remains with the same percentage of the beginning of the problem and all other ports have a higher probability of getting the prize. So choosing to switch doors will increase your chances of getting the prize you want.

## Solution [Portuguese]
A melhor opção como podemos ver nos resultados estatisticos sempre ocorrerá quando decidimos trocar de porta, pois quando fazemos isso, estamos escolhendo uma porta que tem uma probabilidade maior de ter o prêmio.  
Como assim !??????
Vamos lá, Quando não existe nenhuma porta aberta ainda a probabilidade do premio está em alguma porta é igual para todas as portas. Porém uma vez que é revelada uma porta vazia qualquer, então a probabilidade que era desta porta é distribuida para todas as outras portas remanecentes menos aquela em que você escolheu inicialmente. Ou seja a porta que foi revelada tem 0% de chance de ter o prêmio como já foi revelado, a sua porta escolhida inicialmente continua com a mesma porcentagem do inicio do problema e todas as outras portas possuiem uma probabilidade maior de obter o prêmio. Por isso, escolher mudar de porta irá aumentar as suas chances de obter o prêmio desejado.

## Statistics
If we uncomment lines 78, 79, 80, 81 and 82 of the main.py file we can see the following probabilistic results for a simulation with 3, 4, 5, 10 and 50 ports.

```
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

## Conclusion
As we can see, the probability of the other ports will always be greater than that of the port that was chosen first. That is, if we want to have a greater chance of winning the prize, we must always choose to change doors.


## Exemple
*The star is where the prize is.
*Where the puppet is is the first option
*The arrow is the door change
*And the empty box is the door that was shown without the prize.

If the person decides to change doors, he will have a 2 out of 3 chance of hitting the prize and his chances increase to 66%

![alt text](https://github.com/luigus/doors_challenger/blob/main/images/3_doors.jpg)
