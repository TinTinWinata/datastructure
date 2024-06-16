
class PriorityQueue {
  constructor(){
    this.heap = [{val: null, priority: -1}]
  } 
  swap(i, j){
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]]
  }
  heapifyUp(){
    let cursor = this.heap.length - 1;
    while(cursor > 1){
      const parentIdx = Math.floor(cursor / 2);
      if(this.heap[cursor].priority < this.heap[parentIdx].priority){
        this.swap(cursor, parentIdx);
        cursor = parentIdx;
      } else {
        break;
      }
    }
  }
  heapifyDown(){
    let cursor = this.heap[1];
    while(cursor * 2 < this.heap.length){
      let smallestIdx = this.heap[cursor * 2];
      let rightIdx = this.heap[cursor * 2 + 1];
      if(rightIdx < this.heap.length && this.heap[rightIdx].priority < this.heap[smallestIdx].priority){
        smallestIdx = rightIdx;
      }
      if(this.heap[smallestIdx].priority < this.heap[cursor].priority) {
        this.swap(smallestIdx, cursor);
        cursor = smallestIdx;
      }else {
        break;
      }
    }
  }
  insert(val, priority){
    this.heap.push({val, priority})
    this.heapifyUp();
  }
  extract(){
    if(this.size() == 0) return null;
    if(this.size() == 1) return this.heap.pop();
    const res = this.heap[1];
    this.heap[1] = this.heap.pop();
    this.heapifyDown();
    return res;
  }
  size(){
    return this.heap.length - 1;
  }
  peek(){
    if(!this.heap[1]) return null;
    return this.heap[1];
  }
}

const pq = new PriorityQueue();
pq.insert({name : 'Justine'}, 2)
pq.insert({name : 'Winata'}, 3)
pq.insert({name : 'Rudy'}, 1)

while(pq.size() > 0){
  console.log('Extract : ', pq.extract().val)
}

