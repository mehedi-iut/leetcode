package main

import (
	"fmt"
)

// func main(){
// 	triangle := [][]int{
// 		[]int{2},
// 		[]int{3,4},
// 		[]int{6,5,7},
// 		[]int{4,1,8,3},
// 	}

// 	dp := make([][]int, len(triangle))
//     for i:=0; i< len(triangle); i++{
//         dp[i] = make([]int, len(triangle[i]))
//         for j:=0; j<len(triangle[i]); j++{
//             dp[i][j] = -1
//         }
//     }

// 	res := recurse(0, 0, triangle, dp)

// 	fmt.Println(res)

// }

// func recurse(n int, c int, triangle [][]int, dp [][]int) int {
// 	if n == len(triangle)-1{
// 		return triangle[n][c]
// 	}

// 	if dp[n][c] != -1{
// 		return dp[n][c]
// 	}

// 	down := triangle[n][c] + recurse(n+1, c, triangle, dp)
// 	diag := triangle[n][c] + recurse(n+1, c+1, triangle, dp)
// 	total := minval(down, diag)

// 	dp[n][c] = total
// 	return dp[n][c]
// }

// with anonymous function
func main(){
	triangle := [][]int{
		[]int{2},
		[]int{3,4},
		[]int{6,5,7},
		[]int{4,1,8,3},
	}
		
	dp := make([][]int, len(triangle))
	for i:=0; i< len(triangle); i++{
		dp[i] = make([]int, len(triangle[i]))
		for j:=0; j<len(triangle[i]); j++{
			dp[i][j] = -1
		}
	}

	var dfs func(row, col int) int
	dfs = func(row, col int) int {
		if row == len(triangle)-1{
			return triangle[row][col]
		}

		if dp[row][col] != -1 {
			return dp[row][col]
		}

		down := triangle[row][col] + dfs(row+1, col)
		diag := triangle[row][col] + dfs(row+1, col+1)
		dp[row][col] = minval(down, diag)
		return dp[row][col]
	}

	dfs(0, 0)

	fmt.Println(dp[0][0])
}


func minval(a int, b int) int {
	if a > b{
		return b
	}

	return a
}

