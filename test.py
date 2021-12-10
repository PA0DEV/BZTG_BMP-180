def smoothMesure(cnt, val):
    """
    Calculate the dew point.
    

    :param cnt: the number of iterations to be used
    :param val: the mesured value
    :return: returns the smoothed value of the mesurement
    """
    values = []
    for i in range(cnt):
        values[i] = val

    #cut the highest and lowest value
    values.sort()
    values.remove(values[0])
    values.remove(values[cnt])

    #get the average value
    valLen = len(values)
    valSum = sum(values)
    ret = valSum / valLen

    return ret

smoothMesure(10, input)