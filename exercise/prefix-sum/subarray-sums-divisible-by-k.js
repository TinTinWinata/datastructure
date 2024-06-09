/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraysDivByK = function(nums, k) {
  const map = {0 : [0]};
  let reminder = 0;
  let count = 0;
  for(let i=0;i<nums.length;i++) {
    reminder += nums[i];
    let result = reminder % k;
    if(result < 0) { 
      result += k
    }
    if(map[result] === undefined){
      map[result] = [i];
    } else {
      count += map[result].length;
      map[result] = [...map[result], i]
    }
  }
  return count;
};

// console.log(subarraysDivByK([4,5,0,-2,-3,1], 5))
// console.log(subarraysDivByK([5], 9))
// console.log(subarraysDivByK([-1,2,9], 2))
// console.log(subarraysDivByK([2,-2,2,-4], 6))