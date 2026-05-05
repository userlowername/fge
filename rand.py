import random

# 读取文件内容
with open('./annotation/FF++_test.txt', 'r') as file:
    lines = file.readlines()

# 处理每一行，替换第二列为随机数
new_lines = []
for line in lines:
    parts = line.split()
    if len(parts) > 1:
        parts[1] = str(random.randint(1, 20))
    new_lines.append(' '.join(parts) + '\n')

# 将修改后的内容写回文件
with open('./annotation/FF++_test.txt', 'w') as file:
    file.writelines(new_lines)