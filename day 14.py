class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximum=max(self.__elements)
        self.minimum=min(self.__elements)
        self.maximumDifference=abs(self.maximum-self.minimum)










# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference