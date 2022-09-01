def einlesen(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    instructions = []
    for line in input_data_lines:
        instruction_line = line.split('\n')
        instruction_and_number = instruction_line[0].split(' ')
        instructions.append(instruction_and_number)
        
    return instructions

def execute_instructions(instructions):
    akku = 0
    durchlaufene_indizes = []
    i = 0
    while i not in durchlaufene_indizes:
        if instructions[i][0] == 'nop':
            durchlaufene_indizes.append(i)
            i += 1
        if instructions[i][0] == 'acc':
            akku += int(instructions[i][1])
            durchlaufene_indizes.append(i)
            i += 1
            print(akku)
        if instructions[i][0] == 'jmp':
            durchlaufene_indizes.append(i)
            i += int(instructions[i][1])
            print("hey")
            print(i)
        print(akku)
    print(durchlaufene_indizes)

def main():
    test = einlesen("input_small.txt")
    execute_instructions(test)
    

if __name__ == "__main__":
    main()
