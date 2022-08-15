def einlesen(input):
    f = open(input, "r")
    lines = f.readlines()
    tree_map = []

    for line in lines:
        tree_line = []
        for char in line:
            if char == "\n":
                break
            if char == '#':
                tree_line.append(True)
            else:
                tree_line.append(False)
        tree_map.append(tree_line)
    return tree_map


def main():
    tree_map = einlesen('input.txt')
    slope_x = 3
    slope_y = 1
    slope_coordinates = slope_to_coordinates(slope_x,slope_y,len(tree_map[0]),len(tree_map))

    tree_count = count_trees(tree_map,slope_coordinates)
    print(tree_count)

    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    tree_count_all_slopes = count_trees_in_slopes(slopes,tree_map)
    print(tree_count_all_slopes)

    
def slope_to_coordinates(rightsteps,downsteps,laenge_x,laenge_y):
    akku_x = 0
    akku_y = 0
    slope_coordinates = []
    while (akku_y < laenge_y):
        slope_coordinates.append((akku_x,akku_y))
        
        akku_x = (akku_x + rightsteps) % laenge_x
        akku_y += downsteps
    return slope_coordinates


def count_trees(tree_map,slope_coordinates):
    tree_count = 0
    for coord in slope_coordinates:
        (x, y) = coord
        if tree_map[y][x] == True:
            tree_count += 1
    return tree_count


def count_trees_in_slopes(slopes,tree_map):
    tree_count_akku = 1
    for slope in slopes:
        (slope_x,slope_y) = slope
        slope_coordinates = slope_to_coordinates(slope_x,slope_y,len(tree_map[0]),len(tree_map))
        tree_count = count_trees(tree_map,slope_coordinates)
        tree_count_akku *= tree_count
    return tree_count_akku


if __name__ == "__main__":
    main()
