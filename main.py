# -*- coding: utf-8 -*-
import os
from threading import Thread

from bst import *
from rbt import *
from util import *

allPermList = ["15K", "30K", "45K", "60K", "75K", "90K", "105K", "120K", "135K", "150K"]
types = ["Perm", "Sorted"]


def main():
    sys.setrecursionlimit(15000)

    exitVar = False
    listType = ""
    while not exitVar:
        print("1. Binary Search Tree")
        print("2. Red Black Tree")
        print("3. RUN ALL! (Run All Trees With all Lists)")
        while True:
            try:
                execType = int(input("Which routine to run? (1-3)"))
                if 3 >= execType > 0:
                    break
            except:
                print("Please type an integer (1-3)")

        if execType != 3:
            print("1. Permutations")
            print("2. Sorted")
            while True:
                try:
                    listsToUse = int(input("Which list to use (1-2)"))
                    if listsToUse == 1:
                        listType = 'Perm'
                    elif listsToUse == 2:
                        listType = 'Sorted'
                    if 2 >= listsToUse > 0:
                        break
                except:
                    print("Please type an integer (1-2)")

            print("1. 15K")
            print("2. 30K")
            print("3. 45K")
            print("4. 60K")
            print("5. 75K")
            print("6. 90K")
            print("7. 105K")
            print("8. 120K")
            print("9. 135")
            print("10. 150K")
            print("11. RUN ALL")
            while True:
                try:
                    length = int(input("Which size to run? (1-11)"))
                    if 11 >= length > 0:
                        break
                except:
                    print("Please type an integer (1-11)")
            while True:
                try:
                    search = str(input("What word to search?"))
                    if search.isalpha():
                        break
                except:
                    print("Enter a valid string")

            if execType == 1:
                if listsToUse == 1 or 2:
                    sys.stdout.flush()
                    if (length > 10):
                        for x in range(len(allPermList)):
                            handle_thread(binary_search, allPermList[x], listType, search)
                    else:
                        handle_thread(binary_search, allPermList[length - 1], listType, search)
            elif execType == 2:
                if listsToUse == 1 or 2:
                    if (length > 10):
                        for x in range(len(allPermList)):
                            handle_thread(redblack_search, allPermList[x], listType, search)
                    else:
                        handle_thread(redblack_search, allPermList[length - 1], listType, search)

            print("Exit? \n")
            while True:
                try:
                    exitInput = int(input("1. Yes \n2. No\n"))
                    if exitInput == 1:
                        exitVar = True
                        break
                    elif exitInput == 2:
                        break
                except:
                    print("Please type and integer (1,2)")
        elif execType == 3:
            while True:
                try:
                    search = str(input("What word to search?"))
                    if search.isalpha():
                        break
                except:
                    print("Enter a valid string")

            for x in range(len(types)):
                for i in range(len(allPermList)):
                    handle_thread(binary_search, allPermList[i], types[x], search)
            for x in range(len(types)):
                for i in range(len(allPermList)):
                    handle_thread(redblack_search, allPermList[i], types[x], search)


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


def redblack_search(length, listType, search_term):
    path = ""
    if (listType == "Perm"):
        path = '/permuted/perm'
    elif (listType == "Sorted"):
        path = 'sorted/sorted'

    input_file = open('lists/' + path + length + '.txt').readlines()
    for x in range(0, len(input_file)):
        input_file[x] = input_file[x].strip('\n')

    start = time.time()
    search = RBTree()
    for i in range(0, len(input_file)):
        search.insert_key(input_file[i])
    end = time.time()
    outTime = (end - start)
    print()
    print("Building Tree Took: " + str(outTime) + " Seconds")
    start1 = time.time()
    search.search(search_term)
    end1 = time.time()
    outTime1 = (end1 - start1)
    print("Finding Value Took: " + str(outTime1) + " Seconds")

    if not os.path.exists('output'):
        os.mkdir('output')
    with open("output/outfile-RBT-" + listType + length + ".txt", "a+") as outfile:
        outfile.write("Type: Binary Search Tree " + listType + "\n")
        outfile.write("Word List Size: " + length + "\n")
        outfile.write("Building Tree Time: \n")
        outfile.write(str(outTime) + "\n")
        outfile.write("Seconds \n")
        outfile.write("Search Time: \n")
        outfile.write(str(outTime1) + "\n")
        outfile.write("Seconds \n")
        outfile.write("--------------------" + "\n")
        outfile.close()
    print("\n")


if __name__ == '__main__':
    main()
