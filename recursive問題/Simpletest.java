package texting;
import java.util.Scanner;

public class Simpletest {
	
	public	static	int gcd(int	a,	int	b) {
		int	c = 0;
		
		while(b!=0){
			c= a%b;
			a=b;
			b=c;
		}
		return a;
	}
	
	public	static void main(String[]	args) {
		Scanner	m=new	Scanner(System.in);
		
		System.out.println("²Ä1¿é¤J : ");
		System.out.print("a:");
		int w = m.nextInt();
		
		System.out.print("b:");
		int r = m.nextInt();
		
		int ret = gcd(w, r);
		System.out.println("gcd : "+ret);
		
	}
}
