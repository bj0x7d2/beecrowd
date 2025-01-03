def main():
    number = int(input())
    hours_worked = int(input())
    hourly_wage = float(input())

    salary = hours_worked * hourly_wage

    print('NUMBER = {}'.format(number))
    print('SALARY = U$ {:.2f}'.format(salary))


if __name__ == '__main__':
    main()
