class Graph {
  constructor(totalVertecs){
    this.totalVertecs = totalVertecs;
    this.lists = Array.from({length: totalVertecs}, () => [])
  }

  addEdge(i, j, dir){
    this.lists[i].push(j);
    if(!dir){
      this.lists[j].push(i);
    }
  }

  print(){
    for(let i=0;i<this.totalVertecs;i++){
      let res = `[${i}] : `
      for(const v of this.lists[i]){
        res += `${v} -> `;
      }
      console.log(res)
    }
  }
}

const graph = new Graph(6);
graph.addEdge(0, 1)
graph.addEdge(0, 4)
graph.addEdge(2, 1)
graph.addEdge(3, 4)
graph.addEdge(4, 5)
graph.addEdge(2, 3)
graph.addEdge(3, 5)
graph.print()