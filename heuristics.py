"""Defines some heuristics for A* algorithm"""

from utils import get_position

def manhatan(state, goal):
    cost = 0
    for row in range(len(state)):
        for col in range(len(state[0])):
            pos = get_position(goal, state[row][col])
            cost += abs(row - pos[0]) + abs(col - pos[1])
    return cost

def misplaced(state, goal):
    cost = 0
    for row1, row2 in zip(state, goal):
        for cell1, cell2 in zip(row1, row2):
            if cell1 != cell2:
                cost += 1
    return manhatan(state, goal) + cost

def linear_conflict(state, goal):
    cost = 0
    for state_line, goal_line in zip(state, goal):
        cells = [ (v, i, state_line.index(v)) for i, v in enumerate(goal_line) if v in state_line ]
        for i, (v, ind_stat1, ind_goal1) in enumerate(cells):
            for j, (v1, ind_stat2, ind_goal2) in enumerate(cells[i + 1:]):
                if ind_stat1 >= ind_goal2 and ind_goal1 <= ind_stat2:
                    cost += 1

    for state_line, goal_line in zip([[line[i] for line in state] for i in range(len(state))], [[line[i] for line in goal] for i in range(len(goal))]):
        cells = [ (v, i, state_line.index(v)) for i, v in enumerate(goal_line) if v in state_line ]
        for i, (v, ind_stat1, ind_goal1) in enumerate(cells):
            for j, (v1, ind_stat2, ind_goal2) in enumerate(cells[i + 1:]):
                if ind_stat1 >= ind_goal2 and ind_goal1 <= ind_stat2:
                    cost += 1

    return manhatan(state, goal) + 2 * cost

def out_of(state, goal):
    cost = 0
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            x, y = get_position(goal, state[i][j])
            if x != j:
                cost += 1
            if y != i:
                cost += 1
    return cost

def mixed(state, goal):
    return (linear_conflict(state, goal) + misplaced(state, goal) + out_of(state, goal) + manhatan(state, goal))

HEURISTICS = {
    'manhatan' : manhatan,
    'misplaced' : misplaced,
    'linear-conflict' : linear_conflict,
    'out-of' : out_of,
    'mixed' : mixed
}