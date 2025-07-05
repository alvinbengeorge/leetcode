/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    let largest = 0;
    for (let element of new Set(arr)) {
        if (arr.filter(x => x == element).length == element && element > largest) largest = element;
    }
    return largest || -1;
};
