/**
 Do not return anything, modify board in-place instead.
 */

const iStep = [0, 0, 1, -1]
const jStep = [1, -1, 0, 0]

 function dfs(i, j, boards, m, n, visited) {
  
  const c = boards[i][j]
//   console.log(`${c}[${i}][${j}]`)
  if(c === 'X' || visited.has(`${i}#${j}`)) {
     return true;
  }

  visited.add(`${i}#${j}`)

  if(c === 'O' && (i >= n - 1 || i <= 0 || j >= m - 1 || j <= 0)) {
     return false;
  } 

  return  dfs(i + 1, j, boards, m, n, visited) && 
  dfs(i - 1,j, boards, m, n, visited) && 
  dfs(i, j + 1, boards, m, n, visited) &&
  dfs(i, j - 1, boards, m, n, visited);
}

function solve(board) {
 const n = board.length;
 const m = board[0].length;
 for(let i=1;i<board.length - 1;i++){
     for(let j=1;j<board[0].length - 1;j++){
         if(board[i][j] === 'O') {
             const visited = new Set();
            //  console.log('start dfs')
             if(dfs(i, j, board, m, n, visited)) {
                const queue = [{i, j}];
                const visited = new Set();
                visited.add(`${i}#${j}`)
                while(queue.length > 0){
                    const x = queue.shift();
                    board[x.i][x.j] = 'X'
                    for(let k=0;k<4;k++){
                        const nI = x.i + iStep[k]
                        const nJ = x.j + jStep[k]
                        if(!visited.has(`${nI}#${nJ}`) && board[nI] && board[nI][nJ] && board[nI][nJ] === 'O') {
                            visited.add(`${nI}#${nJ}`)
                            queue.push({i: nI, j: nJ})
                        }
                    }
                }
             }
         } 
     }
 }
};

const boards = [
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"],
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"]]

console.log('Before : ', boards)
solve(boards)
console.log('Results : ', boards)

