package coder;

import java.util.ArrayList;
import java.util.Collections;

public class arraylist_sort {
public static void main(String args[])
{
	ArrayList<String> a=new ArrayList<>();
	a.add("china");
	a.add("india");
	a.add("brazil");
	a.add("america");
	a.add("mexico");
	System.out.println("The list before sorting\n" +a);
	Collections.sort(a);	
	System.out.println("The list after sorting\n" +a);
	Collections.sort(a,Collections.reverseOrder());
	System.out.println("Reverse order of sorted list\n" +a);
}
}
