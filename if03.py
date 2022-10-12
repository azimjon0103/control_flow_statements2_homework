def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    
    mx=a
    if mx<b:
        mx=b
    if mx<c:
        mx=c
    min=c
    if min>b:
        min=b
    if min>a:
        min=a           
    return  a+b+c-min-mx
print(main(1,4,2))    