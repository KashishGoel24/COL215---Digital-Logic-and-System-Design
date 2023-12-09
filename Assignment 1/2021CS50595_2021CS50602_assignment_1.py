from K_map_gui_tk import *

def gray_code(i,n):
    # Returns gray-code for 'i' expressed in n binary digits
    if n==1:
        thisdict={0:(0,),1:(1,)}
        return thisdict[i]
    if n==2:
        thisdict={0:(0,0),1:(0,1),2:(1,1),3:(1,0)}
        return thisdict[i]

def variables(cell,key):
    #Takes as input the cell coordinates and returns the value of variables in that cell
    if(key==2):
        xlen,ylen=1,1
    if (key==3):
        xlen,ylen=1,2
    if (key==4):
        xlen,ylen=2,2
    return gray_code(cell[1],ylen)+gray_code(cell[0],xlen)   #Returns the gray code for variables

def evalfunc(cell, term, key):
    # cell-->(i,j) tuple
    # term-->list of max size =4
    # evaluates the expression for the given cell according to the term given.
    result = 1
    n = len(term)
    for i in range(n):
        if term[i] == 1:
            result = result and variables(cell, key)[i]
        elif term[i] == 0:
            result = result and not variables(cell, key)[i]
        else:
            pass
    return int(result)

def key(dimension):
    #dimension --> a tuple having number of rows and number of columns in k-map function.
    #returns key i.e. the number of variables for which k-map is made.
    if dimension==(2,2):
        return 2
    if dimension==(2,4):
        return 3
    if dimension==(4,4):
        return 4

def max_block(cell, term, dimension_map):
    # finds maximal valid block size (i.e. the block which evaluates to 1 for the term given) with cell as the top-left corner
    rows=dimension_map[0]
    columns=dimension_map[1]
    key_map=key(dimension_map)
    if (not evalfunc(cell, term, key_map)):
        return 0
    # block should have cells not containing 0
    else:
        # traversing the rows
        i = 0
        while (i < rows):
            if not evalfunc(((cell[0] + i) % rows, cell[1]), term, key_map):
                break
            else:
                i += 1
        # traversing the columns
        j = 0
        while (j < columns):
            if not evalfunc((cell[0], (cell[1] + j) % columns), term, key_map):
                break
            else:
                j += 1
        return [cell,((cell[0]+i-1)%rows,(cell[1]+j-1)%columns)]  #returns the top-left and bottom-right coordinate for maximal block possible


def area_block(block, dimension_map):
    #block --> list containing tuples of top left and botton right coordinate
    #Returns the area of the rectangle enclosed by top left and bottom right coordinate.
    cell1 = block[0]
    cell2 = block[1]
    (x1, y1) = cell1
    (x2, y2) = cell2
    if (x2 >= x1):
        rows = x2 - x1 + 1
    else:
        rows= x2 - x1 + 1 + dimension_map[0]
    if (y2 >= y1):
        columns = y2 - y1 + 1
    else:
        columns= y2 - y1 + 1 +dimension_map[1]
    return rows * columns

def dimension(block, dimension_map):
    #block --> list containing tuples of top left and botton right coordinate
    #returns the number of rows and columns of the rectangle enclosed by top-left and bottom-right coordinate.
    cell1 = block[0]
    cell2 = block[1]
    (x1, y1) = cell1
    (x2, y2) = cell2
    if (x2 >= x1):
        rows = x2 - x1 + 1
    else:
        rows = x2 - x1 + 1 + dimension_map[0]
    if (y2 >= y1):
        columns = y2 - y1 + 1
    else:
        columns = y2 - y1 + 1 + dimension_map[1]

    return (rows,columns)


def is_legal_region(kmap_function, term):
    key = len(term)
    dimension_map=(len(kmap_function),len(kmap_function[0]))
    area = 0
    cell = (0, 0)  # cell will store cell(i,j) that gives the largest possible block

    #Traversing through the k-map and finding the region corresponding to the term given.
    for i in range(dimension_map[0]):
        for j in range(dimension_map[1]):

            if (max_block((i, j), term,dimension_map) != 0):
                if (area_block(max_block((i, j), term,dimension_map),dimension_map) > area):
                    area = area_block(max_block((i, j), term,dimension_map),dimension_map)
                    cell = (i, j)

    checking_area = max_block(cell, term, dimension_map)

    bottom_right = checking_area[1]
    top_left = checking_area[0]
    dimensions = dimension(checking_area, dimension_map)
    i = 0
    #traversing through the region to check whether it is a valid region i.e. it doesn't contain 0s.
    while (i < dimensions[0]):
        j = 0
        while (j < dimensions[1]):
            if kmap_function[(top_left[0] + i) % 4][(top_left[1] + j) % 4] == 0:
                return (top_left, bottom_right, False)
            else:
                j += 1
        i += 1

    return (top_left, bottom_right, True)
