class emp:
    def __init__(self,name,salary,location):
        self.name=name
        self.salary=salary
        self.location=location
    def display(self):
        print('name:',self.name)
        print('salary:',self.salary)
        print('location:',self.location)
class manager(emp):
    def __init__(self,name,salary,location,dept,deptid):
        super().__init__(name,salary,location)
        self.dept=dept
        self.deptid=deptid
    def display1(self):
        super().display()
        print('dept:',self.dept)
        print('deptid:',self.deptid)
obj=manager('john',65000,'pune','admin',4531)
print(obj.display1())