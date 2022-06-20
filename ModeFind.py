def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key

    return "key doesn't exist"

def nonRepeatingVal(newls, mode):
    for i in range(len(newls)):
        if newls[i] == mode:
            return 1
    return 0
def myMode(ls):
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



n = int(input("Enter size of list : "))
ls = []
for i in range(n):
    val = int(input(f"Enter value in index {i} : "))
    ls.append(val)

myMode(ls)



