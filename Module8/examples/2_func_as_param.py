# =========================================
#   Передача функции в качестве аргумента
#   Функции - объекты первого порядка
# =========================================

# Функции в python являются объектами первого класса (First Class Object).
# Это означает, что с функциями вы можете работать, также как и с данными:
# передавать их в качестве аргументов другим функциям, присваивать переменным


# Обычная функция принимающая число и выводящая его значение на экран
def f(value):
    print("value = ", value)


# Вызов функции
f(6)

# В переменной func сохранены ссылка на объект-функцию
func = f

# Теперь через переменную func можно вызвать функцию f()
func(10)


def stars(func, val):
    print("***************")
    func(val)
    print("***************")


# Мы можем передать одну функцию в качестве аргумента другой функциии вызвать ее внутри
stars(f, 6)