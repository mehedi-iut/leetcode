/*
ninja is planing this n days long training schedule each day he can perform any one-of-these-three-activities
- running 
- fighting
- practice or learning-new-moves
each-activity-has-some-merit-points-on-each-day
-as-ninja-has-to-improve-all-his-skills-he-can-t-do-the-same-activity-in-two-consecutive-days-
can-you-help-ninja-find-out-the-maximum-merit-points-ninja-can-earn"
Ninja is planing this ‘N’ days-long training schedule. 
Each day, he can perform any one of these three activities. (Running, Fighting Practice or Learning New Moves). 
Each activity has some merit points on each day. 
As Ninja has to improve all his skills, he can’t do the same activity in two consecutive days. 
Can you help Ninja find out the maximum merit points Ninja can earn?

you-are-given-a-2d-array-of-size-n-3-points-with-the-points-corresponding-to-each-day-and-activity-
your-task-is-to-calculate-the-maximum-number-of-merit-points-that-ninja-can-earn"
You are given a 2D array of size N*3  ‘POINTS’ with the points corresponding to each day and activity.
Your task is to calculate the maximum number of merit points that Ninja can earn

If the given ‘POINTS’ array is [[1,2,5], [3 ,1 ,1] ,[3,3,3] ],the answer will be 11 as 5 + 3 + 3.
*/
package main

import (
	"fmt"
)

func main(){
	points := [][]int{
		[]int{10, 40, 70},
		[]int{20, 50, 80},
		[]int{30, 60, 90},
	}
	fmt.Println(points)
	n := len(points)
	c := len(points[0])
	// recursive solution
	res := recursive(points, n-1, 3)
	// memoization
	dp := make([][]int, n)
	for i:=0; i< n; i++{
		dp[i] = make([]int, 4)
		for j:=0; j<4; j++{
			dp[i][j] = -1
		}
	}
	// res_memo := recursive_memo(points, dp, n-1, 3)

	// tabulation
	dp[0][0] = maxval(points[0][1], points[0][2])
	dp[0][1] = maxval(points[0][0], points[0][2])
	dp[0][2] = maxval(points[0][0], points[0][1])
	dp[0][3] = maxval(points[0][0], maxval(points[0][1], points[0][2]))
	for day:=1; day < n; day++{
		for last:=0; last < 4; last++{
			dp[day][last] = 0
			for task:=0; task < 3; task++{
				if task != last{
					pts := points[day][task] + dp[day-1][task]
					dp[day][last] = maxval(pts, dp[day][last])
				}
			}
		}
	}


	// space optimize
	prev := make([]int, n+1)

	prev[0] = maxval(points[0][1], points[0][2])
	prev[1] = maxval(points[0][0], points[0][2])
	prev[2] = maxval(points[0][0], points[0][1])
	prev[3] = maxval(points[0][0], maxval(points[0][1], points[0][2]))
	for day:=1; day < n; day++{
		temp := make([]int, n+1)
		for last:=0; last < 4; last++{
			for task:=0; task < 3; task++{
				if task != last{
					pts := points[day][task] + prev[task]
					temp[last] = maxval(pts, temp[last])
				}
			}
		}
		prev = temp
	}


	fmt.Println(res, dp[n-1][3], prev[c])
}

func recursive_memo(points [][]int, dp [][]int, day int, last int) int {
	if day == 0{
		max := 0
		for i:=0; i<3; i++{
			if i != last{
				max = maxval(points[0][i], max)
			}	
			
		}
		return max
	}

	if dp[day][last] != -1{
		return dp[day][last]
	}

	max:=0
	for task:=0; task < 3; task ++{
		if task != last{
			pts := points[day][task] + recursive(points, day-1, task)
			max = maxval(pts, max)
		}
	}
	dp[day][last] = max
	return dp[day][last]
}

func recursive(points [][]int, day int, last int) int {
	if day == 0{
		max := 0
		for i:=0; i<3; i++{
			if i != last{
				max = maxval(points[0][i], max)
			}	
			
		}
		return max
	}

	max:=0
	for task:=0; task < 3; task ++{
		if task != last{
			pts := points[day][task] + recursive(points, day-1, task)
			max = maxval(pts, max)
		}
	}

	return max

}

func maxval(a int, b int) int {
	if a > b{
		return a
	}
	return b
}