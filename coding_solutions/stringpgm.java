package coder;
public class stringpgm {
	public static void main(String[] args) {
		String S="Hello friend";
		int count;
		int[] freq=new int[S.length()]; 
		for(int i=0;i<S.length();i++) {
			count=1;
			if(freq[i]==0)
			{
				for(int j=i+1;j<S.length();j++)
				{
					if((S.charAt(i))==(S.charAt(j))) {
						count++;
						freq[j]=1;} }
				System.out.println(S.charAt(i)+" : "+count);
			}		
		}
	}

}
