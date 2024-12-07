class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int maximum = -1, max_num = -1, cnt;
        vector<int> v = nums;
        auto it = unique(v.begin(), v.end());
        v.erase(it, v.end());

        for (auto num: v) {
            cout << num << endl;
            cnt = count(nums.begin(), nums.end(), num);
            if (cnt > maximum) {
                maximum = cnt;
                max_num = num;
            }
        }
        return max_num;
    }
};
