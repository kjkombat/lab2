class factorials:
    def calc( self,n ):
        self.n=n
        if self.n <1:   # base case
            return 1
        else:
            return self.n * factorials.calc(self,self.n-1)  # recursive call
