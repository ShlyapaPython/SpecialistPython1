# По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений:
# «n коров», «n корова», «n коровы», правильно склоняя слово «корова».
# Формат входных данных
# Дано целое положительное число n
# Формат выходных данных
# Программа должна вывести введенное число n и одно из слов (на латинице):
# коров, корова или коровы
# Например, 1 корова, 2 коровы, 5 коров, 125 коров.

# TODO: your code here
num_k = int(input("введите количество коров ")) 
if 11 <= num_k <= 20 :
    print ("На лугу пасется", num_k, "коров")
elif num_k%10==1:
    print ("На лугу пасется", num_k, "корова")        
elif num_k%10==2 or num_k%10==2 or num_k%10==3 or num_k%10==4:
    print ("На лугу пасется", num_k, "коровы")
else:
    print ("На лугу пасется", num_k, "коров")
