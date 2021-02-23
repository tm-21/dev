
class order():
    def __init__(self):
        super().__init__()
        self.count = ""
    def display(self,count,log):
        print(count,log)

N = 1
OR1 = order()
OR1.count = N
OR2 = order()
OR2.count = N+1
OR1.display(OR1.count,"hello world")
OR2.display(OR2.count,"aa")
