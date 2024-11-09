class Maze:
    def __init__(self, maze_map):
        columnsInMaze = 0
        self.mazelist = []
        lines = open(maze_map, 'r')
        rowsInMaze = 0
        for line in lines:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            if columnsInMaze == 0:
                columnsInMaze = len(rowList)
            self.mazelist.append(rowList)
