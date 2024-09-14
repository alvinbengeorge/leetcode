impl Solution {
    pub fn title_to_number(column_title: String) -> i32 {
        let mut c: Vec<char> = column_title.chars().collect();
        let mut sum: i32 = 0;
        let mut n: i32 = c.len() as i32;
        let base: i32 = 26;
        for i in 0..n {
            sum = sum + ((c[i as usize] as i32 - 64) * base.pow((n-i-1).try_into().unwrap()));
        }
        return sum;
    }
}
