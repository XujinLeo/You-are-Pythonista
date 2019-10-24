# python 实现约瑟夫环(链表方式和数组方式)

### 问题由来
据说著名犹太历史学家 Josephus有过以下的故事：在罗马人占领乔塔帕特后，39 个犹太人与Josephus及他的朋友躲到一个洞中，39个犹太人决定宁愿死也不要被敌人抓到，于是决定了一个自杀方式，41个人排成一个圆圈，由第1个人开始报数，每报数到第3人该人就必须自杀，然后再由下一个重新报数，直到所有人都自杀身亡为止。然而Josephus 和他的朋友并不想遵从。首先从一个人开始，越过k-2个人（因为第一个人已经被越过），并杀掉第k个人。接着，再越过k-1个人，并杀掉第k个人。这个过程沿着圆圈一直进行，直到最终只剩下一个人留下，这个人就可以继续活着。问题是，给定了和，一开始要站在什么地方才能避免被处决？Josephus要他的朋友先假装遵从，他将朋友与自己安排在第16个与第31个位置，于是逃过了这场死亡游戏。

上面就是约瑟夫问题的由来，在大学里面《数据结构》这门课中，也会将这个例子拿出来让大家编写程序实现这个算法。接下来我们就用两种方式来实现这个算法。(链表方法和数组方法)

### 演示环境
* 操作系统：windows10
* python版本：python 3.7
* 代码编辑器：pycharm 2018.2

### 数组方法

首先我们先使用一个相对来说比较简单的方法，使用数组（列表）的方法.

编程思路：
新建一个列表，长度为41，存放1到41总共41个数据，从第一个位置开始数，每数到第三个，就让这个位置的值变为0，并且从当前位置重新从零开始数数，每次数到3都这样，当数到最后一个位置的时候，又开始从第一个位置开始数数，知道整个数组中只有两个不为0的数为止。

1. 我们先编写一个get_array_length()的函数，用来获取列表中值不为零的个数。
```python
def get_array_length(array):
    length = 0
    for value in array:
        if value != 0:
            length += 1

    return length
```

上面的代码应该很简单吧，大家都能看懂吧。

2. 接下来就开始编写主要的逻辑函数了
```python
def array_method(length=41, step=3, remain_human_number=2):
    '''
    :param length: 列表的长度，也就是人的个数
    :param step: 每次数到几就杀掉这个人
    :param remain_human_number: 剩下的人的个数
    '''
    # 首先使用列表生成式初始化一个列表，对应的值为 [1,2,...,41]
    data = [ i+1 for i in range(length) ]
    # 定义初始计数的值为1
    i = 1
    # 记录数组下标的值index
    index = 0
    # 调用get_array_length函数，得到列表中值不为零的个数
    # 如果个数大于 remain_human_number这个值，就一直执行这个循环
    while get_array_length(data) > remain_human_number:
        # 如果i == step了，说明应该杀掉这个人了
        if i == step:
            # 重新设置i = 0，及重新开始计数
            i = 0
            # 设置当前位置的值为0， 表示这个值已被杀死
            data[index] = 0

        # 下标+1，也就是开始数下一个人
        index += 1
        # 如果index == len(data)， 说明超出了数组的长度
        # 重新赋值为0，从头开始
        if index == len(data):
            index = 0
        
        # 如果这个位置的值为0，表示这是被杀死了人，不能继续算在循环中
        # index 继续加一，直到是不为0的位置
        while data[index] == 0:
            index += 1
            if index == len(data):
                index = 0
        
        # i + 1
        i += 1
    
    # 最后打印这个数组
    print(data)
```

结果数据为：
```python
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

上面我们可以看出，最后剩下的两个人就是站在16和31位置的。所以我们的代码也是正确的。

### 链表方法

使用链表的方法就是考察我们对循环链表的掌握，要求我们知道怎样创建设使用循环链表。首先我们先创建节点类。

1. 创建节点类，Node()
```python
class Node():
    def __init__(self, data=None, next=None):
        # 存放下一个节点对象
        self.next = next
        # 存放自身节点的值
        self.data = data
```

2. 创建链表类， LinkList()， 准确的说是循环链表。
```python
class LinkList():
    def __init__(self, length=0):
        '''
        :param length : 链表的长度，也就是人的个数
        '''
        # 临时变量pre_node， 用来存放上一次node对象
        pre_node = None
        for i in range(length):
            # 初始化Node(), 值为i+1
            node = Node(i+1)
            #如果i==0
            if i == 0:
                # 设置属性self.head = node
                # 及设置链表的头结点
                self.head = node
                # 临时变量pre_node = node
                # 用于下一次循环设置链表的下一个节点对象
                pre_node = node
            else:
                # 如果i != 0
                # 设置上映节点的next属性为当前node
                pre_node.next = node
                # 将当前node赋值给pre_node
                pre_node = node

        # 循环完成之后， 这只是一个单链表，链表的最后一个节点的指向为None
        # 我们将它设置为self.head，这样就是一个循环链表了
        node.next = self.head
    
    # @property，将这个函数当做一个属性使用   
    # 因为我们要知道链表的长度，所以我们定义一个方法来获取这个链表的长度
    # 并且当做属性来使用
    @property
    def length(self):
        # 得到头结点
        node = self.head
        # 初始化长度为1， 因为已经有一个头结点了
        length = 1
        # 如果node.next 不是头结点
        while node.next != self.head:
            # length+1
            length += 1
            # 依次移动节点
            node = node.next
        # 返回length
        return length
        
    # 定义一个删除节点的方法，节点被删除，代表人被杀死
    def remove(self, node):

        # 首先需要判断删除的节点是否为头结点
        if node == self.head:
            # 找到头结点的前一个节点
            while node.next != self.head:
                node = node.next

            # 将头节点的前一个节点的next值赋值为头节点的next,将相当于删除了头节点
            node.next = self.head.next
            # 定义临时变量del_node用来存放当前还未改变的head这个节点
            del_node = self.head
            # 重新赋值新的头节点为还未改变之前的头节点的next指向的节点
            self.head = self.head.next
            # 删除这个之前的头结点
            del del_node
            return

        # 如果需要删除的节点不是头结点
        # 定义一个temp_node临时变量，赋值为头节点
        temp_node = self.head
        # 找到传入的node节点的上一个节点
        while temp_node.next != node:
            temp_node = temp_node.next

        # 然后直接将这个节点的next属性赋值为node节点的next属性，这样，
        temp_node.next = node.next
        # 再删除node
        del node
        return
        
    # 定义一个函数用来显示当前链表中的所有数据
    def show_link_list_data(self):
        # 找到头节点
        node = self.head

        #打印头结点的值
        print(f'head data is {self.head.data}')

        # 在依次打印链表中每个节点的值
        print(node.data)
        while node.next != self.head:
            node = node.next
            print(node.data)
```

到了这里为止，我们所有的准备工作都做好了，接下来我们就需要写这个算法的逻辑函数了
```python
def link_method(length=41, step=3, remain_human_number=2):
    '''
    :param length: 列表的长度，也就是人的个数
    :param step: 每次数到几就杀掉这个人
    :param remain_human_number: 剩下的人的个数
    '''
    
    # 首先初始化一个链表
    link_list = LinkList(length=length)
    # 定义计数的变量 i=1
    i = 1
    # 找到头结点
    node = link_list.head
    # 如果link_list.length大于remain_human_number， 就一直执行下去
    while link_list.length > remain_human_number:
        # 如果i == step
        if i == step:
            # 重新开始计数
            i = 0
            # 移除这个节点
            link_list.remove(node)
        # 赋值node = node.next
        node = node.next
        # i加一
        i += 1

    # 上面的循环结束之后，说明只剩下两个节点了，显示剩下节点的值。
    link_list.show_link_list_data()
```
运行结果
```python
head data is 16
16
31
```

这样，我们使用循环链表的方法也写出来了约瑟夫循环了。

其实两个方法的大致思路都是一样的，只是因为我们使用的数据结构不同，所以我们实现起来难度也略有差异而已。所以，选择一种合适的数据结构对实现一个算法是至关重要的。
