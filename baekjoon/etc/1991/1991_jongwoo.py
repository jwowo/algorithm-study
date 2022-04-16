"""class를 이용한 풀이방법"""
import sys

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def preorder(node):
    print(node.key, end='')
    if node.left != ".":
        preorder(tree[node.left])
    if node.right != ".":
        preorder(tree[node.right])

def inorder(node):
    if node.left != ".":
        inorder(tree[node.left])
    print(node.key, end='') 
    if node.right != ".":
        inorder(tree[node.right])

def postorder(node):
    if node.left != ".":
        postorder(tree[node.left])
    if node.right != ".":
        postorder(tree[node.right])
    print(node.key, end='')
    

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    tree = {}

    for _ in range(n):
        root, left, right = sys.stdin.readline().split()

        tree[root] = Node(key=root, left=left, right=right)

    preorder(tree["A"])
    print()
    inorder(tree["A"])
    print()
    postorder(tree["A"])



""" 딕셔너리 인덱스를 이용한 풀이방법
import sys

n = int(sys.stdin.readline())
tree = {}

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != ".":
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')


for _ in range(n):
    root, left, right = sys.stdin.readline().split()

    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
"""