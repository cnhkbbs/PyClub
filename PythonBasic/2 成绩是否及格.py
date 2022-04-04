# 输入成绩值x∈[0,100]，如果x≥60，则输出pass，否则输出fail。

# 输入格式:
# 直接输入[0,100]之间的1个整数，没有其它任何附加字符。

# 输出格式:
# 直接输出你“pass”或“fail”，没有其它任何附加字符。

# 输入样例:
# 78
# 输出样例:
# pass
# 输入样例:
# 46
# 输出样例:
# fail

# -*- coding:UTF-8 -*-
x = int(input())
if x >= 60:
    print('pass')
else:
    print('fail')
