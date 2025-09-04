class Solution {
    public int differenceOfSums(int n, int m) {
        int divisibles=0;
        int non_divisibles=0;
        for (int i=1; i<=n; i++) {
            if (i % m == 0) divisibles += i;
            else non_divisibles += i;
        }
        return non_divisibles - divisibles;
    }
}
