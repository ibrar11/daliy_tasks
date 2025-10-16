class Employee:

    def __init__(self, salary, increment):
        assert salary >= 0
        assert increment >= 0
        self.__salary = salary
        self.__increment = increment
        

    @property
    def getSalary(self):
        return self.__salary
    
    @getSalary.setter
    def setSalary(self, salary):
        self.__salary = salary

    @property
    def getIncrement(self):
        return self.__increment


emp1 = Employee(1000, 0.2)
print(emp1.getSalary)
print(emp1.getIncrement)