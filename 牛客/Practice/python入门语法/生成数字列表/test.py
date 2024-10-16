
# * 1
def func_1():
    str = input().split()
    num_list = []
    for i in str:
        num_list.append(int(i))
    return num_list

# * 2
def func_2():
    list = [int(i) for i in input().split()]
    return list


def main():
    print(func_1())
    print(func_2())
    
main()
