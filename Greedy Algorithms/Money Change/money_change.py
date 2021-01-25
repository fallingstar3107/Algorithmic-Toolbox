# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coins = 0
    denoms = [10, 5, 1]
    for denom in denoms:
        coins = coins + money // denom
        money = money % denom
    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
