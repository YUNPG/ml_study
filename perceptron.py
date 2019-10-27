import numpy as np


def perceptron_raw(x_train, y_train, x_test):
    print('raw form start')
    w = np.array([0]*len(x_train[0]))
    b = 0
    eta = 1
    while True:
        flag = True
        for (x, y) in zip(x_train, y_train):
            x_in = np.array(x)
            #print('cur x:', x_in)
            if y * (np.inner(w, x_in.T) + b) <= 0:
                w += np.inner(y, x_in)*eta
                b += y*eta
                flag = False
                #print('update w:', w)
                #print('update b:', b)
                break
        if flag:
            break
    print('fin w:', w)
    print('fin b:', b)
    for x in x_test:
        x_out = np.array(x)
        print('test x:', x_out, ' out:', '-1' if np.inner(w, x_out.T)+b <= 0 else '1')
    print('raw form end')


def perceptron_dual(x_train, y_train, x_test):
    print('dual form start')
    alpha = np.array([0] * len(x_train))
    x_in = np.array(x_train)
    y_in = np.array(y_train)
    b = 0
    eta = 1
    gram = np.zeros([len(x_train), len(x_train)], dtype='int')
    for i in range(len(x_train)):
        for j in range(i, len(x_train)):
            gram[i][j] = np.inner(x_in[i], x_in[j].T)
            gram[j][i] = gram[i][j]
    print('Gram', gram)

    while True:
        flag = True
        for i in range(len(x_train)):
            sum = y_in[i]*b
            for j in range(len(x_train)):
                sum += y_in[i]*alpha[j]*y_in[j]*gram[j][i]
            if sum <= 0:
                alpha[i] += eta
                b += eta*y_in[i]
                flag = False
                #print('update alpha:', alpha)
                #print('update b:', b)
                break
        if flag:
            break
    w = 0
    for i in range(len(x_train)):
        w += alpha[i]*y_in[i]*x_in[i]
    print('fin w:', w)
    print('fin b:', b)
    for x in x_test:
        x_out = np.array(x)
        print('test x:', x_out, ' out:', '-1' if np.inner(w, x_out.T) + b <= 0 else '1')
    print('dual form end')


if __name__ == '__main__':
    x_train = [[3, 3], [4, 3], [1, 1]]
    y_train = [1, 1, -1]
    x_test = [[0, 0]]
    #perceptron_raw(x_train, y_train, x_test)
    perceptron_dual(x_train, y_train, x_test)
