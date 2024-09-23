def sum(a,b):
    print(a+b)
sum(20,10)    
sum(90,78)


# -----------------------

# default parameter value

def sum(a,b=1):
    print(a+b)
sum(20)
sum(40,20)


# ------------------
# retuen value

def square(x):
    return x*x,x*2
s=square(5) 
print(s)