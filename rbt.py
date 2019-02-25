class RBNode(object):
    def __init__(self, val):
        self._val = val
        self._red = False
        self._left = None
        self._right = None
        self._parent = None

    val = property(fget=lambda self: self._val)
    # Not red black, just a red and ... not red, but that's basically the same?
    red = property(fget=lambda self: self._red)
    left = property(fget=lambda self: self._left)
    right = property(fget=lambda self: self._right)
    parent = property(fget=lambda self: self._parent)


class RBTree(object):
    def __init__(self, create_node=RBNode):
        self._nil = create_node(val=None)
        self._root = self.nil
        self._create_node = create_node

    root = property(fget=lambda self: self._root)
    nil = property(fget=lambda self: self._nil)

    def search(self, key, x=None):
        if None == x:
            x = self.root
        while x != self.nil and key != x.val:
            if key < x.val:
                x = x.left
            else:
                x = x.right
        return x

    def insert_key(self, val):
        self.insert_node(self._create_node(val=val))

    def insert_node(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.val < x.val:
                x = x.left
            else:
                x = x.right
        z._parent = y
        if y == self.nil:
            self._root = z
        elif z.val < y.val:
            y._left = z
        else:
            y._right = z
        z._left = self.nil
        z._right = self.nil
        z._red = True
        self._insert_fix(z)

    def _insert_fix(self, z):
        while z.parent.red:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.red:
                    z.parent._red = False
                    y._red = False
                    z.parent.parent._red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)
                    z.parent._red = False
                    z.parent.parent._red = True
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.red:
                    z.parent._red = False
                    y._red = False
                    z.parent.parent._red = True
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)
                    z.parent._red = False
                    z.parent.parent._red = True
                    self._left_rotate(z.parent.parent)
        self.root._red = False

    def _left_rotate(self, x):
        y = x.right
        x._right = y.left
        if y.left != self.nil:
            y.left._parent = x
        y._parent = x.parent
        if x.parent == self.nil:
            self._root = y
        elif x == x.parent.left:
            x.parent._left = y
        else:
            x.parent._right = y
        y._left = x
        x._parent = y

    def _right_rotate(self, y):
        x = y.left
        y._left = x.right
        if x.right != self.nil:
            x.right._parent = y
        x._parent = y.parent
        if y.parent == self.nil:
            self._root = x
        elif y == y.parent.right:
            y.parent._right = x
        else:
            y.parent._left = x
        x._right = y
        y._parent = x
