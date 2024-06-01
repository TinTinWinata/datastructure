class Node {
  constructor(data, next = null){
    this.data = data;
    this.next = next;
  }
}

let tail, head = null;

function popHead(){
  if(!head){
    throw 'There is no node to be deleted!';
  }
  let toBeDeleteNode = head;
  head = head.next;

  if(!head){
    tail = null;
  }

  toBeDeleteNode.next, toBeDeleteNode = null;
}

function printAll(){
  let current = head;
  let result = ''
  while(current){
    result += `-> ${current.data} `
    current = current.next;
  }
  console.log('Result : ', result)
}

function pushHead(node){
  if(!head){
    head = tail = node;
  } else {
    node.next = head;
    head = node;
  }
}

function pushTail(node){
  if(!head){
    head = tail = node;
  } else{
    tail.next = node;
    tail = node;
  }
}

pushTail(new Node('Node 1'))
pushTail(new Node('Node 2'))
pushTail(new Node('Node 3'))
pushHead(new Node('Node 0'))
popHead();
printAll();