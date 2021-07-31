class convert:
    def __init__(self, hexnum,R,G,B):
        self.hexnum = hexnum
        self.R = R
        self.G = G
        self.B = B
        self.hexnum1 = self.hexnum[0:2]
        self.hexnum2 = self.hexnum[2:4]
        self.hexnum3 = self.hexnum[4:6]
        self.hexnum = [self.hexnum1, self.hexnum2,self.hexnum3]
        self.R = int(self.hexnum[0], 16)
        self.G = int(self.hexnum[1], 16)
        self.B = int(self.hexnum[2], 16)


