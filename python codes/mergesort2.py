#Question 3
def merge():            #Function that merges two sorted lists into a new sorted list.
    list1 = input("Enter elements of list 1: ").split()
    list2 = input("Enter elements of list 2: ").split()
    print(sorted(list1+list2))
merge()