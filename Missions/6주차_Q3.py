stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]


def stock_profit(stocks, sells):
    portfolio = dict()
    stocks = stocks.split(',')
    for stock in stocks:
        stock_name = stock.split('/')[0]
        stock_count = int(stock.split('/')[1])
        avg_purchase_price = int(stock.split('/')[2])
        sell_price = sells[stocks.index(stock)]
        profit = (stock_count * sell_price) - \
            (stock_count * avg_purchase_price)

        portfolio[stock_name] = (
            profit / (stock_count * avg_purchase_price)) * 100

    portfolio_inorder = sorted(portfolio.items(), key=lambda x: -x[1])

    for name, ror in portfolio_inorder:
        print(f'{name}의 수익률 {ror:.3}')


stock_profit(stocks, sells)
