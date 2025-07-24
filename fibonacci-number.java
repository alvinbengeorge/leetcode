class Solution {
    public int fib1(int n) { // recursive edition
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);        
    }
    public int fib(int n) { // faster loop edition
        if ( n==0 ) return 0;
        int currentNumber = 1;
        int prevNumber = 0;
        int temp;
        for (int i=2; i<=n; i++) {
            temp = prevNumber + currentNumber;
            prevNumber = currentNumber;
            currentNumber = temp;
        }
        return currentNumber;
    }
}
