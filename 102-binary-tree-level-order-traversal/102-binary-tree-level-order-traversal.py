# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue,result,temp, level  = [root], [] , [], 0
        
        while len(queue) > 0:
            result.append([])
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                
                if node:
                    result[level].append(node.val)
                    
            
                # add the left child to queue
                if node.left:
                    queue.append(node.left)

                # add the right child to queue
                if node.right:
                    queue.append(node.right)
                
            level += 1
        print(result)
        return result
                
            
            
        