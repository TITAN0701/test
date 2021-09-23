package texting;
import java.util.*;
//河內塔堆疊問題
public class hannoi {
	//移動軌跡
	public static void move(String m1,String m3){
		System.out.println(m1+"->"+m3);
	}
	
	//移動過程
	public static void hannoi1(int m,String m1,String m2,String m3) {
		if(m == 1){
			move(m1, m3); //m1至m3，由小至大中止
		}else {
			hannoi1(m-1, m1, m3, m2); //由m1移動m-1個，並借助m3至m2，因此m2已有2塊
			move(m1, m3); // 將最後m1的最大圓盤先移至m3處，此時m2已有兩塊
			hannoi1(m-1, m2, m1, m3); //再從m2藉由m1處，移至m3處
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n = 3; //共有三塊
		String a= "A";
		String b= "B";
		String c= "C";
	    hannoi1(n,a,b,c); 
	    //定義 a為起始點，b為借助點，c為目標點
		
	}
}
