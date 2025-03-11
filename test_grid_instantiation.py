import squaredleGrid    # The code to test
import pytest


# Unit tests to ensure robust instantiation of the Squaredle Grid object, regardless of
# the inputs provided

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
    
    # instantiation of a grid which contains empty items (holes)
    # Paths cannot traverse holes
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
    
# Inputs should be all uppercase. Lower case entries are allowed,
# but are converted to uppercase.
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

# Invalid instantiation because the 2D grid is not
# rectangular. That is, not all rows have the same
# length
def test_sg_object_creation_ivalid_2D_grid_01():
    inputGrid = [['A','B','C'],
                 ['D','E','F'],
                 ['G','H','I','J']]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: 2D grid not rectangular"

def test_sg_object_creation_ivalid_2D_grid_02():
    inputGrid = [['A','B','C'],
                 ['D','E','F'],
                 []]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: 2D grid not rectangular"

def test_sg_object_creation_ivalid_2D_grid_03():
    inputGrid = [[],
                 ['D','E','F'],
                 ['G','H','I']]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: 2D grid not rectangular"

def test_sg_object_creation_invalid_2D_grid_04A():
    # 2x1 grid is smaller than minimum allowable grid (2x2). Exception
    # should be thrown when instantiating squaredle object
    inputGrid = [['A'],
                 ['B']]
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: grid less than minimum size"

def test_sg_object_creation_ivalid_2D_grid_04B():
    # Verify that an empty list is rejected
    inputGrid = []
    dictionaryList=["Hello", "woRld"]
    
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: empty list"

def test_sg_object_creation_ivalid_2D_grid_04C():
    # Verify the input grid is of type 'list', or inherits from 'list'
    inputGrid = "Hello World"
    dictionaryList=["Hello", "woRld"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: grid not type 'list'"

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
    assert str(excinfo.value) == "Invalid Input: not 2D list"

def test_sg_object_creation_invalid_grid_contents_01():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h',':']]
    dictionaryList=["Hello", "woRld"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: grid must contain only single characters [A-Z] or ''"

def test_sg_object_creation_invalid_grid_contents_02():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h','AB']]
    dictionaryList=["Hello", "woRld"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: grid must contain only single characters [A-Z] or ''"

def test_sg_object_creation_invalid_dictionary_not_sorted():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h','i']]
    dictionaryList=["World", "Hello"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: dictionary not sorted"

def test_sg_object_creation_invalid_dictionary_empty_list():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h','i']]
    dictionaryList=[]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: empty dictionary"

def test_sg_object_creation_dictionary_has_only_one_entry():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h','i']]
    dictionaryList=["World"]
    sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert sg.dictionaryList == ["WORLD"]

def test_sg_object_creation_dictionary_not_a_list():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G','h','i']]
    dictionaryList="Hello"
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: dictionary not type 'list'"

def test_sg_object_creation_grid_contains_numbers():
    # Only single characters [A-Za-z] or '' allowed in grid
    inputGrid = [['a','b','c'],
                 ['d','','F'],
                 ['G',7,'i']]
    dictionaryList=["Hello", "World"]
    with pytest.raises(Exception) as excinfo:
        sg = squaredleGrid.squaredleGrid(inputGrid, dictionaryList)
    assert excinfo.type == ValueError
    assert str(excinfo.value) == "Invalid Input: grid entries not strings"