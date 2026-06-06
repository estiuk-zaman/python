import numpy as np

prices = np.array([100,200,300])
discount=10
discounted_prices = prices-prices*discount/100
print(discounted_prices)