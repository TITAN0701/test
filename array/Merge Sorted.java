
// Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
//Output: [1,2,2,3,5,6]
 

public class test1_Merge {

	/*
	 * public void me(int[] nums1,int m,int[] nums2,int n) { int[] nums3=new
	 * int[m+n];
	 * 
	 * int i = 0,j=0,k; for(k=0;k<m+n && i<m && j<n;k++) { if(nums1[i]>nums2[j]){
	 * nums3[k] = nums2[k]; j++; System.out.println(j); }else{ nums3[k]=nums1[i];
	 * i++; System.out.println(i); } }
	 * 
	 * 
	 * if(i==m) { for(int q=k;q<m+n;q++) { nums3[q]=nums2[j]; j++; } }else if(j==n)
	 * { for(int q=0;q<m+n;q++) { nums3[q]=nums1[i]; i++; } }
	 * 
	 * for(int q=0;q<m+n;q++) { nums1[q]=nums3[q]; System.out.print(nums1[q]); }
	 * 
	 * 
	 * }
	 * 
	 * 
	 * public static void main(String[] args) { // TODO Auto-generated method stub
	 * test1_Merge a = new test1_Merge(); int[] b= {1,2,3,0,0,0}; int[] c= {2,5,6};
	 * a.me(b, 3, c, 3);
	 * 
	 * }
	 */
	public void me(int[] nums1,int m,int[] nums2,int n) {
		int index= m+n-1;
		m--;
		n--;
		while(m>=0 && n>=0) {
			if(nums1[m]>=nums2[n]) {
				nums1[index]=nums1[m];
				m--;
			}else {
				nums1[index]=nums2[n];
				n--;
			}
			index--;
		}
		
		while(m>=0) {
			nums1[index]=nums1[m];
			m--;
			index--;
		}
		while(n>=0) {
			nums1[index]=nums2[n];
			n--;
			index--;
		}
		
	}
	public static void main(String[] args) {
		test1_Merge a = new test1_Merge();
		int[] b= {1,2,3,0,0,0}; 
		int[] c= {2,5,6};
		a.me(b, 3, c, 3);
		System.out.println();
	}
	

}
