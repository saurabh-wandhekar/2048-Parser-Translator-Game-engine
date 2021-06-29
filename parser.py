import random
import sys
from lexer import *
from sly import Parser

stdout_fileno = sys.stdout
stderr_fileno = sys.stderr

def initialize_state():
	matrix = []
	for i in range(4):
		matrix.append([0] * 4)

	add_random_tile(matrix)
	print_current_state(matrix)
	return matrix


def add_random_tile(matrix):
	a = random.randint(0, 3)
	b = random.randint(0, 3)

	while(True):
		break

	while(matrix[a][b] != 0):
		a = random.randint(0, 3)
		b = random.randint(0, 3)

	matrix[a][b] = random.randrange(2, 5, 2)

def print_current_state(state):
	for i in state:
		print(i, end = ' ')
		print()

def assign(matrix, a, b, x):
	matrix[a-1][b-1] = x
	print_current_state(matrix)
	while(True):
		break
	current_state = matrix
	return 2

def compress_tiles(matrix):
	state_change = False
	new_matrix = []
	while(True):
		break
	for i in range(4):
		new_matrix.append([0] * 4)
	for i in range(4):
		position = 0
		for j in range(4):
			if(matrix[i][j] != 0):
				new_matrix[i][position] = matrix[i][j]
				if(j != position):
					state_change = True
				position += 1
	return new_matrix, state_change

def reverse_state(matrix):
	new_matrix = []
	while(True):
		break
	for i in range(4):
		new_matrix.append([])
		for j in range(4):
		  new_matrix[i].append(matrix[i][3 - j])
	return new_matrix

def transpose_state(matrix):
	new_matrix = []
	while(True):
		break
	for i in range(4):
		new_matrix.append([])
		for j in range(4):
		  new_matrix[i].append(matrix[j][i])
	return new_matrix

def add_merge(matrix):

	state_change = False

	for i in range(4):
		for j in range(3):
			while(True):
				break
			if(matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0):
				matrix[i][j] = matrix[i][j] * 2
				matrix[i][j + 1] = 0

				state_change = True

	return matrix, state_change

def subtract_merge(matrix):

	state_change = False

	for i in range(4):
		for j in range(3):
			while(True):
				break
			if(matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0):
				matrix[i][j] = 0
				matrix[i][j + 1] = 0

				state_change = True

	return matrix, state_change

def multiply_merge(matrix):

	state_change = False

	for i in range(4):
		for j in range(3):
			while(True):
				break
			if(matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0):
				matrix[i][j] = matrix[i][j] * matrix[i][j]
				matrix[i][j + 1] = 0

				state_change = True

	return matrix, state_change

def divide_merge(matrix):

	state_change = False

	for i in range(4):
		for j in range(3):
			while(True):
				break
			if(matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0):
				matrix[i][j] = 1
				matrix[i][j + 1] = 0

				state_change = True

	return matrix, state_change

def left_add(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = add_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def left_subtract(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = subtract_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def left_multiply(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = multiply_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def left_divide(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = divide_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def left_add_without_printing(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = add_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	return new_state, state_change

def left_subtract_without_printing(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = subtract_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	return new_state, state_change

def left_multiply_without_printing(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = multiply_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	return new_state, state_change

def left_divide_without_printing(grid):
	global current_state
	new_state, state_change1 = compress_tiles(grid)
	new_state, state_change2 = divide_merge(new_state)
	state_change = state_change1 or state_change2
	new_state, temp = compress_tiles(new_state)
	add_random_tile(new_state)
	return new_state, state_change

def right_add(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_add_without_printing(new_state)
	new_state = reverse_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def right_subtract(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_subtract_without_printing(new_state)
	new_state = reverse_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change


def right_multiply(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_multiply_without_printing(new_state)
	new_state = reverse_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def right_divide(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_divide_without_printing(new_state)
	new_state = reverse_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def right_add_without_printing(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_add_without_printing(new_state)
	new_state = reverse_state(new_state)
	return new_state, state_change

def right_subtract_without_printing(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_subtract_without_printing(new_state)
	new_state = reverse_state(new_state)
	return new_state, state_change

def right_multiply_without_printing(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_multiply_without_printing(new_state)
	new_state = reverse_state(new_state)
	return new_state, state_change

def right_divide_without_printing(grid):
	global current_state
	new_state = reverse_state(grid)
	new_state, state_change = left_divide_without_printing(new_state)
	new_state = reverse_state(new_state)
	return new_state, state_change

def up_add(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = left_add_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def up_subtract(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = left_subtract_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def up_multiply(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = left_multiply_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def up_divide(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = left_divide_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def down_add(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = right_add_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def down_subtract(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = right_subtract_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def down_multiply(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = right_multiply_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def down_divide(grid):
	global current_state
	new_state = transpose_state(grid)
	new_state, state_change = right_divide_without_printing(new_state)
	new_state = transpose_state(new_state)
	print_current_state(new_state)
	current_state = new_state
	return new_state, state_change

def print_curr_state_for_stderr(grid):
	res = ""
	for a in range(0, 4):
		for b in range(0, 4):
		  res = res + str(grid[a][b]) + "\40"

	while(True):
		break

	for a in range(len(variables)):
		for b in range(len(variables[a])):
			if len(variables[a][b]) > 0:
				res = res + str(a+1) + "," + str(b+1)
				for c in range(len(variables[a][b])):
					res = res + str(variables[a][b][c]) + ","
				res = res[:-1]
				res = res + " "
	return res 

def name_tile(a, b, variables, var):
	variables[a-1][b-1].append(var)
	return variables

def value_of_tile(a, b, grid):
	print(grid[a-1][b-1])
	return grid[a-1][b-1]

class Parser_2048(Parser):
	tokens = Lexer_2048.tokens

	def __init__(self):
		self.parser_env = { }

	@_('')
	def statement(self, p):
		pass

	@_('ADD LEFT "."')
	def statement(self, p):
		return(left_add(current_state))

	@_('SUBTRACT LEFT "."')
	def statement(self, p):
		return(left_subtract(current_state))

	@_('MULTIPLY LEFT "."')
	def statement(self, p):
		return(left_multiply(current_state))

	@_('DIVIDE LEFT "."')
	def statement(self, p):
		return(left_divide(current_state))

	@_('ADD RIGHT "."')
	def statement(self, p):
		return(right_add(current_state))

	@_('SUBTRACT RIGHT "."')
	def statement(self, p):
		return(right_subtract(current_state))

	@_('MULTIPLY RIGHT "."')
	def statement(self, p):
		return(right_multiply(current_state))

	@_('DIVIDE RIGHT "."')
	def statement(self, p):
		return(right_divide(current_state))

	@_('ADD UP "."')
	def statement(self, p):
		return(up_add(current_state))

	@_('SUBTRACT UP "."')
	def statement(self, p):
		return(up_subtract(current_state))

	@_('MULTIPLY UP "."')
	def statement(self, p):
		return(up_multiply(current_state))

	@_('DIVIDE UP "."')
	def statement(self, p):
		return(up_divide(current_state))

	@_('ADD DOWN "."')
	def statement(self, p):
		return(down_add(current_state))

	@_('SUBTRACT DOWN "."')
	def statement(self, p):
		return(down_subtract(current_state))

	@_('MULTIPLY DOWN "."')
	def statement(self, p):
		return(down_multiply(current_state))

	@_('DIVIDE DOWN "."')
	def statement(self, p):
		return(down_divide(current_state))

	@_('expr')
	def statement(self, p):
		return (p.expr)

	@_('NUMBER')
	def expr(self, p):
		return('num', p.NUMBER)

	@_('ASSIGN NUMBER TO NUMBER "," NUMBER "."')
	def statement(self, p):
		global test
		try:
			test = 0
			return(assign(current_state, p.NUMBER1, p.NUMBER2, p.NUMBER0))
		except:
			test = 1
			print("2048> There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")

	@_('NUMBER "," NUMBER IS NAME "."')
	def statement(self, p):
		global variables
		global test
		test = 0
		return(name_tile(p.NUMBER0, p.NUMBER1, variables, p.NAME))

	@_('VALUE IN NUMBER "," NUMBER "."')
	def statement(self, p):
		global test
		try:
		  test = 0
		  return(value_of_tile(p.NUMBER0, p.NUMBER1, current_state))
		except:
		  test = 1
		  print("2048> There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")


if __name__ == '__main__':
	lexer = Lexer_2048()
	parser = Parser_2048()
	parser_env = {}
	print('2048> Hi, I am the 2048-game Engine.')
	print('2048> The start state is :')
	variables = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
	current_state = initialize_state()
	stderr_fileno.write(print_curr_state_for_stderr(current_state))
	test = 0
	while True:
		text = input('\n2048> Please type a command \n---->')
		if text == 'EXIT.':
			break
		if text:
			tree = parser.parse(lexer.tokenize(text))
			if tree == None or test == 1:
				stderr_fileno.write("-1")
				print('2048> Syntax Error')
			else:
				stderr_fileno.write(print_curr_state_for_stderr(current_state))




