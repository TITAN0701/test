package texting;

import java.util.*;
public class test5 {
	
	/*
	 * private static Integer[] geta(Integer[] m,Integer[] n) { List<Integer> res =
	 * new ArrayList<Integer>(); Set<Integer> set = new
	 * HashSet<Integer>(Arrays.asList(m.length>n.length ? m:n)); for(Integer
	 * i:m.length>n.length ? n:m) { if(set.contains(i)) { res.add(i); } } Integer[]
	 * arr= {}; return res.toArray(arr);
	 * 
	 * }
	 */
	//�H�U���D�涰����k
	 private static Integer[] geta(Integer[] nums1, Integer[] nums2) {
	        Set<Integer> set1 = new HashSet<>();
	        Set<Integer> set2 = new HashSet<>();      
	        for(Integer i:nums1){
	            set1.add(i);
	        }
	        for(Integer i:nums2){
	            if(set1.contains(i)){
	                set2.add(i);
	            }
	        }
	        Integer[] arr = new Integer[set2.size()];
	        Integer j=0;
	        for(Integer i:set2){
	            arr[j++] = i;
	        }
	        return arr;
	    }
	 
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer[]	a= {77,5,5,22,13,55,97,4,796,1,0,9};
		Integer[]	b= {0,1,2,3,4,5,6,7,8,9};
		System.out.print("1.�}�Cc=�}�Ca�涰�}�Cb: ");
		Integer[] j=geta(a,b);
		for(Integer i:j) {
			System.out.print(i+" ");
		}
		
		//�Q��Linklist���S�I�A��X�}�C�����涰
		List<Integer>	InteList = new ArrayList<>(Arrays.asList(77,5,5,22,13,55,97,4,796,1,0,9));
		List<Integer>	InteList2 = new ArrayList<>(Arrays.asList(0,1,2,3,4,5,6,7,8,9));
		InteList.removeAll(InteList2);
		System.out.print("\n2.�}�Cd=�}�Ca�t���}�Cb: "+InteList);
		
		List<Integer>	InteList3 = new ArrayList<>(Arrays.asList(77,5,5,22,13,55,97,4,796,1,0,9));
		InteList3.removeAll(InteList2); //�Q��a�}�C�R��b�}�C����a�Bb�᪺�t��
		InteList2.addAll(InteList3);//�A�Q�ήt���Pb�}�C���X�A�o�X�p��
		System.out.println("\n2.�}�Ce=�}�Ca�p���}�Cb: "+InteList2);
		
	}
}
