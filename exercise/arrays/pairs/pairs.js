
function pairs(arr, target){
  const set = new Set();
  for(const v of arr){
    const temp = target - v;
    if(set.has(temp)){
      return [temp, v];
    } 
    set.add(v)
  }
  throw 'There is no pair of this'
}

console.log(pairs([10, 5, 2, 3, -6, 9, 11], 4))

// Big O Notation :
// O(N)