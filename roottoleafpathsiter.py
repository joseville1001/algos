# Problem idea by u/kbielefe in this reddit post:
# https://www.reddit.com/r/AskProgramming/comments/q8glj6/what_is_it_like_to_work_as_an_algorithm_developer/hgqjvg4/

# Solution:

# `path` reuse:
# Many root to leaf paths differ by only a few nodes (the trailing nodes),
# so a good optimization is to reuse `path` as much as possible, which this solution does.
class TreeNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

def root_to_leaf_paths_path_iter(root):
    def dfs(node):
        path.append(node.val)
        if not node.children:
            # node is a leaf
            yield path
        else:
            for child in node.children:
                if child:
                    yield from dfs(child)
        path.pop()
        
    path = []
    yield from dfs(root)

def root_to_leaf_paths_node_iter(root):
    for path in root_to_leaf_paths_path_iter(root):
        yield from path

# Notes:
# - Can be easily modified to yield `node`'s instead of `node.val`'s.
# - Possible speed improvement: do iterative dfs instead of recursive dfs.
# - Can be lazier:
#   - Currently, the complete root to leaf path is computed before we yield any of its nodes.
#   - If we wanted to be lazier, we could yield nodes from a partial path and lazily complete the path as we are asked to yield more nodes.

# "Testing" on a small tree

# The tree:
# 
# https://bit.ly/3FQcjYU
#
# 1
# 45              700
# 40        75    300
# 10 100 20 12 60 200
#                 80

leaf10 = TreeNode(10)
leaf100 = TreeNode(100)
leaf20 = TreeNode(20)
node40 = TreeNode(40, [leaf10, leaf100, leaf20])

leaf12 = TreeNode(12)
leaf60 = TreeNode(60)
node75 = TreeNode(75, [leaf12, leaf60])

node45 = TreeNode(45, [node40, node75])

leaf80 = TreeNode(80)
node200 = TreeNode(200, [leaf80])
node300 = TreeNode(300, [node200])
node700 = TreeNode(700, [node300])

root = TreeNode(1, [node45, node700])

# "Test"

# print each root to leaf path
for path in root_to_leaf_paths_path_iter(root):
    print(path)

# i.e. prints:
# [1, 45, 40, 10]
# [1, 45, 40, 100]
# [1, 45, 40, 20]
# [1, 45, 75, 12]
# [1, 45, 75, 60]
# [1, 700, 300, 200, 80]

# print each node value in each root to leaf path
for nodeval in root_to_leaf_paths_node_iter(root):
    print(nodeval)

# i.e. prints:
# 1
# 45
# 40
# 10
# 1
# 45
# 40
# 100
# 1
# 45
# 40
# 20
# 1
# 45
# 75
# 12
# 1
# 45
# 75
# 60
# 1
# 700
# 300
# 200
# 80
