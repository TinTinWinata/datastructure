#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
      int n = height.size();
      vector<int> lefts;
      vector<int> rights;

      // 1. Define the Heighest Left and Heighest Right
      int highest = 0;
      for(int i=0;i<height.size();i++){ 
        if(height.at(i) > highest) {   
          highest = height.at(i);
        }
        lefts.push_back(highest);
      }

      highest = 0;
      for(int i=n-1;i>=0;i--){
        if(height.at(i) > highest){
          highest = height.at(i);
        }
        rights.push_back(highest);
      }

      reverse(rights.begin(), rights.end());

      // 2. Calculate with the Equation : min(l, r) - h[i]
      int result = 0;
      for(int i=0;i<n;i++){
        result += min(lefts[i], rights[i]) - height.at(i);
      }

      return result;
    }
};

int main(){
    Solution s;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    int result = s.trap(height);
    cout << "Result : " << result << "\n";
    return 0;
}
