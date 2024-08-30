print("Нахождение факториала натурального целого числа.");

# Функция нахождения факториала с помощью рекурсии
def findFactorial(n):
    if n == 0:
        return 1;
    return findFactorial(n - 1) * n;

num = int(input("Введите натуральное целое число: "));

for i in range(num, 0, -1):
    print(findFactorial(i));