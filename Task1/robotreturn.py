class Solution:
    def judgeCircle(self, moves: str) -> bool:
     horizontal_movement = 0
     vertical_movement = 0

     for move in moves:
        if move == 'R':
            horizontal_movement += 1
        elif move == 'L':
            horizontal_movement -= 1
        elif move == 'U':
            vertical_movement += 1
        elif move == 'D':
            vertical_movement -= 1

     return horizontal_movement == 0 and vertical_movement == 0
