/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
  const set = new Set();
  let c = 0;
  const map = new Map();
  for(const n of nums){
    if(set.has(n)){
      let t = n + 1;
      while(set.has(t)){
        if(map.has(t)) {
         t = map.get(t) 
        }
        t += 1;
      }
      map.set(n, t)
      set.add(t);
      c += t - n;
    }
    set.add(n);
  }
  return c;
};

// console.log(minIncrementForUnique([1,2,2]))
console.log(minIncrementForUnique([3,2,1,2,1,7]))