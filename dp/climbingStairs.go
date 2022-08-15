package main

import "fmt"

func climbStairs(n int) int {
	res := recurse(n)
	return res
}

func recurse(n int) int {
	if n == 0{
		return 1
	}
	if n < 0{
		return 0
	}

	step1 := recurse(n-1)
	step2 := recurse(n-2)

	return step2 + step1
}

func main(){
	n := 2
	res := climbStairs(n)
	fmt.Println(res)
}