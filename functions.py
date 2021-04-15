import copy as c
import heapq as h
from math import sqrt

frontier = []
goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

explored = []


def get_indices(list2d, item):
    for i in range(3):
        for j in range(3):
            if list2d[i][j] == item:
                return i, j


def goal_indices(item):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == item:
                return i, j


def swap(list2d, i1, i2):
    s_list = c.deepcopy(list2d)
    s_list[i1[0]][i1[1]] = list2d[i2[0]][i2[1]]
    s_list[i2[0]][i2[1]] = list2d[i1[0]][i1[1]]
    return s_list


def can_swap_x(zero_index_x):
    c_swaps = []
    cx1 = zero_index_x + 1
    cx2 = zero_index_x - 1
    if cx1 > 2:
        c_swaps.append(cx2)
        return c_swaps
    if cx2 < 0:
        c_swaps.append(cx1)
        return c_swaps

    c_swaps.append(cx1)
    c_swaps.append(cx2)
    return c_swaps


def can_swap_y(zero_index_y):
    c_swaps = []
    cy1 = zero_index_y + 1
    cy2 = zero_index_y - 1
    if cy1 > 2:
        c_swaps.append(cy2)
        return c_swaps
    if cy2 < 0:
        c_swaps.append(cy1)
        return c_swaps

    c_swaps.append(cy1)
    c_swaps.append(cy2)
    return c_swaps


def can_swap(zero_index):
    cswapx = can_swap_x(zero_index[0])
    cswapy = can_swap_y(zero_index[1])
    cs = []
    for i in cswapx:
        cs.append((zero_index, (i, zero_index[1])))
    for j in cswapy:
        cs.append(((zero_index[0], j), zero_index))

    return cs


def cell_manhattan(n, p):
    g = goal_indices(n)
    return abs(p[0] - g[0]) + abs(p[1] - g[1])


def manhattan_heuristic(board_node):
    mh = 0
    for i in range(3):
        for j in range(3):
            mh = mh + cell_manhattan(board_node[i][j], (i, j))
    return mh


def cell_euclidean(n, p):
    g = goal_indices(n)
    return sqrt((p[0] - g[0]) ** 2 + (p[1] - g[1]) ** 2)


def euclidean_heuristic(board_node):
    eh = 0
    for i in range(3):
        for j in range(3):
            eh = eh + cell_euclidean(board_node[i][j], (i, j))
    return eh


def board_print(board):
    for i in range(3):
        print(board[i])


def a_star_manhattan():
    g_n = 0
    cost = 0
    while frontier:
        frontier_boards = []
        print('$$$$$$$$$$$$$$ frontier now $$$$$$$$$$$$$$$$$$$$:')
        i = 0
        for b in frontier:
            i += 1
            print('##### board number ' + str(i))
            board_print(b[1])
            frontier_boards.append(b[1])

        h.heapify(frontier)
        state = h.heappop(frontier)
        cost += 1
        print()
        print('We choose :')
        board_print(state[1])
        print('f(n)=' + str(state[0]))
        explored.append(state[1])

        if goal == state[1]:
            print('Goal was found!')
            print('cost=' + str(cost))
            return True

        zero_index = get_indices(state[1], 0)
        cs = can_swap(zero_index)

        for i in cs:
            ch = swap(state[1], i[0], i[1])
            if ch not in explored or frontier_boards:
                frontier.append((manhattan_heuristic(ch) + g_n, ch))

        # print()
        # print("#####Frontier Now, " + str(g_n))
        #
        # for ch in frontier:
        #     print()
        #     board_print(ch[1])
        #     print('f(n)=' + str(ch[0]))
        g_n += 1

    print('Goal was not found!')
    return False


def a_star_euclidean():
    g_n = 0
    cost = 0

    while frontier:
        frontier_boards = []

        print('$$$$$$$$$$$$$$ frontier now $$$$$$$$$$$$$$$$$$$$:')
        i = 0
        for b in frontier:
            i += 1
            print('##### board number ' + str(i))
            board_print(b[1])
            frontier_boards.append(b[1])

        h.heapify(frontier)
        state = h.heappop(frontier)
        cost += 1
        print()
        print('We choose :')
        board_print(state[1])
        print('f(n)=' + str(state[0]))
        explored.append(state[1])

        if goal == state[1]:
            print('Goal was found!')
            print('cost=' + str(cost))
            return True

        zero_index = get_indices(state[1], 0)
        cs = can_swap(zero_index)

        for i in cs:
            ch = swap(state[1], i[0], i[1])
            if ch not in explored or frontier_boards:
                frontier.append((euclidean_heuristic(ch) + g_n, ch))

        # print()
        # print("#####Frontier Now, " + str(g_n))

        # for ch in frontier:
        #     print()
        #     board_print(ch[1])
        #     print('f(n)=' + str(ch[0]))
        g_n += 1

    print('Goal was not found!')
    return False
