/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number}
 */
var minPatches = function(nums, n) {
  let t = BigInt(1);
  let p = 0;
  let result = 0;
  while(t <= n){
    if(p < nums.length && nums[p] <= t){
      t += BigInt(nums[p])
      p++;
    } else {
      t += t
      result++;
    }
  }
  return result;
};


console.log(minPatches([1, 5, 10], 20))
console.log(minPatches([1,2,31,33], 2147483647))
console.log(minPatches([1,2,32], 2147483647))