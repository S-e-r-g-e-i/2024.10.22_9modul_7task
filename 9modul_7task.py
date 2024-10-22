# Домашнее задание по теме "Декораторы"

def decorator(func):
    def mod(*args):
        mod_result = func(*args)
        flag = False
        for i in range(2, mod_result):
            if mod_result > 1 and mod_result % i == 0:
                flag += True
                if flag:
                    print('Составное')
                    break
            else:
                print('Простое')
                break
        return mod_result
    return mod



@decorator
def sum_three(*args):
    result_sum = sum(args)
    return result_sum

# Пример:
result = sum_three(2, 3, 6)
print(result)


