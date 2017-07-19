public abstract class SortAlgo {

    protected int[] array;

    public SortAlgo(int[] array) {
        this.array = array;
    }

    public abstract void sort();

    public String array() {
        String arrayStr = "";
        for (int i : array) {
            arrayStr = arrayStr + (i + " ");
        }
        return arrayStr;
    }
}


class QuickSort extends SortAlgo {

    public QuickSort(int[] array) {
        super(array);
    }

    @Override
    public void sort() {
        //qs(0, array.length - 1);
        threeWayQs(0, array.length - 1);
    }

    private void swap(int i, int j) {
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }

    protected void qs(int lo, int hi) {
        if (lo >= hi) return;
        int p = partition(lo, hi);
        // if shrink first part ie. p - 1
        // pick pivot at the end, make sure p changes because lo doesn't
        qs(lo, p - 1);

        // if shrink second part ie. p + 1
        // pick pivot at the beginning for the same reason above.
        qs(p, hi);
    }

    // the key to hoare partition is to understand
    // that the return p is not necessarily where pivot is
    // instead [lo, p] guarantees all elem is not great than pivot
    // (p, hi] not less than pivot
    protected int partition(int lo, int hi) {
        int pVal = this.array[hi], l = lo - 1, h = hi + 1;
        while (l < h) {
            do l++; while (array[l] < pVal);
            do h--; while (array[h] > pVal);

            if (l < h) swap(l, h);
        }
        // l stops at [lo, l] >= pVal
        // h stops at [h, hi] <= pVal
        return l;
    }

    protected void threeWayQs(int lo, int hi) {
        if (lo >= hi) return;

        int pVal = array[lo], lt = lo, gt = hi, visited = lo;

        while (visited <= gt) {
            if (array[visited] == pVal) {
                visited++;
            } else if (array[visited] < pVal) {
                swap(lt++, visited++);
            } else { // pVal > array[visited]
                swap(gt--, visited);
            }
        }

        threeWayQs(lo, lt - 1);
        threeWayQs(gt + 1, hi);
    }
}

class SortRunner {

    public static void main(String[] args) {

        int[] testArray = {2, 4, 5, 21, 42, 123, 1, 3, 2, 2, 123, 9};
        //int[] testArray = {4, 3, 2};


        SortAlgo qs = new QuickSort(testArray);
        qs.sort();
        System.out.println(qs.array());

    }
}