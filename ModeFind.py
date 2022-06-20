def get_key(val, my_dict):
    """

    :param val: An Integer
    :param my_dict: A dictionary
    :return: Will return key against specific value.
    """
    ls = []
    for key, value in my_dict.items():
        if val == value:
            ls.append(key)
    if len(ls) > 1:
        return key
    else:
        return ls[0]

    return "key doesn't exist"

def nonRepeatingVal(newls, mode):
    """

    :param newls: A list
    :param mode:  An Integer
    :return: Will return 1 if it will find same value as saved in mode var
    otherwise will return 0.
    """
    for i in range(len(newls)):
        if newls[i] == mode:
            return 1
    return 0
def myMode(ls):
    """

    :param ls: A list
    This function will calculate the mode with help of other functions.
    """
    print(ls)
    newls = []
    dict = {}
    for i in range(len(ls)):
        mode = ls[i]
        count_mode = 1
        if i > 0 and nonRepeatingVal(newls, mode):
            continue
        newls.append(mode)
        for j in range(i + 1, len(ls)):
            if mode == ls[j]:
                count_mode = count_mode + 1
        dict[mode] = count_mode

    val = dict.values()
    val = max(val)
    key = get_key(val, dict)
    print(f"So the mode is : {key}")


if __name__ == '__main__':
    n = int(input("Enter size of list : "))
    ls = []
    for i in range(n):
        val = int(input(f"Enter value in index {i} : "))
        ls.append(val)

    myMode(ls)



