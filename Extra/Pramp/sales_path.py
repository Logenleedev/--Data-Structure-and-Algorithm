def traversal(root, sum, result):
    if root.left == None and root.right == None:
        result.append(sum)
        return
        
    if root.left:
        sum += root.left.val
        
        traversal(root, sum, result)

        sum -= root.left.val

    if root.right:
        sum += root.right.val
        traversal(root, sum, result)
        sum -= root.right.val



def get_cheapest_cost(rootNode):
    if rootNode == None:
        return

    sum = rootNode.val
    result = []
    traversal(rootNode, sum, result)
    return min(result)


