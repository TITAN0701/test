package texting;

import java.util.*;
public class test6 {
	public static void main(String[]	args) {
		int[]	nums={6,7,8,9,4};
		System.out.print("��X��l�}�Cnums: ["+nums[0]+nums[1]+nums[2]+nums[3]+nums[4]+"]");
		Scanner c=new Scanner(System.in);
		System.out.print("\t�п�J�Ʀr1�A�������}�C��m:");
		int r = c.nextInt();
		if(r==0) {
			System.out.print("�}�C��m:"+nums[0]);
		}else if(r==1) {
			System.out.print("��Jtarget:"+(nums[3]+nums[4]));
		}
		
		//���L��X�C�}�C����
		for(int i=3;i<4;i++) {
			if(r==0) {
				System.out.print("�}�C��m"+nums[3]);
			}else if(r==1) {
				System.out.print("\n��X:["+i+","+(i+1)+"]");
				System.out.print("��������!!");
			}
			
		}
	}
}
