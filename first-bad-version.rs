// The API isBadVersion is defined for you.
// isBadVersion(version:i32)-> bool;
// to call it use self.isBadVersion(version)

impl Solution {
    pub fn first_bad_version(&self, n: i32) -> i32 {
        for i in (0..n).rev() {
            if (!self.isBadVersion(i)) { return i + 1; }
        }
        n
    }
}
