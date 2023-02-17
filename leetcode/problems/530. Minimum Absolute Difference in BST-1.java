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
    int result = Integer.MAX_VALUE;
    Integer prev = null;
    public int getMinimumDifference(TreeNode root) {
        
        dfs(root);
        return result;
    }
    private void dfs(TreeNode node){

        if(node==null){
            return ;

        }
        dfs(node.left);
        if (prev!=null){
            result=Math.min(result, node.val - prev);
        }
        prev=node.val;
        dfs(node.right);
        
    }
}