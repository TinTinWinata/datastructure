class Node {
  constructor(data, next = null, prev = null){
    this.data = data;
    this.next = next;
    this.prev = prev;
  }
}

let head, tail = null;

function pushHead(node){
  if(!head){
    head = tail = node;
  } else {
    node.next = head;
    head.prev = node;
    head = node;
  }
}

function popTail(){
  if(!head){
    throw 'There is no node to be deleted!'
  }
  let toBeDeletedNode = tail;
  tail = tail.prev;
  tail.next = null;

  if(!head){
    tail = null;
  }

  toBeDeletedNode.prev, toBeDeletedNode = null;
}


function popHead(){
  if(!head){
    throw 'There is no node to be deleted!'
  }
  let toBeDeletedNode = head;
  head = head.next;
  head.prev = null;

  if(!head){
    tail = null;
  }

  toBeDeletedNode.next, toBeDeletedNode = null;
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

function pushTail(node){
  if(head === null){
    head = tail = node;
  } else {
    tail.next = node;
    node.prev = tail;
    tail = node;
  }
}

pushHead(new Node('Node 1'))
pushTail(new Node('Node 2'))
pushTail(new Node('Node 3'))
popTail();
popHead();

printAll();