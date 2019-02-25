# -*- coding: utf-8 -*-
import os
from threading import Thread

from bst import *
from util import *


def main():
    handle_thread(binary_search, '15K', 'Perm', 'BIMORPHEMIC')


def handle_thread(search_function, length, list_type, search):
    util.go = True

    spinnerThread = Thread(target=util.spinning_cursor)
    spinnerThread.start()
    threadAlgo = Thread(target=search_function,
                        args=(length, list_type, search,))
    threadAlgo.start()
    threadAlgo.join()

    util.go = False
    spinnerThread.join()


def binary_search(length, listType, search_term):
    path = ""
    if (listType == "Perm"):
        path = '/permuted/perm'
    elif (listType == "Sorted"):
        path = 'sorted/sorted'

    input_file = open('lists/' + path + length + '.txt').readlines()
    for x in range(0, len(input_file)):
        input_file[x] = input_file[x].strip('\n')

    start = time.time()
    search = Node(input_file[0])
    for i in range(0, len(input_file)):
        search.insert_node(input_file[i])
    end = time.time()
    outTime = (end - start)
    print()
    print("Building Tree Took: " + str(outTime) + " Seconds")
    start1 = time.time()
    search.returnVal(search_term)
    end1 = time.time()
    outTime1 = (end1 - start1)
    print("Finding Value Took: " + str(outTime1) + " Seconds")

    if not os.path.exists('output'):
        os.mkdir('output')
    with open("output/outfile-BST-" + listType + length + ".txt", "a+") as outfile:
        outfile.write("Type: Binary Search Tree " + listType + "\n")
        outfile.write("Word List Size: " + length + "\n")
        outfile.write("Building Tree Time: \n")
        outfile.write(str(outTime) + "\n")
        outfile.write("Seconds \n")
        outfile.write("Search Time: \n")
        outfile.write(str(outTime1) + "\n")
        outfile.write("Seconds \n")
        outfile.write("--------------------" + "\n")
        search.outputTree(outfile)
        outfile.close()
    print("\n")


if __name__ == '__main__':
    main()
