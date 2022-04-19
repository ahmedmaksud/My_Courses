def read_maze(filename):
    try:
        with open(filename) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            temp = len(maze[0])
            for row in maze:
                if len(row) != temp:
                    print("the maze is not rectengular")
                    raise SystemExit
            for row in maze:
                print(row)
            return maze
    except OSError:
        print("There is a problem reading the file")
        raise SystemExit


offsets = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1)
}


def is_legal_pos(maze, pos):
    len_col = len(maze)
    len_row = len(maze[0])
    return 0 <= pos[1] < len_row and 0 <= pos[0] < len_col and maze[pos[0]][pos[1]] != '*'


def get_path(predecessors, start, goal):
    my_path = []
    current = goal
    while current != start:
        my_path.append(current)
        current = predecessors[current]
    my_path.append(start)
    my_path.reverse()
    return my_path

def get_dist(goal,start):
    return abs(goal[0]-start[0])+abs(goal[1]-start[1])


