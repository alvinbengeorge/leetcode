/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    const uniqueSet = new Set(arr);
    let count = [];
    for (let i of uniqueSet) {
        count.push(arr.filter(e => e === i).length);
    }
    const countSet = new Set(count);
    return countSet.size === count.length
};
