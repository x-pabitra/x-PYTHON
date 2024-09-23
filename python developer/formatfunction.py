#4/8/11
w="welcome {}to{} Wscubetech".format("hello",20);
print(w) 

w="welcome {1}to {0} wscubetch".format("hello",20);
print(w)

w="welcome {b:^10} to {a} Wscubetech".format(a=30,b=40);
print(w)
w="welcome {b:>10} to {a:^10} Wscubetech".format(a=30,b=40);
print(w)