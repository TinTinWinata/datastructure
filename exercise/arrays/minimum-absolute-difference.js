

function minimumAbsDifference(arr) {
    const m = new Map()
    let min = Number.POSITIVE_INFINITY;
    arr.sort((a, b) => a - b)
    const add = (d, a, b) => {
      if(d <= min){
        min = d;
      } else return;
      if(m.has(d)){
        const t = m.get(d);
        t.push([a, b])
        m.set(d, t)
      } else {
        m.set(d, [[a, b]])
      }
    }
    for(let i=0;i<arr.length - 1;i++){
      const d = arr[i + 1] - arr[i]
      add(d, arr[i], arr[i + 1])
    }
    return m.get(min);
};

// console.log(minimumAbsDifference([4,2,1,3]))
// console.log(minimumAbsDifference([1,3,6,10,15]))