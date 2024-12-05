class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length()) 
        return false;
        unordered_map<char, char> s_to_t = {};
        unordered_map<char, char> t_to_s = {};
        for (int i=0; i<s.length(); i++) {
            if (s_to_t.count(s[i]) == 0 && t_to_s.count(t[i]) == 0) {
                s_to_t[s[i]] = t[i];
                t_to_s[t[i]] = s[i];
            } else {
                if (s_to_t[s[i]] != t[i] || t_to_s[t[i]] != s[i]) return false;
            }
        }
        return true;
    }
};
