package texting;
import java.util.*;

public class fibonaci_SimpleN {
	public	static	int	fibonaci(int m2){
		if(m2 == 1){
			return 0;
		}else if(m2 == 2){
			return 1;
		}
		
		return fibonaci(m2-1)+fibonaci(m2-2);
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner	m=new	Scanner(System.in);
		
		System.out.println("²Ä1¿é¤J : ");
		System.out.print("a:");
		int w = m.nextInt();
		
		int rest = fibonaci(w);
		System.out.print("a:"+rest);
		
	}

}
