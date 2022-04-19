import MyStack as ST
if __name__ == "__main__":

    string = "!!edoc taerg si sihT"

    reversed_string = ""

    s = ST.MyStack()

    for char in string:
        s.push(char)

    while not s.is_empty():
        reversed_string += s.pop()

    print(string)
    print(reversed_string)
# %%
import dfs_helper as HF
if __name__ == "__main__":
    maze = HF.read_maze("mazes\mini_maze_dfs.txt")
    for row in maze:
        print(row)
# %%
if __name__ == "__main__":
    import dfs_helper as HF
    import my_dfs as DFS

    start = (0, 0)
    goal = (2, 2)

    maze = HF.read_maze("mazes\mini_maze_bfs.txt")
    path = DFS.my_dfs(maze, start, goal)
    print(path)

    path = DFS.my_bfs(maze, start, goal)
    print(path)
    
    path = DFS.my_astar(maze, start, goal)
    print(path)

