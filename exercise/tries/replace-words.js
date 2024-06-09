class Node {
  constructor(v){
    this.v = v;
    this.map = {}
    this.terminal = false;
  }
}

class Trie {
  constructor(){
    this.root = new Node('\0');
  }
  insert(word){
    let cursor = this.root;
    for(const char of word){
      if(cursor.map[char] ===  undefined){
        cursor.map[char] = new Node(char);
      }
      cursor = cursor.map[char];
    }
    cursor.terminal = true;
  }

  searchPrefix(word){
    if(this.root.map[word.charAt(0)] === undefined){
      return null;
    }
    let cursor = this.root;
    let text = ''
    const stack = []
    // console.log('Search Prefix : ', word)
    for(const char of word){
      // console.log('word : ', word , '   stack : ', stack)
      if(cursor.map[char] ===  undefined){
        return stack.pop();
      } 
      text += char;
      if(cursor.map[char].terminal){
        stack.unshift(text)
      }
      cursor = cursor.map[char];
    }
    return stack.pop();
  }
}

/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function(dictionary, sentence) {
    const trie = new Trie();
    for(const dict of dictionary){
      trie.insert(dict);
    }
    return sentence.split(' ').map((word) => {
      const prefix = trie.searchPrefix(word);
      if(prefix === null || prefix === undefined) return word;
      return prefix;
    }).join(' ')
};

console.log(replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery"))