from sudElement import sudElement

class sudoku:
    gridsize = 0
    box = 0
    updatecount = 1 
    grid = []

    def clearknowns(self):
        print("hello")

    def __init__(self, size, setup, gridtype):
        self.gridsize = size
        index = 0
        for x in range(self.gridsize):
           self.grid.append([])
           for y in range(self.gridsize):
               self.grid[x].append(sudElement(x, y, 1, 9, int(setup[index]), 0))
               index=index+1
        if gridtype == "std":
            self.box = 3

    def sud_print(self, whichGrid):
        rowcounter = 0
        colcounter = 0
        for row in self.grid:
            colcounter = 0
            if rowcounter%3 == 0:
                if whichGrid == "soln":
                    print("-------------------------")
                if whichGrid == "opts":
                    print("-------------------------------------------------------------------------------------------------")
            for val in row:
                if colcounter%3 == 0:
                    print("|",end=" ")
                if whichGrid == "soln":
                     print(self.grid[rowcounter][colcounter].value, end=" ")
                if whichGrid == "opts":
                     print(format(self.grid[rowcounter][colcounter].opts, "09b"), end=" ")   
                colcounter+=1
            print("|")
            rowcounter+=1
        if whichGrid == "soln":
            print("-------------------------")
        if whichGrid == "opts":
            print("-------------------------------------------------------------------------------------------------")
 
    
    