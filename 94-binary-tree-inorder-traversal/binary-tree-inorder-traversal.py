class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result (in-order traversal)
        res = []
        
        # Initialize an empty stack for iterative traversal
        stack = []
        
        # Loop until either the current node is not None or the stack is not empty
        while root or stack:
            # Traverse to the leftmost node and push each encountered node onto the stack
            while root:
                stack.append(root)
                root = root.left

            # Pop the last node from the stack (most recently left-visited node)
            root = stack.pop()
            
            # Append the value of the popped node to the result list
            res.append(root.val)
            
            # Move to the right subtree to continue the in-order traversal
            root = root.right
        
        # Return the final result list
        return res