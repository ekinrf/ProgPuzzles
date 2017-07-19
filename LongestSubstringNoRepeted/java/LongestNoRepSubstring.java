public class LongestNoRepSubstring {

    public static int lengthOfLNRSubstring(String src){
        int maxLen = 0, lenEndHere = 0;
        String substringEndHere = "";
        for(int chIdx = 0; chIdx < src.length(); chIdx++){
            char ch = src.charAt(chIdx);
            int chInSubString = substringEndHere.indexOf(ch); // use map or char map for quicker lookup
            if(chInSubString < 0){
                substringEndHere += ch;
            } else {
                substringEndHere = substringEndHere.substring(chInSubString + 1) + ch;
            }
            lenEndHere = lenEndHere - chInSubString; // chInSubString -1 if not found
            maxLen = Math.max(maxLen, lenEndHere);
        }
        return maxLen;
    }

    public static void main(String[] args) {
        System.out.println(lengthOfLNRSubstring("dvdf"));
    }
}
