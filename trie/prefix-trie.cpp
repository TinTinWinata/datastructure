#include <iostream>
#include <unordered_map>
using namespace std;

class Node {
  public:
    char data;
    unordered_map<char, Node*> map;
    bool terminal;
    Node(char _data){
      data = _data;
      terminal = false;
    }
};

class Trie {
public:
    Node* root;
    Trie() {
      root = new Node('\0');
    }
    
    void insert(string word) {
      Node *cursor = root;
      for(char w : word){
        if(cursor->map.count(w) == 0){
          cursor->map[w] = new Node(w);
        }
        cursor = cursor->map[w];
      }
      cursor->terminal = true;
    }
    
    bool search(string word) {
        Node *cursor = root;
        for(char w : word){
          if(cursor->map.count(w) == 0){
            return false;
          }
          cursor = cursor->map[w];
        }
        return cursor->terminal;
    }
    
    bool startsWith(string prefix) {
      Node *cursor = root;
      for(char w : prefix){
        if(cursor->map.count(w) == 0){
          return false;
        }
        cursor = cursor->map[w];
      }
      return true;
    }
};

int main(){
  Trie* trie = new Trie();
  trie->insert("hello");
  return 0;
}