def compute_hcf(x,y):
    if x>y :
        smaller = y
    else:
        smaller =x
    for i in range(1,smaller+1):
        if((x%i ==0)and (y%1==0)):
            hcf=i
            return hcf
num1 = 54
num2 = 45
print("hcf is",compute_hcf(num1,num2))