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

function maxSubarraySum(nums){
    let maxSum = Number.NEGATIVE_INFINITY;
    let currSum = 0;
    for(const num of nums){
        currSum += num;
        if(currSum > maxSum){
            maxSum = currSum;
        }
        if(currSum < 0){
            currSum = 0;
        }
    }
    return maxSum;
}

console.log(maxSubarraySum([-2,1,-3,4,-1,2,1,-5,4]))