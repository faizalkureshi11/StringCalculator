#TASK-2
import pytest

def test():
    # Empty String
    assert(add("") == 0)
    # 1 digit Number
    assert(add("1") == 1)
    assert(add("2") == 2)
    # 2 digit Number
    assert(add("1,2") == 3)
    assert(add("2,3") == 5)
    # For Unknown Numbers
    assert(add("1,2,3") == 6)
    assert(add("2,3,4,5") == 14)
    assert(add("1,2,3,6,8") == 20)
    assert(add("2,3,7,7,6,9") == 34)

def add(numbersString):
    if len(numbersString) == 0:
        return 0
    elif len(numbersString) == 1:
        return int(numbersString)
    else:
        result = 0 
        ans = numbersString.split(",")
        for num in ans:
            result += int(num)
        return result
        
test()
