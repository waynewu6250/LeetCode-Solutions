
#  * 計算河內塔
#  *
#  * @param n 搬移的盤子數目
#  * @param a 來源地 (source)
#  * @param b 中繼站 (bridge)
#  * @param c 目的地 (destination)
#  * @return


def hanoi(n, a, b, c):
    if n == 1:
        print("From"+a+"To"+c)
    else:
        hanoi(n-1, a, c, b) #先搬 n-1 個盤子 到 b (將 c 當中繼)
        hanoi(1, a, b, c) #將剩下的一個盤子 由 a 搬到 c
        hanoi(n-1, b, a, c) #將剛剛 塔b 的 n-1 個盤子 再由 b 搬到 c (a 當中繼)
