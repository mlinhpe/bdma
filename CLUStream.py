import math
import numpy as np

# initPoints = 6
# q = 3
# factor of clu radius
t = 5
# n: number of points in the cluster

time_of_point = {(1, 1): 1,
                 (2, 1): 2,
                 (4, 9): 3,
                 (4, 8): 4,
                 (10, 4): 5,
                 (9, 3): 6,
                 (2, 3): 7,
                 (11, 3): 8,
                 (12, 12): 9,
                 (12, 11): 10,
                 (11, 12): 11,
                 (4, 2): 12}

# points that are not initial
test_points = [(2, 3), (11, 3), (12, 12), (12, 11), (11, 12), (4, 2)]

# draw all initial points and then cluster them
# clusters = [[]]
clusters = [
    [(1, 1), (2, 1)],
    [(4, 9), (4, 8)],
    [(10, 4), (9, 3)]
]

# for each cluster compute: CFT = (CF2x, CF1x, CF2t, CF1t, n)
# CF2x: sum of the squares of each dimension of the data values
# CF1x: sum of the values of each dimension
# CF2t: sum of the squares of the timestamps
# CF1t: sum of the timestamps


def get_radius(cf2x, cf1x, nval):
    minuend = [point/nval for point in cf2x]
    subtrahend = [(point/nval) ** 2 for point in cf1x]
    difference = (minuend[0] - subtrahend[0], minuend[1] - subtrahend[1])
    sqrt_result = [math.sqrt(elem) for elem in difference]
    return math.sqrt(sum([elem ** 2 for elem in sqrt_result]))


# used to name the clusters
i = 0
clu_stream = []

for cluster in clusters:
    i += 1
    CF2x = (sum([point[0] ** 2 for point in cluster]), sum([point[1] ** 2 for point in cluster]))
    CF1x = (sum([point[0] for point in cluster]), sum([point[1] for point in cluster]))
    CF2t = sum([time_of_point[point] ** 2 for point in cluster])
    CF1t = sum([time_of_point[point] for point in cluster])
    n = len(cluster)
    center = (CF1x[0]/n, CF1x[1]/n)
    radius = get_radius(CF2x, CF1x, n)
    print("CFT" + str(i) + " = ( " + str(CF2x) + ", " + str(CF1x) + ", "
          + str(CF2t) + ", " + str(CF1t) + ", " + str(n) + " )"
          + "  center = " + str(center) + "  radius = " + str(radius))
    clu_stream.append([CF2x, CF1x, CF2t, CF1t, n, center, radius])


for point in test_points:
    count = 0
    min_dist = float('inf')
    cluster_name = 0
    cluster_radius = 0
    cluster_center = 0
    for cluster in clu_stream:
        count += 1
        center = cluster[5]
        dist = math.dist(point, center)
        if dist < min_dist:
            min_dist = dist
            cluster_name = count
            cluster_radius = cluster[6]
            cluster_center = cluster[5]

    boundary = (t * cluster_radius) ** 2
    dist_p = (point[0] - cluster_center[0]) ** 2 + (point[1] - cluster_center[1]) ** 2
    print("closest cluster for point " + str(point)
          + " is: " + "CFT" + str(cluster_name) + " with dist = " + str(min_dist))
    if dist_p <= boundary:
        print("point " + str(point) + " is within the boundary of cluster " + "CFT" + str(cluster_name))
    else:
        print("point " + str(point) + " is NOT within the boundary of cluster " + "CFT" + str(cluster_name))




