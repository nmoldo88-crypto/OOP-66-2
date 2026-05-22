
# Импортируем внешнюю библиотеку
from faker import Faker

# Создаём объект Faker
fake = Faker()

# ==================== Часть 1 — Внешняя библиотека ====================

# Эта библиотека нужна для генерации фейковых (тестовых) данных.
# Faker позволяет быстро создавать реалистичные имена, адреса, телефоны,
# email-ы, профессии и т.д. Очень полезна для тестирования программ.
print("=== Сгенерированные фейковые данные ===")
print(f"Имя: {fake.name()}")
print(f"Адрес: {fake.address()}")
print(f"Email: {fake.email()}")
print(f"Телефон: {fake.phone_number()}")
print(f"Профессия: {fake.job()}")
print("-" * 40)

# ==================== Часть 2 — Алгоритм Two Sum ====================

def two_sum(nums, target):
    """
    Находит два индекса чисел, сумма которых равна target.
    Решение с помощью двух вложенных циклов.
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):   # j начинается с i+1, чтобы не брать одно и то же число
            if nums[i] + nums[j] == target:
                return [i, j]
    return None  # если пара не найдена


# Пример из задания
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print("Задача Two Sum:")
print(f"Список: {nums}")
print(f"Target: {target}")
print(f"Индексы: {result}")
print(f"Проверка: {nums[result[0]]} + {nums[result[1]]} = {nums[result[0]] + nums[result[1]]}")