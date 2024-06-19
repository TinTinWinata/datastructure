/**
 * @param {number[]} bloomDay
 * @param {number} m needed bouquet
 * @param {number} k flowers per bouquet
 * @return {number}
 */
var minDays = function(bloomDay, m, k) {
    if(m * k > bloomDay.length) return -1
    let left = Number.POSITIVE_INFINITY;
    let right = Number.NEGATIVE_INFINITY;
    for(const v of bloomDay){
      left = Math.min(v, left)
      right = Math.max(v, right)
    }

    const isValid = (low) => {
      let flower = 0;
      let bouquet = 0;
      for(const v of bloomDay){
        if(v <= low){
          flower += 1;
          if(flower === k){
            bouquet += 1;
            flower = 0;
            if(bouquet === m){
              return true;
            }
          }
        } else {
          flower = 0;
        }
      }
      return false;
    }
    while(left < right){
      const mid = Math.floor((left + right) / 2)
      if(isValid(mid)){
        right = mid;
      }else{
        left = mid + 1;
      }
    }
    return left;
};

console.log(minDays([7, 6, 4, 20, 32, 1, 5, 4], 2, 2))