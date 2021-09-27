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
	//以下為求交集之方法
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
		System.out.print("1.陣列c=陣列a交集陣列b: ");
		Integer[] j=geta(a,b);
		for(Integer i:j) {
			System.out.print(i+" ");
		}
		
		//利用Linklist的特點，算出陣列中的交集
		List<Integer>	InteList = new ArrayList<>(Arrays.asList(77,5,5,22,13,55,97,4,796,1,0,9));
		List<Integer>	InteList2 = new ArrayList<>(Arrays.asList(0,1,2,3,4,5,6,7,8,9));
		InteList.removeAll(InteList2);
		System.out.print("\n2.陣列d=陣列a差集陣列b: "+InteList);
		
		List<Integer>	InteList3 = new ArrayList<>(Arrays.asList(77,5,5,22,13,55,97,4,796,1,0,9));
		InteList3.removeAll(InteList2); //利用a陣列刪除b陣列等於a、b後的差集
		InteList2.addAll(InteList3);//再利用差集與b陣列結合，得出聯集
		System.out.println("\n2.陣列e=陣列a聯集陣列b: "+InteList2);
		
	}
}
