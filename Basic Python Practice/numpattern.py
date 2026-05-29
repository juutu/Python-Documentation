def number_pattern(n):
    # 1. Check if n is an integer first
    if not isinstance(n, int):
        return "Argument must be an integer value."
      #3. If it is an integer > 0
    
    # 2. If it is an integer > 0
    if n <= 0:
        return "Argument must be an integer greater than 0."
        
    # 2. If it is an integer, proceed to build the pattern
    pattern = ""
    for i in range(1, n + 1):
        pattern += str(i) + " "
    return pattern.strip()

    # 3. Use join for efficient string construction
    return " ".join(str(i) for i in range(1, n + 1))