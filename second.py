# Step 1 - write test


def check(height, weight, res):
    """
    The function checks that all the input is int or float - nothing else will be accepted,
    checks if the weight and height are positive,
    checks if the sentence matches the BMI
    :param height: height of the person
    :param weight: weight of the person
    :param res: tuple of the calculated BMI and sentence
    :return: true if all the tests are validates, else false.
    """
    if not (isinstance(height, int) or isinstance(height, float)):
        return False
    if not (isinstance(weight, int) or isinstance(weight, float)):
        return False
    if not (isinstance(res[1], int) or isinstance(res[1], float)):
        return False
    if height <= 0 or weight <= 0 or res[1] <= 0:
        return False
    if res[1] < 18.5:
        if not res[0] == "Your BMI means that you are underweight":
            return False
    if res[1] > 25:
        if not res[0] == "Your BMI means that you are overweight":
            return False
    if res[1] < 25 and res[1] > 18:
        if not res[0] == "Your BMI means that your weight is correct":
            return False
    return True


# Step 2 - make it run


def calcBMI(height, weight):
    """
    The function gets the height and the weight and returns the calculated bmi
    The function checks if the inputs are numbers and positive.
    :param height: input - the height of the person
    :param weight: input - the weight of the person
    :return: tuple of the bmi and sentence matching the result
    """
    if (isinstance(height, int) or isinstance(height, float)) and isinstance(weight, int) or isinstance(weight, float):
        if height > 0 and weight > 0:
            res = float(weight) / ((float(height)) ** 2)
            if res < 18.5:
                return ("Your BMI means that you are underweight", res)
            elif res > 25:
                return ("Your BMI means that you are overweight", res)
            else:
                return ("Your BMI means that your weight is correct", res)
        else:
            raise ValueError("-----The height/weight has to be positive-----")
    else:
        raise ValueError("-----The height/weight has to be number-----")


# Step 3 - run the check function with the calculation function

def main():
    #Check for numbers that supposed to return true and value in the correct range
    res = calcBMI(1.80, 80)
    print(res)
    print(check(1.80, 80, res))
    # Check for numbers that supposed to return true and value above the range
    res = calcBMI(1.70, 100)
    print(res)
    print(check(1.70, 100, res))
    # Check for numbers that supposed to return true and value under the range
    res = calcBMI(1.80, 50)
    print(res)
    print(check(1.80, 50, res))
    # Check with negative height, supposed to return false and raise exception
    print(check(-1.80, 50, res))
    res = calcBMI(-1.80, 50)
    print(res)
    #check with negative weight, supposed to return false and raise exception
    print(check(1.80, -50, res))
    res = calcBMI(1.80, -50)
    print(res)
    #check with string for height, supposed to return false and raise exception
    res = calcBMI('lalala', 180)
    print(res)
    print(check('lalal', 180, res))
    # check with string for weight, supposed to return false and raise exception
    res = calcBMI(80,'lalala')
    print(res)
    print(check(80,'lalala',res))

main()
