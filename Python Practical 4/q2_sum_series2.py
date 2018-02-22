def sum_series2(i):
    if i == 1:
        return i / (2*i + 1)
    else:
        return i / (2*i + 1) + sum_series2(i-1)
