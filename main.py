import matplotlib.pyplot as plt

def function(x):
    return x**2


def simpsons(f, a, b, n):
    h = (b-a)/n
    k = 0
    x = a + h

    for i in range(1, (n//2)+1):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h

    for i in range(1, (n//2)+1):
        k += 2*f(x)
        x += 2*h

    return (h/3)*(f(a)+f(b)+k)


lower_limit = int(input("Enter lower limit of integration: "))
upper_limit = int(input("Enter upper limit of integration: "))
user_n = int(input("Enter a value for n: "))
answer = (simpsons(function, lower_limit, upper_limit, user_n))
print(answer)

x_values = []
y_values = []

for x in range(user_n):
    h = (upper_limit-lower_limit)/user_n
    z = (h*x)
    x_values.append(z)
    y_values.append(function(z))


plt.plot(x_values, y_values)

plt.xlabel("Integration = " + str(answer))

plt.show()