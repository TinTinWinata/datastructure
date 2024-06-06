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

  bfs(source, target){
    const queue = [source]
    const visited = Array.from({length: this.lists.length}, () => false)
    const parent = Array.from({length: this.lists.length}, () => -1)
    const dist = Array.from({length: this.lists.length}, () => 0)
    let result = ''
    while(queue.length > 0){
      const current = queue.shift();
      
      for(const v of this.lists[current]){
        if(!visited[v]){
          visited[v] = true;
          parent[v] = current;
          dist[v] = dist[current] + 1;
          queue.push(v);
        }
      }

      result += `${current} -> `
    }
    console.log('BFS Result : ', result)
    
    // Print the Fasted Node Neede
    for(let i=0;i<this.lists.length;i++){
      console.log(`Fasted Node Needed To ${i} From ${source} Is ${dist[i]}`)
    }

    // Backtracking Target Node
    let cursor = parent[target];
    result = ''
    while(cursor != -1){
      result += `${cursor} <- `
      cursor = parent[cursor];
    }
    console.log("Backtracking Fast Result : ", result)
  }
}

const graph = new Graph(7);
graph.addEdge(1, 2, true)
graph.addEdge(1, 0, true)
graph.addEdge(2, 3, true)
graph.addEdge(3, 4, true)
graph.addEdge(0, 4, true)
graph.addEdge(4, 5, true)
graph.addEdge(5, 6, true)
graph.bfs(1,6);