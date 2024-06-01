function recrusive(arr, target, start, end){
  const mid = Math.floor((start + end) / 2)
  if(arr[mid] === target){
    return mid;
  } 

  if(end <= start){
    throw 'Not Found!';
  }
  
  if(arr[mid] < target){
    return recrusive(arr, target, mid + 1, end);
  } else {
    return recrusive(arr, target, start, mid - 1);
  }
}

function binarySearch(arr, target){
  return recrusive(arr, target, 0, arr.length - 1)
}

console.log('Result : ', binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))