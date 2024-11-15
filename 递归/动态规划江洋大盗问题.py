baowu = ((0, 0), (2, 3), (3, 4), (4, 8), (5, 8), (9, 10))
maxweig = 20
m = {(i, w): 0 for i in range(len(baowu)) for w in range(maxweig + 1)}
restore = []
# 神骐
# 初始化记录选择的数组
select = [[0 for _ in range(maxweig + 1)] for _ in range(len(baowu))]

for i in range(1, len(baowu)):
    for j in range(1, maxweig + 1):
        if baowu[i][0] > j:  # 如果当前物品重量大于当前背包容量，不拿
            m[(i, j)] = m[(i - 1, j)]
        else:
            # 比较不拿和拿的情况，选择价值更大的
            if m[(i - 1, j)] > m[(i - 1, j - baowu[i][0])] + baowu[i][1]:
                m[(i, j)] = m[(i - 1, j)]
            else:
                m[(i, j)] = m[(i - 1, j - baowu[i][0])] + baowu[i][1]
                select[i][j] = 1  # 记录选择了当前物品

# 根据select数组恢复选择的物品
j = maxweig
for i in range(len(baowu) - 1, 0, -1):
    if select[i][j] == 1:
        restore.append(baowu[i])
        j -= baowu[i][0]  # 更新剩余的背包容量

restore.reverse()  # 反转恢复的物品顺序，因为我们是倒序添加的

print("最大价值：", m[len(baowu) - 1, maxweig])
print("选择的物品：", restore)
