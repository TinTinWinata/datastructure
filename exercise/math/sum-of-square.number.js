/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function(c) {
    if(c == 0) return true;
    let max = Math.floor(Math.sqrt(c))
    for(let i=1;i<=max;i++){
      const b = Math.sqrt(c - (i * i))
      if(b - Math.floor(b) == 0){
        return true;
      }
    }
    return false;
};

console.log(judgeSquareSum(3))
console.log(judgeSquareSum(4))
console.log(judgeSquareSum(5))