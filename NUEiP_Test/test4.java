package texting;

public class test4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[]	a= {77,5,5,22,13,55,97,4,796,1,0,9};
		
		//��w�ƧǪk
		for(int i=0;i<a.length;i++) {
			for(int j=(i+1);j<a.length;j++) {
				if(a[i]>a[j]) {//�洫��
					int c=a[i];
					a[i]=a[j];
					a[j]=c;
				}
			}
		}
		//�Q�ΰj��̧ǦC�X
		for(int m:a) {
			System.out.print(m+"  ");
		}
	}

}
