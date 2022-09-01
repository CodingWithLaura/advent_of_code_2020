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
    for i in range (0,len(instructions)):
        print(instructions[i][0])
        print(instructions[i][1])
        if instructions[i][0] == 'nop':
            durchlaufene_indizes.append([i][0])
        if instructions[i][0] == 'acc':
            akku += int(instructions[i][1])
            durchlaufene_indizes.append([i][0])
        if instructions[i][0] == 'jmp':
            #kp
    print(akku)
    print(durchlaufene_indizes)

def main():
    test = einlesen("input_small.txt")
    execute_instructions(test)
    

if __name__ == "__main__":
    main()
