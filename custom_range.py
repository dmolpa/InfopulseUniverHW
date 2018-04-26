def custom_range(start,stop=0):
    ''' 
    custom_range expect one or two integers and calls start_custom_range function/generator
    
    custom_range(start,stop)
    custom_range(stop) - in this case 'start == 0'
    
    if one int is given function assign given int value to 'stop' and sets 'start == 0'
    returns a generator
    '''
    if stop == 0:
        stop = start
        start = 0
    def start_custom_range(start,stop):
        '''
        takes two ints and generates the sequence
        upto but not including 'stop' value
        '''
        yield start
        if start+1 < stop:
            yield from start_custom_range(start+1,stop)
    return start_custom_range(start,stop)

for i in custom_range(14):
    print(i)