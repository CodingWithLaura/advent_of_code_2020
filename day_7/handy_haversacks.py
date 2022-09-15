def einlesen(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    bag_dict = {}
    for line in input_data_lines:
        if "no other bags" not in line:
            parts = line.replace(" bags","").replace(" bag","").split(" contain")
            first_part = parts[0]
            last_part = parts[1]
            last_raw_parts = last_part.split(",")
            last_parts = []
            for part_with_num in last_raw_parts:
                last_elements = part_with_num[1:].split(" ", 1)
                number = int(last_elements[0])
                real_part = last_elements[1].replace("\n", "").replace(".", "")
                last_parts.append(real_part)
            for key in last_parts:
                if key in bag_dict:
                    bag_dict[key].append(first_part)
                else:
                    bag_dict[key] = [first_part]
    print(bag_dict)
def main():
    data_structure = einlesen("bags_small.txt")

if __name__ == "__main__":
    main()
