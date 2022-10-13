from people import *
from salary import calculate_salary
from  datetime import datetime

if __name__ == '__main__':
    maan = Person("1234")
    maan.salary = [1, 4, 5, 6, 2, 76, 11]

    print(f'{datetime.now()} salary {calculate_salary(man)}')
    print(f'{datetime.now()} salary {calculate_salary(maan)}')