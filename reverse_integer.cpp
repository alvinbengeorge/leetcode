class Solution {
public:
    int reverse(int x) {
       long int num=0;
        while(x!=0){
            int rem=x%10;
            num=num*10+rem;
            x/=10;
        }
        if(num<INT_MIN || num>INT_MAX)return 0;
        return num;
    }
};
