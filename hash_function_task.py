import random
import string
import numpy as np

class HashTable:
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        """Хэш-функция на основе SHA-256."""
        return sum(ord(char) for char in str(key)) % self.size


    def insert(self, key, value):
        """Добавление пары ключ-значение в хэш-таблицу."""
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, (k) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Обновляем значение, если ключ уже существует
                return
        bucket.append((key, value))  # Добавляем новую пару

    def search(self, key):
        """Поиск значения по ключу в хэш-таблице."""
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(f"Ключ '{key}' не найден в хэш-таблице.")

    def delete(self, key):
        """Удаление пары ключ-значение из хэш-таблицы."""
        hash_key = self._hash_function(key)
        bucket = self.table[hash_key]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        raise KeyError(f"Ключ '{key}' не найден в хэш-таблице.")

    def fill_random(self, num_items, collision_keys=3):
        """
        Заполняет хэш-таблицу случайными значениями.
        num_items: количество случайных элементов для добавления.
        collision_keys: количество ключей, которые гарантированно вызовут коллизии.
        """
        def random_string(length=5):
            """Генерирует случайную строку фиксированной длины."""
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))

        # Добавляем случайные элементы
        for _ in range(num_items - collision_keys):
            key = random_string()
            value = random.randint(1, 1000)
            self.insert(key, value)

        # Добавляем элементы, которые вызовут коллизии
        base_key = random_string()
        for i in range(collision_keys):
            # Создаём ключи, которые будут иметь тот же хэш, что и base_key
            key = f"{base_key}_{i}"
            value = random.randint(1001, 2000)
            self.insert(key, value)
    def check_bucket_uniformity(self):
        """
        Проверяет равномерность заполнения бакетов.
        Возвращает:
        - bucket_sizes: список с количеством элементов в каждом бакете.
        - variance: дисперсия количества элементов в бакетах.
        - std_dev: стандартное отклонение.
        """
        bucket_sizes = [len(bucket) for bucket in self.table]
        variance = np.var(bucket_sizes)

        return {
            "bucket_sizes": bucket_sizes,
            "metric": variance,
        }
    def __str__(self):
        """Строковое представление хэш-таблицы для удобства отладки."""
        return str(self.table)