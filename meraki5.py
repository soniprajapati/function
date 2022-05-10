
list = [8, 6, 4, 8, 4, 50, 2, 7]
def minimum():
    small=min(list)
    print("Minimum no.=",small)
minimum()

def check_number(a,b):
    if a%2==0 and b%2==0:
        print("dono even hai")
    else:
        print("dono even nhi hai")
a=int(input("enter no."))
b=int(input("enter no."))
check_number(a,b)

def check_number_list(a,b):
    i=0
    while i<len(a):
        j=0
        while j<len(b):
            if a[i]%2==0 and b[j]%2==0:
                print("dono even hain")
            else:
                print("dono even nahi hai")
            j+=1
        i+=1
check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
