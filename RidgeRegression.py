import numpy as np

def RidgeRegression(x, y, degrees=5, l=0.1):
    """
    :param x:
    :param y:
    :param degrees:
    :param l:
    :return:
    """
    X = np.empty((len(x), degree+1))
    for i in range(degree+1):
        X[:,i] = np.power(x[:, 0], i)

    pass
