def main():
    old_salary = float(input())

    if old_salary <= 400:
        adjustment = 0.15
    elif old_salary <= 800:
        adjustment = 0.12
    elif old_salary <= 1200:
        adjustment = 0.10
    elif old_salary <= 2000:
        adjustment = 0.07
    else:
        adjustment = 0.04

    increase = adjustment * old_salary
    new_salary = old_salary + increase

    print('Novo salario: {:.2f}'.format(new_salary))
    print('Reajuste ganho: {:.2f}'.format(increase))
    print('Em percentual: {} %'.format(int(adjustment * 100)))


if __name__ == '__main__':
    main()
