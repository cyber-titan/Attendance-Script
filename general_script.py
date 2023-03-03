import datetime
from tqdm import tqdm
import time

def get_date():
    date = datetime.datetime.now()
    date = str(date.strftime('%d/%m/%Y'))
    return date

"""
total students roll numbers
can keep list of strings as roll numbers can also have alphabets
Example: 18H51A05A0
"""
master_data = [x for x in range(1, 11)]

# Welcome message
print("\t\t\t     Welcome Back AbhisheK!!!\n\n\t\t\t\tHave A Great Day.\n")
time.sleep(1)

"""
Added loading to make it look nice (optional)
"""
print('Loading Attendance Program.........\n')
for i in tqdm(range(int(30))):
    time.sleep(0.1)

print("\nEnter Roll Numbers Space Seperated In Same Line Everytime:")
roll_numbers = list(map(int, input().split(' ')))
# wrong stores wrong roll numbers entered, human error
present, wrong = [], []
absent = master_data.copy()

for roll in roll_numbers:
    if roll in absent:
        absent.remove(roll)
        present.append(roll)
    else:
        wrong.append(roll)

print("\nToday's Date: ", get_date())
print('Total Students: ', len(master_data))

print('Present Students: ', len(present))
present.sort()
for i in present:
    print(i)
print('\nAbsent Students: ', len(absent))
absent.sort()
for i in absent:
    print(i)
print('\nWrong or Re-Entered Roll Numbers Entered: ', len(wrong))
wrong.sort()
for i in wrong:
    print(i)
"""
input in single line, as it makes easy to delete few roll numbers while entering input also
Input: 1 2 3 3 30
"""
