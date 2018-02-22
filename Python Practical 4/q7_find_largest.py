def find_largest(alist):
    if len(alist) == 0:
        return "Empty list!"
    elif len(alist) == 1:
        return alist[0]
    else:
        m = find_largest(alist[1:])
        return m if m > alist[0] else alist[0]
        
        
alist = [5, 1, 8, 100, 2]
print(find_largest(alist))


        
