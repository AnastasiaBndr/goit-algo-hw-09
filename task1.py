import timeit


class Coin:
    def __init__(self, nominal) -> None:
        self.nominal = nominal


class Cash_Register:
    def __init__(self) -> None:
        self.rest = [Coin(50), Coin(25), Coin(10), Coin(5), Coin(2), Coin(1)]

    def find_coins_greedy(self, sum: int):
        self.rest.sort(key=lambda x: x.nominal, reverse=True)
        rest = {}
        for item in self.rest:
            amount = 0
            while sum >= item.nominal:
                amount=int(sum/item.nominal)
                sum=sum%item.nominal
            rest[item.nominal] = amount
        return rest

    def find_min_coins(self, sum):
        dp = [float('inf')] * (sum + 1)
        dp[0] = 0
        coin_used = [-1] * (sum + 1)

        for i in range(1, sum + 1):
            for item in self.rest:
                if i - item.nominal >= 0:
                    if dp[i] > dp[i - item.nominal] + 1:
                        dp[i] = dp[i - item.nominal] + 1
                        coin_used[i] = item.nominal

        result = {}
        while sum > 0:
            nominal = coin_used[sum]
            if nominal == -1:
                break
            if nominal in result:
                result[nominal] += 1
            else:
                result[nominal] = 1
            sum -= nominal

        return result


def timer(string, func, sum):
    start = timeit.default_timer()
    print(string)
    func(sum)

    print("Time consumed :", timeit.default_timer() - start)
    print("\n")


if __name__ == '__main__':
    sum = 146
    cash_register = Cash_Register()
    print(f'\n---------------------------------\nSum: {sum}\n---------------------------------')
    print(cash_register.find_coins_greedy(sum))
    timer("Find coins greedy: ", cash_register.find_coins_greedy, sum)
    print(cash_register.find_min_coins(sum))
    timer("Find min coins: ", cash_register.find_min_coins, sum)
