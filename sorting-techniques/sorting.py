class Sorting:
    def __init__(self, list = []):
        self.list = list

    def bubbleSort(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)-1):
                if j < len(self.list)-1:
                    a,b = self.list[j], self.list[j+1]
                    if a > b:
                       self.list[j], self.list[j+1] = b, a

            print(self.list)


obj = Sorting([60,30,50,10,100,70])
obj.bubbleSort()