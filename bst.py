class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # Function inserts data & creates nodes
    def insert_node(self, val):
        if self.val:
            # If val is less than stored val of current node
            if val < self.val:
                # And node to the left is null
                if self.left is None:
                    # Insert Node to the left with value
                    self.left = Node(val)
                else:
                    # Else Insert node into the node to the left
                    self.left.insert_node(val)
            # If val is > stored val
            elif val > self.val:
                # And node to the right is null
                if self.right is None:
                    # Insert node to the right
                    self.right = Node(val)
                else:
                    # Else insert node into the right node that exists.
                    self.right.insert_node(val)
        else:
            self.val = val

    # Function returns a requested value in the tree structure.
    def returnVal(self, search):
        # Search left node if search < val
        if search < self.val:
            # If null(None) return negative.
            if self.left is None:
                print(" Searched Term Not Found.")
                return str(search)
            # Else check search again.
            return self.left.returnVal(search)
        # Check right node if search > val
        elif search > self.val:
            # If left is Null(None) return negative.
            if self.right is None:
                print(" Searched Term Not Found.")
                return str(search)
            # Else check search again
            return self.right.returnVal(search)
        else:
            # Else val found.
            print(str(self.val) + " Is Found")

    # Prints entire tree to console (With a small change) or file.
    def outputTree(self, file):
        if self.left:
            self.left.outputTree(file)
        #print(self.val)
        file.write(self.val + "\n")
        if self.right:
            self.right.outputTree(file)
