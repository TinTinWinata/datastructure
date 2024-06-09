/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var checkSubarraySum = function(nums, k) {
  const map = new Map();
  map.set(0, -1)
  let total = 0;
  for(let i=0;i<nums.length;i++){
    const n = nums[i];
    total += n
    const r = total % k;
    if(map.has(r)){
      const old = map.get(r);
      if(i - old > 1) {
        return true;
      }
    }else {
      map.set(r, i);
    }
  }
  return false;
};

console.log('Result : ', checkSubarraySum([23,2,4,6,6], 7))


