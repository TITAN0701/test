package texting;
import java.util.*;
//�e������|���D
public class hannoi {
	//���ʭy��
	public static void move(String m1,String m3){
		System.out.println(m1+"->"+m3);
	}
	
	//���ʹL�{
	public static void hannoi1(int m,String m1,String m2,String m3) {
		if(m == 1){
			move(m1, m3); //m1��m3�A�Ѥp�ܤj����
		}else {
			hannoi1(m-1, m1, m3, m2); //��m1����m-1�ӡA�íɧUm3��m2�A�]��m2�w��2��
			move(m1, m3); // �N�̫�m1���̤j��L������m3�B�A����m2�w�����
			hannoi1(m-1, m2, m1, m3); //�A�qm2�ǥ�m1�B�A����m3�B
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 3; //�@���T��
		String a= "A";
		String b= "B";
		String c= "C";
	    hannoi1(n,a,b,c); 
	    //�w�q a���_�l�I�Ab���ɧU�I�Ac���ؼ��I
		
	}
}
