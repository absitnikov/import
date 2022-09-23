from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime
from colorama import Fore


def main():
    print(f'{Fore.RED}{datetime.now().date()}')
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
