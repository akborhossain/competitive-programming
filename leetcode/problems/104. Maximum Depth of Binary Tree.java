/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {

        if(root==null){
            return 0;
        }
        int leftdepth,rightdepth;
        leftdepth=maxDepth(root.left);
        rightdepth=maxDepth(root.right);
        if(leftdepth>rightdepth){
            return leftdepth+1;
        }else{
            return rightdepth+1;
        }
        
    }
}