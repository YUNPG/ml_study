import numpy as np
import matplotlib.pyplot as plt

def linear_regression(mode, x_in, y_in, alpha=0.001, epsilon=1e-5):
    sample_num = len(y_in)
    if mode == 'Formula':
        return lr_formula(sample_num, x_in, y_in)
    elif mode == 'BGD':
        return gradient_descent(sample_num, x_in, y_in, cost_function_lr, alpha, epsilon)
    elif mode == 'SGD':
        pass
    elif mode == 'MBGD':
        pass
    elif mode == 'Momentum':
        pass
    elif mode == 'NAG':
        pass

def lr_formula(sample_num, x_in, y_in):
    res_theta = np.linalg.pinv(x_in.T * x_in)*x_in.T*y_in
    diff = (x_in*res_theta)-y_in
    j_theta = diff.T*diff/sample_num
    return (j_theta, res_theta)

def cost_function_lr(sample_num, alpha, theta, x_in, y_in):
    diff = (x_in*theta)-y_in
    j_theta = diff.T*diff/sample_num
    partial_theta = (x_in.T*diff)/sample_num*alpha
    return (j_theta, partial_theta)

def gradient_descent(sample_num, x_in, y_in, cost_function, alpha, epsilon):
    theta = np.mat(np.zeros((x_in.shape[1],1)))
    diff = (x_in*theta)-y_in
    pre_j_theta = 0xFFFFFFFF
    count = 5000
    while count:
        (j_theta, partial_theta) = cost_function(sample_num, alpha, theta, x_in, y_in)
        if pre_j_theta-j_theta < epsilon or np.fabs(partial_theta).all() < epsilon:
            break
        theta -= partial_theta
        pre_j_theta = j_theta;
        count -= 1
    if not count:
        print('get max count')
    return (pre_j_theta, theta)

def data_creat():
    m = 30
    X0 = np.ones((m, 1))
    X1 = np.arange(1, m+1).reshape(m, 1)
    x_in = np.mat(np.hstack((X0, X1)))
    theta = np.mat([5, 0.5]).reshape(2, 1)
    y_in = x_in*theta + np.random.randn(m).reshape(m, 1)
    return (m, x_in, y_in)

def data_analysis(m, x_in, y_in, j_theta, theta):
    x = x_in[:,1]
    plt.figure()
    plt.scatter(np.array(x), np.array(y_in))
    plt.plot(x, np.array(x_in*theta), color='r')
    plt.title('cost: %f' % j_theta)
    plt.show()

if __name__ == '__main__':
    m = 30
    X0 = np.ones((m, 1))
    X1 = np.arange(1, m+1).reshape(m, 1)
    x_in = np.mat(np.hstack((X0, X1)))
    theta = np.mat([5, 0.5]).reshape(2, 1)
    y_in = x_in*theta + np.random.randn(m).reshape(m, 1)
    (m, x_in, y_in) = data_creat()

    res_j_theta, res_theta_formula = linear_regression('Formula', x_in, y_in)
    data_analysis(m, x_in, y_in, res_j_theta, res_theta_formula)

    res_j_theta, res_theta_gd = linear_regression('BGD', x_in, y_in, 0.001, 1e-5)
    data_analysis(m, x_in, y_in, res_j_theta, res_theta_gd)

