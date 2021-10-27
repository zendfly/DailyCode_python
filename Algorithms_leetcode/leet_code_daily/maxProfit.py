"""
股票的最佳买卖时期
    给定一个数组i，记录该股票每天的价格。
    例如，i = [1,2,3,4,5],i[0]为第一天的股票价格
    买卖股票的最佳时期为 第1天买入，第5天卖出 5 - 1 = 4 为最大利润
    最大利润 max{前一天的最大利润，当前价格 - 以前最低价格}
"""
# class solution:
#     def __init__(self,list):
#         self.list = list
#
#     def maxProfit(self):
#         max = 0
#         min_index = self.list[0]
#         max_daiy = [0,0]
#         for i in range(len(self.list)):
#             for j in range(i):
#                 # max = self.list[i] - self.list[j] if max <= self.list[i] - self.list[j]
#                 if self.list[i] < self.list[j]: #
#                     if max <= self.list[i] - self.list[j]:
#                         max = self.list[i] - self.list[j]
#                         max_daiy[0] = i     #卖出时间
#                         max_daiy[1] = j     #买入时间
#
#         max_rise = 0
#         for i in range(len(self.list)):
#             min_index = min(self.list[i],min_index)
#             max_rise = max(max_rise,self.list[i] - min_index)
#
#         return max

class Solution:
    """
    最大利润 max{前一天的最大利润，当前价格 - 以前最低价格}
    """
    def maxProfit(self, prices):
        min_prices = prices[0]
        max_prices = float(0)
        for i in range(len(prices)):
            min_prices = min(min_prices,prices[i])
            max_prices = max(max_prices,prices[i] - min_prices)
        return max_prices

if __name__ == '__main__':
    list = [7,1,5,3,6,4]
    res = Solution().maxProfit(list)
    print(res)