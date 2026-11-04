def calculate_bmi(weight: float, height: float) -> float:
    if height <= 0:
        return 0.0
    return weight / (height ** 2)

def analyze_health(bmi: float, age: int) -> str:
    if bmi < 18.5:
        status = "Занижена маса тіла"
    elif 18.5 <= bmi < 25.0:
        status = "Нормальна маса тіла (Показники в нормі)"
    elif 25.0 <= bmi < 30.0:
        status = "Надмірна маса тіла"
    else:
        status = "Ознаки ожиріння"

    if age > 60 and status == "Нормальна маса тіла (Показники в нормі)":
        return f"{status} [Чудовий показник для вашого віку]"
    return status