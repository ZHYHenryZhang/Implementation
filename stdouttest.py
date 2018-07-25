import sys,time
#1
for i in range(5):
    time.sleep(1)
    print('#',end='')

#2
for i in range(5):
    time.sleep(1)
    print('#',end='')
    print('\n')

#3
for i in range(5):
    time.sleep(1)
    sys.stdout.write('#')
    sys.stdout.flush()
    
# 这三段代码执行一下，结果如下:
# 1 会在5秒过后一起输出:#####，而不是一秒输出一个
# 2 会每秒输出一个# 和 '\n'
# 3 会每秒输出一个#
# stdout不仅逼格高，而且最好用。

# 作者：西木杨
# 链接：https://www.zhihu.com/question/20390166/answer/262521949
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。