#TASK-1
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

def add(numbersString):
    if len(numbersString) == 0:
        return 0
    elif len(numbersString) == 1:
        return int(numbersString)
    else:
        ans = numbersString.split(",")
        return int(ans[0]) + int(ans[1])
        
test()