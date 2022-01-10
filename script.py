import sys
from random import randint


class Scale:
    __L__ = "lighter"
    __H__ = "heavier"
    def __init__(self):
        self._weight_count = 0

    def weight(self, left_arm, right_arm):
        if self._weight_count == 3:
            print("Weight count exceeded")
            sys.exit()
        self._weight_count += 1
        diff = sum(left_arm) - sum(right_arm)
        if diff < 0:
            return -1
        elif diff > 0:
            return 1
        return 0


s = Scale()

printSolutionFormat = "The inconsistent ball is the one with index {} (value {}) - {}"

if "--manual-input" in sys.argv:
    marbles = list(map(int, input().split()))[:12]
else:
    marble_weight = randint(200, 300)
    marbles = [marble_weight for _ in range(0xC)]

    inconsistent_index = randint(0, 11)
    inconsistent_value = randint(-100, 100)
    while inconsistent_value == 0:
        inconsistent_value = randint(-100, 100)

    marbles[inconsistent_index] = marbles[inconsistent_index] + inconsistent_value

print(marbles)

left_arm = marbles[:4]
right_arm = marbles[4:8]
table = marbles[8:]

result = s.weight(left_arm, right_arm)
if result == 0:
    left_arm = marbles[:3]
    right_arm = marbles[8:11]
    result = s.weight(left_arm, right_arm)
    weight_2_result = result

    if result == 0:
        result = s.weight([marbles[0]], [marbles[11]])
        heavier = True
        if result == 1:
            heavier = False
        print(printSolutionFormat.format(11, marbles[11], Scale.__H__ if heavier == 1 else Scale.__L__))

    else:
        left_arm = [marbles[8]]
        right_arm = [marbles[9]]
        result = s.weight(left_arm, right_arm)
        if result == 0:
            heavier = weight_2_result
            print(printSolutionFormat.format(10, marbles[10], Scale.__H__ if heavier == -1 else Scale.__L__))

        else:
            if result == 1:
                if weight_2_result == 1:
                    print(printSolutionFormat.format(9, marbles[9], Scale.__L__))
                else:
                    print(printSolutionFormat.format(8, marbles[8], Scale.__H__))
            else:
                if weight_2_result == 1:
                    print(printSolutionFormat.format(8, marbles[8], Scale.__L__))
                else:
                    print(printSolutionFormat.format(9, marbles[9], Scale.__H__))

elif result == 1:
    left_arm = marbles[9:] + [marbles[4]]
    right_arm = marbles[5:8] + [marbles[0]]
    table = marbles[1:4] + [marbles[8]]

    result = s.weight(left_arm, right_arm)
    if result == 0:
        result = s.weight([table[0]], [table[1]])
        if result == 0:
            print(printSolutionFormat.format(3, marbles[3], Scale.__H__))
        elif result == 1:
            print(printSolutionFormat.format(1, marbles[1], Scale.__H__))
        else:
            print(printSolutionFormat.format(2, marbles[2], Scale.__H__))
    elif result == 1:
        result = s.weight([marbles[5]], [marbles[6]])
        if result == 0:
            print(printSolutionFormat.format(7, marbles[7], Scale.__L__))
        elif result == 1:
            print(printSolutionFormat.format(6, marbles[6], Scale.__L__))
        else:
            print(printSolutionFormat.format(5, marbles[5], Scale.__L__))
    else:
        result = s.weight([marbles[4]], [marbles[8]])
        print("RR1 = {}".format(result))
        if result == 0:
            print(printSolutionFormat.format(0, marbles[0], Scale.__H__))
        else:
            print(printSolutionFormat.format(4, marbles[4], Scale.__L__))

else:
    left_arm = marbles[9:] + [marbles[0]]
    right_arm = marbles[1:4] + [marbles[4]]
    table = marbles[5:8] + [marbles[8]]

    result = s.weight(left_arm, right_arm)
    print("Result weight 2 = {}".format(result))
    if result == 0:
        result = s.weight([table[0]], [table[1]])
        if result == 0:
            print(printSolutionFormat.format(7, marbles[7], Scale.__H__))
        elif result == 1:
            print(printSolutionFormat.format(5, marbles[5], Scale.__H__))
        else:
            print(printSolutionFormat.format(6, marbles[6], Scale.__H__))
    elif result == 1:
        result = s.weight([marbles[1]], [marbles[2]])
        if result == 0:
            print(printSolutionFormat.format(3, marbles[3], Scale.__L__))
        elif result == 1:
            print(printSolutionFormat.format(2, marbles[2], Scale.__L__))
        else:
            print(printSolutionFormat.format(1, marbles[1], Scale.__L__))
    else:
        result = s.weight([marbles[0]], [marbles[8]])
        if result == 0:
            print(printSolutionFormat.format(4, marbles[4], Scale.__H__))
        else:
            print(printSolutionFormat.format(0, marbles[0], Scale.__L__))
