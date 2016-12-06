def get_max_profit(stock_prices_yesterday):

	min_price = stock_prices_yesterday[0]
	max_profit = 0

	for current_price in stock_prices_yesterday:

		potential_profit = current_price - min_price
		max_profit = max(max_profit, potential_profit)
		min_price = min(min_price, current_price)

	return max_profit