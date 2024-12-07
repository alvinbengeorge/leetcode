class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        long long maxi = LONG_MIN, sum = 0;
        for (auto n: nums) {
            sum += n;
            if (sum > maxi) maxi = sum;
            if (sum < 0) sum = 0;
        }
        return maxi;
    }
};
