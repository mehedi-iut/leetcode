package main

import (
	"fmt"
	"math"
)

func main(){
	// matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
	matrix := [][]byte{
		[]byte{1,0,1,0,0},
		[]byte{1,0,1,1,1},
		[]byte{1,1,1,1,1},
		[]byte{1,0,0,1,0},
	}

	fmt.Println(matrix)

	m, n := len(matrix), len(matrix[0])
	// for memoization
	memo := make([][]int, m)
	for i:=0; i<m; i++{
		memo[i] = make([]int, n)
		for j:=0; j< n; j++{
			memo[i][j] = -1
		}
	}


	res := 0
	// dp(matrix, m-1, n-1, &res)
	dpMemo(matrix, m-1, n-1, &res, memo)
	fmt.Println(res*res)
}

func dp(matrix [][]byte, r int, c int, res *int) int {
	if r < 0 || c < 0{
		return 0
	}
	up := dp(matrix, r-1, c, res)
	left := dp(matrix, r, c-1, res)
	diag := dp(matrix, r-1, c-1, res)
	val := 0
	if matrix[r][c] != 0{
		val = 1 + int(math.Min(float64(up), math.Min(float64(left), float64(diag))))
	}

	*res = int(math.Max(float64(*res), float64(val)))
	return val
}

func dpMemo(matrix [][]byte, r int, c int, res *int, memo [][]int) int {
	if r < 0 || c < 0 {
		return 0
	}
	if memo[r][c] != -1 {
		return memo[r][c]
	}

	up := dp(matrix, r-1, c, res)
	left := dp(matrix, r, c-1, res)
	diag := dp(matrix, r-1, c-1, res)
	val := 0
	if matrix[r][c] != 0{
		val = 1 + int(math.Min(float64(up), math.Min(float64(left), float64(diag))))
	}

	memo[r][c] = val
	*res = int(math.Max(float64(*res), float64(val)))
	return memo[r][c]
}