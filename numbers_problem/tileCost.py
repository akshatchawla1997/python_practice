"""You want to replace tiles in your bathroom which is exactly square and 5.5 feet is 
its length. If tiles cost 500 rs per square feet, how much will be the total cost to 
replace all tiles. Calculate and print the cost using python (Hint: Use power operator 
** to find area of a square)"""


len = 5.5
area = len ** 2
cost = area * 500
print(f"total cost of bathroom tile replacement is {cost}")