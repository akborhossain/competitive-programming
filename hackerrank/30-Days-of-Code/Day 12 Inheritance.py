class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber,scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores= scores
        
    
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function her
    def calculate(self):
        sum=0
        n=len(self.scores)
        for x in self.scores:
            sum=sum+x
        res=sum//n
        if res <=100 and res >=90:
            return 'O'
        elif res <90 and res >=80:
            return 'E'
        elif res <80 and res >=70:
            return 'A'
        elif res <70 and res >=55:
            return 'P'
        elif res <55 and res >=40:
            return 'D'
        else:
            return 'T'
            
        
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())