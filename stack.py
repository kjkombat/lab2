class stack:
    def __init__(self,data):
        self.data=data
    def isFull(self):
        if len(self.data)>=10:
            return 1
        else:
            return 0

    def isEmpty(self):
        if len(self.data) == 0:
            return 1
        else:
            return 0

    def push(self, num):
        if stack.isFull(self):
            print "Stack overflowing"
            return False
        else:
            self.data.append(num)
            return True
    def pop(self):
        if stack.isEmpty(self):
            print "stack underflowing"
            return False
        else:
            val=self.data.pop()
            print val
            return val
