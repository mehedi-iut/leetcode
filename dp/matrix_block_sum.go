package main

import (
	"fmt"
	"math"
)

func main(){
	// [[67,64,78],[99,98,38],[82,46,46],[6,52,55],[55,99,45]]
	// output: [[731,731,731],[930,930,930],[930,930,930],[930,930,930],[721,721,721]]

	mat := [][]int{
		[]int{67,64,78},
		[]int{99,98,38},
		[]int{82,46,46},
		[]int{6,52,55},
		[]int{55,99,45},
	}
	m := len(mat)
	n := len(mat[0])
	k := 3
	prefMat := make([][]int, m)
	for i:=0; i<m; i++{
		prefMat[i] = make([]int, n)
		prefMat[i][0] = mat[i][0]
		for j:=1; j<n; j++{
			prefMat[i][j] = prefMat[i][j-1] + mat[i][j]
		}
	}

	for j:=0; j<n; j++{
		prefMat[0][j] = prefMat[0][j]
		for i:=1; i < m; i++{
			prefMat[i][j] = prefMat[i-1][j] + prefMat[i][j]
		}
	}

	fmt.Println(prefMat)

	for i:=0; i<m; i++{
		row_upper := int(math.Max(float64(0), float64(i-k)))
		row_down := int(math.Min(float64(i+k), float64(m-1)))

		for j:=0; j<n; j++{
			col_upper := int(math.Max(float64(0), float64(j-k)))
			col_down := int(math.Min(float64(j+k), float64(n-1)))

			value := prefMat[row_down][col_down]

			if row_upper-1 >= 0{
				value -= prefMat[row_upper-1][col_down]
			}
			if col_upper-1 >= 0{
				value -= prefMat[row_down][col_upper-1]
			}
			if row_upper-1 >= 0 && col_upper-1 >= 0{
				value += prefMat[row_upper-1][col_upper-1]
			}
			mat[i][j] = value
		}
	}
	fmt.Println(mat)
}