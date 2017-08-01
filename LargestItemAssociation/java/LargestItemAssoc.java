import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class LargestItemAssoc {
    public static String[] largestItemAssociation(String[][] itemAssociation) {
        Map<String, String> itemMap = new HashMap<>();

        for (int x = 0; x < itemAssociation.length; x++) {
            for (int y = 0; y < itemAssociation[x].length; y++) {
                String itemName = itemAssociation[x][y];
                if (itemMap.containsKey(itemName)) {
                    if (y == 1) {
                        String root1 = findRoot(itemName, itemMap);
                        String root2 = findRoot(itemAssociation[x][0], itemMap);
                        itemMap.put(root1, root2);
                    }
                } else {
                    if (y == 0) itemMap.put(itemName, itemName);
                    else itemMap.put(itemName, itemAssociation[x][0]);
                }
            }
        }

        Map<String, ArrayList<String>> ret = new HashMap<>();
        int largest = 0;
        String largestRoot = "";
        for (String key : itemMap.keySet()) {
            String root = findRoot(key, itemMap);
            ArrayList<String> aList;
            if (ret.containsKey(root)) {
                aList = ret.get(root);
                aList.add(key);
            } else {
                aList = new ArrayList<>();
                aList.add(key);
                ret.put(root, aList);
            }
            if (aList.size() > largest) {
                largest = aList.size();
                largestRoot = root;
            }
        }
        ArrayList<String> largestSet = ret.get(largestRoot);
        return largestSet.toArray(new String[largestSet.size()]);
    }

    private static String findRoot(String itemName, Map<String, String> itemMap) {
        if(itemMap.containsKey(itemName)){
            String rootName = itemMap.get(itemName);
            while (rootName != itemName) {
                itemName = rootName;
                rootName = itemMap.get(itemName);
            }
            return rootName;
        } else {
            return itemName;
        }

    }

    public static void main(String[] args) {
        String[][] test = new String[][]{{"Item1", "Item2"}, {"Item3", "Item4"}, {"Item4", "Item5"}, {"Item5", "Item1"}};

        String [] a = largestItemAssociation(test);
        for(String s : a)
            System.out.println(s);
    }
}
