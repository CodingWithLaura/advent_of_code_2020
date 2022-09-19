from collections import deque

def einlesen(input_path):
    #einlesen2 ähnlich nur andersrum
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    bag_dict = {}
    for line in input_data_lines:
        if "no other bags" not in line:
            parts = line.replace(" bags","").replace(" bag","").split(" contain")
            first_part = parts[0]
            last_part = parts[1]
            last_raw_parts = last_part.split(",")
            last_colorbags = []
            for part_with_num in last_raw_parts:
                numer_and_color_list = part_with_num[1:].split(" ", 1)
                number = int(numer_and_color_list[0])
                color = numer_and_color_list[1].replace("\n", "").replace(".", "")
                last_colorbags.append(color)
            for key in last_colorbags:
                if key in bag_dict:
                    bag_dict[key].append(first_part)
                else:
                    bag_dict[key] = [first_part]
    return bag_dict

def einlesen_part_two(input_path):
    file_handler = open(input_path,"r")
    input_data_lines = file_handler.readlines()

    bag_dict = {}
    for line in input_data_lines:
        if "no other bags" not in line:
            parts = line.replace(" bags", "").replace(" bag","").split(" contain")
            first_part = parts[0]
            last_part = parts[1]
            last_raw_parts = last_part.split(",")
            last_colorbags = []
            
            #print(last_raw_parts)
            for parts_with_num in last_raw_parts:
                number_and_color_list = parts_with_num[1:].split(" ", 1)
                number = int(number_and_color_list[0])
                color = number_and_color_list[1].replace("\n", "").replace(".","")
                last_colorbags.append((number,color))
            print(last_colorbags)
            bag_dict[first_part] = last_colorbags            
        else: # here are no other bags
            parts = line.replace(" bags", "").replace(" bag","").split(" contain")
            first_part = parts[0]
            bag_dict[first_part] = []
    return bag_dict

def find_contained_bags(bag_dict):
    akku_numbers = 0
    next_bags_list = deque()    # <- müssen tuble mit anzahl
    next_bags_list.appendleft((1,"shiny gold"))
    while len(next_bags_list) > 0 :
        print("next_bags_list: {}".format(next_bags_list))
        (number, next_bag) = next_bags_list.pop()
        new_bag_list_raw = bag_dict[next_bag]
        if len(new_bag_list_raw) > 0:
            # müssen mal number die anzahl multiplizieren für die nächsten bags die wir durchgehen wollen
            for (bag_number, new_bag) in new_bag_list_raw:
                next_bags_list.appendleft((number * bag_number, new_bag))    
        akku_numbers += number
    return akku_numbers - 1
    

def find_containing_bags(bag_dict):
    akku = {}
    next_bags_list = deque()
    next_bags_list.appendleft("shiny gold")
    while len(next_bags_list) > 0 :
        next_bag = next_bags_list.pop()
        new_bag_list = []
        if next_bag in bag_dict:
            new_bag_list = bag_dict[next_bag]
        for bag in new_bag_list:
            next_bags_list.appendleft(bag)
        akku[next_bag] = True
    return akku    
    
def main():
    print("part1")
    data_structure = einlesen("input.txt")
    print(data_structure)
    containing_bags = find_containing_bags(data_structure)
    print("number of bags: {}".format(len(containing_bags)))
    print("contianing bags: {}".format(containing_bags))

    print("\npart2")
    data_structure2 = einlesen_part_two("input.txt")
    bag_numbers = find_contained_bags(data_structure2)
    print("bag_numbers: {}".format(bag_numbers))

if __name__ == "__main__":
    main()
