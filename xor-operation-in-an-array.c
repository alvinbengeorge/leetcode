int xorOperation(int n, int start) {
    int xorValue = 0;
    for (int i = start; i < start + 2 * n; i+=2) {
        
        xorValue ^= i;
    }
    return xorValue;
}
