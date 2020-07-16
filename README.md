# OctaKing
This is a custom made OpenAI gym environment.Most games like chess, Go have a very large branching factor and are difficult to solve with limited rescources. While games like Tic-Tac-Toe are very trivially solved because of a very small game-tree. OctaKing is a board game which might help you fetch the best of both these worlds.
 
 ## Summary
  - [Rules](#getting-started)
  - [Installation](#How-to-install)
  - [Environment details](#About-Environment) 
 
## Rules
1) Each player will start the game with four kings on a 4 cross 4 board, with the black and white kings on the fourth and the first rank respectively.
2) Kings can move in the same way they do in chess, excpet they cannot take a move in the backward direction, i.e of the 8 cardinal and inter-cardinal directions, the king can move only in five.The following image shows all 5 legal moves that a king can choose from.

<p align="center">
<a href="url"><img src="https://i.imgur.com/ldswIVh.png" height="200" width="200" ></a>
</p>

3) If there is a black king on any of these marked squares then the white king can capture it and vice versa.
4) A player wins if any one of his kings reaches the other end of the board or all of the pieces of the opponent player have been captured.
5) If 16 half-moves are played without any capture then the game ends in a draw.

## How to install

### Dependencies:
* [Gym](https://github.com/openai/gym)
* [Numpy](https://github.com/numpy/numpy)

## Setup:
* To setup the OctaKing package  
```
pip install -e .
```
## Imports:
To import the environment in python
```
import gym
import gym_OctaKing
env = gym.make('OctaKing-v0')
```

## About Environment

### State: 
numpy array of shape (2,4,4)                        
```
state[0] = contains the position of player 0's pieces.
state[1] = contains the position of player 1's pieces.

state[player,x,y] = 1, indicates the presence of king at square (x,y)
state[player,x,y] = 0, indicates an empty square at (x,y)
```

### Action:
List of size 3
```
action[0] = contains the from square of a move
action[1] = contains the to square of the move
action[2] = if the move was a capture(1) or not(0)
```

The squares are denoted in the following way:
```
 0   1  2   3                       
 4   5  6   7                                 
 8   9  10  11                            
 12  13 14  15                        
 ```
