from copy import deepcopy
from heuristics import HEURISTICS
import heapq
from utils import (get_position)
from time import time

DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


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

def get_ans_dict(open_set_size, closed_set_size, states):
    return {
        'complexity_in_time': open_set_size,
        'complexity_in_size': closed_set_size,
        'states': states
    }

def get_neigbors(state):
    neighbors = []
    empty_x, empty_y = get_position(state, 0)
    size = len(state)

    for (dx, dy) in DIRECTIONS.values():
        x, y = empty_x + dx, empty_y + dy

        if 0 <= x < size and 0 <= y < size:
            new_state = deepcopy(state)
            new_state[empty_x][empty_y] = state[x][y]
            new_state[x][y] = 0

            neighbors.append(new_state)

    return neighbors

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[repr(current)]
        path.append(current)
    path.append(start) # optional
    path.reverse() # optional
    return path

def a_star_search(start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[repr(start)] = None
    cost_so_far[repr(start)] = 0

    closed_set_size = 0
    open_set_size = 0

    start_time = time()
    while not frontier.empty():
        current = frontier.get()
        current_repr = repr(current)

        closed_set_size += 1

        if current == goal:
            break

        for next in get_neigbors(current):
            if time() - start_time > 10 ** len(start):
                print('It is unsolvable dude')
                exit()
            next_repr = repr(next)
            new_cost = cost_so_far[current_repr] + 1
            if next_repr not in cost_so_far or new_cost < cost_so_far[next_repr]:
                cost_so_far[next_repr] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next_repr] = current

                open_set_size += 1

    return get_ans_dict(open_set_size, closed_set_size, reconstruct_path(came_from, start, goal))
    

def solve(pattern, heuristic):
    ans = a_star_search(pattern, get_end_matrix(len(pattern)), HEURISTICS[heuristic])
    return ans