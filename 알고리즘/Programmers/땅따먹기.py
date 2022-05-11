from collections import deque

# def solution(land):
#     height, width = len(land), len(land[0])
#     dist = [[0 for _ in range(width)] for _ in range(height)]
#     que = deque([[0,i] for i in range(width)])
#     dist[0] = land[0]
#     for h in range(0, height-1):
#         for w in range(width):
#             next_points = [[h+1, j] for j in range(width)]
#             next_points.remove([h+1, w])
#             for point in next_points:
#                 if dist[h][w] + land[point[0]][point[1]] > dist[point[0]][point[1]]:
#                     dist[point[0]][point[1]] = dist[h][w] + land[point[0]][point[1]]
#     return max(dist[-1])

def solution(land):
    height = len(land)
    for h in range(1, height):
        land[h][0] += max(land[h-1][1], land[h-1][2], land[h-1][3])
        land[h][1] += max(land[h-1][0], land[h-1][2], land[h-1][3])
        land[h][2] += max(land[h-1][0], land[h-1][1], land[h-1][3])
        land[h][3] += max(land[h-1][0], land[h-1][1], land[h-1][2])
        
    return max(land[-1])
