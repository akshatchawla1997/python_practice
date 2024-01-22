"""You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?"""

packets = 9
packetpercost = 1.49

shopkeeper = 20

def shopkeeper_return(packets, packetpercost, shopkeeper):
    return shopkeeper-(packets*packetpercost)

returnAmount = shopkeeper_return(packets, packetpercost, shopkeeper)
print(returnAmount)