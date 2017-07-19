import java.util.*;

public class GreyCode {

    public static List<Integer> genCodes(int n){
        if(n <= 0) return Collections.singletonList(0);
        else if(n == 1){
            return new ArrayList<>(Arrays.asList(0, 1));
        } else {
            List<Integer> codes = genCodes(n - 1);
            int itr = codes.size() - 1;
            while(itr >= 0){
                int code = codes.get(itr) + (int)Math.pow(2, n - 1);
                codes.add(code);
                itr--;
            }
            return codes;
        }
    }

    public static void main(String[] args) {
        for(int i : genCodes(2)){
            System.out.println(i);
        }
    }

}
