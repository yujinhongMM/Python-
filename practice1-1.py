#天气指数
num=eval(input("请输入天气指数："));
if 0 < num <= 35:
    print("优")
elif num <= 75:
    print("良")
elif num <= 115:
    print("轻度污染")
elif num <= 150:
    print("中度污染")
elif num <= 250:
    print("重度污染")
elif num <= 500:
    print("严重污染")
else:
    print("参数错误")


