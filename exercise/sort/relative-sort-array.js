/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var relativeSortArray = function(arr1, arr2) {
  const m = new Map()
  for(let i=0;i<arr2.length;i++){
      m.set(arr2[i], i)
  }
  arr1.sort((a, b) => {
      if(!m.has(a) && !m.has(b)){
          return a - b
      } else if(!m.has(a)) {
        return 1
      } else if(!m.has(b)) {
        return -1
      } else {
          return m.get(a) - m.get(b)
      }
  })
  return arr1
};

console.log(relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))