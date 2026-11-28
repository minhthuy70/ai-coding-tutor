<!-- page: 1 -->

## [QHD Basic]. Bài 1. Giai Thừa Chia Dư

```txt
Problem	Submissions	Discussions

Đề bài rất đơn giản, bạn hây tính N! chia dư cho (10^9 + 7).
Gợi ò : Xây dựng mảng F[], trong đó F[i] lưu il chia dư cho 10^9 + 7, mỗi test nhập n thì chỉ cần in ra F[n].
Input Format
• Dòng 1 là số bộ test T
• T dòng tiếp theo mỗi dòng là 1 số nguyên không âm N
Constraints
• 1<=T<=10000
• 0<=N<=10^6
Output Format
Đưa ra kết quả của mỗi test trên 1 dòng
Sample Input 0

5
11
6
8
10
13

Sample Output 0

39916800
720
40320
3626800
227020758
```

<!-- page: 2 -->

## [QHD Basic]. Bài 2. Fibonacci

```txt
Problem	Submissions	Discussions

Cho đầy số Fibonacci với F[0] = 0, F[1] = 1, F[n] = F[n - 1] + F[n - 2] với n >= 2. Hầy tính F[n] chia dư cho 10^9 + 7.
Input Format
• Dòng 1 là số bộ test T
• T dòng tiếp theo mỗi dòng là 1 số nguyên không âm N
Constraints
• 1<=T<=10000
• 0<=N<=10^6
Output Format
Đưa ra kết quả của mỗi test trên 1 dòng
Sample Input 0

6
5
13
10
14
8
11

Sample Output 0

5
233
55
377
21
89
```

<!-- page: 3 -->

## [QHD Basic]. Bài 3. Tribonacci

```txt
Problem	Submissions	Discussions

Cho d$y$ s$o Tribonacci vói F[0] = 0, F[1] = 0, F[2] = 1, F[n] = F[n - 1] + F[n - 2] + F[n - 3] vói n >= 3. H$ay$ tinh F[n] chia du cho $10^{9} + 7$.

Input Format
• Dòng 1 là s$o bó test T$
• T dòng tiếp theo mõi dòng là 1 s$o nguyên kh$ông âm N

Constraints
• 1<=T<=10000
• 0<=N<=10^6

Output Format

Đưa ra kết quả của mõi test trèn 1 dòng

Sample Input 0

7
8
14
12
7
9
7
12

Sample Output 0

24
927
274
13
44
13
274
```

<!-- page: 4 -->

## [QHD Basic]. Bài 4. Prime 1

```txt
Problem	Submissions	Discussions

Cho số nguyên dương N, hấy đếm xem trong đoạn từ 0 tới N có bao nhiêu số nguyên tố. Hướng dẫn :
• Bước 1 : Sàng số nguyên tố
• Bước 2 : Gọi F[i] là số lượng các số nguyên tố từ 0 tới i, xây dựng màng F[i] sau khi sàng

Input Format

• Dòng 1 là số bộ test T
• T dòng tiếp theo mỗi dòng là 1 số nguyên không âm N

Constraints

• 1<=T<=10000
• 0<=N<=10^6

Output Format

Đưa ra kết quả của mỗi test trên 1 dòng

Sample Input 0

5
39
68
26
87
6

Sample Output 0

12
19
9
23
3
```

<!-- page: 5 -->

## [QHD Basic]. Bài 5. Prime 2

```txt
Problem	Submissions	Discussions

Cho 2 số nguyên L, R, hảy đếm xem trong đoạn từ L tới R có bao nhiêu số nguyên tố.
Gọi ý :
• Bước 1 : Sàng số nguyên tố
• Bước 2 : Gọi F[i] là số các nguyên tố từ 0 tới i, khi đó số các số nguyên tố từ L tới R là F[R] - F[L - 1]
Input Format
• Dòng 1 là số bộ test T
• T dòng tiếp theo mỗi dòng là 2 số nguyên không âm L, R
Constraints
• 1<=T<=10000
• 0<=L<=R<=10^6
Output Format
Đưa ra kết quả của mỗi test trên 1 đồng
Sample Input 0

5
3 19
4 65
4 44
1 17
1 7

Sample Output 0

7
16
12
7
4
```

<!-- page: 6 -->

## [QHD Basic]. Bài 6. Prime 3

```csv
Problem	Submissions	Discussions

Cho số nguyên dương N, hấy tính tích các số nguyên tố trong đoạn từ 0 đến N. Khi N = 0 hoặc 1 thì đáp án là 0.

Input Format
• Dòng 1 là số bộ test T
• T dòng tiếp theo mỗi dòng là 1 số nguyên không âm N

Constraints
■ 1<=T<=10000
■ 0<=N<=10^6

Output Format
Đưa ra kết quả của mỗi test trên 1 đồng, vì kết quả quả lớn nên hây chia dư cho 10^9 + 7.

Sample Input 0

5
20
16
10
22
29

Sample Output 0

9699690
30039
210
9699690
469693188
```
