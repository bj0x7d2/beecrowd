def main():
    salary = float(input())

    tax = 0
    free_tax = False
    if salary > 4500:
        tax = 1500 * 0.18 + 1000 * 0.08
        tax += (salary - 4500) * 0.28
    elif salary > 3000:
        tax = 1000 * 0.08
        tax += (salary - 3000) * 0.18
    elif salary > 2000:
        tax = (salary - 2000) * 0.08
    else:
        free_tax = True
    
    if free_tax:
        print('Isento')
    else:
        print('R$ {:.2f}'.format(tax))


if __name__ == '__main__':
    main()
