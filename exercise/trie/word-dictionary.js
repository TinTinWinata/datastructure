
class Node {
  constructor(d){
    this.d = d;
    this.map = {};
    this.terminal = false;
  }
}

class Trie {
  constructor(){
    this.root = new Node('\n')
  }
  add(words){
    let cursor = this.root;
    for(const c of words){
      if(cursor.map[c] === undefined){
        cursor.map[c] = new Node(c)
      }
      cursor = cursor.map[c];
    }
    cursor.terminal = true;
  }
  dfs(pivot, word, node){
    if(pivot >= word.length) {
      if(node.terminal) {
        return true;
      } else {
        return false;
      }
    }

    const c = word.charAt(pivot);
    // console.log(`pivot ${pivot} | c ${c}`)
    let result = false;
    if(c === '.'){
      for(const k of Object.keys(node.map)){
        const v = node.map[k];
        if(this.dfs(pivot + 1, word, v)){
          result = true;
        }
      }
    } else if(node.map[c] === undefined) {
      return false;
      } else if(this.dfs(pivot + 1, word, node.map[c])){
      result = true;
    }
    return result;
  }
  search(key){
    return this.dfs(0, key, this.root);
  }
}

let t;
var WordDictionary = function() {
  t = new Trie();
};

/** 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
  t.add(word)
};

/** 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    return t.search(word)
};

/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

// t.add('justine')

// console.log(t.search('a'))