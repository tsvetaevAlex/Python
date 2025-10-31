
def count_args(args):
    print(">ArgsQTY: ", len(args))
    return(len(args))


a = 10
b = "010"
c = int(b)
 
print(a)
print (c)



print("---CountArgs----------")

count_args(1)
count_args(1,2,3)
count_args()
count_args(None)