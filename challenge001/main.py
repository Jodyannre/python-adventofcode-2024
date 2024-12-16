from functools import reduce

def main():
    part_one()
    part_two()


def part_two():
    file = open("./input/input.txt","r")
    left = []
    right = []
    accumulate = 0
    for line in file:
        items = line.replace("\n","").split("   ")
        left.append(int(items[0]))
        right.append(int(items[1]))
    for item in left:
        times = right.count(item)
        accumulate += times * item
    print(accumulate)
    file.close()


def part_one():
    file = open("./input/input.txt","r")
    left = []
    right = []
    for line in file:
        items = line.replace("\n","").split("   ")
        left.append(int(items[0]))
        right.append(int(items[1]))
    left.sort()
    right.sort()
    acumulate = reduce((lambda acc,pair: acc + abs(pair[0]-pair[1])), zip(left,right),0)
    print(acumulate)
    file.close()

if __name__ == '__main__':
    main()