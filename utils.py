def print_error(msg, type='error', _exit=True):
	print('n-puzzle: {type}: {msg}'.format(type=type, msg=msg))

	if _exit:
		exit(1)

def get_end_matrix(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += dx[i % 4]
            y += dy[i % 4]
            m[x][y] = c
            c += 1
    m[x][y] = 0
    return m

def get_position(state, elem):
	for row in range(len(state)):
		if elem in state[row]:
			return (row, state[row].index(elem))

def findXPosition(puzzle):
	for i in range(len(puzzle) - 1, -1, -1):
		for j in range(len(puzzle) - 1, -1, -1):
			if puzzle[i][j] == 0:
				return len(puzzle) - i