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
    int res=Integer.MAX_VALUE;
    TreeNode prev=null;
    public int minDiffInBST(TreeNode root) {
       dfs(root);
        return res;
        
    }
    private void dfs(TreeNode node){
        if(node==null){
            return ;
        }
        dfs(node.left);
        if(prev!=null){
            res=Math.min(res,node.val-prev.val);
        }
        prev=node;
        dfs(node.right);
    }
}