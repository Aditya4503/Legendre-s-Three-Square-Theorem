#Legendre's three-square theorem    :      n=4**a(8*b+7)
def threesquares(n): 
    condition = True
    for i in range(0,n+1):
        for j in range(0,n+1):
            if n==(4**i)*(8*j+7):
                condition = False
                break
    print(condition)
    
threesquares(143)

#Code by : alpha_maverick
