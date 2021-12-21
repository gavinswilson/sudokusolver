class sudoku:
    gridsize = 0
    box = 0
    updatecount = 1 

    def clearknowns(self):
        print("hello")
        while self.updatecount < 1:
            print(self.updatecount)
            self.updatecount = 0
            for x in range(self.gridsize):
                for y in range(self.gridsize):
                    if int(self.soln[x][y]) > 0:
                        #rows
                        #cols
                        #areas
                        self.bitflip(y,x,self.soln[x][y])
        self.updatecount = 1

    def bitflip(self, r, c, b):
        filter = 1 << int(b)-1
        if self.opts[c][r] & filter:
            #print("r:",r," c:",c," b:",b," current:", format(self.opts[c][r], "09b")," filter:",format(filter, "09b"), filter)
            self.opts[c][r] = filter ^ int(self.opts[c][r])
            self.updatecount = self.updatecount+1

    def __init__(self, size, setup, gridtype):
        self.gridsize = size
        index = 0
        self.opts = []
        self.soln = []
        self.areas = []
        for x in range(self.gridsize):
           self.opts.append([])
           self.soln.append([])
           for y in range(self.gridsize):
               self.soln[x].append(setup[index])
               self.opts[x].append(511)
               index=index+1
        if gridtype == "std":
            self.box = 3

    def soln_print(self):
        rowcounter = 0
        colcounter = 0
        for row in self.soln:
            if rowcounter%3 == 0:
                print("-------------")
            for val in row:
               if colcounter%3 == 0:
                    print("|",end="")
               print(val, end ="")
               colcounter+=1
            print("|")
            rowcounter+=1
        print("-------------")
    
    def opts_print(self):
        rowcounter = 0
        colcounter = 0
        for row in self.opts:
            if rowcounter%3 == 0:
                print("--------------------------------------------------------------------------------------------------")
            for val in row:
               if colcounter%3 == 0:
                    print("| ",end="")
               #print(int(bin(val).split('0b')[1]), end =" ")
               print(format(val, "09b"),end=" ")
               colcounter+=1
            print(" |")
            rowcounter+=1
        print("--------------------------------------------------------------------------------------------------")



