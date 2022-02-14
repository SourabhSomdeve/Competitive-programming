
## Implementation of Binary Search Tree using DFS


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
    def addChild(self,data):
        if data == self.data:
            return

        if data < self.data:

            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:

            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)



    def search(self, val):

        if val == self.data:
            return True
        
        if val < self.data:

            if self.left:
                return self.left.search(val)

            else:
                return False

        if val > self.data:

            if self.right:
                return self.right.search(val)

            else:
                return False

    def inOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.inOrderTraversal()
            # print(elements)
        
        elements.append(self.data)
        # print(elements)

        if self.right:
            elements +=  self.right.inOrderTraversal()
            # print(elements)

        return elements

    def preOrderTraversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.preOrderTraversal()

        if self.right:
            elements +=  self.right.preOrderTraversal()

        return elements

    def postOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.postOrderTraversal()

        if self.right:
            elements +=  self.right.postOrderTraversal()

        elements.append(self.data)

        return elements

    def findMin(self):

        if self.left is None:
            return self.data

        return self.left.findMin()

    def findMax(self):

        if self.right is None:
            return self.data
        
        return self.right.findMax()

        

    def calcSum(self):

        # total_sum = 0
        # total_sum += self.data

        if self.left:
            left_sum= self.left.calcSum()
        else:
            left_sum = 0

        if self.right:
            right_sum = self.right.calcSum()
        else:
            right_sum = 0
            
        return self.data + left_sum + right_sum

def buildTree(elements):
    
    root  = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.addChild(elements[i])

    return root

if __name__ == '__main__':
    # numbers = [15,12,7,14,27,20,23,88 ]
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    # numbers = [5,1,6,4,2]

    numbers_tree = buildTree(numbers)

    # print("The Number is present on the list ?",numbers_tree.search(10))

    # print(f"Printing the In-Order Traversal and it gives sorted list: {numbers_tree.inOrderTraversal()}")

    # print(f"Printing the Pre-Order Traversal: {numbers_tree.preOrderTraversal()}")

    # print(f"Printing the Post-Order Traversal: {numbers_tree.postOrderTraversal()}")

    # print(f"The minimum element in the binary search Tree:{numbers_tree.findMin()}")

    # print(f"The maximum element in the binary search Tree:{numbers_tree.findMax()}")

    print(f"The sum of element in the binary search Tree:{numbers_tree.calcSum()}")

    # print(numbers_tree)