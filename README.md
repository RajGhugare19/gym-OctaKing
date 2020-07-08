# OctaKing
This is a custom made OpenAI gym environment I've made for a boardgame I invented. 

## Rules
1) Each player will start the game with four kings on a 4 cross 4 board, with the black and white kings on the fourth and the first respectively.
2) Kings can move in the same way they do in chess, excpet they cannot take a move in the backward direction, i.e of the 8 cardinal and inter-cardinal directions, the king can move only in five.The following image shows all 5 legal moves that a king can choose from.

<p align="center">
<a href="url"><img src="https://i.imgur.com/ldswIVh.png" height="200" width="200" ></a>
</p>

3) If there is a black king on any of these marked squares then the white king can capture it and vice versa.
4) A player wins if any one of his kings reaches the other end of the board or all of the pieces of the opponent player have been captured.
5) If 16 half-moves are played without any capture then the game ends in a draw.
