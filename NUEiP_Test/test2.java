package texting;
//import java.util.regex.*;
//import org.apache.commons.lang.StringUtils;
public class test2 {
// 全型字元轉換　　例子 000 , ０００
	
	private static void printAllCharacter() {
		for (int i = Character.MIN_VALUE; i <= Character.MAX_VALUE; ++i) {
			System.out.println(i +" "+ (char)i);
		}
	}
	public static String toSbc(String input) {
		char c[] = input.toCharArray();
		for ( int i = 0 ; i < c.length; i ++ ) {
			if (c[i] == ' ') {
				c[i] = '\u3000';
			}else if (c[i] < 177) {
				c[i] = ( char ) (c[i] + 65248 );
			}
		}
		return new String(c);
	}
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String str = "人易科技:上 機 測 驗 - 演算法 ";
		System.out.println("半形 -> 全形前：" + str);
		
		//StringUtils.substringBefore("人易科技:上 機 測 驗 - 演算法", ":");
		//擷取需要轉換的字元 --> :
		String sbcResult = toSbc(str);
		
		//以下為轉換所有字元
		//System.out.println("半形-->全形轉換後：" + sbcResult);
		//以下則是擷取字串中的其中一個字元並轉換
		String sbcResult1 = toSbc(str.substring(4,5));
		System.out.println("1.全型轉換後 ->" + sbcResult.replace(":", sbcResult1));
		//String sbcRes1 = sbcResult.replace(":", sbcResult1);
		//去除字元中的空白字元
		
		String sbcResult2 = toSbc(str.replaceAll("\\s+", ""));
		System.out.println("半型-->去除空白：" + sbcResult2);
		
		String sbcResult12 = sbcResult.replace(":", sbcResult1);
		//System.out.println(sbcResult12);
		
		String sbcResult12_rep = sbcResult2.substring(0,9);
		String str_sbcR_rep = str.substring(12,15);
		String str_sbcR_rep1 = str.substring(15,19);
		System.out.println("2.去掉中文字間的空白(保留-號2側空白): "+sbcResult12_rep+str_sbcR_rep+str_sbcR_rep1);
		
		String str_sbcR_rep2 = str.substring(5,13);
		System.out.println("3.列印:到-之間的字元:"+str_sbcR_rep2);
		
		
		//String sbcRes12detespac = sbcRes12.replace("\\s+", "");
	}
}
