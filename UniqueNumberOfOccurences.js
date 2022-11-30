/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    const set = new Set(arr);
    return !(set.size === arr.length)
};
