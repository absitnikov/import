from application.db.people import *
from application.salary import *
from datetime import *


def main():
    print(datetime.now().date())
    get_employees()
    calculate_salary()

if __name__ == '__main__':
    main()