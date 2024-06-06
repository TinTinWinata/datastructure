function triplets(arr, target){
  arr.sort((a, b) => a - b)
  const res = [];
  for(let i=0;i<arr.length - 2;i++){
    let l = i + 1;
    let r =  arr.length - 1;
    const v = arr[i];
    const targetTemp = target - v;
    while(r > l){
      const vR = arr[r];
      const vL = arr[l];
      const vTemp = vR + vL
      if(vTemp  === targetTemp){
        res.push([v, vL, vR])
        l += 1;
      } else if(vTemp > targetTemp){
        r -= 1;
      } else if(vTemp < targetTemp){
        l += 1;
      }
    }
  }
  return res;
}

console.log(triplets([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18))