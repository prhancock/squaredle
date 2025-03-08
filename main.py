import squaredleGrid as sg

# inputGridArray = [['C','E','P'], 
#                   ['T','A','R']]

inputGridArray =   [['O','A','R', 'E'], 
                    ['L','w','L', 'D'],
                    ['L','K','Y','P'],
                    ['S','A','w','S']]

dictionaryList = []
with open("scrabbleDict2019.txt", "r") as file:
    dictionaryList = [line.rstrip() for line in file]

grid = sg.squaredleGrid(inputGridArray, dictionaryList)
paths = grid.getPaths(min_length=4)
for path in paths:
    print(f'{grid.pathToString(path)} {path}')