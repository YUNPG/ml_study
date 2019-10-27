def bayes(x_train, y_train, x_test, lamda):
    prim_p = dict()
    for y_in in y_train:
        if prim_p.get(y_in, 'no') == 'no':
            prim_p[y_in] = 1
        else:
            prim_p[y_in] += 1

    for key in prim_p.keys():
        prim_p[key] = (prim_p[key] + lamda) / (len(y_train) + len(prim_p)*lamda)

    #print(prim_p)

    condi_p = dict()
    count_dict = dict()
    class_value_dict = dict()
    for (x_in, y_in) in zip(x_train, y_train):
        for index in range(len(x_in)):
            # compute condition p
            value = (index, x_in[index], y_in)
            if condi_p.get(value, 'no') == 'no':
                condi_p[value] = 1
            else:
                condi_p[value] += 1
            # compute count
            value = (index, y_in)
            if count_dict.get(value, 'no') == 'no':
                count_dict[value] = 1
            else:
                count_dict[value] += 1
            #  compute class count
            if class_value_dict.get(index, 'no') == 'no':
                class_value_dict[index] = {x_in[index]}
            else:
                class_value_dict[index].add(x_in[index])

    #print(class_value_dict)

    for key in condi_p.keys():
        condi_p[key] = (condi_p[key]+lamda)/(count_dict[(key[0], key[2])]+len(class_value_dict[key[0]])*lamda)

    #print(condi_p)
    for x in x_test:
        out_dict = dict()
        for y_key in prim_p.keys():
            out_dict[(y_key, tuple(x))] = prim_p[y_key]
            for i in range(len(x)):
                out_dict[(y_key, tuple(x))] *= condi_p[(i, x[i], y_key)]
        #print(out_dict)
        max = 0
        max_key = None
        for key in out_dict.keys():
            if out_dict[key] > max:
                max = out_dict[key]
                max_key = key
        print ('test x:', x, 'result:', max_key[0])

def native_bayes(x_train, y_train, x_test):
    bayes(x_train, y_train, x_test, 0)


if __name__ == '__main__':
    x_train = [[1, 'S'], [1, 'M'], [1, 'M'], [1, 'S'], [1, 'S'],
               [2, 'S'], [2, 'M'], [2, 'M'], [2, 'L'], [2, 'L'],
               [3, 'L'], [3, 'M'], [3, 'M'], [3, 'L'], [3, 'L']]
    y_train = [-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1]
    x_test = [[2, 'S']]
    native_bayes(x_train, y_train, x_test)
    bayes(x_train, y_train, x_test, 1)