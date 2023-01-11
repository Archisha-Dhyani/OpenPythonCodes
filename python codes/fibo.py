#Question 1
def fibonacci():        #function that computes the list of the first 100 Fibonacci numbers
    a=1;                
    b=1;
    n=0;
    print(a,"\n")
    print(b,"\n")
    while(n<=97):           # to run this loop 98 times since the first two terms are already prited.
        c=a+b
        print(c,"\n")
        a=b
        b=c
        n+=1              
fibonacci()                 #to invoke the function
