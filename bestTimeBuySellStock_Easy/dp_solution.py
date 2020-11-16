def maxProfit(prices):
    # I guess this is dynamic because it uses a dict?
    if len(prices) in [0, 1]:
        return 0

    min_val_dict = {}
    min_val = prices[0]
    for ii in range(1, len(prices)):
        # creating dict entry, then:
        min_val_dict[ii] = prices[ii] - min_val
        # checking if entry is smaller than min val
        if prices[ii] < min_val:
            min_val = prices[ii]
    max_profit = max(min_val_dict.values())
    return max_profit if max_profit > 0 else 0
