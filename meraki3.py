
numbers = [1, 2, 3, 4, 5]
def sum():
    i=0
    total_sum=0
    while i<len(numbers):
        total_sum=total_sum+numbers[i]
        i+=1
    print("sum=",total_sum)
sum()

unorder_list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
def accending():
    unorder_list.sort()
    print("SORTED LIST=",unorder_list)
accending()
