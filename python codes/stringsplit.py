#Question 5
def print_list():
    list= input("Enter elements of list : ").split()
    n=len(max(list, key = len))         #To find the maximum element so we can arrange the other elements accordingly
    print("*"*n+"*"*4)
    for i in list:
         c=n-len(i)                     #To store the amount of block to add so that the pattern remains undisturbed
         print("* "+ i +" "*c+" *")
    print("*"*n+"*"*4)                  #printing lower boundary
print_list()