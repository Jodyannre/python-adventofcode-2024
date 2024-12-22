from os import access
from typing import TextIO
import copy

def main():
    second_part()
    pass


def find_direction(data):
    positive = 0
    negative = 0
    for i in range(len(data)-2):
        acc = int(data[i])
        next = int(data[i+1])
        if acc < next:
            negative += 1
        else:
            positive += 1

    return True if positive > negative else False



#Esta mal da 424 y el correcto es 413
def second_part():
    file = MyFile('./input.txt')
    file.open()
    count_goods = 0
    safe = ""
    iteraciones = 0
    for line in file.get_file():
        bad_levels = 0
        count = True
        data = line.split(' ')
        safe = copy.deepcopy(data)
        decremental = find_direction(data)
        i = 0
        iteraciones+=1
        while i <len(data)-1:
            actual = int(data[i]) - int(data[i+1])
            if (actual == 0)\
                    or (decremental and not (0 < actual < 4))\
                    or (not decremental and  not (-4 < actual < 0)):
                bad_levels += 1
                if bad_levels > 1:
                    print(iteraciones)
                    print(data)
                    count = False
                    break
                if decremental:
                    if int(data[i]) > int(data[i+1]):
                        data.pop(i+1)
                    else:
                        if i+2 < len(data):
                            if int(data[i+1]) > int(data[i+2]):
                                data.pop(i+1)
                            else:
                                data.pop(i)
                        else:
                            data.pop(i+1)
                else:
                    if int(data[i]) <  int(data[i+1]):
                        data.pop(i+1)
                    else:
                        if i+2 < len(data):
                            if int(data[i + 1]) < int(data[i + 2]):
                                data.pop(i + 1)
                            else:
                                data.pop(i)
                        else:
                            data.pop(i + 1)
                i = 0

            i+=1
        count_goods+=1 if count else 0
    file.close()
    print(count_goods)


def first_part():
    file = MyFile('./input.txt')
    file.open()
    count_goods = 0
    for line in file.get_file():
        count = True
        data = line.split(' ')
        decremental = True if (int(data[0]) - int(data[1])) > 0 else False

        for i in range(len(data)-1):
            actual = int(data[i]) - int(data[i+1])
            if actual == 0:
                count = False
                break
            if decremental and not (0 < actual < 4):
                count = False
                break
            elif not decremental and  not (-4 < actual < 0):
                count = False
                break

        count_goods+=1 if count else 0

    file.close()
    print(count_goods)



class MyFile:
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__file = None

    def open(self):
        self.__file = open(self.__file_path, 'r')

    def close(self):
        self.__file.close()

    def get_file(self):
        return self.__file

if __name__ == '__main__':
    main()



