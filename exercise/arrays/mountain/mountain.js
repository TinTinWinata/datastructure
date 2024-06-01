function mountain(arr){
  let leftPivot = null;
  let peakPivot = null;
  let max = Number.MIN_VALUE;
  for(let i=0 ; i<arr.length;i++){
    const v = arr[i];
    const vNext = arr[i + 1];
    if(vNext === undefined || vNext > v){
      // Up
      if(leftPivot === null){
        leftPivot = i;
      }
      if(leftPivot !== null && peakPivot !== null){
        // From the deepest down to up

        // !Debugging Purposes
        // console.log(`left ${arr[leftPivot]} | peak ${arr[peakPivot]} | now ${arr[i]}`)

        const result = arr[peakPivot] - arr[leftPivot] + arr[peakPivot] - arr[i]; 
        if(result > max){
          max = result;
        }
        leftPivot = i;
        peakPivot = null;
      }
    } else {
      // Down
      if(leftPivot !== null && peakPivot === null){
        peakPivot = i;
      }
    }
  }
  return max;
}

console.log(mountain([5, 6, 1, 2, 3, 4, 5, 4, 3, 2, 0, 1, 2, 3, -2, 4]))