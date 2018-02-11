#!/usr/bin/env python3

def get_info(module_name):
    '''
    Returns the dictionary of callable objects in the module
    and their doc strings: {'name':'doc_string', ...}
    
    module_name argument is a string name of module.
    '''
    names_dict = globals() #get the dictionary of global names: {'name':object, ...}
    if not module_name in names_dict: #module's not imported
        try:
            module = __import__(module_name) #import module and get it's object
        except ImportError:
            return None
    else:
        module = names_dict[module_name] #get the module object by it's name
    info = {}
    for name in dir(module): #loop through all the names in the module
        obj = getattr(module, name) #get the object inside the module by it's name
        if name[0] != '_' and callable(obj): #we don't want private, built-in and non-callable objects
            info[name] = obj.__doc__
    return info
    
def print_info(info, module_name):
    '''
    Prints info about callable objects.
    
    info arguments is a dictionary returned by get_info function.
    '''
    print(YELLOW + '-' * N + RESET) #yellow line
    print('The module {0}{1}{2} has the following callable objects:'.format(RED, module_name, RESET))
    for name in sorted(info):
        print(YELLOW + '-' * N + RESET)
        print('{0}{1}{2}'.format(BLUE, name, RESET)) #blue coloured module name
        print('*' * M)
        if info[name]: print(info[name])
        else: print("No info is provided in doc string.")
    print(YELLOW + '-' * N + RESET)

#bash colour escape sequences
BLUE = '\033[1;34m'
RED = '\033[1;31m'
YELLOW = '\033[1;33m'
RESET = '\033[0m'
N = 80
M = 10

if __name__ == '__main__':

    #let's test on functools module
    module_name = 'functools'

    info = get_info(module_name)
    if info:        
        print_info(info, module_name)
    elif info is None:
        print("Unknown module {0}{1}{2}!".format(RED, module_name, RESET))
    else:
        print("No callable objects found.")