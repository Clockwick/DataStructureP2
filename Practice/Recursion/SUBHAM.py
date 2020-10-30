def fun(x):

    if(x > 0):
        x -= 1
        fun(x)
        print(x, end=" ")
        x -= 1
        fun(x)


# Driver code
a = 5
fun(a)

# This code is contributed by SHUBHAMSINGH10
