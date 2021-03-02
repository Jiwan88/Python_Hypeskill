cells = '         '
print('''
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7], cells[8]))

cells_match = [['1', '3'], ['2', '3'], ['3', '3'], ['1', '2'],
               ['2', '2'], ['3', '2'], ['1', '1'], ['2', '1'], ['3', '1']]
cell_list = [x for x in cells]
cell_list_full = [cell_list[i] for i in range(9) if (cell_list[i] != ' ')]


def option():
    user_input = input("Enter the coordinates: >")
    coordinates = user_input.split(' ')
    x = coordinates[0]
    y = coordinates[1]
    global cells_match, cell_list, empty
    count_o, count_x, empty = 0, 0, 9
    for i in range(9):
        if cell_list[i] == 'X':
            count_x += 1
        if cell_list[i] == 'O':
            count_o += 1
        
        
    if x.isdigit() and y.isdigit():
        if 1 <= int(x) <= 3 and 1 <= int(y) <= 3:
            for i in range(9):
                if coordinates == cells_match[i]:
                    if cell_list[i] == ' ':
                        cell_list[i] = 'X' if (count_o - count_x == 1 or count_o - count_x == 0) else "O"
                    else:
                        print("This cell is occupied! Choose another one!")
                        option()
            print('''
---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(cell_list[0], cell_list[1], cell_list[2], cell_list[3], cell_list[4], cell_list[5], cell_list[6], cell_list[7], cell_list[8]))
            win_func()
            option()
            
            
            
        else:
            print("Coordinates should be from 1 to 3!")
            option()
    else:
        print("You should enter numbers!")
        option()


def win_func():
    # cell_list_full = [i for i in range(9) if all(cell_list[i] != ' ')]
    global cell_list
    cell_list_full = [cell_list[i] for i in range(9) if (cell_list[i] != ' ')]
    # print("cell_list_full length ", len(cell_list_full))

    x_win = ['X', 'X', 'X']
    y_win = ['O', 'O', 'O']

    win1 = True if ((cell_list[0:3] == x_win or cell_list[0:7:3] == x_win or cell_list[0:9:4] == x_win) or (
            cell_list[0:3] == y_win or cell_list[0:7:3] == y_win or cell_list[0:9:4] == y_win)) else False


    win2 = True if ((cell_list[3:6] == x_win or cell_list[1:8:3] == x_win or cell_list[2:7:4] == x_win) or (
        cell_list[3:6] == y_win or cell_list[1:8:3] == y_win or cell_list[2:7:4] == y_win)) else False

    win3 = True if ((cell_list[6:9] == x_win or cell_list[2:9:3] == x_win) or (
        cell_list[6:9] == y_win or cell_list[2:9:3] == y_win)) else False

    win = win1 or win2 or win3


    if win1 == True:  #and (cell_list[0] == 'X' or cell_list[0] == 'O'):
        print(f'{cell_list[0]} wins')
        exit()
    if win2 == True: #and (cell_list[4] == 'X' or cell_list[4] == 'O'):
        print(f'{cell_list[4]} wins')
        exit()
    if win3 == True: # and (cell_list[8] == 'X' or cell_list[8] == 'O'):
        print(f'{cell_list[8]} wins')
        exit()
    if win == False and len(cell_list_full) == 9:
        print("Draw")
        exit()


option()



#damn, this took me my whole night or whole day like 4-5 hrs, how to think this shit my mind time like 22:34
