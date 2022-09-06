def c2n(charactersOfCode):
    numbersOfCode = []
    numbers = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    characters = list(str(charactersOfCode))
    for character in characters:
        switch = False
        for number in numbers:
            if character == number:
                character = str(numbers.index(number))
                numbersOfCode.append(character)
                switch = True
                break
        if not switch:
            numbersOfCode.append(character)
    return "".join(numbersOfCode)

