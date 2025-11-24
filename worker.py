class WORKER:
    """Класс для хранения данных о сотруднике университета"""
    
    def __init__(self, surname_initials="", position="", salary=0.0, start_year=0):
        """Конструктор класса"""
        self.surname_initials = surname_initials
        self.position = position
        self.salary = salary
        self.start_year = start_year
    
    def set_surname_initials(self, surname_initials):
        """Установка фамилии и инициалов"""
        self.surname_initials = surname_initials
    
    def set_position(self, position):
        """Установка должности"""
        self.position = position
    
    def set_salary(self, salary):
        """Установка зарплаты"""
        self.salary = salary
    
    def set_start_year(self, start_year):
        """Установка года начала работы"""
        self.start_year = start_year
    
    def calculate_experience(self, current_year):
        """Вычисление стажа работы"""
        return current_year - self.start_year
    
    def display(self):
        """Вывод информации о сотруднике"""
        print(f"Фамилия и инициалы: {self.surname_initials}")
        print(f"Должность: {self.position}")
        print(f"Зарплата: {self.salary}")
        print(f"Год поступления: {self.start_year}")