class Employee:
    """
    Klasa reprezentująca indywidualnego pracownika.
    """

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik: {self.name}, Wiek: {self.age}, Wynagrodzenie: {self.salary} PLN"

    def update_salary(self, new_salary: float):
        self.salary = new_salary


class EmployeesManager:
    """
    Klasa zarządzająca listą pracowników.
    """

    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Dodano pracownika: {employee}")

    def list_employees(self):
        if not self.employees:
            print("Brak pracowników.")
        else:
            print("Lista pracowników:")
            for employee in self.employees:
                print(employee)

    def remove_employees_by_age_range(self, min_age: int, max_age: int):
        original_count = len(self.employees)
        self.employees = [emp for emp in self.employees if not (min_age <= emp.age <= max_age)]
        removed_count = original_count - len(self.employees)
        print(f"Usunięto {removed_count} pracowników w przedziale wiekowym {min_age}-{max_age} lat.")

    def find_employee_by_name(self, name: str):
        for emp in self.employees:
            if emp.name == name:
                print(f"Znaleziono pracownika: {emp}")
                return emp
        print("Pracownik nie znaleziony.")
        return None

    def update_employee_salary(self, name: str, new_salary: float):
        employee = self.find_employee_by_name(name)
        if employee:
            employee.update_salary(new_salary)
            print(f"Wynagrodzenie pracownika {name} zostało zaktualizowane do {new_salary} PLN.")


class FrontendManager:
    """
    Klasa zapewniająca interfejs użytkownika do zarządzania pracownikami.
    """

    def __init__(self):
        self.manager = EmployeesManager()

    def add_employee_ui(self):
        name = input("Podaj imię i nazwisko pracownika: ")
        age = int(input("Podaj wiek pracownika: "))
        salary = float(input("Podaj wynagrodzenie pracownika: "))
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)

    def list_employees_ui(self):
        self.manager.list_employees()

    def remove_employees_by_age_ui(self):
        min_age = int(input("Podaj minimalny wiek: "))
        max_age = int(input("Podaj maksymalny wiek: "))
        self.manager.remove_employees_by_age_range(min_age, max_age)

    def update_employee_salary_ui(self):
        name = input("Podaj imię i nazwisko pracownika do aktualizacji wynagrodzenia: ")
        new_salary = float(input("Podaj nowe wynagrodzenie: "))
        self.manager.update_employee_salary(name, new_salary)

    def run(self):
        while True:
            print("\n--- Employees System Project ---")
            print("1. Dodaj nowego pracownika")
            print("2. Wyświetl listę pracowników")
            print("3. Usuń pracowników według przedziału wiekowego")
            print("4. Zaktualizuj wynagrodzenie pracownika")
            print("5. Wyjdź")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                self.add_employee_ui()
            elif choice == "2":
                self.list_employees_ui()
            elif choice == "3":
                self.remove_employees_by_age_ui()
            elif choice == "4":
                self.update_employee_salary_ui()
            elif choice == "5":
                print("Zamknięcie systemu.")
                break
            else:
                print("Niepoprawna opcja, spróbuj ponownie.")


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()
