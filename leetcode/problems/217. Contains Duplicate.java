class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set seen =new HashSet<>();
        for(int x :nums){
            if(seen.contains(x)){
                return true;
            }
            seen.add(x);
        }
        return false;
        
    }
}