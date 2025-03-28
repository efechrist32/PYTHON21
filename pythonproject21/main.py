#Shubhangi has written some code and now wants to calculate the time complexity of the same. She wants to calculate the recurrence relations of the functions, Help her find the same, and print the output.
def myfunction1(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)
    def myfunction2(n):
        if(n<=1):
            return
        print("Codingal")
        myfunction2(n-1)