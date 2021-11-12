#%%

def a_function(a_parameter):
    a_variable = 15
    return a_parameter
a_function(10)
print(a_variable)

#%%
def outer_function(a,b):
    def inner_function(c,d):
        return c+d
    return inner_function(a,b)

result = outer_function(5,10)
print(result)


# %%
def all_aboard(a, *args, **kw):
    print(a,args,kw)

all_aboard(4,7,3,0,z=10,y=64)

# %%
