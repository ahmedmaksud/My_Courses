import MyStack as ST
import dfs_helper as HF
import MyQueue as QU
import MyPriorityQueue as PQ


def my_dfs(maze, start, goal):
    s = ST.MyStack()
    pred = {start: None}
    s.push(start)
    while not s.is_empty():
        current_cell = s.pop()
        if current_cell == goal:
            return HF.get_path(pred, start, goal)
        for direction in ["up", "right", "down", "left"]:
            dir_step = HF.offsets[direction]
            neigh = (current_cell[0]+dir_step[0], current_cell[1]+dir_step[1])
            if HF.is_legal_pos(maze, neigh) and neigh not in pred:
                s.push(neigh)
                pred[neigh] = current_cell
    return None


def my_bfs(maze, start, goal):
    q = QU.MyQueue()
    q.enqueue(start)
    pred = {start: None}
    while not q.is_empty():
        current_cell = q.dequeue()
        if current_cell == goal:
            return HF.get_path(pred, start, goal)
        for direction in ["up", "right", "down", "left"]:
            dir_step = HF.offsets[direction]
            neigh = (current_cell[0]+dir_step[0], current_cell[1]+dir_step[1])
            if HF.is_legal_pos(maze, neigh) and neigh not in pred:
                q.enqueue(neigh)
                pred[neigh] = current_cell
    return None
# GHF


def my_astar(maze, start, goal):
    pq = PQ.MyPriorityQueue()
    pq.put(start, 0)
    pred = {start: None}
    Gval = {start: 0}
    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return HF.get_path(pred, start, goal)
        for direction in ["up", "right", "down", "left"]:
            dir_step = HF.offsets[direction]
            neigh = (current_cell[0]+dir_step[0], current_cell[1]+dir_step[1])
            if HF.is_legal_pos(maze, neigh) and neigh not in pred:
                temp=Gval[current_cell]+1
                pred[neigh] = current_cell
                Gval[neigh] = temp
                pq.put(neigh,temp+HF.get_dist(goal,neigh))
    return None
