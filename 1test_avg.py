m1= int(input("Enter marks for test1: "))
m2= int(input("Enter marks for test2: "))
m3= int(input("Enter marks for test3: "))

if m1<=m2 and m1<=m3:
    avg_marks= (m2+m3)/2
elif m2<=m1 and m1<=m3:
    avg_marks= (m1+m3)/2
elif m3<=m1 and m3<=m2:
    avg_marks= (m1+m2)/2

print("The best average marks case is : ",avg_marks)