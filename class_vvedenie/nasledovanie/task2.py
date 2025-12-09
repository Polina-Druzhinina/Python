class Bachelor:
    def __init__(self, firstName,lastName,group,averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark
    def getScholarship(self):
        if self.averageMark == 5:
            return 10000
        elif self.averageMark > 3:
            return 5000
        else:
            return 0

class Undergraduate(Bachelor):
    def __init__(self, firstName,lastName,group,averageMark, researchWork):
        super().__init__(firstName,lastName,group,averageMark)
        self.researchWork = researchWork
    def getScholarship(self):
        if self.averageMark == 5:
            return 15000
        elif self.averageMark > 3:
            return 7500
        else:
            return 0
    
lst = [
    Bachelor("Ivan", "Ivanov", "14121", 5),
    Bachelor("Vasya", "Petrov", "14122", 4),
    Undergraduate("Anna", "Sidorova", "12456", 5, "Somthing"),
    Undergraduate("Polina", "Smirnova", "255544", 3, "Anything")
]

for i in lst:
    print(i.getScholarship())