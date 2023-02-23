class Solution {
    public Node connect(Node root) {
        Node cur=root, nxt;
        if (root!=null){
            nxt= root.left;
        }else 
             nxt= null;
        while(cur!=null && nxt!=null){
            cur.left.next=cur.right;
            if(cur.next!=null){
                cur.right.next=cur.next.left;
            }
            cur=cur.next;
            if(cur==null){
                cur=nxt;
                if (cur!=null)
                    nxt=cur.left;
            }
        }
        return root;
    }
}
Console
