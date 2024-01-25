"""You are given following list of stocks and their prices in last 3 days,

Stock	Prices
info	[600,630,620]
ril	[1430,1490,1567]
mtl	[234,180,160]
Write a program that asks user for operation. Value of operations could be,
print: When user enters print it should print following,
info ==> [600, 630, 620] ==> avg:  616.67
ril ==> [1430, 1490, 1567] ==> avg:  1495.67
mtl ==> [234, 180, 160] ==> avg:  191.33
add: When user enters 'add', it asks for stock ticker and price. If stock already exist 
in your list (like info, ril etc) then it will append the price to the list. Otherwise it
will create new entry in your dictionary. For example entering 'tata' and 560 will add 
tata ==> [560] to the dictionary of stocks."""

import statistics
stocks = {
    "info": [600,630,620],
    "ril": [1430,1490,1567],
    "mtl": [234,180,160]

}

def avg(price):
    return statistics.mean(map(float,price))

def main():
    choice = input("enter your choice as print to print all the stocks and add to add a new stock and no for do nothing")
    while choice != 'no':
        if choice.lower() == 'print':
            for key, value in stocks.items():
                print(f"{key} ==> {value} ==> average: {avg(value)}")
        elif choice.lower() == 'add':
            key = input("enter a stock name")
            value = input(f"enter a stock price of {key}")
            if key in stocks:
                stocks[key].append(value)
            else:
                stocks[key] = [value] 
        choice = input("enter your choice as print to print all the stocks and add to add a new stock and no for do nothing")
    
if __name__ == '__main__':
    main()
