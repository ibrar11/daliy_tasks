class Programmer:
    employeeName = ''
    employeeCity = ''
    employeeCountry = ''
    employeeAge = ''
    companyName = 'Microsoft'

    def showEmployeeDetails (self):
        print(f'''Employee Name: {self.employeeName}\n
Employee City: {self.employeeCity}\n
Employee Country: {self.employeeCountry}\n
Employee Age: {self.employeeAge}\n
Company Name: {self.companyName}\n''')

employee1 = Programmer()
employee1.employeeName = "Haider Nadeem"
employee1.employeeCity = "LA"
employee1.employeeCountry = "USA"
employee1.employeeAge = 25

employee1.showEmployeeDetails()