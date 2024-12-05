class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()) 
        return false;
        if (s == goal)
        return true;
        for (int i=0; i<s.length(); i++) {
            rotate(goal.begin(), goal.begin() + 1, goal.end());
            if (s == goal)
            return true;
        }
        return false;        
    }
};
