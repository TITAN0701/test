package texting;

import java.util.*;
public class test3 {
	//3. 皚矪瞶
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] a = {0,1,2,3,4,5,6,7,8,9};
		int oddsum =0;
		int evensum =0;
		
		oddsum = evensum= a[0];
		for(int i=0;i<a.length;i++) {
			if(a[i]%2==0) {
				if(a[i]>evensum) {
					evensum = a[i];
				}else if(a[i]>oddsum) {
					oddsum = a[i];
				}
				//皚い案计
				System.out.print("案计皚:");
				System.out.println(a[i]+" ");
			}else if(a[i]%2==1) {
				if(a[i]>oddsum) {
					oddsum = a[i];
				}
				System.out.print("计皚:");
				System.out.println(a[i]+" ");
			}
		}
		
		for(int i = 0 ; i <= a.length ; i++) {
			if(i % 2 == 1) {
				oddsum += i;
			}else if(i % 2 == 0){
				evensum += i;
			}
		}
		System.out.println("计羆㎝ :"+oddsum);
		System.out.println("案计羆㎝ :"+evensum);
		System.out.println("计-案计 :"+ (oddsum-evensum));
		
		
		//System.out.println("羆㎝:"+sum);
		
	}

}
