# 背包問題解法 (全部都從1開始)
# 建立一個nxm的陣列來解
w = [0, 1, 4, 3, 1] #物品重量
p = [0, 1500, 3000, 2000, 2000] #物品價值

n = len(w)-1 #計算物品個數
m = 4 #背包負重

x = [] #紀錄物品編號
optp = [[0 for col in range(m + 1)] for raw in range(n + 1)] #紀錄價值

for i in range(1,n+1): #物品一件一件來
    for j in range(1,m+1): #依據背包容量填入
        if w[i] <= j:
            optp[i][j] = max(optp[i-1][j], p[i]+optp[i-1][j-w[i]])
        else:
            optp[i][j] = optp[i-1][j]
    
#往回倒推去看物品在哪
j = m
for i in range(n,0,-1):
    if optp[i][j] > optp[i-1][j]:
        x.append(i)
        j = j - w[i]

print("Problem 1:")
print("最大值: ", optp[n][m])
print("物品索引: ", x)

#######################################
# cpu雙核問題
# 把問題視為差值最小, 代表每個cpu要大概分一半
w = list(map(lambda x: int(x/1024), [0, 3072, 3072, 7168, 3072, 1024]))
p = w
n = len(w)-1 #計算package數
m = int(sum(w)/2+1)

optp = [[0 for col in range(m + 1)] for row in range(n + 1)] #紀錄價值

for i in range(1,n+1): #package一件一件來
    for j in range(1,m+1): #依據背包容量填入
        if w[i] <= j:
            optp[i][j] = max(optp[i-1][j], p[i]+optp[i-1][j-w[i]])
        else:
            optp[i][j] = optp[i-1][j]

print("Problem 2:")
print("最大值: ", optp[n][m])

#######################################
# 選擇一個數組內的任意數字, 使其和為sum的方法數
# 直接依序往下計算方法數
a = [0, 5, 5, 10, 2, 3]
sum_ = 15
n = len(a)-1
optp = [[1]+[0]*sum_ for i in range(n+1)]  # 第一列为1的原因是和为0的时候只有一种取法，就是什么都不取

for i in range(1,n+1): # 一個一個數字來
    for j in range(1,sum_+1): #依據sum種類填入累加方法數
        if a[i] <= j:
            optp[i][j] = optp[i-1][j]+optp[i-1][j-a[i]]
        else:
            optp[i][j] = optp[i-1][j]

print("Problem 3:")
print("方法數: ", optp[-1][-1])