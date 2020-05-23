package coder;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

public class keysort {
	public static void main(String[] args) {
		Map<String,String> arr=new HashMap<>();
		arr.put("pirate", "JACK sparrow");
		arr.put("iron man", "TONY stark");
		arr.put("avenger", "Captain america");
		arr.put("god", "thor");
		
		for(Map.Entry<String,String> ent:arr.entrySet())
		{
			System.out.println(ent.getKey()+ "---"+ent.getValue());
		}
		Map<String,String> arr2=new TreeMap<>(arr);
		for(Map.Entry<String,String> ent:arr2.entrySet())
		{
			System.out.println(ent.getKey()+ "---"+ent.getValue());
		}
		
		
		
	}

}
