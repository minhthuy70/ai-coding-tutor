## [Set Map]. Bài 1. Phần tử phân biệt

```txt
Problem	Submissions	Leaderboard	Discussions

Cho dãy số A[] gồm có N phần tử, bạn hãy đếm xem trong màng có bao nhiêu phần tử phân biệt? Chú ý giải bài này với 3 cách : Sử dụng set, map, sắp xếp.

Nếu dùng set hoặc map bạn chỉ cần đưa các phần tử vào set hoặc đưa phần tử vào làm key trong map thì nó sẽ tự loại bổ trùng, khi đó size của set và map sẽ là số lượng phần tử khác nhau trong màng A[] ban đầu. 3 cách dùng set, map, sort đều có độ phức tạp là O(NlogN) nên bạn dùng cách nào cũng được

Input Format

Dòng đầu tiên là số nguyên N. Dòng tiếp theo gồm N số nguyên A[i]

Constraints

1≤ N ≤ 10^5; -10^9 ≤ A[i] ≤ 10^9

Output Format

In ra số lượng phần tử khác nhau trong màng.

Sample Input 0

5
2 1 2 1 3

Sample Output 0

3
```

## [Set Map]. Bài 2. Truy vấn phần tử trong màng.

```txt
Problem	Submissions	Leaderboard	Discussions

Cho đầy số A[] gồm có N phần tử, bạn hấy trả lời các truy vấn đề xác định xem phần tử X nào đó có nằm trong mảng hay không? Bạn hấy thử giải bài này bằng 3 cách : Set, Map, Binary Search.

Nếu dùng set, map để lưu mảng A[] mỗi truy vấn tìm kiếm (hàm find) bạn chỉ mất độ phức tạp O(logN) thay vì O(N) như duyệt tuần tự, tương tự bạn có thể sort mảng A[] để áp dụng tìm kiếm nhị phân trên mỗi truy vấn.

Input Format
• Đồng đầu tiên là số nguyên N.
• Đồng thứ 2 gồm N số nguyên A[i]
• Đồng thứ 3 là số lượng truy vấn Q.
• Q dòng tiếp theo mỗi dòng là một số nguyên X.

Constraints
1≤ N ≤ 10^5; 0 ≤ A[i]. X ≤ 10^9; 1≤ Q ≤ 1000;

Output Format
Đối với mỗi truy vấn in ra YES nếu phần tử X xuất hiện trong mảng, ngược lại in ra NO.

Sample Input 0

5
1 2 1 3 4
2
1
6

Sample Output 0

YES
NO
```

## [Set Map]. Bài 3. Phần tử riêng biệt.

| Problem | Submissions | Leaderboard | Discussions |
| --- | --- | --- | --- |

Cho dây số A□ gồm có N phản tử, bạn hây liệt kê các giá trị xuất hiện trong dây theo thứ tự xuất hiện, mỗi giá trị chỉ liệt kê một lần.

Goi ÿ : Dùng set dé lùu các phần tử đã được in ra trước đó, gặp phần tử a[i] thì kiểm tra nhanh trong set có giả trị a[i] chưa đế in ra

Input Format

Dòng đầu tiên là số nguyên N. Dòng thử 2 gồm N số nguyên A[i]

Constraints

$1 \leq N \leq 10^{5}; 0 \leq A[i], X \leq 10^{9};$

Output Format

In ra các giá trị xuất hiện trong mảng theo thứ tự xuất hiện.

Sample Input 0

B
1 2 3 2 1 3 4 8

Sample Output 0

| Problem | Submissions | Leaderboard | Discussions |
| --- | --- | --- | --- |

## [Set Map]. Bài 4. Truy vấn trên mắng

Cho đầy số A[] gồm có N phần tử, có 3 thao tác như sau :

• Thao tác 1 : Thêm 1 phần tử X vào mắng.

\- Thao tác 2 : Xóa 1 phần tử X khởi mắng. Trong trường hợp phần tử X không xuất hiện trong mắng, sẽ không thực hiện xóa, nếu trong mắng có nhiều phần tử X thì chỉ xóa đi 1 phần tử X trong mắng.

\- Thao tác 3 : Truy vấn xem phần tử X có xuất hiện trong mắng hay không?

Ban đầu mảng A có N phần tử, với các truy vấn phần tử X trong mảng, in ra YES nếu X xuất hiện trong mảng, ngược lại in ra NO.

Gọi ý : Bài này vừa muốn xóa nhanh vừa muốn tìm kiếm nhanh lại phải lưu được giá trị trùng nhau => Sử dụng multiset

## Input Format

\- Dòng đầu tiên là số nguyên N.

\- Dòng thứ 2 gồm N số nguyên A[i].

\- Dòng thứ 3 là số lượng thao tác Q.

\- Q dòng tiếp theo mỗi dòng là thông tin của một thao tác, gồm 2 số, số đầu tiên là loại thao tác, số tiếp theo là phần tử X trong thao tác.

Constraints

$1 \leq N \leq 10^{4}; 0 \leq A[i], X \leq 10^{9}; 1 \leq Q \leq 1000; 0 \leq X \leq 10^{9};$

Output Format

Đối với mỗi thao tác loại 3, in ra YES nếu X xuất hiện trong mắng, ngược lại in ra NO.

Sample Input 0

Sample Output 0

YES
NO

## Explanation 0

Ban đầu mảng có 6 phần tử 1, 2, 3, 4, 5, 6. Sau thao tác đầu tiên mảng có thêm 1 phần tử 1 và trở thành mảng (1, 1, 2, 3, 4, 5, 6). Sau thao tác thứ 2, mảng xóa đi 1 phần tử 6 và trở thành mảng (1, 1, 2, 3, 4, 5). Thao tác thứ 3 truy vấn phần tử 1, câu trả lời là YES vì 1 xuất hiện trong mảng. Thao tác thứ 4 truy vấn phần tử 6, câu trả lời là NO vì 6 không xuất hiện trong mảng.

## [Set Map]. Bài 9. Union

```txt
Problem	Submissions	Leaderboard	Discussions

Cho máng A[] và B[] lần lượt gồm N và M số nguyên, nhiệm vụ của bạn là tìm hợp của 2 máng này và in theo thứ tự từ lớn về nhỏ.

Goi ý : Đề tìm hợp của 2 máng thì chỉ cần dùng 1 set và lưu mọi phần tử của 2 máng, set sẽ tự loại bỏ các phần tử trùng nhau trong cả 2 máng.

Cú pháp duyệt ngược của set như sau:

for(auto it - se.rbegin(); it != se.rend(); ++it){
    cout << *it << ' ';
}

Input Format
• Dòng 1 gồm N và M
• Dòng 2 gồm N số trong máng A[]
• Dòng 3 gồm M số trong máng B[]
Constraints
• 1<=N.M<=10^5
• -10^9<=A[i].B[i]<=10^9

Output Format
In ra tập hợp của 2 máng theo thứ tự giảm đàn

Sample Input 0

9 6
7 9 2 0 0 5 6 4 7
9 7 3 4 5 7

Sample Output 0

9 7 6.5 4 3 2 0
```

## [Set Map]. Bài 10. Intersection

```tsv
Problem	Submissions	Leaderboard	Discussions

Cho mảng A[] và B[] lần lượt gồm N và M số nguyên, nhiệm vụ của bạn là tìm giao của 2 mảng này và in theo thứ tự xuất hiện trong mảng A[].

Gợi ý：

Cách 1 : Dùng 2 set để lưu 2 mảng A, B sau đó duyệt 1 trong 2 mảng và tìm kiếm sự xuất hiện của phần tử đang duyệt trong mảng còn lại.

Cách 2 : Dùng 1 map để đánh dấu, duyệt qua các phần tử trong mảng A[] và cho map của từng phần tử trong mảng A[] = 1, duyệt qua mảng B[] thì kiểm tra nếu map của phần tử trong mảng B đã bằng 1 thì chuyển thành 2. Cuối cùng duyệt map và in ra những phần tử được đánh dấu là 2.

Input Format

• Dòng 1 gồm N và M
• Dòng 2 gồm N số trong mảng A[]
• Dòng 3 gồm M số trong mảng B[]

Constraints

• 1<=N,M<=10^5
• -10^9<=A[i],B[i]<=10^9

Output Format

In ra tập giao của 2 mảng theo thứ tự xuất hiện trong mảng A[]

Sample Input 0

9	8
7	5	0	0	1	6	2	7	3
6	4	9	4	2	8	3	5

Sample Output 0

5	6	2	3
```

## [Set Map]. Bài 11. Difference

```txt
Problem	Submissions	Leaderboard	Discussions

Cho măng A[] và B[] lần lượt gồm N và M số nguyên, nhiệm vụ của bạn là tìm những phần tử xuất hiện trong măng thứ nhất nhưng không xuất hiện trong măng thứ 2, liệt kê theo thứ tự từ bề đến lớn.

Gọi ý : Dùng 2 set để lưu măng A, B. Duyệt các phần tử trong set 1 và tìm kiếm nếu phần tử ko nằm trong set 2 thì in ra.

Input Format
• Dòng 1 gồm N và M
• Dòng 2 gồm N số trong măng A[]
• Dòng 3 gồm M số trong măng B[]
Constraints
• 1<=N,M<=10^5
• -10^9<=A[i],B[i]<=10^9

Output Format

In ra đáp ăn của bài toán

Sample Input 0

6 6
1 9 3 8 0 7
3 1 7 3 7 5

Sample Output 0

0 0 9
```

## [Set Map]. Bài 12. Symmetric difference

```txt
Problem	Submissions	Leaderboard	Discussions

Cho măng A[] và B[] lần lượt gồm N và M số nguyên, nhiệm vụ của bạn là tìm những phần tử xuất hiện ở 1 trong 2 măng nhưng không được xuất hiện ở cả 2 măng.

Input Format
• Dòng 1 gồm N và M
• Dòng 2 gồm N số trong măng A[]
• Dòng 3 gồm M số trong măng B[]
Constraints
• 1<=N,M<=10^5
• -10^9<=A[i],B[i]<=10^9

Output Format
In ra đáp án của bài toán theo thứ tự từ bề đến lớn

Sample Input 0

9 8
9 0 2 3 9 7 8 1 4
1 0 2 1 1 2 0 5

Sample Output 0

3 4 5 7 6 9
```

## [Set Map]. Bài 13. Loại trừ

Submissions

Leaderboard

Discussions

Cho mảng A[] và B[] có N và M phần tử là các số nguyên, hây tìm các phần tử xuất hiện trong mảng 1 mà không xuất hiện trong mảng 2.

Input Format

Dòng đầu tiên là N và M; Dòng thứ 2 là N số của màng A[]; Dòng thứ 3 là M số của màng B[];

Constraints

1<=N, M<=10^6; -10^9<=A[i], B[i] <= 10^9;

Output Format

In ra các số xuất hiện trong màng 1 mà không xuất hiện trong màng 2 theo thử tự từ bề đến lớn, mỗi giá trị thỏa mãn chỉ liệt kê 1 lần.

Sample Input 0

3 4
1 2 3
1 2 4 5

Sample Output 0

## [Màng 1 Chièu]. Bài 9. Đém tần suất

```txt
Problem	Submissions	Leaderboard	Discussions

Cho mảng các số nguyên không âm gồm n phần tử, thực hiện đếm tàn suất xuất hiện của các phần tử và in theo mẫu.

Input Format

Dòng đầu tiên là số lượng phần tử trong mảng. Dòng thứ 2 là N phần tử trong mảng.

Constraints

2≤n≤10^6; 0≤a≤10^7

Output Format

In ra tần suất xuất hiện của các phần tử theo thứ tự từ nhỏ tới lớn sau đó bỏ trống 1 dòng và in ra tần suất xuất hiện của các phần tử theo thứ tự xuất hiện trong mảng(mỗi giá trị chỉ liệt kê 1 lần).

Sample Input 0

8
2 1 2 3 4 8 2 3

Sample Output 0

1 1
2 3
3 2
4 1
8 1
2 3
1 1
3 2
4 1
8 1
```

## [Màng 1 Chiêu]. Bài 10. Tîm hợp và giao của 2 màng 1

```txt
Problem	Submissions	Leaderboard	Discussions

Cho 2 mảng số nguyên a và b gồm n và m phần tử. Goi mảng c và d lần lượt là mảng chỉ bao gồm các phần tử khác nhau của a và b. Hây tìm mảng giao và hợp của mảng c và d và liệt kê theo thứ tự tăng dần.

Hướng dẫn tìm giao : Dùng 1 map để đánh dấu những giá trị xuất hiện trong mảng a, Dùng 1 map để đánh dấu những giá trị xuất hiện trong mảng b. Duyệt 1 trong 2 map và kiểm tra xem phần tử của map hiện tại có nằm trong map thứ 2 hay không => giao. Tìm hợp : Đưa các phần tử trong 2 mảng vào 1 cải set

Input Format

Dòng đầu tiên là số lượng phần tử của 2 đầy n và m. Dòng thứ 2 là n phần tử trong đầy số 1. Dòng thứ 3 là m phần tử trong đầy thứ 2.

Constraints

1≤n,m≤10^6; 0≤a≤10^7

Output Format

Dòng đầu tiên in ra giao của 2 mảng c và d. Dòng thứ 2 in ra hợp của 2 mảng c và d.

Sample Input 0

5 6
1 2 1 2 7
1 2 3 4 5 6

Sample Output 0

1 2
1 2 3 4 5 6 7
```

## [Màng 1 Chiều]. Bài 11. Tìm hợp và giao của 2 màng 2

```txt
Problem	Submissions	Leaderboard	Discussions

Cho 2 mảng số nguyên a và b gồm n và m phần tử, các phần tử trong mảng là đôi một khác nhau, các phần tử trong 2 mảng đã được sắp xếp theo thứ tự tăng dần. Hấy tìm mảng giao và mảng hợp của 2 mảng.

Input Format

Dòng đầu tiên là số lượng phần tử của 2 đầy n và m. Đồng thứ 2 là n phần tử trong đầy số 1. Đồng thứ 3 là m phần tử trong đầy thứ 2.

Constraints

1≤n,m≤10^7; -10^7≤s≤10^7

Output Format

Dòng đầu tiên in ra mảng hợp của 2 mảng Dòng thứ 2 in ra mảng giao của 2 mảng

Sample Input 0

4 5
1 2 3 4
2 3 5 6 7

Sample Output 0

1 2 3 4 5 6 7
2 3
```

## [Màng 1 Chiêu]. Bài 12. Đém tần suất số nguyên tố

Problem

Submissions

Leaderboard

Discussions

Cho một đầy số nguyên chưa biết trước số lượng phần tử, hấy đếm tàn xuất hiện của các số nguyên tố trong đầy và in ra theo thứ tự xuất hiện trong đầy

Input Format

Gồm nhiều dòng chưa các số nguyên trong dãy

Constraints

Dây không quá 10000 số nguyên không âm. Các số trong dây là số nguyên không âm không quá 10^9

Output Format

In ra các số nguyên tố trong dây kèm theo tần suất của nó.

Sample Input 0

2353251

Sample Output 0

## [Màng 1 Chiêu]. Bài 14. Liệt kê và đếm

<table><tr><td>Problem</td><td>Submissions</td><td>Leaderboard</td><td>Discussions</td></tr><tr><td colspan="4">Cho một đầy các số nguyên dương không quá 9 chữ số, mỗi số cách nhau vài khoảng trống, có thể xuống dòng. Hây tìm các số không giảm (các chữ số theo thứ tự từ trái qua phải tạo thành đầy không giảm) và đếm số lần xuất hiện của các số đó.</td></tr><tr><td colspan="4">Input Format</td></tr><tr><td colspan="4">Gồm 1 đầy các số nguyên dương không quá 9 chữ số</td></tr><tr><td colspan="4">Constraints</td></tr><tr><td colspan="4">Dầy không quá 100000 số. Các số đều nguyên dương và không quá 9 chữ số.</td></tr><tr><td colspan="4">Output Format</td></tr><tr><td colspan="4">Ghi ra các số không giám kèm theo số lần xuất hiện. Các số được liệt kê theo thứ tự sắp xếp số lần xuất hiện giám dản. Trong trường hợp có nhiều số có cùng số lần xuất hiện thì thì số nhỏ hơn sẽ xếp trước.</td></tr><tr><td colspan="4">Sample Input 0</td></tr><tr><td colspan="4">888 289 123321 54 888</td></tr><tr><td colspan="4">Sample Output 0</td></tr><tr><td colspan="4">688 2123 1289 1</td></tr></table>