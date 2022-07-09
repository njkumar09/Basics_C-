


#Scope of functions


def scope(var):
    # the below variable can be accesed by nested functions, However, immutable objects like str, int can't be changed 
    new = "value"
    
    def nested_function():
        new = "new value"
        
 #the below return is focused to scope function 
return nested_function()





