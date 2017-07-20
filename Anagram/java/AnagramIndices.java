import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class AnagramIndices {


    public static List<Integer> getAnagramIndices(String haystack, String needle) {
        int hLen = haystack.length();
        int nLen = needle.length();
        if(nLen > hLen) return Collections.emptyList();
        List<Integer> ret = new ArrayList<>();
        char[] needleArray = needle.toCharArray();
        Arrays.sort(needleArray);
        for (int i = 0; i < hLen; i++) {
            if (i + nLen > hLen)
                break;
            String candidate = haystack.substring(i, i + nLen);
            char[] charArray = candidate.toCharArray();
            Arrays.sort(charArray);
            if (Arrays.equals(charArray, needleArray))
                ret.add(i);
        }

        return ret;
    }

    public static void main(String[] args) {
        String h = "bbbababaaabbbb";
        String n = "ab";
        getAnagramIndices(h, n).forEach(System.out::println);
    }
}
