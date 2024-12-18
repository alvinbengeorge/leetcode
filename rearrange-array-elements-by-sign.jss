/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    const negatives = nums.filter((num) => num < 0)
    const positives = nums.filter((num) => num >= 0)
    const arr = [];
    for (let i=0; i<negatives.length; i++) {
        arr.push(positives[i])
        arr.push(negatives[i])
    }
    return arr;
};
