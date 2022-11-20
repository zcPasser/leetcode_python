'''
    leetcode-1184-distance between bus stops
'''
'''
    思路：
        1、
'''


def distanceBetweenBusStops(distance, start, destination):
    n = len(distance)
    # 边界:非环状态
    if n == 1:
        return 0
    if n == 2 and start in (0, 1) and destination in (0, 1):
        return distance[0]
    # 关键：求逆时针 距离
    dest1, dest2 = 0, 0
    # 顺时针 距离
    if start < destination:
        dest1 = sum(distance[start: destination])
        dest2 = sum(distance[0: start] + distance[destination:])
    else:
        dest1 = sum(distance[destination: start])
        dest2 = sum(distance[0: destination] + distance[start:])
    return min(dest1, dest2)