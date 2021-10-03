// 最大連續1的個數 
//Input: nums = [1,1,0,1,1,1]
//Output: 3


class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
         if (nums.length == 0){ // base case,陣列為空時返回0
           return 0;  
         } 
		 
		 
        int count = 0;  // 計數
        int result = 0;  // 連續個數最多的個數
        for (int i = 0; i < nums.length; i++){
            if (nums[i] == 1){ // 遇到1則連續的個數加一
              count++;  
            }else{  // 遇到0，則先保留前面已經計算過的連續個數的最大值並使計數歸零進行下一輪的計算
                result = Math.max(count,result);  // 儲存已經計算過的連續個數的最大值
                count = 0;
            } 
        }
        return Math.max(count,result);
    }
    
}