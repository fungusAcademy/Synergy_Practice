from worker import WORKER

def main():
    workers = []
    current_year = 2025
    
    try:
        n = int(input("Введите количество сотрудников университета: "))
        
        for i in range(n):
            print(f"\n Сотрудник {i + 1}:")
            surname = input("Введите фамилию и инициалы: ")
            position = input("Введите должность: ")
            salary = float(input("Введите зарплату: "))
            year = int(input("Введите год поступления на работу: "))
            
            worker = WORKER(surname, position, salary, year)
            workers.append(worker)
        
        min_experience = int(input("\n Введите минимальный требуемый стаж работы: "))
        
        found = False
        print(f"\n Сотрудники со стажем более {min_experience} лет:")
        
        for worker in workers:
            experience = worker.calculate_experience(current_year)
            if experience > min_experience:
                print(f"{worker.surname_initials} (стаж: {experience} лет, должность: {worker.position})")
                found = True
        
        if not found:
            print(f"Сотрудников со стажем более {min_experience} лет не найдено.")
            
    except ValueError:
        print("Ошибка: введите корректные числовые значения")

if __name__ == "__main__":
    main()