def triangle_area(base,height,shape="rectangle"):
    if shape == "rectangle":
        return base*height
    else:
        
        return base*height*(1/2)

print(triangle_area(19,10,"rectangle"))