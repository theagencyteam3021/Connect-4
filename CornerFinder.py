def corner_finder(detection_list):
    least_distance=10
    answer=None

    for d in detection_list:
        distance=(d.x**2+d.y**2)**0.5
        if distance<least_distance:
            least_distance=distance
    return least_distance