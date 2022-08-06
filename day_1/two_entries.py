def two_entries(input):
    result = 0
    for x in range(0,len(input)):
        for y in range(1,len(input)-1):
            if input[x] + input[y] == 2020:
                result = input[x] * input[y]
    return result

#part two of day_1
def three_entries(input):
    result = 0
    for x in range(0,len(input)):
        for y in range(1,len(input)-1):
            for z in range(2,len(input)-2):
                if input[x] + input[y] + input[z] == 2020:
                    result = input[x] * input[y] * input[z]
    return result


def main():
    input = [1721,979,366,299,675,1456]

    f = open("numbers.txt", "r")
    lines = f.readlines()
    result = []

    for x in lines:
        result.append(int(x.rstrip("\n")))
    
    test = two_entries(result)
    print(test)

    test2 = three_entries(result)
    print(test2)
    
if __name__ == "__main__":
    main()
