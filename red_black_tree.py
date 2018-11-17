from binarytree import Node

# This value to be assigned to color
RED = 'R'
BLACK = 'B'

class RedBlackTree():

    def __init__(self, root=None):
        self.root = root
        self.nil = RedBlackNode(-1)
        if root == None:
            self.root = self.nil
        else:
            self.root.parent = self.nil

    def __str__(self):
        if self.root == None:
            return "Nothing"
        else:
            return self.root.__str__()

    def insert(self, new_node):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if new_node.value < x.value:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y == self.nil:
            self.root = new_node
            new_node.parent = self.nil
        elif new_node.value < y.value:
            y.left = new_node
        else:
            y.right = new_node
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = RED
        self.insert_fixup(new_node)

    def insert_fixup(self, node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left:
                y = node.parent.parent.right
                if y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.right_rotate(node.parent.parent)
            else:
                y = node.parent.parent.left
                if y.color == RED:
                    node.parent.color = BLACK
                    y.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.left_rotate(node.parent.parent)

        self.root.color = BLACK

    def delete(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.nil:
            x = node.right
            self.transplant(node, node.left)
        else:
            y = self.minimum(node.right)
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self.transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, node):
        while node != self.root and node.color == BLACK:
            if node == node.parent.left:
                w = node.parent.left
                if w.color == RED:
                    w.color = BLACK
                    node.parent.color = RED
                    self.left_rotate(node.parent)
                    w = node.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    node = node.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BALCK
                        w.color = RED
                        self.right_rotate(node.parent)
                        w = node.parent.right
                    w.color = node.parent.color
                    node.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(node.parent)
                    node = self.root
            else:
                w = node.parent.right
                if w.color == RED:
                    w.color = BLACK
                    node.parent.color = RED
                    self.right_rotate(node.parent)
                    w = node.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    node = node.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BALCK
                        w.color = RED
                        self.left_rotate(node.parent)
                        w = node.parent.left
                    w.color = node.parent.color
                    node.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = BLACK

    def search(self, value):
        x = self.root

        while x != self.nil:
            if x.value == value:
                break
            elif x.value < value:
                x = x.right
            else:
                x = x.left
        return x

    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def maximum(self, x):
        while x.right != self.nil:
            x = x.right
        return x

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
            y.parent = self.nil
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
            y.parent = self.nil
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
            v.parent = self.nil
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


class RedBlackNode(Node):

    def __init__(self, value, color='B', parent=None):
        """
        :param value: Key of this node
        :type value: number (float, integer .. etc)
        :param color: Color of this node(maybe B:black or R:red)
        :type color: string
        :param parent: Parent node of this node
        :type parent: Node
        """
        super().__init__(value)
        self.color = color
        self.parent = parent

    def __str__(self):
        """Overring method of ''__str__'' of Node class"""
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def __setattr__(self, attr, obj):
        """Modified version of ``__setattr__`` with extra sanity checking.

        Class attributes **left** , **right** and **parent** are validated.

        :param attr: Name of the class attribute.
        :type attr: str | unicode
        :param obj: Object to set.
        :type obj: object
        :raise binarytree.exceptions.NodeTypeError: If left , right child or
            parent is not an instance of :class:`binarytree.Node`.
        """

        if attr == 'left':
            if obj is not None and not isinstance(obj, Node):
                raise NodeTypeError(
                    'left child must be a Node instance')
        elif attr == 'right':
            if obj is not None and not isinstance(obj, Node):
                raise NodeTypeError(
                    'right child must be a Node instance')
        elif attr == 'parent':
            if obj is not None and not isinstance(obj, Node):
                raise NodeTypeError(
                    'parent must be a Node instance')

        object.__setattr__(self, attr, obj)

def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    """This method is overrided to change data type of value from number
    to string

    Recursively walk down the binary tree and build a pretty-print string.

    In each recursive call, a "box" of characters visually representing the
    current (sub)tree is constructed line by line. Each line is padded with
    whitespaces to ensure all lines in the box have the same length. Then the
    box, its width, and start-end positions of its root node value repr string
    (required for drawing branches) are sent up to the parent call. The parent
    call then combines its left and right sub-boxes to build a larger box etc.

    :param root: Root node of the binary tree.
    :type root: binarytree.Node | None
    :param curr_index: Level-order_ index of the current node (root node is 0).
    :type curr_index: int
    :param index: If set to True, include the level-order_ node indexes using
        the following format: ``{index}{delimiter}{value}`` (default: False).
    :type index: bool
    :param delimiter: Delimiter character between the node index and the node
        value (default: '-').
    :type delimiter:
    :return: Box of characters visually representing the current subtree, width
        of the box, and start-end positions of the repr string of the new root
        node value.
    :rtype: ([str], int, int, int)

    .. _Level-order:
        https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
    """
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []

    rootValue = root.color + str(root.value)

    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, rootValue)
    else:
        #node_repr = str(root.value)
        node_repr = rootValue

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        _build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end

def main():
    """Test Red black tree

    In each iteration, you can input mode
    The modes are as follows:
    1. insert node
    2. delete node
    3. search node
    4. exit

    """
    tree = RedBlackTree()

    print('---Test of red black tree---')
    while(True):
        mode = int(input('Select mode : (1. insert, 2. delete, 3. search, 4. exit): '))
        print('mode : %d' % mode)
        if mode == 1:
            key = int(input("Enter the key: "))
            node = RedBlackNode(key)
            tree.insert(node)
        elif mode == 2:
            key = int(input("Enter the key: "))
            node = tree.search(key)
            tree.delete(node)
        elif mode == 3:
            key = int(input("Enter the key: "))
            node = tree.search(key)
            print(node)
        elif exit:
            print('exit')
            break
        print('----tree----')
        print(tree)

if __name__ == '__main__':
    main()
