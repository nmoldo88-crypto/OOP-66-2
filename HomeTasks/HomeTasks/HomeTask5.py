
import time
from functools import wraps

# ========== Задание 1 ==========
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.role == "admin":
            return func(user, *args, **kwargs)
        else:
            print("У вас нет доступа")
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

# ========== Задание 2 ==========
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {elapsed_time:.4f} секунд")
        return result
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")

# ========== Тестирование ==========
if __name__ == "__main__":
    print("=== Задание 1 — Проверка администратора ===")
    admin = User("Ardager", "admin")
    user = User("Bek", "user")

    delete_video(admin)  # Видео удалено
    delete_video(user)   # У вас нет доступа

    print("\n=== Задание 2 — Декоратор таймера ===")
    download_video()