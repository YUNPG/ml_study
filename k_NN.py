
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.cousin = None

    def print(self):
        print('value:', self.value)
        print('left:', self.left.value if self.left else 'No')
        print('right:', self.right.value if self.right else 'No')
        print('parent:', self.parent.value if self.parent else 'No')
        print('cousin:', self.cousin.value if self.cousin else 'No')

def creat_kd_tree(x_train):
    x0 = sorted(x_train, key=lambda x: x[0])
    half_index = len(x0) // 2
    root = TreeNode(x0[half_index])
    def sub_creat_kd_tree(root, x_left, x_right, k, max):
        #print('root:', root.value)
        #print('left_list:', x_left)
        #print('right_list:', x_right)
        k += 1
        if k == max:
            k = 0
        #print('k:', k)
        left_node = None
        right_node = None
        if x_left:
            x_left_temp = sorted(x_left, key=lambda x: x[k])
            half_index = len(x_left_temp) // 2
            left_node = TreeNode(x_left_temp[half_index])
            left_node.parent = root
            root.left = left_node
            sub_creat_kd_tree(root.left, x_left_temp[0:half_index], x_left_temp[half_index+1:], k, max)
        if x_right:
            x_right_temp = sorted(x_right, key=lambda x: x[k])
            half_index = len(x_right_temp) // 2
            right_node = TreeNode(x_right_temp[half_index])
            right_node.parent = root
            root.right = right_node
            sub_creat_kd_tree(root.right, x_right_temp[0:half_index], x_right_temp[half_index+1:], k, max)
        if left_node:
            left_node.cousin = right_node
        if right_node:
            right_node.cousin = left_node

    sub_creat_kd_tree(root, x0[0:half_index], x0[half_index+1:], 0, len(x_train[0]))
    return root

def print_tree(root):
    if root:
        root.print()
        print_tree(root.left)
        print_tree(root.right)

def kd_tree_search(root, test_data):
    def node_find(root, test_data, k, max):
        if k == max:
            k = 0
        if test_data[k] <= root.value[k]:
            if root.left:
                return node_find(root.left, test_data, k+1, max)
            else:
                return (k, root)
        else:
            if root.right:
                return node_find(root.right, test_data, k+1, max)
            else:
                return (k, root)

    (k, min_node) = node_find(root, test_data, 0, len(test_data))
    #min_node.print()
    def list_dis(list_data1, list_data2):
        dis = 0
        for (data1, data2) in zip(list_data1, list_data2):
            dis += (data1 - data2)*(data1 - data2)
        return dis
    min_value = list_dis(min_node.value, test_data)
    #print(min_value)
    def node_check(cur_node, test_data, min_node,  min_value, cur_k):
        while cur_node.parent!=None:
            if list_dis(cur_node.cousin.value, test_data) < min_value:
                (cur_k, min_node) = node_find(cur_node.cousin, test_data, cur_k, len(test_data))
                cur_node = min_node
                min_value = list_dis(cur_node.value, test_data)
                return node_check(cur_node, test_data, min_value, cur_k)
            else:
                cur_node = cur_node.parent
                dis_temp = list_dis(cur_node.value, test_data)
                if dis_temp < min_value:
                    min_node = cur_node
                    min_value = dis_temp
                cur_k -= 1
                if cur_k < 0:
                    cur_k = len(test_data)-1
        return (min_node, min_value)

    (min_node, min_value) = node_check(min_node, test_data, min_node,  min_value, k)
    #min_node.print()
    #print(min_value)
    return min_node


if __name__ == '__main__':
    x_train = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
    y_train = ['a', 'b', 'c', 'd', 'e', 'f']
    x_test = [[6, 3]]
    root = creat_kd_tree(x_train)
    #print_tree(root)
    for x in x_test:
        min_node = kd_tree_search(root, x)
        index = 0
        for i in range(len(x_train)):
            if min_node.value == x_train[i]:
                index = i
                break
        y_test = y_train[index]
        print('x:', x, 'y:', y_test)