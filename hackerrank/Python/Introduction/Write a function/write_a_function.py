    def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if not year % 100 == 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    return leap