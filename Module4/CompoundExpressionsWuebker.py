MAX = 10
MIN = 0
y = 5
if y > MAX:
    print("Y is Greater than MAX")
else:
    print("Y is less than MAX")
if y < MIN:
    print("Y is greater than MIN")
else:
    print("Y is greater than MIN")
x = 7
if x < MAX:
    if x > MIN:
        if x != MAX:
            if x != MIN:
                print("X is in between MAX and MIN value")
else:
    print("X is greater than or equal to Max or less than or equal to MIN")
if x < MAX:
    if x > MIN:
        if x != MAX:
            print("X is between MIN and MAX values and is not equal to MAX")
else:
    print("X is either not between MAX and MIN or is equal to MAX")
if x < MAX:
    if x > MIN:
        if x != MIN:
            print("X is in between MIN and MAX but not equal to MIN")
else:
    print("X is not between MIN and MAX or is equal to MIN")
