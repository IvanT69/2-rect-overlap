#Find whether the 2 rectangles overlap
def rectangles_overlap(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2    

    if x1 >= x4 or x3 >= x2:
        return False    

    if y1 >= y4 or y3 >= y2:
        return False
    
    return True

# Example usage
rect1 = (1, 1, 4, 4) 
rect2 = (5, 5, 8, 8)  

if rectangles_overlap(rect1, rect2):
    print("The rectangles overlap.")
else:
    print("The rectangles do not overlap.")
