package texting;
//import java.util.regex.*;
//import org.apache.commons.lang.StringUtils;
public class test2 {
// �����r���ഫ�@�@�Ҥl 000 , ������
	
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
		String str = "�H�����:�W �� �� �� - �t��k ";
		System.out.println("�b�� -> ���Ϋe�G" + str);
		
		//StringUtils.substringBefore("�H�����:�W �� �� �� - �t��k", ":");
		//�^���ݭn�ഫ���r�� --> :
		String sbcResult = toSbc(str);
		
		//�H�U���ഫ�Ҧ��r��
		//System.out.println("�b��-->�����ഫ��G" + sbcResult);
		//�H�U�h�O�^���r�ꤤ���䤤�@�Ӧr�����ഫ
		String sbcResult1 = toSbc(str.substring(4,5));
		System.out.println("1.�����ഫ�� ->" + sbcResult.replace(":", sbcResult1));
		//String sbcRes1 = sbcResult.replace(":", sbcResult1);
		//�h���r�������ťզr��
		
		String sbcResult2 = toSbc(str.replaceAll("\\s+", ""));
		System.out.println("�b��-->�h���ťաG" + sbcResult2);
		
		String sbcResult12 = sbcResult.replace(":", sbcResult1);
		//System.out.println(sbcResult12);
		
		String sbcResult12_rep = sbcResult2.substring(0,9);
		String str_sbcR_rep = str.substring(12,15);
		String str_sbcR_rep1 = str.substring(15,19);
		System.out.println("2.�h������r�����ť�(�O�d-��2���ť�): "+sbcResult12_rep+str_sbcR_rep+str_sbcR_rep1);
		
		String str_sbcR_rep2 = str.substring(5,13);
		System.out.println("3.�C�L:��-�������r��:"+str_sbcR_rep2);
		
		
		//String sbcRes12detespac = sbcRes12.replace("\\s+", "");
	}
}
