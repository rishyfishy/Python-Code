def newtonRaphson(f, f_prime, x0, eps_a):
    x = x0
    x_prev = x0
    ea = eps_a+1  # arbitrary but always satisfies initial while statement
    iterations = 0
    # just give up after 10000 iterations, probably not converging
    # avoids infinite loop
    while(ea > eps_a and iterations < 10000):

        if f_prime(x) == 0 and f(x) != 0:
            raise (zeroSlopeError)  # ho
        x = x-f(x)/f_prime(x)
        ea = (x-x_prev)/x
        x_prev = x
        iterations += 1

    return x
