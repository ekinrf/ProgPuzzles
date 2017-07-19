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
        qs(0, 1, array.length - 1);
    }

    private void swap(int i, int j){
        int tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }

    protected void qs(int p, int lo, int hi){
        if(lo >= hi) return;
        int newP = partition(p, lo, hi);
        qs(p, p + 1, newP - 1);
        qs(newP + 1, newP + 2, hi);
    }

    protected int partition(int p, int lo, int hi) {
        int l = lo, h = hi, pVal = array[p];
        while (l <= h) {
            while (this.array[l] < pVal && l <= h) {
                l++;
            }

            while (this.array[h] > pVal && l <= h) {
                h--;
            }
            if(l < h) swap(l++, h--);
        }
        if(h < lo) return p;
        else swap(p, h);
        return h;
    }

}

class SortRunner {

    public static void main(String[] args) {

        int[] testArray = {2, 4, 5, 21, 42, 123, 1, 3, 2, 2, 123, 9};

        SortAlgo qs = new QuickSort(testArray);
        qs.sort();
        System.out.println(qs.array());

    }
}