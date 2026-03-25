def snail(snail_map):
    finalList = []
    topLimit = 0
    rigthLimit = len(snail_map[0])-1
    bottomLimit = len(snail_map) -1
    leftLimit = 0

    while topLimit <= bottomLimit and leftLimit <= rigthLimit:
        for i in range(leftLimit , rigthLimit +1):
            finalList.append(snail_map[topLimit][i])
        topLimit = topLimit +1 

        for i in range(topLimit, bottomLimit +1 ):
            finalList.append(snail_map[i][rigthLimit])
        rigthLimit = rigthLimit -1

        if topLimit <= bottomLimit:
            for i in range(rigthLimit, leftLimit -1, -1):
                finalList.append(snail_map[bottomLimit][i])
            bottomLimit = bottomLimit -1
    
        if leftLimit <= rigthLimit:
            for i in range(bottomLimit, topLimit-1, -1):
                finalList.append(snail_map[i][leftLimit])
            leftLimit = leftLimit +1
    return finalList
