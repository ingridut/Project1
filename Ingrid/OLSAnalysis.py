from Analysis import plotFrankes, MeanSquaredError, R2, FrankeFunction, var2, varBeta, betaConfidenceInterval_OLS, bias, var_f
from OrdinaryLeastSquare import ols
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from kFoldValidation import k_fold_validation
"""
    Analysis of a OLS model of Franke's function, using set of 1000 random x and y points
"""

# Load random data, 1000 points
X = np.load('data_for_part_1.npy')
x = X[:, 0]
y = X[:, 1]

#Noise

noises = [0, 0.001, 0.01, 0.1, 0.2, 0.3, 0.4]

#Degree
degree = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#GENERAL
MSE_noise1 = []
R2_noise1 = []

z = FrankeFunction(x, y, noise=0)
z001 = FrankeFunction(x, y, noise=0.001)
z01 = FrankeFunction(x, y, noise=0.01)
z1 = FrankeFunction(x, y, noise=0.1)
z2 = FrankeFunction(x, y, noise=0.2)
z3 = FrankeFunction(x, y, noise=0.3)
z4 = FrankeFunction(x, y, noise=0.4)



########################################################################################################
########################################################################################################
        #          DEGREE = 2
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=2)
Bs001 = ols(x, y, z001, degree=2)
Bs01 = ols(x, y, z01, degree=2)
Bs1 = ols(x, y, z1, degree=2)
Bs2 = ols(x, y, z2, degree=2)
Bs3 = ols(x, y, z3, degree=2)
Bs4 = ols(x, y, z4, degree=2)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(2)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 14.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 2 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 3
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=3)
Bs001 = ols(x, y, z001, degree=3)
Bs01 = ols(x, y, z01, degree=3)
Bs1 = ols(x, y, z1, degree=3)
Bs2 = ols(x, y, z2, degree=3)
Bs3 = ols(x, y, z3, degree=3)
Bs4 = ols(x, y, z4, degree=3)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(3)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 14.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 3 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 4
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=4)
Bs001 = ols(x, y, z001, degree=4)
Bs01 = ols(x, y, z01, degree=4)
Bs1 = ols(x, y, z1, degree=4)
Bs2 = ols(x, y, z2, degree=4)
Bs3 = ols(x, y, z3, degree=4)
Bs4 = ols(x, y, z4, degree=4)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(4)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 14.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 4 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
#          DEGREE = 5
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=5)
Bs001 = ols(x, y, z001, degree=5)
Bs01 = ols(x, y, z01, degree=5)
Bs1 = ols(x, y, z1, degree=5)
Bs2 = ols(x, y, z2, degree=5)
Bs3 = ols(x, y, z3, degree=5)
Bs4 = ols(x, y, z4, degree=5)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(5)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 5.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 5 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
#          DEGREE = 6
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=6)
Bs001 = ols(x, y, z001, degree=6)
Bs01 = ols(x, y, z01, degree=6)
Bs1 = ols(x, y, z1, degree=6)
Bs2 = ols(x, y, z2, degree=6)
Bs3 = ols(x, y, z3, degree=6)
Bs4 = ols(x, y, z4, degree=6)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(6)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 6.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 6 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
#          DEGREE = 7
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=7)
Bs001 = ols(x, y, z001, degree=7)
Bs01 = ols(x, y, z01, degree=7)
Bs1 = ols(x, y, z1, degree=7)
Bs2 = ols(x, y, z2, degree=7)
Bs3 = ols(x, y, z3, degree=7)
Bs4 = ols(x, y, z4, degree=7)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(7)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 7.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 7 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
    #          DEGREE = 8
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=8)
Bs001 = ols(x, y, z001, degree=8)
Bs01 = ols(x, y, z01, degree=8)
Bs1 = ols(x, y, z1, degree=8)
Bs2 = ols(x, y, z2, degree=8)
Bs3 = ols(x, y, z3, degree=8)
Bs4 = ols(x, y, z4, degree=8)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(8)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 8.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 8 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
    #          DEGREE = 9
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=9)
Bs001 = ols(x, y, z001, degree=9)
Bs01 = ols(x, y, z01, degree=9)
Bs1 = ols(x, y, z1, degree=9)
Bs2 = ols(x, y, z2, degree=9)
Bs3 = ols(x, y, z3, degree=9)
Bs4 = ols(x, y, z4, degree=9)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(9)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 9.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 9 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 10
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=10)
Bs001 = ols(x, y, z001, degree=10)
Bs01 = ols(x, y, z01, degree=10)
Bs1 = ols(x, y, z1, degree=10)
Bs2 = ols(x, y, z2, degree=10)
Bs3 = ols(x, y, z3, degree=10)
Bs4 = ols(x, y, z4, degree=10)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(10)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 10.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 10 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
    #          DEGREE = 11
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=11)
Bs001 = ols(x, y, z001, degree=11)
Bs01 = ols(x, y, z01, degree=11)
Bs1 = ols(x, y, z1, degree=11)
Bs2 = ols(x, y, z2, degree=11)
Bs3 = ols(x, y, z3, degree=11)
Bs4 = ols(x, y, z4, degree=11)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(11)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 11.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 11 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 12
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=12)
Bs001 = ols(x, y, z001, degree=12)
Bs01 = ols(x, y, z01, degree=12)
Bs1 = ols(x, y, z1, degree=12)
Bs2 = ols(x, y, z2, degree=12)
Bs3 = ols(x, y, z3, degree=12)
Bs4 = ols(x, y, z4, degree=12)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(12)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 12.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 12 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 13
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=13)
Bs001 = ols(x, y, z001, degree=13)
Bs01 = ols(x, y, z01, degree=13)
Bs1 = ols(x, y, z1, degree=13)
Bs2 = ols(x, y, z2, degree=13)
Bs3 = ols(x, y, z3, degree=13)
Bs4 = ols(x, y, z4, degree=13)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(13)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 13.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 13 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
    #          DEGREE = 14
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=14)
Bs001 = ols(x, y, z001, degree=14)
Bs01 = ols(x, y, z01, degree=14)
Bs1 = ols(x, y, z1, degree=14)
Bs2 = ols(x, y, z2, degree=14)
Bs3 = ols(x, y, z3, degree=14)
Bs4 = ols(x, y, z4, degree=14)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(14)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 14.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 14 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 15
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=15)
Bs001 = ols(x, y, z001, degree=15)
Bs01 = ols(x, y, z01, degree=15)
Bs1 = ols(x, y, z1, degree=15)
Bs2 = ols(x, y, z2, degree=15)
Bs3 = ols(x, y, z3, degree=15)
Bs4 = ols(x, y, z4, degree=15)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(15)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 15.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 15 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 16
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=16)
Bs001 = ols(x, y, z001, degree=16)
Bs01 = ols(x, y, z01, degree=16)
Bs1 = ols(x, y, z1, degree=16)
Bs2 = ols(x, y, z2, degree=16)
Bs3 = ols(x, y, z3, degree=16)
Bs4 = ols(x, y, z4, degree=16)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(16)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 16.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 16 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 17
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=17)
Bs001 = ols(x, y, z001, degree=17)
Bs01 = ols(x, y, z01, degree=17)
Bs1 = ols(x, y, z1, degree=17)
Bs2 = ols(x, y, z2, degree=17)
Bs3 = ols(x, y, z3, degree=17)
Bs4 = ols(x, y, z4, degree=17)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(17)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 17.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 17 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 18
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=18)
Bs001 = ols(x, y, z001, degree=18)
Bs01 = ols(x, y, z01, degree=18)
Bs1 = ols(x, y, z1, degree=18)
Bs2 = ols(x, y, z2, degree=18)
Bs3 = ols(x, y, z3, degree=18)
Bs4 = ols(x, y, z4, degree=18)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(18)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 18.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 18 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 19
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=19)
Bs001 = ols(x, y, z001, degree=19)
Bs01 = ols(x, y, z01, degree=19)
Bs1 = ols(x, y, z1, degree=19)
Bs2 = ols(x, y, z2, degree=19)
Bs3 = ols(x, y, z3, degree=19)
Bs4 = ols(x, y, z4, degree=19)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(19)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 19.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 19 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
        #          DEGREE = 20
########################################################################################################
########################################################################################################
Bs = []
Bs001 = []
Bs01 = []
Bs1 = []
Bs2 = []
Bs3 = []
Bs4 = []


Bs = ols(x, y, z, degree=20)
Bs001 = ols(x, y, z001, degree=20)
Bs01 = ols(x, y, z01, degree=20)
Bs1 = ols(x, y, z1, degree=20)
Bs2 = ols(x, y, z2, degree=20)
Bs3 = ols(x, y, z3, degree=20)
Bs4 = ols(x, y, z4, degree=20)
    


# Generate new test data
x_test = np.random.rand(200)
y_test = np.random.rand(200)

z_test = FrankeFunction(x_test, y_test, noise=0)
z_test001 = FrankeFunction(x_test, y_test, noise=0.001)
z_test01 = FrankeFunction(x_test, y_test, noise=0.01)
z_test1 = FrankeFunction(x_test, y_test, noise=0.1)
z_test2 = FrankeFunction(x_test, y_test, noise=0.2)
z_test3 = FrankeFunction(x_test, y_test, noise=0.3)
z_test4 = FrankeFunction(x_test, y_test, noise=0.4)



M_ = np.c_[x_test, y_test]
poly = PolynomialFeatures(20)
M = poly.fit_transform(M_)

MSEs = []
R2scoreS = []

#Noise = 0
z_predict= M.dot(Bs)
MSE = MeanSquaredError(z_test, z_predict)
R2score = R2(z_test, z_predict)
MSEs.append(MSE)
R2scoreS.append(R2score)

#Noise = 0.001
z_predict001 = M.dot(Bs001)
MSE001 = MeanSquaredError(z_test001, z_predict001)
R2score001 = R2(z_test001, z_predict001)
MSEs.append(MSE001)
R2scoreS.append(R2score001)


##Noise = 0.01
z_predict01= M.dot(Bs01)
MSE01 = MeanSquaredError(z_test01, z_predict01)
R2score01 = R2(z_test01, z_predict01)
MSEs.append(MSE01)
R2scoreS.append(R2score01)

#Noise = 0.1
z_predict1= M.dot(Bs1)
MSE1 = MeanSquaredError(z_test1, z_predict1)
R2score1 = R2(z_test1, z_predict1)
MSEs.append(MSE1)
R2scoreS.append(R2score1)
###GENERAL
MSE_noise1.append(MSE1)
R2_noise1.append(R2score1)

#Noise = 0.2
z_predict2= M.dot(Bs2)
MSE2 = MeanSquaredError(z_test2, z_predict2)
R2score2 = R2(z_test2, z_predict2)
MSEs.append(MSE2)
R2scoreS.append(R2score2)

#Noise = 0.3
z_predict3= M.dot(Bs3)
MSE3 = MeanSquaredError(z_test3, z_predict3)
R2score3 = R2(z_test3, z_predict3)
MSEs.append(MSE3)
R2scoreS.append(R2score3)

#Noise = 0.4
z_predict4= M.dot(Bs4)
MSE4 = MeanSquaredError(z_test4, z_predict4)
R2score4 = R2(z_test4, z_predict4)
MSEs.append(MSE4)
R2scoreS.append(R2score4)



fig, ax1 = plt.subplots()
ax1.plot(noises, MSEs, 'bo-')
ax1.set_xlabel('Data with different degree of noise')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(noises, R2scoreS, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of noise on MSE and R2 Score. Polynomial degree 20.')
fig.tight_layout()
plt.show()

for i in range(len(noises)):
    print("Model of degree 20 with noise: {}, MSE: {}, R2 score {}".format(noises[i], MSEs[i], R2scoreS[i]))

########################################################################################################
########################################################################################################
 
#GENERAL D= 0.1, Degree=2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, MSE, R2
#MSE_noise1
#R2_noise1
    
fig, ax1 = plt.subplots()
ax1.plot(degree, MSE_noise1, 'bo-')
ax1.set_xlabel('Different polynomial degrees (2, 3, ..., 20)')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('MSE', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(degree, R2_noise1, 'r*-')
ax2.set_ylabel('R2 score', color='r')
ax2.tick_params('y', colors='r')

plt.grid(True)
plt.title('Influence of different polynomial degree on MSE and R2 Score for data with noise degree D= 0.1.')
fig.tight_layout()
plt.show()


############################################################################
