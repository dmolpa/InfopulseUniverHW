import random

def get_input():
    '''ask user width and height. returns a tuple with two ints. handles value error.'''
    try:                                                                                  # trying to get ints from input
        width = int(input('desired width of field: '))
        height = int(input('desired height of field: '))
        return width, height                                                              # return if ok
    except ValueError:
        print('looks like it is not an integer') 
        
def generate_matrix():
    '''calls 'get_input' and return a matrix. 
    example: matrix_generator.generate_matrix()''' 
    size = get_input()                                                                     # (width, height) tuple

    matrix = [[random.randint(0,1) for i in range(0,size[0])] for i in range(0,size[1])]  # [[row] columns]
        
    return matrix

def print_matrix(matrix):
    ''' expect matrix as input. prints matrix row by row. example: matrix_generator.print_matrix()'''
    if isinstance(matrix, list):
        for each_row in matrix:                                                                # prints row by row
            print(each_row) 
    else:
        print(f'looks like input is a {type(matrix)} an not a list')

if __name__ == '__main__':
    matrix = generate_matrix()                                                                  # generate matrix
    print_matrix(matrix)                                                                       # prints matrix