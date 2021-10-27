class Solutions:
    """
    斐波那锲数列
    爬楼梯：
        n阶楼梯，当先爬1阶时，剩下的楼梯有n-1种
                当先爬2阶时，剩下的楼梯有n-2种
                故 f(n) = f(n-1) + f(n-2)
    """
    def climbStair(self,n):
        a,b = 1,1
        for i in range(n-1):
            a,b = a+b,a
        return a
