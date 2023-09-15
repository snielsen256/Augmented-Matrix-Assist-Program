"""
Augmented Matrix Assist
Stephen Nielsen
9/13/2023
"""

# 1 2 3 4 5 6 7 8 9 10 11 12

def main():

    """
    Create matrix
    """
    print("Augmented Matrix Assist Program - Stephen Nielsen")
    print("CREATE MATRIX ----------")
    input_col = input("How many columns? (number of variables + 1): ")

    input_col = int(input_col)

    # get data
    raw_content = input("Enter the values for the matrix, from left to right, then top to bottom. Use one space only between numbers, no commas: ")

    # turn data into an array
    split_content = raw_content.split(" ")
    
    # convert array from string to float
    for item in split_content:
        item = float(item)

    # make sure the number if items is divisible by the column count
    while not((len(split_content) % input_col) == 0):
        split_content.append(0)

    # turns list into matrix by splitting the array into smaller arrays
    matrix = [split_content[i:i+input_col] for i in range(0, len(split_content), input_col)]
    

    

    """
    Begin cycle
    """
    print("ALTER MATRIX ----------")
    history = []
    history.append(matrix)
    while True:
        # display
        display(matrix)

        # make decision
        choice = input("| 1) Swap rows | 2) Scale row | 3) Scale and Add | 4) Undo | 5) Exit | : ")
        choice = int(choice)
        
        if choice == 1:
            swap(matrix)
        elif choice == 2:
            scale(matrix)
        elif choice == 3:
            scale_add(matrix, input_col)
        elif choice == 4:
            if len(history) >= 1:
                matrix = history.pop()
        else:
            break

        # add to history
        if not(choice == 4):
            history.append(matrix)

    print("TERMINATED")

def swap(matrix):
    row_choices = input("Enter <first row index> <second row index> : ")
    row_choices = row_choices.split(" ")

    # turn into int and compensate for lists starting at 0
    index_1 = int(row_choices[0]) - 1
    index_2 = int(row_choices[1]) - 1

    # swap
    placeholder = matrix[index_1]
    matrix[index_1] = matrix[index_2]
    matrix[index_2] = placeholder

def scale(matrix):
    choices = input("Enter <row index> <factor>: ")
    choices = choices.split(" ")


    # turn into int and compensate for lists starting at 0
    row_index = int(choices[0]) - 1
    if "/" in choices[1]:
        division = choices[1].split("/")
        factor = float(division[0]) / float(division[1])
    else:
        factor = float(choices[1])

    # scale
    new_row = []
    for item in matrix[row_index]:
        new_row.append(float(item) * float(factor))
    
    matrix[row_index] = new_row

def scale_add(matrix, num_col):
    choices = input("Enter <row to scale> <row to alter> <factor>: ")
    choices = choices.split(" ")

    # turn into int and compensate for lists starting at 0
    row_index_1 = int(choices[0]) - 1
    row_index_2 = int(choices[1]) - 1
    if "/" in choices[2]:
        division = choices[2].split("/")
        factor = float(division[0]) / float(division[1])
    else:
        factor = float(choices[2])

    # scale
    new_row = []
    for item in matrix[row_index_1]:
        new_row.append(float(item) * float(factor))
    
    # add to row
    for i in range(0, num_col):
        matrix[row_index_2][i] = float(matrix[row_index_2][i]) + new_row[i]

def display(matrix):
    index = 1
    space = 4

    #print
    for row in matrix:
        print(f"{index}: [ ", end="")
        for item in row:
            if float(item) % 1 == 0:
                print(f" {str('%g'%(float(item))).center(space)} ", end="")
            else:
                print(f" {str(item).center(space)} ", end="")
        print(" ]")
        index += 1
    print("----------------")

if __name__ == '__main__':
    main()

   