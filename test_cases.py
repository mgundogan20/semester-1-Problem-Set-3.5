from permutations import get_permutations
from powerset import generate_powerset
from matrix import determinant
from grid import print_paths

def test_permutations1():
  test1 = get_permutations('a')
  assert len(test1) == 1 and set(test1) == {'a'}

def test_permutations2():
  test2 = get_permutations('bc')
  assert len(test2) == 2 and set(test2) == {'bc', 'cb'}

def test_permutations3():
  test3 = get_permutations('abc')
  assert len(test3) == 6 and set(test3) == {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}

def test_permutations4():
  test4 = get_permutations('zaz')
  assert len(test4) == 6 and test4.count('azz') == 2 and test4.count('zaz') == 2 and test4.count('zza') == 2

def test_permutations5():
  test5 = get_permutations('noam')
  assert len(test5) == 24 and set(test5) == {'noam',  'onam',  'oanm',  'oamn',  'naom',  'anom',  'aonm',  'aomn',  'namo',  'anmo',
  'amno',  'amon',  'noma',  'onma',  'omna',  'oman',  'nmoa',  'mnoa',  'mona',  'moan',
   'nmao',  'mnao',  'mano',  'maon'}


def check_sets(output, correct):
    if len(output) != len(correct):
        return False
    for item1 in correct:
        found_in_output = False
        for item2 in output:
            if len(item1) == len(item2) and set(item1) == set(item2):
                found_in_output = True
        if not found_in_output:
            return False
    return True


def test_powerset1():
  test1 = generate_powerset([])
  correct1 = [[]]
  assert check_sets(test1, correct1)

def test_powerset2():
  test2 = generate_powerset([1])
  correct2 = [[], [1]]
  assert check_sets(test2, correct2)

def test_powerset3():
  test3 = generate_powerset([1, 2])
  correct3 = [[], [1], [2], [1, 2]]
  assert check_sets(test3, correct3)

def test_powerset4():
  test4 = generate_powerset([1,2,3])
  correct4 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
  assert check_sets(test4, correct4)

def test_powerset5():
  test5 = generate_powerset([1,2,3,4])
  correct5 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
  assert check_sets(test5, correct5)

def test_determinant1():
  assert determinant([[7]]) == 7

def test_determinant2():
  assert determinant([[4, 3],[5, 6]]) == 9

def test_determinant3():
  assert determinant([[3,1, 2], [-2,3, 7], [0, 4, 2]]) == -78

def test_determinant4():
  assert determinant([[7,12,6,5], [-3,7,-4,2],[5,5,-4,0], [8, 6, 9,3]]) == 308

def test_determinant5():
  assert determinant([[10,20,15,11,12], [14,2,10,5,8],[16,2,3,16,14], [8,12,-5,-4,2], [1,8,9,14,15]]) == -410964


def test_grid1(capsys):
  grid = [[4],[20]]
  print_paths(grid)
  captured = capsys.readouterr()
  out = captured.out.strip().split('\n')
  correct = ['[4, 20]']
  assert len(out) == len(correct) and set(out) == set(correct)

def test_grid2(capsys):
  grid = [[1,4,3],
        [5,6,7]]
  print_paths(grid)
  captured = capsys.readouterr()
  out = captured.out.strip().split('\n')
  correct = ['[1, 5, 6, 7]', '[1, 4, 6, 7]', ]
  assert len(out) == len(correct) and set(out) == set(correct)

def test_grid3(capsys):
  grid = [[1,20,30],
          [4,8,40]]
  print_paths(grid)
  captured = capsys.readouterr()
  out = captured.out.strip().split('\n')
  correct = ['[1, 20, 30, 40]', '[1, 4, 8, 40]', '[1, 4, 8, 20, 30, 40]']
  assert len(out) == len(correct) and set(out) == set(correct)


def test_grid4(capsys):
  grid = [[1, 2, 3],
        [3, 6, 7],
        [8, 10, 8],
        [9,11,13]]
  print_paths(grid)
  captured = capsys.readouterr()
  out = captured.out.strip().split('\n')
  correct = ['[1, 2, 3, 7, 8, 10, 11, 13]',
    '[1, 2, 3, 7, 8, 13]',
    '[1, 2, 6, 7, 8, 10, 11, 13]',
    '[1, 2, 6, 7, 8, 13]',
    '[1, 2, 6, 10, 11, 13]',
    '[1, 3, 6, 7, 8, 10, 11, 13]',
    '[1, 3, 6, 7, 8, 13]',
    '[1, 3, 6, 10, 11, 13]',
    '[1, 3, 8, 10, 11, 13]',
    '[1, 3, 8, 9, 11, 13]']
  assert len(out) == len(correct) and set(out) == set(correct)

def test_grid5(capsys):
  grid = [[1, 5, 6, 7],
        [11, 10, 9, 8],
        [12,13,14,15],
        [16,17,18,19]]
  print_paths(grid)
  captured = capsys.readouterr()
  out = captured.out.strip().split('\n')
  correct = ['[1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 19]',
    '[1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 18, 19]',
    '[1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 18, 19]',
    '[1, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18, 19]',
    '[1, 5, 6, 7, 8, 9, 10, 13, 14, 15, 19]',
    '[1, 5, 6, 7, 8, 9, 10, 13, 14, 18, 19]',
    '[1, 5, 6, 7, 8, 9, 10, 13, 17, 18, 19]',
    '[1, 5, 6, 7, 8, 9, 14, 15, 19]',
    '[1, 5, 6, 7, 8, 9, 14, 18, 19]',
    '[1, 5, 6, 7, 8, 15, 19]',
    '[1, 5, 6, 9, 10, 11, 12, 13, 14, 15, 19]',
    '[1, 5, 6, 9, 10, 11, 12, 13, 14, 18, 19]',
    '[1, 5, 6, 9, 10, 11, 12, 13, 17, 18, 19]',
    '[1, 5, 6, 9, 10, 11, 12, 16, 17, 18, 19]',
    '[1, 5, 6, 9, 10, 13, 14, 15, 19]',
    '[1, 5, 6, 9, 10, 13, 14, 18, 19]',
    '[1, 5, 6, 9, 10, 13, 17, 18, 19]',
    '[1, 5, 6, 9, 14, 15, 19]',
    '[1, 5, 6, 9, 14, 18, 19]',
    '[1, 5, 10, 11, 12, 13, 14, 15, 19]',
    '[1, 5, 10, 11, 12, 13, 14, 18, 19]',
    '[1, 5, 10, 11, 12, 13, 17, 18, 19]',
    '[1, 5, 10, 11, 12, 16, 17, 18, 19]',
    '[1, 5, 10, 13, 14, 15, 19]',
    '[1, 5, 10, 13, 14, 18, 19]',
    '[1, 5, 10, 13, 17, 18, 19]',
    '[1, 11, 12, 13, 14, 15, 19]',
    '[1, 11, 12, 13, 14, 18, 19]',
    '[1, 11, 12, 13, 17, 18, 19]',
    '[1, 11, 12, 16, 17, 18, 19]']
  assert len(out) == len(correct) and set(out) == set(correct)
