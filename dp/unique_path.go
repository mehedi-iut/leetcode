package main

import "fmt"

func main(){
	m, n := 3, 7
	memo := make([][]int, m)
	for i:=0; i< m; i++{
		memo[i] = make([]int, n)
		for j:=0; j<n; j++{
			memo[i][j] = -1
		}
	}
	// recursion approach
	// res := recurse_memo(m-1, n-1, memo)
	// fmt.Println(res)
	// Tabulation method
	for i:=0; i<m; i++{
		for j:=0; j<n; j++{
			if i == 0 || j == 0{
				memo[i][j] = 1
			} else {
				memo[i][j] = memo[i-1][j] + memo[i][j-1]
			}

		}
	}
	fmt.Println(memo[m-1][n-1])
}

// recursion only

func recurse(r int, c int) int{
	if r == 0 && c == 0{
		return 1
	}

	if r < 0 || c < 0{
		return 0
	}

	up := recurse(r-1, c)
	left := recurse(r, c-1)
	return up + left
}

func recurse_memo(r int, c int, memo [][]int ) int {
	if r == 0 && c == 0{
		return 1
	}
	if r < 0 || c < 0{
		return 0
	}
	if memo[r][c] != -1{
		return memo[r][c]
	}

	up := recurse_memo(r-1, c, memo)
	left := recurse_memo(r, c-1, memo)
	memo[r][c] =  up + left
	return memo[r][c]
}