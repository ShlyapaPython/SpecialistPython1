# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример:
# Дано: [2, -5, 8, 9, -25, 25, 4]
# Результат: [3, 5, 2]
lst =[2, -5, 8, 9, -25, 25, 4]
lst1 = []
for el in lst:
    if el>0:
        el = el**0.5
        if el%1 == 0:
            el=el//1
            lst1.append(el)
print(lst1)
