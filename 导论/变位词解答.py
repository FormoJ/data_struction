input1 = "python"
input2 = "tpuyon"

# 取出所有字符
input1_list = list(input1)
input2_list = list(input2)
if len(input1_list) == len(input2_list):
    for i in input1_list:
        try:
            input2_list.remove(i)
        except ValueError:
            pass
else:
    print("不是")
if len(input2_list) != 0:
    print("不是")
else:
    print("是")