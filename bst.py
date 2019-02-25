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
