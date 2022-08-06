def two_entries(input):
    result = 0
    for x in range(0,len(input)):
        for y in range(1,len(input)-1):
            if input[x] + input[y] == 2020:
                result = input[x] * input[y]
    return result
                

def main():
    input = [1721,979,366,299,675,1456]

    f = open("numbers.txt", "r")
    lines = f.readlines()
    result = []

    for x in lines:
        result.append(int(x.rstrip("\n")))
    print(result)
    
    test = two_entries(result)
    print(test)
    
if __name__ == "__main__":
    main()
