import algebra
import graderUtil
import main

grader = graderUtil.Grader()

########################### Basic Test Cases for Problem 1 ########################
def test_1a_0_basic():
    grader.requireIsEqual(27, main.cube(3))
    grader.requireIsEqual(-64, main.cube(-4))

def test_1b_0_basic():
    grader.requireIsEqual(120, main.factorial(5))
    grader.requireIsEqual(1, main.factorial(0))

def test_1c_0_basic():
    grader.requireIsEqual("word", main.findAlphabeticallyLastWord("What is the last word in this sentence?"))
    grader.requireIsEqual("zebra", main.findAlphabeticallyLastWord("apple zebra dog"))

def test_1d_0_basic():
    grader.requireIsEqual(2, main.count_pattern(('a', 'b'), ('a', 'b', 'c', 'e', 'b', 'a', 'b', 'f')))
    grader.requireIsEqual(3, main.count_pattern(('a', 'b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a')))

# Add tests to the grader
grader.addBasicPart('1a-0-basic', test_1a_0_basic)
grader.addBasicPart('1b-0-basic', test_1b_0_basic)
grader.addBasicPart('1c-0-basic', test_1c_0_basic)
grader.addBasicPart('1d-0-basic', test_1d_0_basic)


############################# Basic Test Cases for Problem 2 #######################
def test_2a_0_basic():
    grader.requireIsEqual(0, main.depth('x'))
    grader.requireIsEqual(1, main.depth(('expt', 'x', 2)))
    grader.requireIsEqual(2, main.depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))
    grader.requireIsEqual(4, main.depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))

grader.addBasicPart('2a-0-basic', test_2a_0_basic)

############################# Basic Test Cases for Problem 3 #######################
def test_3a_0_basic():
    tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
    grader.requireIsEqual(9, main.tree_ref(tree, (3, 1)))
    grader.requireIsEqual(6, main.tree_ref(tree, (1, 1, 1)))
    grader.requireIsEqual(((1, 2), 3), main.tree_ref(tree, (0,)))
    grader.requireIsEqual(7, main.tree_ref(tree, (2,)))

# Add basic test cases to the grader
grader.addBasicPart('3a-0-basic', test_3a_0_basic)

############################# Basic Test Cases for Problem 4 #######################

def test_4a_0_basic():
    x = 'x'
    y = 'y'

    expr1 = algebra.Product([2, x])
    expr2 = algebra.Sum([y, 3])
    expected_result = algebra.Sum([
        algebra.Product([2, x, y]),
        algebra.Product([2, x, 3])
    ])
    result = algebra.multiply(expr1, expr2)
    grader.requireIsEqual(expected_result, result)

# Adding the test case to the grader
grader.addBasicPart('4a-0-basic', test_4a_0_basic)


############################# Hidden Test Cases for Problem 1 ######################
def test_1a_0_hidden():
    grader.requireIsEqual(1000, main.cube(10))
    grader.requireIsEqual(0, main.cube(0))

def test_1b_0_hidden():
    grader.requireIsEqual(3628800, main.factorial(10))

def test_1c_0_hidden():
    grader.requireIsEqual("zoo", main.findAlphabeticallyLastWord("elephant apple Zebra zoo"))
    grader.requireIsEqual("under", main.findAlphabeticallyLastWord("The quick brown fox jumps over the lazy dog under the shining sun."))
    grader.requireIsEqual("zzz", main.findAlphabeticallyLastWord("apple banana carrot ZZZ zzz"))

def test_1d_0_hidden():
    grader.requireIsEqual(4, main.count_pattern(('a',), ('a', 'a', 'a', 'a')))
    grader.requireIsEqual(3, main.count_pattern(('a', 'b'), ('a', 'b', 'a', 'b', 'a', 'b')))
    grader.requireIsEqual(3, main.count_pattern(('b', 'a', 'b'), ('a', 'b', 'a', 'b', 'a', 'b', 'a', 'b')))
    grader.requireIsEqual(0, main.count_pattern(('a', 'b'), ('c', 'd', 'e', 'f')))


# Add hidden tests to the grader
grader.addHiddenPart('1a-0-hidden', test_1a_0_hidden)
grader.addHiddenPart('1b-0-hidden', test_1b_0_hidden)
grader.addHiddenPart('1c-0-hidden', test_1c_0_hidden)
grader.addHiddenPart('1d-0-hidden', test_1d_0_hidden)

############################# Hidden Test Cases for Problem 2 ######################
def test_2a_0_hidden():
    grader.requireIsEqual(4, main.depth(('+', ('/', ('-', ('expt', 'a', 2), ('b',)), ('+', 1, 2)), ('c', 'd'))))
    grader.requireIsEqual(6, main.depth(('a', ('b', ('c', ('d', ('e', ('f',))))))))

grader.addHiddenPart('2a-0-hidden', test_2a_0_hidden)
############################# Hidden Test Cases for Problem 3 ######################
def test_3a_0_hidden():
    tree = (((1, (2, 3)), 4), (5, 6), (7, 8, (9, (10, 11))))
    grader.requireIsEqual(11, main.tree_ref(tree, (2, 2, 1, 1)))
    grader.requireIsEqual(5, main.tree_ref(tree, (1, 0)))
    grader.requireIsEqual(((1, (2, 3)), 4), main.tree_ref(tree, (0,)))
    grader.requireIsEqual(9, main.tree_ref(tree, (2, 2, 0)))

# Add hidden test cases to the grader
grader.addHiddenPart('3a-0-hidden', test_3a_0_hidden)

############################# Hidden Test Cases for Problem 4 ######################

def test_4a_0_hidden():
    x = 'x'
    y = 'y'
    expr1 = algebra.Sum([algebra.Product([1, x]), algebra.Product([2, y])])
    expr2 = algebra.Product([3])
    expected_result = algebra.Sum([
        algebra.Product([1, x, 3]),
        algebra.Product([2, y, 3])
    ])
    grader.requireIsEqual(expected_result, algebra.do_multiply(expr1, expr2))
    
    expr1 = algebra.Product([2, x])
    expr2 = algebra.Product([3, y])
    expected_result = algebra.Product([2, x, 3, y])
    grader.requireIsEqual(expected_result, algebra.do_multiply(expr1, expr2))




# Add hidden test cases to the grader
grader.addHiddenPart('4a-0-hidden', test_4a_0_hidden)

# Run the grader
grader.grade()
