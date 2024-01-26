"""
stocks.csv contains stock price, earnings per share and book value. You are writing a stock market application that will process this file and create a new file with financial metrics such as pe ratio and price to book ratio. These are calculated as,
pe ratio = price / earnings per share
price to book ratio = price / book value

Your input format (stocks.csv) is,

Company Name	Price	Earnings Per Share	Book Value
Reliance	1467	66	653
Tata Steel	391	89	572
Output.csv should look like this,

Company Name	PE Ratio	PB Ratio
Reliance	22.23	2.25
Tata Steel	4.39	0.68
"""

with open('stocks.csv', 'r') as stocks_price, open("csv_output.csv", "w") as output_csv:
    output_csv.write("Company name, PE ratio, PB ratio\n")
    next(stocks_price)
    for stock_price in stocks_price:
        tokens = stock_price.split(',')
        stock =  tokens[0]
        price = float(tokens[1])
        eps = float(tokens[2])
        book = float(tokens[3])
        pe = round(price / eps, 2)
        pb = round(price / book, 2)
        output_csv.write(f"{stock},{pe},{pb}\n")
        print(stock_price)
