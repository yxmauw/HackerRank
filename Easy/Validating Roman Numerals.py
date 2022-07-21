# Not sure why this is considered easy by HackerRank. Basically had to google for the Regular Expression that checks if a string is Valid Roman Numeral or not. 
# Regular Expression copied from https://www.geeksforgeeks.org/validating-roman-numerals-using-regular-expression/
# input that Regular Expression to regex_pattern value

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	

import re
print(str(bool(re.match(regex_pattern, input()))))
