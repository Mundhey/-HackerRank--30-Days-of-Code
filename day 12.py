class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber


class Student(Person):
    def __init__(self,fn,ln,idn,scor):
        self.scorecard=scores
        Person.__init__(self,fn,ln,idn)
        
    def printPerson(self):
        Person.printPerson(self)

    def calculate(self):
        self.avg=0
        for i in range(0,len(self.scorecard)):
            self.avg+=int(self.scorecard[i])
        self.avg=self.avg/len(self.scorecard)

        if(self.avg<40):
            return 'T'
        elif(self.avg<55 and self.avg>=40):
            return 'D'
        elif(self.avg<70 and self.avg>=55):
            return 'P'
        elif(self.avg<80 and self.avg>=70):
            return 'A'
        elif(self.avg<90 and self.avg>=80):
            return 'E'
        else:
            return 'O'










# Class Constructor
#
#   Parameters:
#   firstName - A string denoting the Person's first name.
#   lastName - A string denoting the Person's last name.
#   id - An integer denoting the Person's ID number.
#   scores - An array of integers denoting the Person's test scores.
#
# Write your constructor here




#   Function Name: calculate
#   Return: A character denoting the grade.
#
# Write your function here

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())  # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:",s.calculate()