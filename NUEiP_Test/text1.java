package texting;

import java.util.*;
//���������T���M����
interface	locomotive{
	public	static String start() {
		return "ST";
	}
	public	static String  startautodrive1(){// �����Ұʦ۰ʾɯ�a�Ϩt��
		return "SD1 is move";
	} 
	public static String stop() {
		return "SP";
	}
}

class car implements locomotive{
	public	static String start() {
		return "ST";
	}
	public	static int  startautodrive1(int ad1){// �����Ұʦ۰ʾɯ�a�Ϩt��
		if(ad1 == 1) {
			System.out.println("�o�ʤ���!!");
		}else {
			System.out.println("�����o�Ϳ��~!!");
		}
		return 1;
	}
	public	static int  startautodrive2(int q1,int q2){// �����Ұʦ۰ʾr�p�t��
		int m = 7;
		if(q1 == 2){
			System.out.println("�o�ʲ�2�t�C�\��!!!");
		}else {
			q1 = q2 % q1;
			q2 = q1;
			m = q2;
			System.out.println("�o�ʲ�2�t�C�\��A�o�Ϳ��~!!");
		}
		return m;
	} 
	public static int stop(int st) {
		if(st == 9) {
			System.out.println("�������!!");
		}else {
			System.out.println("�����N����B��!!!!");
		}
		return 0;
	}
}

class allfunc extends car{
	public static	int getfunc(int m) {
		int a=0;
		if(a == 5) {
			System.out.println("�Ұʲ�5�ӥ\����");
		}else {
			System.out.println("�Ұʵo�Ϳ��~");
		}
		return 0;
	}
}
public class text1 extends allfunc implements locomotive{
	
	public static void main(String[] args) {
		allfunc a =new text1();
		text1 b=new text1(); 
		
		Scanner	m=new	Scanner(System.in);
		System.out.print("�п�J���N�Ʀr�� -->");
		int st=m.nextInt();
		int ret = a.startautodrive1(st);
		System.out.println("��J���\��Ұ��䬰:"+ret+"���\��!!!!");
		
		System.out.print("�п�J���N�Ʀr��A�q����J��1�� -->");
		int st1=m.nextInt();
		System.out.print("�п�J���N�Ʀr��A�q����J��2�� -->");
		int st2=m.nextInt();
		int ret1 = a.startautodrive2(st1, st2);
		System.out.println("�o�ʨt�C2���\��Ұ��䬰:"+ret1+"���\��!!!!");
		
		System.out.print("�п�J���N�Ʀr�� -->");
		int st3=m.nextInt();
		int ret2 = b.stop(st3);
		System.out.println("�o�ʨt�C2���\��Ұ��䬰:"+ret2+"���\��!!!!");
		
		System.out.print("���s�ҿ�J�q���� -->");
		int st4=m.nextInt();
		int ret3 = b.getfunc(st4);
		System.out.println("�o�ʨt�C2���\��Ұ��䬰:"+ret3+"���\��!!!!");
	}
}
