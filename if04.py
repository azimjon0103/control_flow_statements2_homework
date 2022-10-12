def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a==b:
        c=0
    if a>b :
        c=a
    else:
        c=b
    return    c
print(main(2,8))     