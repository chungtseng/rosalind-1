import sys

def main():
    with open(sys.argv[1], "r") as f:
        money = int(f.readline())
        coins = tuple(int(coin) for coin in f.readline().split(","))

    print coins
    min_num_coins = {0: 0}
    for m in range(1, money+1):
        min_change = m * 10
        coin_gen = (coin for coin in coins if coin <= m)
        for coin in coin_gen:
            change = min_num_coins[m - coin] + 1
            if change < min_change:
                min_change = change
                min_num_coins[m] = min_change
        print m, min_change
    print min_num_coins[money]


if __name__ == '__main__':
    main()