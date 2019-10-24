
class LinkList():
    def __init__(self, length=0):
        pre_node = None
        for i in range(length):
            node = Node(i+1)
            if i == 0:
                self.head = node
                pre_node = node
            else:
                pre_node.next = node
                pre_node = node

        node.next = self.head

    @property
    def length(self):
        node = self.head
        length = 1
        while node.next != self.head:
            length += 1
            node = node.next
        return length

    def remove(self, node):

        if node == self.head:
            while node.next != self.head:
                node = node.next

            node.next = self.head.next
            del_node = self.head
            self.head = self.head.next
            del del_node
            return

        temp_node = self.head
        while temp_node.next != node:
            temp_node = temp_node.next

        temp_node.next = node.next
        del node

        return

    def show_link_list_data(self):
        node = self.head

        print(f'head data is {self.head.data}')

        print(node.data)
        while node.next != self.head:
            node = node.next
            print(node.data)

    def get_node(self, index):
        if index == 1:
            return self.head

        i = 1
        node = self.head
        while i != index:
            node = node.next
            i += 1
        return node

class Node():
    def __init__(self, data=None, next=None):
        self.next = next
        self.data = data

def link_method(length=41, step=3, remain_human_number=2):
    '''
   :param length: 列表的长度，也就是人的个数
   :param step: 每次数到几就杀掉这个人
   :param remain_human_number: 剩下的人的个数
   '''
    link_list = LinkList(length=length)
    i = 1
    node = link_list.head
    while link_list.length > remain_human_number:
        if i == step:
            i = 0
            link_list.remove(node)
        node = node.next
        i += 1

    link_list.show_link_list_data()

def get_array_length(array):
    length = 0
    for value in array:
        if value != 0:
            length += 1

    return length


def array_method(length=41, step=3, remain_human_number=2):
    '''
    :param length: 列表的长度，也就是人的个数
    :param step: 每次数到几就杀掉这个人
    :param remain_human_number: 剩下的人的个数
    '''
    data = [ i+1 for i in range(length) ]
    i = 1
    index = 0
    while get_array_length(data) > remain_human_number:
        if i == step:
            i = 0
            data[index] = 0

        index += 1
        if index == len(data):
            index = 0
        while data[index] == 0:
            index += 1
            if index == len(data):
                index = 0
        i += 1
    print(data)

if __name__ == '__main__':
    link_method()
    # array_method()
