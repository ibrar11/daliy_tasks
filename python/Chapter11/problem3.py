class Employee:

    def __init__(self, salary, increment):
        assert salary >= 0
        assert increment >= 0
        self.setSalary = salary
        self.setIncrement = increment
        

    @property
    def getSalary(self):
        return self.__salary
    
    @getSalary.setter
    def setSalary(self, salary):
        self.__salary = salary

    @property
    def getIncrement(self):
        return self.__increment
    
    @getIncrement.setter
    def setIncrement(self, increment):
        self.__increment = increment
    
    @property
    def salaryAfterIncrement(self):
        return self.__salary + self.__salary * self.__increment



emp1 = Employee(1000, 0.2)
print(emp1.getSalary)
print(emp1.getIncrement)
print(emp1.salaryAfterIncrement)