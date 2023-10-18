from numpy import euler_gamma



def funct1(x):
    return 1/4 * (x[0] ** 4)


def gradient1(x):
    return [x[0] ** 3]


def funct2(x):
    return 1.5 - euler_gamma**(-x[0]**2 - x[1]**2) - 0.5 * euler_gamma ** ( -(x[0] - 1)**2 - ((x[1] + 2)**2))


def gradient2(x):
    return [2*x[0]*euler_gamma**(-x[0]**2 - x[1]**2) + (x[0] - 1) * euler_gamma **( -(x[0] - 1)**2 - ((x[1] + 2)**2)),
            2*x[1]*euler_gamma**(-x[0]**2 - x[1]**2) + (x[1] - 1) * euler_gamma **( -(x[0] - 1)**2 - ((x[1] + 2)**2))]
    
    
    

    