class Solution {
    public int lengthOfLastWord(String s) {
        int track=0;
        int flag=0;
        int length=0;
        var h=s.trim();
        if (h.length()==0)
        {
            return 0;
        }
        else if (h.length()==1)
        {
            return 1;
        }
        else{
        for(int i=0;i<h.length();i++)
        {
                if (h.charAt(i)==' ') 
                {
                    track=i;
                    flag=1;
                }
            
        }
        if (flag==0)
            return h.length();
        else
        length=h.length()-track-1;
        
        return length;}
    }
}