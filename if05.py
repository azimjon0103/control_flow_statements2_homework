def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1=n%10
    n//=10
    x2=n%10
    n//=10
    x3=n%10
    n//=10
    x4=n%10
    n//=10
    x5=n%10
    if x1<x2:
        c= x2
    else :
        c= x1
    if x1<x3:
        c= x3
    else :
        c= x1
    if x1<x4:
        c= x4
    else :
        c= x1    
    if x1<x5:
        c= x5
    else :
        c= x1
    if x2<x3:
        c= x3 
    else :
        c= x2
    if x2<x4:
        c= x4
    else :
        c= x2
    if x2<x5:
        c= x5
    else :
        c= x2
    if x3<x4:
        c= x4
    else :
        c= x3
    if x4<x5:
        c= x5 
    else :
        c= x4
    return c                                                                 
print(main(98527))