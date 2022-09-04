## Tree Traversal Algorithm Example Code
## Input => 트리의 크기, (node, left, right) 입력, leaf node의 경우 자식 node들을 None으로 입력

n = int(input())        # 트리의 총 node 수 입력
tree = {}

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node):         # Preorder Traversal(전위 순회) : 노드 -> 왼쪽 자식 -> 오른쪽 자식 순으로 순회
    print(node.data, end=" ")
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

def in_order(node):          # Inorder Traversal(중위 순회) : 왼쪽 자식 -> 노드 -> 오른쪽 자식 순으로 순회
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node != None:
        in_order(tree[node.right_node])

def post_order(node):        # Postorder Traversal(후위 순회) : 왼쪽 자식 -> 오른쪽 자식 -> 노드 순으로 순회
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=" ")

for _ in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])