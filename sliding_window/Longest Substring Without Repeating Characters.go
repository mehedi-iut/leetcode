package main

import (
	"fmt"
)

func main(){
	// s := "abcabcbb"
	s := "pwwkew"
	fmt.Println(s)

	bucket := map[byte]bool{}
	start := 0
	maxLength := 0

	for end:=0; end<len(s); end++{
		for bucket[s[end]]{
			bucket[s[start]] = false
			start++
		}
		bucket[s[end]] = true

		if end - start + 1 > maxLength{
			maxLength = end-start+1
		}
	}

	fmt.Println(maxLength)
}

func findMax(a,b int)int{
	if a>b{
		return a
	}
	return b
}