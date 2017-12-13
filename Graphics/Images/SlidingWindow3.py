def slidingWindow(point, epsilon):
    global anchorPointIndex,count
    sliding_Window.append(point)

    if len(sliding_Window)<3:
        return

    sizeOfSlidingWindow = len(sliding_Window)

    point_1 =  sliding_Window[anchorPointIndex]
    point_2 =  sliding_Window[sizeOfSlidingWindow - 1]
    point_3 =  point

    tempAllDistance = []
    d = calculateThresholdToLine(point_1,point_2,point_3)
    tempAllDistance.append(d)
    tempNewEndPoint = sizeOfSlidingWindow-2

    diff= abs(anchorPointIndex-tempNewEndPoint)
    if diff>=2:
        for i,val  in enumerate(sliding_Window[anchorPointIndex+1:tempNewEndPoint]):
            temp_point_2 = val
            if point_1[0] != temp_point_2[0]:
                d = calculateThresholdToLine(point_1, temp_point_2, point_3)
                tempAllDistance.append(d)

    for i,val in enumerate(tempAllDistance):
        temp_d = val
        if temp_d > epsilon:
            approximateTrajectory.append(point_2)
            anchorPointIndex = sizeOfSlidingWindow - 2
    count = count +1





