import squaredleGrid    # The code to test
import pytest

def test_sg_object_creation_3x3():
    inputGrid = [['a','b','c'],
                 ['d','e','f'],
                 ['g','h','i']]
    dictionaryList=["hello", "world"]

    sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert sg.rows == 3
    assert sg.cols == 3
    assert sg.flatGrid == ['A','B','C','D','E','F','G','H','I']
    assert sg.dictionaryList == ["HELLO", "WORLD"]
    assert sg.adj_matrix == [[0,1,0,1,1,0,0,0,0],
                             [1,0,1,1,1,1,0,0,0],
                             [0,1,0,0,1,1,0,0,0],
                             [1,1,0,0,1,0,1,1,0],
                             [1,1,1,1,0,1,1,1,1],
                             [0,1,1,0,1,0,0,1,1],
                             [0,0,0,1,1,0,0,1,0],
                             [0,0,0,1,1,1,1,0,1],
                             [0,0,0,0,1,1,0,1,0]]
    
def test_sg_object_creation_3x3_hole_in_middle():
    # adjacency matrix should avoid creating edges where
    # there are 'holes' in the grid
    inputGrid = [['a','b','c'],
                 ['d','','f'],
                 ['g','h','i']]
    dictionaryList=["hello", "world"]

    sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert sg.rows == 3
    assert sg.cols == 3
    assert sg.flatGrid == ['A','B','C','D','','F','G','H','I']
    assert sg.dictionaryList == ["HELLO", "WORLD"]
    assert sg.adj_matrix == [[0,1,0,1,0,0,0,0,0],
                             [1,0,1,1,0,1,0,0,0],
                             [0,1,0,0,0,1,0,0,0],
                             [1,1,0,0,0,0,1,1,0],
                             [0,0,0,0,0,0,0,0,0],
                             [0,1,1,0,0,0,0,1,1],
                             [0,0,0,1,0,0,0,1,0],
                             [0,0,0,1,0,1,1,0,1],
                             [0,0,0,0,0,1,0,1,0]]
    

def test_sg_object_creation_lower_case_grid():
    # inputGrid and dictionary should be uppercase
    # in the squaredle object
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h','i']]
    dictionaryList=["Hello", "woRld"]
    sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert sg.grid == [['A','B','C'],
                       ['D','','F'],
                       ['G','H','I']]
    assert sg.dictionaryList==["HELLO", "WORLD"]

def test_sg_object_creation_ivalid_2D_grid_01():
    inputGrid = [['A','B','C'],
                 ['D','E','F'],
                 ['G','H','I','J']]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "2D grid not rectangular"

def test_sg_object_creation_ivalid_2D_grid_02():
    inputGrid = [['A','B','C'],
                 ['D','E','F'],
                 []]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "2D grid not rectangular"

def test_sg_object_creation_ivalid_2D_grid_03():
    inputGrid = [[],
                 ['D','E','F'],
                 ['G','H','I']]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "2D grid not rectangular"

def test_sg_object_creation_ivalid_2D_grid_04():
    # 2x1 grid is smaller than minimum allowable grid (2x2). Exception
    # should be thrown when instantiating squaredle object
    inputGrid = [['A'],
                 ['B']]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Grid: Less than 2x2"

def test_sg_object_creation_ivalid_2D_grid_05A():
    #minimum valid grid (2x2)
    inputGrid = [['A','B'],
                 ['C','D']]
    dictionaryList=["Hello", "woRld"]
    
    sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert sg.adj_matrix == [[0,1,1,1],
                             [1,0,1,1],
                             [1,1,0,1],
                             [1,1,1,0]]
    
def test_sg_object_creation_ivalid_2D_grid_05B():
    #maximum valid grid (10x10)
    inputGrid = [['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J'],
                 ['A','B','C','D','E','F','G','H','I','J']]

    dictionaryList=["Hello", "woRld"]
    
    sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    
    assert len(sg.adj_matrix) == 100
    assert sg.adj_matrix[0:2] == [[0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                                  [1,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def test_sg_object_creation_ivalid_2D_grid_06():
    # empty grid results in empty adjacency. Should throw an
    # exception

    inputGrid = [['',''],
                 ['','']]
    dictionaryList=["Hello", "woRld"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid input Grid - empty adjacency"

    
def test_sg_object_creation_ivalid_2D_grid_07():
    # grid results in empty adjacency. Should throw an
    # exception
    inputGrid = [['','A'],
                 ['','']]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid input Grid - empty adjacency"
    
def test_sg_object_creation_ivalid_2D_grid_08():
    #3D grid not allowed
    inputGrid = [[['A','B'],['C','D']],
                 [['E','F'],['G','H']],
                 [['I','J'],['K','L']]]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "not 2D"

def test_sg_object_creation_invalid_grid_contents_01():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h',':']]
    dictionaryList=["Hello", "woRld"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Grid contents: Must be single characters [A-Z] or ''"

def test_sg_object_creation_invalid_grid_contents_02():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h','AB']]
    dictionaryList=["Hello", "woRld"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Grid contents: Must be single characters [A-Z] or ''"

