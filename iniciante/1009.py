def main():
    name = input()
    fixed_salary = float(input())
    total_sales = float(input())

    salary = fixed_salary + total_sales * 0.15

    print('TOTAL = R$ {:.2f}'.format(salary))


if __name__ == '__main__':
    main()
