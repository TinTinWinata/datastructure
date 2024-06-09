

class Node {
  constructor(val, isTerminal = false){
    this.val = val;
    this.map = {};
    this.isTerminal = isTerminal;
  }
}
class Trie {
  constructor(){
    this.root = new Node('\0')
  }

  insert(word){
    let cursor = this.root;
    for(const char of word){
      if(cursor.map[char] === undefined){
        const newNode = new Node(char);
        cursor.map[char] = newNode;
      } 
      cursor = cursor.map[char];
    }
    cursor.isTerminal = true;
  }

  search(word){
    let cursor = this.root;
    for(const char of word){
      if(cursor.map[char] === undefined) {
        return false;
      }
      cursor = cursor.map[char];
    }
    return cursor.isTerminal;
  }
}

const words = ['apple', 'ape', 'no', 'news', 'not', 'never']
const trie = new Trie();
for(const word of words){
  trie.insert(word);
}
console.log(trie.search('apple'))
