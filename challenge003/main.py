import re

def main():
    part_two()
    pass

def part_one():
    file = MyFile("./input.txt")
    file.open()
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    result = 0
    for line in file.get_file():
        matches = re.findall(regex, line)
        for match in matches:
            num1,num2 = match
            result += int(num1)*int(num2)
    print(result)


def part_two():
    file = MyFile("./input.txt")
    file.open()
    regex = r"(?:do\(\)|^)([\s\S]*?)(?:don't\(\)|$)"
    regex_mul = r"mul\((\d{1,3}),(\d{1,3})\)"
    result= 0
    matches = re.findall(regex, file.get_file().read())

    for match in matches:
        match_mul = re.findall(regex_mul, match)

        for match_do in match_mul:
            num1,num2 = match_do
            result = (int(num1)*int(num2)) + result

    print(result)
    file.close()

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