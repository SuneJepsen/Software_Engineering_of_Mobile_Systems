    for i,val  in enumerate( tempAllDistance):
        temp_d_1 = val[0]
        if temp_d_1> epsilon:
            if temp_d_1 > temp_d_2:
                temp_d_2 = temp_d_1
                tempAnchorPointIndex = val[1]
                temp_point_2 = val[2]


