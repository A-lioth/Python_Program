
# * 练习使用
# * f"{}"
# * %
name = "nmu"
stockPrice = 19.99
stockCode = "000001"
stockPriceDailyGrowthFactor = 1.2
growthDays = 7

print(f"单位: {name}, 股票代码: {stockCode}, 当前股价: {stockPrice}元")
print("股票每日增长率: %.2f%%, 经过%d天后, 股价将涨至: %.2f元" % (stockPriceDailyGrowthFactor,
      growthDays, stockPrice * stockPriceDailyGrowthFactor ** growthDays))
