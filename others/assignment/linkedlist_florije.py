# -*- coding: utf-8 -*-
__author__ = 'florije'

"""
Creates and returns a linked list containing all of the elements
of the Python-style list parameter.  A useful shortcut for testing.
"""


def createList(plist):
    linkedList = None
    # goes backwards, adding each element to the beginning
    # of the list.
    for index in range(len(plist) - 1, -1, -1):
        linkedList = insertValueHead(linkedList, plist[index])
    return linkedList


'''
Create an empty linked list
'''


def emptyList():
    return None  # absence of a value -- nothing


'''
Creates a string representation of the values in the linked list such as:
5->6->9->14.
'''


def listString(linkedList):
    ptr = linkedList
    str1 = ''
    while ptr != None:
        str1 += str(ptr['data'])
        ptr = ptr['next']
        if ptr != None:
            str1 += "->"
    str1 = str1
    return str1


'''
Inserts a new node containing the value "value" to the head of the list.
LinkedList is the head of the list to be added to
Value is the data to be stored in the node
'''


def insertValueHead(linkedList, value):
    newnode = {}
    newnode["data"] = value
    # set the next pointer of this new node to the head of the list, linkedList
    #newnode is now the head of the list
    newnode["next"] = linkedList
    return newnode


"""
Helper method: returns a reference to node n in a list counting from zero).
Parameters: the list and an index n
If there is no node n, returns None.
"""


def nthNode(linkedList, n):
    ptr = linkedList
    count = 0
    if n < 0:
        return None
    while ptr is not None and count < n:
        ptr = ptr['next']
        count += 1
    return ptr


def insertNode(list, index, value):
    '''
    insert a new node(index to insert and the value) to the list(dict)
    :param list: {'data': 1, 'next': {'data': 2, 'next': {'data': 3, 'next': {'data': 4, 'next': {'data': 5, 'next': {'data': 6, 'next': None}}}}}}
    :param index: where will to insert the new node
    :param value:
    :return:
    '''
    # This function is a general function for inserting values in a linked list.  I have provided a
    #skeleton, it is your job to complete it.

    #case 1:  Adding to the head of the list -- index == 0
    #Create a new node and pass back the new node, which is the new head of the list.

    #case 2:  Adding elsewhere in the list
    #use nthNode() to find the node before the position to insert (this will be at index - 1)
    #if this function returns None, then the index is invalid -- print an error message
    #otherwise, add the node

    if index == 0:
        new_node = {"data": value, "next": list}
        return new_node
    else:
        target_node = nthNode(list, index - 1)
        if target_node:
            next_node = target_node['next']
            new_node = {"data": value, "next": next_node}
            target_node['next'] = new_node
            return list
        else:
            raise Exception('The index is invalid!')


def switch(list, index):
    '''

    :param list:
    :param index:
    :return:
    '''
    target_node = nthNode(list, index)
    if index < 0:
        raise Exception('The index is invalid!')
    elif index == 0:
        return list
    if target_node:
        head_node = nthNode(list, 0)  # head节点

        tmp_head_node = {"data": head_node['data'], "next": None}
        tmp_target_node = {"data": target_node['data'], "next": None}

        target_pre_node = nthNode(list, index - 1)
        target_next_node = target_node['next']
        tmp_head_node['next'] = target_next_node
        target_pre_node['next'] = tmp_head_node
        tmp_target_node['next'] = head_node['next']

        return tmp_target_node
    else:
        raise Exception('The index is invalid!')


def sumEvens(linkedList):
    sum_evens = 0
    while linkedList != None:
        if linkedList['data'] % 2 == 0:
            sum_evens += linkedList['data']
        linkedList = linkedList['next']
    return sum_evens


def testInsert():
    # test code to ensure that insertNode is working correctly.
    myList = createList([1, 2, 3, 4, 5, 6])
    print "The initial list", listString(myList)
    #insert 0 at the head
    myList = insertNode(myList, 0, 0)
    print "Inserted 0 at the start of list: ", listString(myList)
    #insert 7 at the end
    myList = insertNode(myList, 7, 7)
    print "Inserted 7 at the end of list: ", listString(myList)
    myList = insertNode(myList, 3, 2.2)
    print "Inserted 2.2 in the 3rd position ", listString(myList)
    myList = insertNode(myList, 26, 12)  #should generate an error


def testSumEvens():
    myList = createList([14, 21, 29, 2, 16, 49, -26])
    print "The sum of the even numbers in the first list is ", sumEvens(myList)
    myList = createList([])
    print "The sum of the even numbers in an empty list is ", sumEvens(myList)
    myList = createList([5, 15, 25])
    print "The sum of the even numbers in the final list is ", sumEvens(myList)


def testSwitch():
    # test code to ensure that switch() is working correctly.
    myList = createList([10, 20, 30, 40, 50, 60])
    print "The initial list", listString(myList)
    myList = switch(myList, 2)
    print "Switching the 1 and the 2.  Resulting list is ", listString(myList)
    myList = switch(myList, 3)
    print "Switching the 4 and the 5.  Resuling list is ", listString(myList)
    myList = switch(myList, 5)
    myList = switch(myList, 29)  #should result in an error


def main():
    '''
    The following code is here for demonstration purposes, to help
    you to understand how to create a list.  First we create an empty list
    and add 2 values using teh insertValueHead() function.  The resulting list
    will be a list with values 20 and then 9.
    You should replace the following code with the code to start the execution
    of your program (that is, call each of the test functions).
    '''
    # linkedList = emptyList()
    # print "Inserting a new node with value 9"
    # linkedList = insertValueHead(linkedList, 9)
    # print "The list contains the following values", listString(linkedList)
    # print "Inserting a new node with value 20"
    # linkedList = insertValueHead(linkedList, 20)
    # print "The list contains the following values", listString(linkedList)

    # testInsert()
    # testSwitch()
    testSumEvens()


main()