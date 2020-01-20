from collections import defaultdict

# TODO
# This file is used to implement the data structure of the tree

class Tree(defaultdict):
    def __call__(self):
        return Tree(self)

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.default_factory = self