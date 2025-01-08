class Employee:
    def __init__(self,name, id):
        self.name=name
        self.id=id

    def get_info(self):
        return (f"Имя: {self.name}, id: {self.id}")

class Manager(Employee):
    def __init__(self, name, id,department):
        Employee.__init__(self, name, id)
        self.department=department

    def manage_project(self):
        return(f"{self.name} курирует проект в {self.department}")

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization=specialization

    def perform_maintenance(self):
        return(f"{self.name} выполняет техническое обслужиывние в {self.specialization}")

class TechManager(Manager, Technician):
    def __init__(self, name, id, department,specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.team=[]

    def project(self):
        return (f"{Manager.manage_project(self)}")

    def maintenance(self):
        return (f"{Technician.perform_maintenance(self)}")

    def add_employee(self, *args):
        for employee in args:
            self.team.append(employee)

    def get_info(self):
        return (f"Имя: {self.name}, id: {self.id}")

    def get_team_info(self):
        info=""
        for employee in self.team:
            info+=employee.get_info()
            return info


emp1 = Employee("Alice", 101)
emp2 = Employee("Bob", 102)

manager = Manager("Charlie", 201, "Sales")
technician = Technician("David", 301, "Electrical")

tech_manager = TechManager("Eve", 401, "IT", "Networking")

# Добавление сотрудников в команду TechManager
tech_manager.add_employee(emp1, emp2, manager, technician)

# Демонстрация функциональности
print(emp1.get_info())
print(manager.get_info())
print(technician.get_info())
print(tech_manager.get_info())
print("Team Info:")
print(tech_manager.get_team_info())

print(tech_manager.perform_maintenance())

