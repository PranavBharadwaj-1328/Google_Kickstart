# Google_Kickstart
Problem

There are N people numbered from 1 to N, standing in a queue to withdraw money from an ATM. The queue is formed in ascending order of their number. The person numbered i wants to withdraw amount Ai. The maximum amount a person can withdraw at a time is X. If they need more money than X, they need to go stand at the end of the queue and wait for their turn in line. A person leaves the queue once they have withdrawn the required amount.

You need to find the order in which all the people leave the queue.
Input

The first line of the input gives the number of test cases T. T test cases follow.

The first line of each test case gives two space separated integers: the number of people standing in the queue, N and the maximum amount X that can be withdrawn in one turn.

The next line contains N space separated integers A_{i}.

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the space separated list of integers that denote the order in which the people leave the queue.
Limits

Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
Test Set 1

1 ≤ N ≤ 100.
1 ≤ Ai ≤ 100.
1 ≤ X ≤ 100.
Test Set 2

1 ≤ N ≤ 105 for at most 10 test cases. For the remaining cases, 1 ≤ N ≤ 100
1 ≤ Ai ≤ 109.
1 ≤ X ≤ 109.
Sample

Input           Output
 

2
3 3
2 7 4         Case #1: 1 3 2
5 6
9 10 4 7 2    Case #2: 3 5 1 2 4
