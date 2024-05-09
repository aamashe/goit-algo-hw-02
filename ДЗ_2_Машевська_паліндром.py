from collections import deque


def is_palindrome(input_str):
    # Перетворюємо рядок в нижній регістр і видаляємо пробіли
    cleaned_str = input_str.lower().replace(" ", "")

    # Створюємо двосторонню чергу (deque) з очищеного рядка
    char_queue = deque(cleaned_str)

    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False  # Якщо хоч одна пара символів не збігається, рядок не є паліндромом

    return True  # Якщо всі пари символів збігаються, рядок є паліндромом


input_string = input("Введіть рядок: ")
result = is_palindrome(input_string)

if result:
    print(f'"{input_string}" - це паліндром.')
else:
    print(f'"{input_string}" - це не паліндром.')
