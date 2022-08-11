def einlesen (datei):

    f = open(datei, "r")
    lines = f.readlines()
    result = []
    bounds = []
    letters = []
    woerter = []
    
    for x in lines:
        y = x.strip("\n")
        result.append(y.split(" "))

    for r in result:
        bound = r[0].split("-")
        bounds.append(bound)

    for b in result:
        letter =b[1].strip(":")
        letters.append(letter)

    for c in result:
        wort = list(c[2])
        woerter.append(wort)

    return (letters, bounds, woerter)


def main():
    # aufgabe test
    datei = "numbers.txt"
    (letters, bounds, woerter) = einlesen(datei)
    # auswertung1

    richtige_anzahl_letter_in_pwd = auswertung1(letters, bounds, woerter)
    print(richtige_anzahl_letter_in_pwd)
    richtige_stelle_letter_in_pwd = auswertung2(letters, bounds, woerter)
    print(richtige_stelle_letter_in_pwd)


def boundcheck(bound, letter_count):
    min = int(bound[0])
    max = int(bound[1])
    if letter_count >= min and letter_count <= max:
        return True
    return False


def auswertung1(letters, bounds, woerter):
    # gehen durch alle Einträge
    # len(woerter) = len(letters) = len(bounds)
    count_good_pwd = 0
    length = len(woerter)
    for index in range(0, length):
        letter = letters[index]
        bound = bounds[index]
        wort = woerter[index]
        letter_count = 0

        for char in wort:
            if char == letter:
                letter_count += 1

        # boundcheck
        if boundcheck(bound, letter_count):
            count_good_pwd += 1
            
    return count_good_pwd

def auswertung2(letters, bounds, woerter):
    # gehen durch alle Einträge
    # len(woerter) = len(letters) = len(bounds)
    count_good_pwd = 0
    length = len(woerter)
    for index in range(0, length):
        letter = letters[index]
        bound = bounds[index]
        wort = woerter[index]
        stelle1 = int(bound[0])-1
        stelle2 = int(bound[1])-1
        
        len_wort = len(wort)
        stelle1_ok = False
        stelle2_ok = False
        if stelle1 < len_wort:
            letter_an_stelle1 = wort[stelle1]
            if letter == letter_an_stelle1:
                stelle1_ok = True
        if stelle2 < len_wort:
            letter_an_stelle2 = wort[stelle2]
            if letter == letter_an_stelle2:
                stelle2_ok = True
        if stelle1_ok ^ stelle2_ok: # ^ = xor
            count_good_pwd += 1
    return count_good_pwd        

if __name__ == "__main__":
    main()
