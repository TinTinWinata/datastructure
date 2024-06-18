/**
 * @param {number[]} difficulty
 * @param {number[]} profit
 * @param {number[]} worker
 * @return {number}
 */
var maxProfitAssignment = function(difficulty, profit, worker) {
  
  const indices = Array.from({length: difficulty.length}, (_, i) => i);
  indices.sort((a, b) => difficulty[a] - difficulty[b])
  
  difficulty = indices.map((i) => difficulty[i])
  profit = indices.map((i) => profit[i])
  worker.sort((a, b) => a - b)
  let result = 0;
  let tempResult = 0;
  let pivot = 0;
  for(const w of worker){
    while(difficulty[pivot] && difficulty[pivot] <= w){
      // console.log(`W ${w} | Difficulty ${difficulty[pivot]} | Profit ${profit[pivot]}`)
      if(tempResult === 0){
        tempResult = profit[pivot];
      } else {
        tempResult = Math.max(tempResult, profit[pivot]);
      }
      pivot++
    }
    // console.log(`W ${w} | Temp Result ${tempResult}`)
    result += tempResult;
  }
  return result;
};

// console.log(maxProfitAssignment([10, 2,4,6,8], [50, 10,20,30,40], [4,5,6,7]))
console.log(maxProfitAssignment([13,37,58], [4,90,96], [34,73,45]))