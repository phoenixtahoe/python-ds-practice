def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    c1 = {}
    c2 = {}
    for n1 in str(num1):
            c1[n1] = c1.get(n1, 0) + 1
    for n2 in str(num2):
            c2[n2] = c2.get(n2, 0) + 1
    return c1 == c2