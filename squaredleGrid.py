
class squaredleGrid(object):
    def __new__(cls, inputGridArray, dictionaryList):
        print("Creating instance")

        # make sure the grid array is legitimate (rectangular 2D grid)

        if not squaredleGrid._is2dList(inputGridArray):
            raise ValueError('not 2D')

        if any(len(i) != len(inputGridArray[0]) for i in inputGridArray[1:]):
            raise ValueError('2D grid not rectangular')

        return super(squaredleGrid, cls).__new__(cls)


    def __init__(self, inputGridArray, dictionaryList):
        #todo: handle capitalization
        print("initializing instance")
        self.grid = [[character.upper() for character in row] for row in inputGridArray]
        self.dictionaryList = [x.upper() for x in dictionaryList]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        if self.rows < 2 or self.cols < 2:
            raise ValueError('Invalid Grid: Less than 2x2')
        if (self.rows * self.cols) > 100:
            raise ValueError('Invalid Grid: Too large to process')
        self.flatGrid = [item for sublist in self.grid for item in sublist]

        # make sure the grid items are single, ASCII characters
        if not all(isinstance(item, str) and len(item) in [0,1] and ('A' <= item <= 'Z' or item == '') for item in self.flatGrid):
            raise ValueError("Invalid Grid contents: Must be single characters [A-Z] or ''")

        self.adj_matrix = self.create_adj_matrix(self.grid)
        if self._emptyAdjacency(self.adj_matrix):
            raise ValueError('Invalid input Grid - empty adjacency')

    # Function to determine if an adjacency matrix is empty ()
    def _emptyAdjacency(self, adj):
        if all(all(element == 0 for element in row) for row in adj):
            return True
        return False

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

