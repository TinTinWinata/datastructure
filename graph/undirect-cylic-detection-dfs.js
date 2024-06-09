
class Graph {
  constructor(){
    this.map = {}
  }

  addEdge(i, j){
    if(this.map[i]){
      this.map[i].push(j)
    } else {
      this.map[i] = [j]
    }

    if(this.map[j]){
      this.map[j].push(i)
    } else {
      this.map[j] = [i];
    }
  }
  
  /**
   * @param {number} v
   * @param {Object} parent
   * @param {Object} visited
   */
  dfs(v, parent, visited) {
    visited[v] = true;
    let isCyclic = false;
    for(const n of this.map[v]) {
      if(visited[n]){
        if(n !== parent[v]) {
          return true;
        }
        continue;
      }
      parent[n] = v;
      const temp = this.dfs(n, parent, visited);
      if(temp) {
          isCyclic = temp;
      }
    }
    return isCyclic;
  }
  isCyclic(start){
    return this.dfs(start, {}, {})
  }
}

/**
 * @param {number[][]} edges
 * @return {number[]}
 */
var isCyclic = function(edges) {
    const g = new Graph()
    for(const [i, j] of edges){
      g.addEdge(i, j)
    }
    return g.isCyclic(edges[0][0]);
};

console.log(isCyclic([[1,2],[1,3],[2,3]]))