class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_person_info(self):
        print(f"Name:{self.name}")
        print(f"age:{self.age}")
class employ(person):
    def __init__(self,name,age,employ_id,salary):
        super().__init__(name,age)
        self.employ_id=employ_id
        self.salary=salary
    def display_employ_info(self):
        print(f"employ_id:{self.employ_id}")
        print(f"salary:{self.salary}")
class manager(employ,person):
    def __init__(self,name,age,employ_id,salary,department):
        super().__init__(name,age,employ_id,salary)
        self.department=department
    def display_manager_info(self):
        print("\n--Maneger info--")
        self.display_person_info()
        self.display_employ_info()
        print(f"department:{self.department}")
    def approve_leave(self):
        print(f"{self.name} has approved the leave request")

manager1=manager(name="Dipak patil",age=40,employ_id=4067,salary=34000,department="IT")
manager2=manager(name="vivek mhaske",age=17,employ_id=1523,salary=12000,department="CS")
        
manager1.display_manager_info()
manager1.approve_leave()

manager2.display_manager_info()
manager2.approve_leave()
