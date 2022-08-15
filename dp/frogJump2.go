package main

import (
	"fmt"
	"math"
)

func main(){
	n:= 5
	k:= 3
	h:= []int{10, 30, 40, 50, 20}

	// // recursive solution
	// res := recurse(n-1, k, h)
	// fmt.Println(res)

	// memoization
	dp := make([]int, n+1)
	for i:=0; i<=n; i++{
		dp[i] = -1
	}

	res := recurse_memo(n-1, k, h, dp)
	fmt.Println(res)



	// Tabulation method
	for i:=0; i<n; i++{
		dp[0] = 0
		minSteps := math.MaxInt
		for j:=0; j<=k; j++{
			if i-j >= 0{
				steps:= dp[i-j] + int(math.Abs(float64(h[i])-float64(h[i-j])))
				minSteps = min(minSteps, steps)
			}
		}
		dp[i] = minSteps
	}
	fmt.Println(dp[n-1])
}

func recurse(n int, k int, h []int) int {
	if n == 0{
		return 0
	}

	minSteps := math.MaxInt

	for i:=1; i<=k; i++{
		if n-i>=0{
			steps := recurse(n-i, i, h) + int(math.Abs(float64(h[n-i]) - float64(h[n])))
			minSteps = min(steps, minSteps)
		}
		
	}
	return minSteps
}

func recurse_memo(n int, k int, h []int, dp []int) int {
	if n == 0{
		return 0
	}

	if dp[n] != -1{
		return dp[n]
	}

	minSteps := math.MaxInt

	for i:=1; i<=k; i++{
		if n-i>=0{
			steps := recurse_memo(n-i, i, h, dp) + int(math.Abs(float64(h[n-i]) - float64(h[n])))
			minSteps = min(steps, minSteps)
		}	
	}
	dp[n] = minSteps
	return dp[n]
}

func min(a int, b int) int {
	if a < b{
		return a
	}
	return b
}