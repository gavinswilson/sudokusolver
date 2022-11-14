from dataclasses import dataclass

@dataclass
class sudElement:
    row: int
    col: int
    box: int
    max: int
    value: int
    opts: int
    
    def __post_init__(self):
        if self.max == 9:
            self.opts = 511
        if self.value != 0:
            self.opts = 0
            self.opts = self.opts | (1<<self.value-1)

    def removeOpt(self,num):
        #do stuff here
        #print(format(self.opts, "09b"))
        self.opts = self.opts & ~(1<<num-1)
        print(format(self.opts, "09b"))

    def setValue(self):
        n = 0
        svalue = self.opts
        while svalue:
            n += 1
            svalue &= svalue-1
        # print(n)
        # print("----")
        if n == 1:
            svalue = self.opts
            for p in range(1,self.max+1):
                if (svalue == 1):
                    #print("setting value")
                    self.value = p
                    break
                svalue = svalue>>1
        print("Value")
        print(self.value)
