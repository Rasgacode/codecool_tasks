def moves(rotated):
    can_random = False
    for x in range(4):
        first_index = rotated[x][0]
        second_index = rotated[x][1]
        third_index = rotated[x][2]
        fourth_index = rotated[x][3]
        observer = [True, True]
        for y in range(1, 4):
            if rotated[x][y] == 0:
                continue
            else:
                if y == 1 and first_index == 0:
                    first_index += second_index
                    second_index = 0
                    can_random = True
                elif y == 1 and first_index == second_index:
                    first_index += second_index
                    second_index = 0
                    observer[0] = False
                    can_random = True
                elif y == 2 and second_index == 0 and first_index == 0:
                    first_index += third_index
                    third_index = 0
                    can_random = True
                elif y == 2 and second_index == 0 and first_index == third_index and observer[0] == True:
                    first_index += third_index
                    third_index = 0
                    observer[0] = False
                    can_random = True
                elif y == 2 and second_index == 0:
                    second_index += third_index
                    third_index = 0
                    can_random = True
                elif y == 2 and second_index == third_index:
                    second_index += third_index
                    third_index = 0
                    observer[1] = False
                    can_random = True
                elif y == 3 and third_index == 0 and second_index == 0 and first_index == 0:
                    first_index += fourth_index
                    fourth_index = 0
                    can_random = True
                elif y == 3 and third_index == 0 and second_index == 0 and first_index == fourth_index and observer[0] == True:
                    first_index += fourth_index
                    fourth_index = 0
                    can_random = True
                elif y == 3 and third_index == 0 and second_index == 0:
                    second_index += fourth_index
                    fourth_index = 0
                    can_random = True
                elif y == 3 and third_index == 0 and second_index == fourth_index and observer[1] == True:
                    second_index += fourth_index
                    fourth_index = 0
                    can_random = True
                elif y == 3 and third_index == 0:
                    third_index += fourth_index
                    fourth_index = 0
                    can_random = True
                elif y == 3 and third_index == fourth_index:
                    third_index += fourth_index
                    fourth_index = 0
                    can_random = True
        rotated[x][0] = first_index 
        rotated[x][1] = second_index
        rotated[x][2] = third_index
        rotated[x][3] = fourth_index
    return  can_random


