# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
max_l = 1
for el in names:
    if len(el) > max_l:
        max_l = len(el)
        max_name = el
print (max_name)
