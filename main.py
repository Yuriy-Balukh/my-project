import lib

def main():
    print("**** ПЕРСОНАЛЬНИЙ КАЛЬКУЛЯТОР ПОКАЗНИКІВ ЗДОРОВ'Я ****")

    age = int(input("Введіть ваш вік (років): "))
    weight = float(input("Введіть вашу вагу (в кг, наприклад, 75): "))
    height_cm = float(input("Введіть ваш зріст (в см, наприклад, 178): "))

    height_m = height_cm / 100

    bmi = lib.calculate_bmi(weight, height_m)
    health_status = lib.analyze_health(bmi, age)

    print("\nРезультати аналізу показників:")
    print("-" * 55)
    print(f"Введені дані : Вік: {age} р., Вага: {weight} кг, Зріст: {height_cm} см")
    print(f"Індекс маси тіла (ІМТ) : {bmi:.2f}")
    print(f"Попередній висновок     : {health_status}")
    print("-" * 55)

if __name__ == "__main__":
    main()