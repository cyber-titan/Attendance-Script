# Attendance-Script
A Python script which prints absent roll numbers for input of present student roll numbers. 
It avoids manual hassle of taking attendance and then again checking for absent student roll numbers.

Functionalities of the script:
1. Wrong roll numbers identified from the input by comparing each input roll number if the roll number is present in master_data or not.
2. Multiple line to single line input.
  - Enter input in "space seperated in single line".
  - Makes it easy to make changes before hitting enter to remove a roll number in input.
3. Irrespecitive of input data order, output is in order.
  - Input roll numbers need not be in order (like 1, 2, 3... increasing order) as the script sorts the roll numbers before printing them.
  - Output is in ascending order (sorts present, absent and wrong roll numbers before printing).
4. Added loader to make it look cool.
5. Prints date.

Python Modules needed:
1. datetime
2. time
3. tqdm
