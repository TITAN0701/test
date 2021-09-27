package texting;

import java.util.*;
public class test6 {
	public static void main(String[]	args) {
		int[]	nums={6,7,8,9,4};
		System.out.print("輸出原始陣列nums: ["+nums[0]+nums[1]+nums[2]+nums[3]+nums[4]+"]");
		Scanner c=new Scanner(System.in);
		System.out.print("\t請輸入數字1，未知的陣列位置:");
		int r = c.nextInt();
		if(r==0) {
			System.out.print("陣列位置:"+nums[0]);
		}else if(r==1) {
			System.out.print("輸入target:"+(nums[3]+nums[4]));
		}
		
		//打印輸出列陣列索引
		for(int i=3;i<4;i++) {
			if(r==0) {
				System.out.print("陣列位置"+nums[3]);
			}else if(r==1) {
				System.out.print("\n輸出:["+i+","+(i+1)+"]");
				System.out.print("此為答案!!");
			}
			
		}
	}
}
