# *args: & **kwargs:
# Rule: params, *args, default parameters, **kwargs
def function(name, *args, age=17, **kwargs):
    """*args used for positional arguments
    **kwargs used for keyword arguments
    """
    print(sum(args) + sum(kwargs.values()))
    print(name)
    print(age)


function("Jasjeet Singh", 1, 2, 3, 4, 5, num1=10, num2=15)
