package texting;

import java.util.*;
public class test3 {
	//3. �}�C�B�z
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
				//�C�X�}�C�������ƭ�
				System.out.print("���ư}�C:");
				System.out.println(a[i]+" ");
			}else if(a[i]%2==1) {
				if(a[i]>oddsum) {
					oddsum = a[i];
				}
				System.out.print("�_�ư}�C:");
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
		System.out.println("�_���`�M :"+oddsum);
		System.out.println("�����`�M :"+evensum);
		System.out.println("�_��-���ƭ� :"+ (oddsum-evensum));
		
		
		//System.out.println("�`�M:"+sum);
		
	}

}
