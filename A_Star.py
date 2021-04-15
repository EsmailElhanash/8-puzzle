import functions as f
import heapq as h

goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# enter initial board configuration , separated by comma. ex: 1,2,5,3,4,0,6,7,8
# board = list(map(int, input('initial board configuration:').split(',')))
board2d = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
# board2d = [board[0:3], board[3:6], board[6:]]
# print(goal)
# print(board2d)
f.frontier.append((f.manhattan_heuristic(board2d) + 0, board2d))
print()
# f.board_print(board2d)

print()
print()
print('***a_star_manhattan:')
f.a_star_manhattan()
f.frontier.clear()
f.frontier.append((f.manhattan_heuristic(board2d) + 0, board2d))
print()
print()
print('***a_star_euclidean:')
f.a_star_euclidean()
