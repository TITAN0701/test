//Input: arr = [1,0,2,3,0,4,5,0]
//Output: [1,0,0,2,3,0,0,4]

class so{
	public void duplicateZeros2(int[] arr) {
    	int n = arr.length, index = 0;
    	int[] copy = arr.clone();
    	
		for (int num : copy) {
        	// 輸入陣列的長度超過時則中斷
			if (index >= n) {
            	break;
        	}
			
			//陣列如小於0+1和等於0時，重複給予一個0
        	if (index+1 < n && num == 0) {
            	arr[index++] = 0;
            	arr[index++] = 0;
        	} else {
            	arr[index++] = num;
        	}
    	}
	}		
}
