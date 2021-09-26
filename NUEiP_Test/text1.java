package texting;

import java.util.*;
//車輛分為汽車和機車
interface	locomotive{
	public	static String start() {
		return "ST";
	}
	public	static String  startautodrive1(){// 此為啟動自動導航地圖系統
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
	public	static int  startautodrive1(int ad1){// 此為啟動自動導航地圖系統
		if(ad1 == 1) {
			System.out.println("發動引擎!!");
		}else {
			System.out.println("引擎發生錯誤!!");
		}
		return 1;
	}
	public	static int  startautodrive2(int q1,int q2){// 此為啟動自動駕駛系統
		int m = 7;
		if(q1 == 2){
			System.out.println("發動第2系列功能!!!");
		}else {
			q1 = q2 % q1;
			q2 = q1;
			m = q2;
			System.out.println("發動第2系列功能，發生錯誤!!");
		}
		return m;
	} 
	public static int stop(int st) {
		if(st == 9) {
			System.out.println("停止引擎!!");
		}else {
			System.out.println("引擎將持續運轉!!!!");
		}
		return 0;
	}
}

class allfunc extends car{
	public static	int getfunc(int m) {
		int a=0;
		if(a == 5) {
			System.out.println("啟動第5個功能鍵");
		}else {
			System.out.println("啟動發生錯誤");
		}
		return 0;
	}
}
public class text1 extends allfunc implements locomotive{
	
	public static void main(String[] args) {
		allfunc a =new text1();
		text1 b=new text1(); 
		
		Scanner	m=new	Scanner(System.in);
		System.out.print("請輸入任意數字鍵 -->");
		int st=m.nextInt();
		int ret = a.startautodrive1(st);
		System.out.println("輸入全功能啟動鍵為:"+ret+"之功能!!!!");
		
		System.out.print("請輸入任意數字鍵，猜測輸入第1次 -->");
		int st1=m.nextInt();
		System.out.print("請輸入任意數字鍵，猜測輸入第2次 -->");
		int st2=m.nextInt();
		int ret1 = a.startautodrive2(st1, st2);
		System.out.println("發動系列2之功能啟動鍵為:"+ret1+"之功能!!!!");
		
		System.out.print("請輸入任意數字鍵 -->");
		int st3=m.nextInt();
		int ret2 = b.stop(st3);
		System.out.println("發動系列2之功能啟動鍵為:"+ret2+"之功能!!!!");
		
		System.out.print("重新啟輸入猜測鍵 -->");
		int st4=m.nextInt();
		int ret3 = b.getfunc(st4);
		System.out.println("發動系列2之功能啟動鍵為:"+ret3+"之功能!!!!");
	}
}
