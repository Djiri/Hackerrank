n=int(input())
pbook=dict(input().split(" ") for _ in range(n))
while True:
    try:
        name=input().strip()
        if name in pbook:
            print("%s=%s" % (name,pbook[name]))
        else:
            print('Not found')
    except:
        break