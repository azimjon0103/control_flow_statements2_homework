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
        if x2<x3:
            if x3<x4:
                if x4<x5:
                    return x5
                else :
                    return x4
            else :
                return x3
        else :
            return x2
    else :
        return x1                            
print(main(23456))