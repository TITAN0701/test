// Find Numbers with Even Number of Digits
//Input: nums = [12,345,2,6,7896]
//Output: 2


class Solution {
    public int findNumbers(int[] nums) {
        int count=0;
        for(int i=0;i<nums.length;i++){
            if(String.valueOf(nums[i]).length()%2 == 0){
                count++;
            }
        }
        return count;
    }
}