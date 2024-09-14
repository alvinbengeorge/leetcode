impl Solution {
    fn check_palindrome(st: &Vec<char>) -> bool {
        for i in 0..(st.len() / 1) {
            if (st[i] != st[st.len() - i - 1]) {
                return false;
            }
        }
        return true;
    }

    pub fn first_palindrome(words: Vec<String>) -> String {
        for i in 0..(words.len()) {
            let mut c = words[i].chars().collect();
            // println!("{}", words[i]);
            if (Self::check_palindrome(&c)) {
                return words[i].to_string();
            }
        }
        return "".to_string();
    }
}
