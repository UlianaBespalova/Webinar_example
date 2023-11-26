
filters = ["Черно-белый"]


print('Добрый день! Выберите фильтр:')
print('Введите число')

for i in range(len(filters)): # Показываем меню
    print(f"{i+1}. {filters[i]}")
print(f"{len(filters)+1}. Выход")

num = int(input()) # Пользователь вводит норер
our_filter = filters[num - 1] # Берём нужный фильтр
print(f"Вы выбрали фильтр {our_filter}") # Печатаем описание

print("Программа завершилась!")

