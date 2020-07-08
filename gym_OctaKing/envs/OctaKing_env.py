import gym
import numpy as np


#player 1:black
#player 0:White

#player 0 goes first


class OctaKingEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        self.state = np.zeros([2,4,4])
        self.state[0,3] = 1
        self.state[1,0] = 1
        self.reward = 0
        self.halfmoves = 0
        sefl.lastcapture = 0
        self.initKingMoves()

    def initKingMoves(self):
        self.KingMoves = np.zeros([2,16,4,4])
        w = np.zeros([16,4,4])
        b = np.zeros([16,4,4])
        for i in range(16):
            temp= np.zeros([4,4])
            row = i//4
            col = i%4
            if(row != 3):
                b[i,row+1,col] = 1
                if col != 0:
                    b[i,row,col-1] = 1
                    b[i,row+1,col-1] = 1
                if col != 3:
                    b[i,row,col+1] = 1
                    b[i,row+1,col+1] = 1
            if(row != 0):
                w[i,row-1,col] = 1
                if col != 0:
                    w[i,row,col-1] = 1
                    w[i,row-1,col-1] = 1
                if col != 3:
                    w[i,row,col+1] = 1
                    w[i,row-1,col+1] = 1
        self.KingMoves[0] = w
        self.KingMoves[1] = b

    def reset(self):
        self.state = np.zeros([2,4,4])
        self.state[0,3] = 1
        self.state[1,0] = 1
        self.done = False
        self.reward = 0
        self.halfmoves = 0
        return self.state

    def step(self,move):
        valid = self.check(move)
        if valid:
            (next_state,reward,done,_) = self.take_action(move)
            return next_state, reward, done, _
        else:
            print("invalid action")
            return 0;

    def check(self,move):
        frm = move[0]
        to = move[1]
        capt = move[2]
        player = self.halfmoves%2
        opp = (self.halfmoves+1)%2

        to_row = to//4
        to_col = to%4
        print(to_row)

        if self.KingMoves[player,frm,to_row,to_col] == 1:
            if capt:
                if self.state[opp,to_row,to_col] == 1:
                    return 1
                else:
                    return 0
            else:
                if self.state[opp,to_row,to_col] == 1:
                    return 0
                else:
                    return 1
        else:
            return 0

    def take_action(self,move):
        frm = move[0]
        to = move[1]
        capt = move[2]
        player = self.halfmoves%2

        frm_row = frm//4
        frm_col = frm%4
        to_row = to//4
        to_col = to%4

        self.state[player,frm_row,frm_col] = 0
        self.state[player,to_row,to_col] = 1
        if capt:
            opp = (self.halfmoves+1)%2
            self.state[opp,to_row,to_col] = 0
            self.lastcapture = 0
        else:
            self.lastcapture += 1
        self.halfmoves += 1
        (done,reward) = self.is_done()
        if done:
            self.reset()
        return self.state,reward,done,0

    def is_done(self):
        if np.sum(self.state[0]) == 0 or np.sum(self.state[1,3]) != 0:
            #black wins
            reward = -1
            done = True
        elif np.sum(self.state[1]) == 0 or np.sum(self.state[0,0]) != 0:
            #white wins
            reward = 1
            done = True
        else:
            reward = 0
            done = False
        if self.lastcapture > 16:
            done = True
            reward = 0
        return done,reward

    def render(self):
        print("\n")
        for i in range(4):
            print(str(4-i) + ' ',end="")
            for j in range(4):
                if self.state[0,i,j]==1:
                    print(' w ',end="")
                elif self.state[1,i,j]==1:
                    print(' b ',end="")
                else:
                    print(' - ',end="")
            print("  ")
        print("   a  b  c  d ")
