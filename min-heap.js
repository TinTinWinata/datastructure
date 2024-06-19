class MinHeap {
  constructor(){
    this.heap = [-1];
  }
  getLeftIdx(p){
    return p * 2;
  }
  getRightIdx(p){
    return p * 2 + 1;
  }
  getParentIdx(c){
    return Math.floor(c / 2)
  }
  insert(v){
    this.heap.push(v)
    this.heapifyUp()
  }

  extract(){
    if(this.size() == 0){
      return null;
    } else if(this.size() == 1){
      return this.heap.pop();
    }
    let result = this.heap[1];
    this.heap[1] = this.heap.pop();
    this.heapifyDown();
    return result;
  }

  heapifyUp(){
    let cursor = this.heap.length - 1;
    while(cursor > 1){
      const parentIdx = this.getParentIdx(cursor);
      if(parentIdx > 0 && this.heap[parentIdx] > this.heap[cursor]){
        this.swap(parentIdx, cursor)
        cursor = parentIdx;
      } else {
        break;
      }
    }
  }
  swap(i, j){
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
  }
  heapifyDown(){
   let cursor = 1;
   while(cursor * 2 < this.heap.length){
      let smallerIdx = this.getLeftIdx(cursor)
      let rightIdx = this.getRightIdx(cursor)
      if(rightIdx < this.heap.length && this.heap[rightIdx] < this.heap[smallerIdx]) {
        smallerIdx = rightIdx;
      }
      if(this.heap[smallerIdx] < this.heap[cursor]) {
        this.swap(smallerIdx, cursor)
        cursor = smallerIdx;
      }else {
        break;
      }
   }
  }
  peek(){
    return this.heap[1];
  }
  size(){
    return this.heap.length - 1;
  }
}

const heap = new MinHeap();

for(const v of [7, 9, 21, 30, 40, 6]){
  heap.insert(v);
}

while(heap.size() > 0){
  console.log('Extract : ', heap.extract())
}

// console.log('Heap Array : ', heap.heap);
// console.log('Extract : ', heap.extract());
// console.log('After Extract : ', heap.heap)