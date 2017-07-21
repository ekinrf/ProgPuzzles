import java.util.*;

public class AnagramIndices {

    public static List<Integer> getAnagramIndices(String haystack, String needle) {
        int hLen = haystack.length();
        int nLen = needle.length();
        if (nLen > hLen) return Collections.emptyList();
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

    // O(n!)
    public static Set<String> genPermutations(String src) {
        Set<String> perms = new HashSet<>();
        if (src.length() == 1) {
            perms.add(src);
        } else if (src.length() > 1) {
            for (int i = 0; i < src.length(); i++) {
                char ch = src.charAt(i);
                String rest = src.substring(0, i) + src.substring(i + 1);
                Set<String> restPerms = genPermutations(rest);

                for (String perm : restPerms) {
                    perms.add(ch + perm);
                }
            }
        }
        return perms;
    }

    public static void main(String[] args) {

        genPermutations("abcc").forEach(System.out::println);

        String h = "bbbababaaabbbb";
        String n = "ab";
        getAnagramIndices(h, n).forEach(System.out::println);
    }
}
