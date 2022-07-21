# THIS is not easy for me. Had to find help online. 
# Code referred from to https://programs.programmingoneonone.com/2021/02/hackerrank-validating-phone-numbers-solution-python.html
# not familiar with regular expressions - still figuring it out what it all means 


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    if re.match(r'[7-9]\d{9}$',input()):   
        print('YES')  
    else:  
        print('NO')
