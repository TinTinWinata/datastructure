class MaxHeap {
  constructor(){
    this.heap = [-1]
  }   
  swap(i, j){
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
  }
  insert(v, p){
    this.heap.push({v, p});
    let cursor = this.heap.length - 1;
    while(cursor > 1){
      const parent = Math.floor(cursor / 2)
      if(this.heap[cursor].p >  this.heap[parent].p){
        this.swap(cursor, parent)
        cursor = parent;
      } else {
        break;
      }
    }
  }
  extract(){
    if(this.size() == 0) return null;
    if(this.size() == 1) return this.heap.pop();
    const res = this.heap[1];
    this.heap[1] = this.heap.pop()
    let cursor = 1;
    while(cursor * 2 < this.heap.length){
      let largest = cursor * 2
      let right = cursor * 2 + 1
      if(right < this.heap.length && this.heap[right].p > this.heap[largest].p){
        largest = right;
      }
      if(this.heap[largest].p > this.heap[cursor].p){
        this.swap(largest, cursor)
        cursor = largest;
      } else {
        break;
      }
    }
    return res;
  }
  peek(){
    return this.heap[1];
  }
  size(){
    return this.heap.length - 1;
  }
}


class MinHeap {
  constructor(){
    this.heap = [-1]
  }   
  swap(i, j){
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
  }
  insert(v, p){
    this.heap.push({v, p});
    let cursor = this.heap.length - 1;
    while(cursor > 1){
      const parent = Math.floor(cursor / 2)
      if(this.heap[cursor].p < this.heap[parent].p){
        this.swap(cursor, parent)
        cursor = parent;
      } else {
        break;
      }
    }
  }
  extract(){
    if(this.size() == 0) return null;
    if(this.size() == 1) return this.heap.pop();
    const res = this.heap[1];
    this.heap[1] = this.heap.pop()
    let cursor = 1;
    while(cursor * 2 < this.heap.length){
      let smallest = cursor * 2;
      let right = cursor * 2 + 1
      if(right < this.heap.length && this.heap[right].p < this.heap[smallest].p){
        smallest = right;
      }
      if(this.heap[smallest].p < this.heap[cursor].p){
        this.swap(smallest, cursor)
        cursor = smallest;
      } else {
        break;
      }
    }
    return res;
  }
  peek(){
    return this.heap[1];
  }
  size(){
    return this.heap.length - 1;
  }
}

/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
var findMaximizedCapital = function(k, w, profits, capital) {
  const maxProfits = new MaxHeap();
  const minCapitals = new MinHeap();
  for(let i=0;i<capital.length;i++){
    minCapitals.insert(profits[i], capital[i])
  }
  while(k > 0){
    while(minCapitals.peek() && minCapitals.peek().p <= w){
      const {v, p} = minCapitals.extract()
      // console.log(minCapitals.heap)
      // console.log(`insert ${v} to max profits`)
      maxProfits.insert(p, v)
    }
    const node = maxProfits.extract();
    // console.log(`extracted : `, node)
    if(node){
      w += node.p;
    } else{
      console.log('error : ', maxProfits.heap)
    }
    k--;
  }
  return w;
};

// console.log(findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
// console.log(findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))