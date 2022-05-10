
reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
def rev():
    reverse_list.reverse()
    print("Reverse list=",reverse_list)
rev()


def function_print_line(name):
    print("mera naam"+" "+name+" "+"hai")
function_print_line("rishabh")
print("mai navgurukul ka co-founder hu")



def sum(a,b):
	res=[]
	i=0
	while i<len(a):
		res.append(a[i]+b[i])
		i=i+1
	print(res)
a=[50, 60, 10] 
b=[10, 20, 13]
sum(a,b)