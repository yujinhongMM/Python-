#猴子分桃
def consume(count, num):
    if count == 0:
        return 1
    elif (num - 1) % 5 != 0:
        return -1
    num = (num - 1) * 4 / 5
    return consume(count - 1, num)


count=5
num=1
while 1:          
    num+=1
    result=consume(count,num)
    if result == 1:
        print("桃子至少有：",num)
        break;

