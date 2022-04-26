from fractions import Fraction #included in challenge
from functools import reduce #included in challenge

def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)  #task was to write single line reduce function so that it is valid for test cases
    return t.numerator, t.denominator
    
#test cases by HackerRank
if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
