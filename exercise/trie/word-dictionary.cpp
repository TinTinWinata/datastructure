#include <iostream>
#include <map>
using namespace std;

class Node {
  public:
    char d;
    map<char, Node*> map;
    bool terminal;

    Node(char _d){
      d = _d;
      terminal = false;
    }
};

class WordDictionary {
public:
    Node* root;
    WordDictionary() {
      root = new Node('\0');
    }
    
    void addWord(string word) {
      Node* cursor = root;
      for(char w : word){
        if(cursor->map.count(w) == 0) {
          cursor->map[w] = new Node(w);
        }
        cursor = cursor->map[w];
      }
      cursor->terminal = true;
    }

    bool dfs(int pivot, string word, Node *node){
      if(pivot >= word.length()) {
        if(node->terminal) {
          return true;
        }
        return false; 
      }
      char c = word.at(pivot);
      bool result = false;
      if(c == '.') {
        for(auto& pair : node->map) {
          if(dfs(pivot + 1, word, pair.second)) {
            result = true;
          }
        }
      } else if(node->map.count(c) == 0){
        return false;
      } else if(dfs(pivot + 1, word, node->map[c])){
        result = true;
      }
      return result;
    }

    bool search(string word) {
      return dfs(0, word, root);
    }
};

int main(){
  WordDictionary *dict = new WordDictionary();
  dict->addWord("bad");
  dict->addWord("dad");
  dict->addWord("mad");

  cout << "Result : " << dict->search("") << "\n";
  return 0;
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */