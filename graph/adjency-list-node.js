class Node {
  constructor(name) {
    this.name = name;
    this.neighbors = [];
  }
}

class Graph {
  constructor(names){
    this.map = new Map();
    for(const name of names){
      this.map.set(name, new Node(name));
    }
  }
  printAll(){
    for(const key of this.map.keys()){
      const node = this.map.get(key);
      let result = `${node.name} : `
      for(const neighbor of node.neighbors){
        result += `${neighbor.name} -> `
      }
      console.log(result)
    }
  }
  addEdge(namesFrom, namesTo, dir){
    const fromNode = this.map.get(namesFrom);
    const toNode = this.map.get(namesTo);
    fromNode.neighbors.push(toNode);
    if(dir){
      toNode.neighbors.push(fromNode);
    }
  }
}

const graph = new Graph(['Delhi', 'London', 'Paris', 'New York'])
graph.addEdge("Delhi", "London")
graph.addEdge("New York", "London")
graph.addEdge("Delhi", "Paris")
graph.addEdge("Paris", "New York")
graph.printAll();