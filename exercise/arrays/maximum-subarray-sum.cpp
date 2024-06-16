// Maximum Subarray Sum
// Implement a function that takes an input a vector of integers, and prints the maximum subarray sum that can be formed. A subarray is defined as consecutive segment of the array. If all numbers are negative, then return 0.

// Input
// {-1,2,3,4,-2,6,-8,3}

// Output
// 13

// Hint
// Expected Time Complexity
// O(N)

// Space Complexity
// O(1)

#include <iostream>
#include<vector>
using namespace std;

int maxSubarraySum(vector<int> arr){
    //Complete this function, your function should return the maximum subarray sum
    int n = arr.size();
    int max = -1;
    int temp = 0;
    for(int i=0;i<n;i++){
        temp += arr.at(i);
        if(temp < 0) {
            temp = 0;
        }
        if(temp > max) {
            max = temp;
        }
    }
    return max;
}

int main(){
  vector<int> nums = {-1,2,3,4,-2,6,-8,3};
  int res = maxSubarraySum(nums);
  cout << "Result : " << res << endl;
  return 0;
}