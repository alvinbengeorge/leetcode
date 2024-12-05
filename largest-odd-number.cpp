class Solution {
public:
    bool checkOdd(int digit) {
        return (
            digit == '1' ||
            digit == '3' ||
            digit == '5' ||
            digit == '7' ||
            digit == '9'
        );
    }
    string largestOddNumber(string num) {
        int len = num.length();              
        for (int i=len; i>0; i--) {
            if (checkOdd(num[i-1])) {
                return num.substr(0, i);
            }
        }
        return "";
    }
};
