import sys

MIN_GRID_ROWS = 2
MIN_GRID_COLS = 2
MAX_GRID_SIZE = 100

class squaredleGrid(object):
    # def __new__(cls, inputGridArray, dictionaryList):
    #     print("Creating instance")
    #     return super(squaredleGrid, cls).__new__(cls)


    def __init__(self, inputGridArray, dictionaryList):

        try:
            self.grid = self._validateGrid(inputGridArray)
        except (ValueError, TypeError) as e:
            raise ValueError('Invalid Input: '+str(e))
        try:
            self.dictionaryList = self._validateDictionaryList(dictionaryList)
        except(ValueError, TypeError) as e:
            raise ValueError('Invalid Input: '+str(e))

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.flatGrid = [item for sublist in self.grid for item in sublist]

        self.adj_matrix = self.create_adj_matrix(self.grid)
        # make sure the adjacency matrix isn't empty (no paths can be traversed)
        if all(all(element == 0 for element in row) for row in self.adj_matrix):
            raise ValueError('Invalid input Grid - empty adjacency')

    def _validateGrid(self, grid):

        # make sure it's a list or decendent of type list
        if not isinstance(grid,list):
             raise ValueError("grid not type 'list'") 
        
        # make sure the grid is not empty
        if len(grid) == 0:
             raise ValueError("empty list") 

        # make sure the list is a 2D list (list of lists)
        if not squaredleGrid._is2dList(grid):
            raise ValueError('not 2D list')
        
        # make sure the list is regular (all rows have same length)
        if any(len(i) != len(grid[0]) for i in grid[1:]):
            raise ValueError('2D grid not rectangular')
        
        if len(grid) < MIN_GRID_ROWS or len(grid[0]) < MIN_GRID_COLS:
            raise ValueError('grid less than minimum size')
        
        if (len(grid) * len(grid[0])) > MAX_GRID_SIZE:
            raise ValueError('grid larger than maximum')
    
        # make sure the grid items are strings (or inherited from 'str')
        if not all(isinstance(item, str) for item in [item for sublist in grid for item in sublist]):
            raise ValueError("grid entries not strings")

        # make uppercase
        grid = [[character.upper() for character in row] for row in grid]
        #flatGrid = [item for sublist in grid for item in sublist]

        # make sure the grid items are strings (or inherited from 'str') and are are single, characters, A-Z or ''
        if not all(len(item) in [0,1] and ('A' <= item <= 'Z' or item == '') for item in [item for sublist in grid for item in sublist]):
            raise ValueError("grid must contain only single characters [A-Z] or ''")
        return grid
    

    def _validateDictionaryList(self, dictionary):
        # make sure it's a list or decendent of type list
        if not isinstance(dictionary,list):
             raise ValueError("dictionary not type 'list'") 

        # Make sure the dictionary isn't an empty list
        if len(dictionary) == 0:
            raise ValueError("empty dictionary")
        
        # make dictionary uppercase
        dictionary = [x.upper() for x in dictionary]

        # make sure the dictionary is sorted in ascending order
        if not all(dictionary[i] <= dictionary[i + 1] for i in range(len(dictionary) - 1)):
            raise ValueError("dictionary not sorted")
        
        return dictionary



    # Function to determine if a list has lists for elements (2D). It is called
    # in __new__ (before 'self' exits).
    # ToDo: consider moving to __init__
    def _is2dList(mylist):
        for item in mylist:
            if not isinstance(item,list):
                return False
            # make sure it's not more than 2D
            for subitem in item:
                if isinstance(subitem,list):
                    return False
        return True

    def create_adj_matrix(self, grid): #rows, cols):
        adj_matrix = [[0 for _ in range(self.rows*self.cols)] for _ in range(self.rows*self.cols)]
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == '':
                    continue
                potential_adjacent_indices=[(row-1,col-1),(row-1,col),(row-1,col+1),(row,col-1),(row,col+1),(row+1,col-1),(row+1,col),(row+1,col+1)]
                for tuple in potential_adjacent_indices:
                    if self.tupleInRange(tuple) and self.grid[tuple[0]][tuple[1]] != '':
                        adj_matrix[row*self.cols+col][tuple[0]*self.cols+tuple[1]]=1
        return adj_matrix

    def tupleInRange(self, tuple,):
        # rows=len(adj_matrix)
        # cols=len(adj_matrix[0])
        if tuple[0] in range(self.rows) and tuple[1] in range(self.cols):
            return True
        else:
            return False
        
    # Function to take a path (e.g. '[2,3,4]') and map it into a string
    # based on the grid characters
    def pathToString(self, path):
        return "".join(list(map(lambda i: self.flatGrid[i], path)))


    def isGoodPath(self, path):
        stringPrefix = self.pathToString(path)
        prefixLength = len(stringPrefix)
        low = 0
        high = len(self.dictionaryList) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.dictionaryList[mid][:prefixLength] == stringPrefix:
                return True
            elif self.dictionaryList[mid] < stringPrefix:
                low = mid + 1
            else:
                high = mid - 1

        return False
    

    def stringInDictionary(self, target):
        low = 0
        high = len(self.dictionaryList) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.dictionaryList[mid] == target:
                return True
            elif self.dictionaryList[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False    

    def getPaths(self, min_length=4):
        validPaths = []
        paths = list(self.iter_paths(min_length))
        for path in paths:
            stringCandidate = self.pathToString(path)
            if self.stringInDictionary(stringCandidate):
                validPaths.append(path)
        return validPaths

    def iter_paths(self, min_length=4, path=None):
        # different paths for starting and recurring
        # you could use two different methods, the first calling the second and 
        #   the second calling itself, if you wanted
        if not path:
            for start_node in range(len(self.adj_matrix)):
                yield from self.iter_paths(min_length, [start_node])
        else:
            #print(f'path is {path}')
            # yield a path as soon as we first encounter it
            if len(path) >= min_length:
                yield path
            # if we encounter a cycle (current location has been visited before)
            # then don't continue to recur
            if path[-1] in path[:-1] or not self.isGoodPath(path):  
                return
            # search for all paths forward from the current node, recursively
            current_node = path[-1]
            for next_node in range(len(self.adj_matrix[current_node])):
                if self.adj_matrix[current_node][next_node] == 1 and next_node not in path:
                    yield from self.iter_paths(min_length, path + [next_node])

