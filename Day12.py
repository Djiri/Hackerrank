class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, allscores):
        Person.__init__(self, firstName, lastName, idNumber,)
        self.scores = allscores
    def calculate(self):
        av = (sum(self.scores))/len(self.scores)
        if av < 40:
            return "T"
        elif av in range(40, 55):
            return "D"
        elif av in range(55, 70):
            return "P"
        elif av in range(70, 80):
            return "A"
        elif av in range(80, 90):
            return "E"
        else:
            return "O"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())