This code first defines the rectangles by its bottom-left and top-right corners:  
Rect A: (x1, y1) to (x2, y2)  
Rect B: (x3, y3) to (x4, y4)  
  
Then, checks whether the rectangle overlaps or not.  
if x1 >= x4 or x3 >= x2:  
        return False    
if y1 >= y4 or y3 >= y2:  
        return False  
    return True
      
Two rectangles will not overlap if one is completely to the left, right, below or top.  
If the rectangles overlap, it sends out a message saying that they overlap, if not it will say they do not overlap.  
rect1 = (1, 1, 4, 4)  
rect2 = (5, 5, 8, 8)  

if rectangles_overlap(rect1, rect2):  
    print("The rectangles overlap.")  
else:  
    print("The rectangles do not overlap.")  
