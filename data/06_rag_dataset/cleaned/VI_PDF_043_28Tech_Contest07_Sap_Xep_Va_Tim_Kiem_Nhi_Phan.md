## [Sắp xếp - Tìm Kiểm]. Bài 1. Các số khác nhau trong màng

```txt
Problem	Submissions	Discussions

Cho máng số nguyên gồm N phần tử. Hấy đếm xem máng có bao nhiêu phần tử riêng biệt
Input Format
Dòng đầu tiên là N Dòng thứ 2 là các phần tử trong máng a1, a2, ... aN
Constraints
1≤n≤2.10^5; 1≤a1≤10^9
Output Format
In ra số lượng phần tử riêng biệt trong máng.
Sample Input 0
10
2 2 2 1 3 2 5 1 4 2
Sample Output 0
5
Explanation 0
5 phần tử khác nhau trong máng là 1, 2, 3, 4, 5
```

## [Sắp xếp - Tìm Kiếm]. Bài 2. Sắp xếp theo trị tuyệt đối

```txt
Problem	Submissions	Discussions

Cho mảng số nguyên A[] có N phần tử, hây sắp xếp các phần tử trong mảng theo thứ tự giá trị tuyệt đối tăng dần. Nếu có 2 số có cùng giá trị tuyệt đối thì số nào xuất hiện trước sẽ được in ra trước

Input Format

Dòng đầu tiên là số nguyên dương N. Dòng thứ 2 là N phần tử trong mảng, các phần tử viết cách nhau một dấu cách.

Constraints

1<=N<=10^5; -10^9<=A[i]<=10^9

Output Format

In ra các phần tử trong mảng sau khi sắp xếp theo thứ tự tăng dần

Sample Input 0

5
1 -3 2 -5 4

Sample Output 0

1 2 -3 4 -5
```

## [Sắp xếp - Tìm Kiểm]. Bài 3. Sắp xếp theo tổng chữ số

Problem

Submissions

Discussions

Cho mảng số nguyên A□ có N phần tử, hấy sắp xếp các phần tử trong mảng theo thứ tự tổng chữ số tăng đàn, nếu 2 số có cùng tổng chữ số, thì số nào nhỏ hơn sẽ được in trước.

Input Format

Dòng đầu tiên là số nguyên dương N. Dòng thứ 2 là N phần tử trong màng, các phần tử viết cách nhau một dấu cách.

Constraints

1<=N<=10^5; 0<=A[i]<=10^9

Output Format

In ra các phản tử trong măng sau khi sắp xếp

Sample Input 0

5
999976710 999982875 999974431 999984407 999972533

Sample Output 0

999974431 999972533 999976710 999984407 999982875

```txt
Problem	Submissions	Discussions

Cho mảng số nguyên A[] có N phần tử, tìm độ chênh lệch nhỏ nhất giữa 2 phần tử A[i] và A[j] trong mảng(i và j khác nhau).

Input Format

Dòng đầu tiên là số nguyên dương N. Dòng thứ 2 là N phần tử trong mảng, các phần tử viết cách nhau một dấu cách.

Constraints

1<=N<=10^6; 0<=A[i]<=10^9

Output Format

In ra độ lệch nhỏ nhất của 2 phần tử trong mảng

Sample Input 0

5
1 2 7 9 8

Sample Output 0

1
```

## [Sắp xếp - Tìm Kiểm]. Bài 4. Khoảng cách nhỏ nhất

## [Sắp xếp - Tìm Kiểm]. Bài 5. Số xuất hiện nhiều nhất trong màng

Problem

Submissions

Discussions

Cho mảng số nguyên A□ có N phần tử, hây tìm sõ xuất hiện nhiều nhất trong mảng.

Input Format

Dòng đầu tiên là số nguyên dương N. Dòng thứ 2 là N phần tử trong màng, các phần tử viết cách nhau một dấu cách.

Constraints

1<=N<=10^5; -10^9<=A[i]<=10^9

Output Format

In ra số có số lần xuất hiện nhiều nhất và tàn suất tương ứng, nếu có nhiều số có cùng số lần xuất hiện thì in ra số nhỏ nhất.

Sample Input 0

5
1 2 2 1 3

Sample Output 0

12

## [Sắp xếp - Tìm Kiểm]. Bài 9. Tìm kiểm nhị phân

```txt
Problem	Submissions	Discussions

Cho mảng số nguyên A[] có N phần tử đã được sắp xếp theo thứ tự giám dàn. Có Q truy vấn, mỗi truy vấn yêu cầu bạn kiểm tra xem phần tử X có xuất hiện trong mảng hay không?

Cách 1 : Sắp xếp mảng tăng đàn rời dùng binary_search để tìm kiếm nhanh

Cách 2 : Đưa các phần tử trong mảng vào set để tìm kiếm nhanh

Mỗi truy vấn chí mất O(logN)

Input Format

Dòng đầu tiên là số nguyên dương N. Dòng thứ 2 là N phần tử trong mảng, các phần tử viết cách nhau một đầu cách. Dòng thứ 3 là số lượng truy vấn Q. Q dòng tiếp theo mỗi dòng là một số nguyên dương X.

Constraints

1 <= N <= 10^6; 1 <= Q <= 10^3; 0 <= A[j], X <= 10^9

Output Format

Đối với truy vấn in ra YES trên 1 dòng nếu X xuất hiện trong mảng, ngược lai in ra NO.

Sample Input 0

5
5 4 3 2 1
2
2
8

Sample Output 0

YES
NO
```

## [Sắp xếp - Tìm Kiếm]. Bài 11. Trộn 2 dãy

Problem

Submissions

Discussions

Đế sắp xếp tăng dần một mắng A gồm n phần tử a1, a2,..., an, thuật toán sắp xếp trộn (MergeSort) áp dụng chia đôi mắng A thành hai mắng B và C, sắp xếp B, C và sau đó trộn B và C cho ra mắng A tăng dần. Ví dụ minh họa phương pháp trộn: - Mắng B gồm 4 phần tử b1, b2, b3, b4 đã sắp tăng dần: 1 2 4 6 - Mắng C gồm 4 phần tử c1, c2, c3, c4 đã sắp tăng dần: 3 5 8 9 Nếu trộn hai mắng trên theo đầy thứ tự trộn b1, b2, c1, b3, c2, b4, c3, c4 thì có được mắng sắp là 1 2 3 4 5 6 8 9. Cho một mắng B gồm n phần tử và mắng C gồm m phần tử. Hây in ra đầy thứ tự trộn sao cho nếu áp dụng đầy thứ tự trộn trên thì mắng kết quả được sắp xếp tăng dần.

## Input Format

\- Dòng đầu tiên là hai số nguyên n, m cách nhau một khoảng trắng là số phần tử của màng B và màng C.

\- Dòng thứ 2 gồm n số nguyên b1, b2,..., bn, mỗi số cách nhau một khoảng trắng.

\- Dòng thứ 3 gồm m số nguyên c1, c2,..., cm, mỗi số cách nhau một khoảng trắng.

## Constraints

1<=n,m<=10^6; 0<=b[i],c[i]<=10^6

## Output Format

In ra dây là thứ tự trộn, trong trường hợp trong 2 màng b và c có phần tử có cùng giả trị t in ra phần tử ở màng b trước.

## Sample Input 0

5 5
4760 9724 9798 20124 25974
3397 9166 13054 18273 30455

## Sample Output 0

c1 b1 c2 b2 b3 c3 c4 b4 b5 c5

# [Sắp xếp - Tìm Kiểm]. Bài 10. Tìm kiểm nhị phân biến đổi

<table><tr><td>Problem</td><td>Submissions</td><td>Discussions</td></tr><tr><td colspan="3">Cho măng số nguyên A[] có N phần tử đã được sắp xếp theo thứ tự tăng dân. Hây viết các hàm sau với độphức tạp O(logN):</td></tr><tr><td colspan="3">1. Tím vị trí xuất hiện đầu tiên của phần tử X trong măng, nếu không tồn tại X in ra -1.</td></tr><tr><td colspan="3">2. Tím vị trí xuất hiện cuối cùng của phần tử X trong măng, nếu không tồn tại X in ra -1.</td></tr><tr><td colspan="3">3. Tím vị trí xuất hiện đầu tiên của phần tử &gt;= X trong măng, nếu không tồn tại phần tử &gt;=X in ra -1.</td></tr><tr><td colspan="3">4. Tím vị trí xuất hiện đầu tiên của phần tử &gt; X trong măng, nếu không tồn tại phần tử &gt;X in ra -1.</td></tr><tr><td colspan="3">5. Tím số lần xuất hiện của phần tử X trong măng sử dụng kết quả của hàm 1 và 2.</td></tr><tr><td colspan="3">Input Format</td></tr><tr><td colspan="3">Dòng đầu tiên là số nguyên dương N và X Dông thứ 2 là N phần tử trong măng, các phần tử viết cách nhau một dấu cách.</td></tr><tr><td colspan="3">Constraints</td></tr><tr><td colspan="3">1&lt;=N&lt;=10^6; 0&lt;=A[i].X&lt;=10^6;</td></tr><tr><td colspan="3">Output Format</td></tr><tr><td colspan="3">In ra 5 dòng tương ứng với 5 kết quả của 5 hàm đề bài yếu cầu.</td></tr><tr><td colspan="3">Sample Input 0</td></tr><tr><td colspan="3">10 116019 1600 2172 2921 3409 4185 4639 6096 6744 9192</td></tr><tr><td colspan="3">Sample Output 0</td></tr><tr><td colspan="3">-1-1110</td></tr></table>

## [Sắp xếp - Tìm Kiểm]. Bài 12. Khiêu vũ

Problem

Submissions

Discussions

Trong lớp học có n bạn nam và m bạn nữ. Các bạn nam có chiều cao là a1, a2, ..., an. Các bạn nữ có chiều cao là b1, b2, ..., bm. Nhân dịp lễ tổng kết cuối năm, cả lớp dự định tổ chức buổi khiêu vũ nhưng có điều kiện là trong một đôi khiêu vũ bắt kỳ, bạn nam phải cao hơn bạn nữ. Và mỗi bạn không tham gia quá 1 đôi khiêu vũ. Hấy tính số lượng cặp đôi nhiều nhất thỏa mãn yêu cầu trên.

Input Format

Input: gồm 3 dòng - Dòng thứ nhất là hai số n, m mỗi số cách nhau một khoảng trắng. - Dòng thứ hai gồm n số nguyên a1, a2, ..., an là chiều cao các bạn nam. - Dòng thứ ba gồm m số nguyên b1, b2, ..., bm là chiều cao các bạn nữ.

Constraints

1<=n,m<=10^5; 1<=a[i],b[i]<=10^6;

Output Format

In ra số lượng cặp khiêu vũ nhiều nhất ghép được.

Sample Input 0

5 5
2668 2956 20933 21199 24224
11521 13084 19573 25628 28958

Sample Output 0

3

```txt
Problem	Submissions	Discussions

Nam có n viên gạch được đánh số từ 1 đến n. Các viên gạch có độ cứng lần lượt là a1, a2,..., an. Một viên gạch
có độ cứng x nghĩa là Nam có thể chồng lên trên viên gạch đó tối đa x viên gạch khác, nếu chồng nhiều hơn thì
viên gạch đó bị vật. Hôi Nam có thể sắp được chồng gạch cao nhất là bao nhiêu?

Input Format
• Đồng đầu tiên là số nguyên n - là số viên gạch.
• Đồng tiếp theo gồm n số nguyên a1, a2,..., an mỗi số cách nhau một khoảng trắng.

Constraints
1<=n<=10^5; 0≤aí≤10^6

Output Format
Số nguyên xác định chiều cao cao nhất của chồng gạch mà Nam sắp được.

Sample Input 0

4
1 2 3 4

Sample Output 0

4
```

## [Sắp xếp - Tìm Kiếm]. Bài 13. Xếp gạch

## [Sắp xếp - Tìm Kiểm]. Bài 14. Vất sữa bò

Problem

Submissions

Discussions

Vào một buổi sáng anh Bo sắp một đàn bỏ gồm n con bỏ để vật sửa. Anh dự kiến là vào sáng hôm đó, con bỏ thứ i có khả năng sẽ vật được ai lít sửa. Tuy nhiên đàn bỏ của anh có đặc tính là cứ mỗi lần vật sửa một con, những con còn lại trồng thấy sợi quả nên sẽ bị giảm sản lượng mỗi con 01 lít sửa. Nếu vật sửa con bỏ thứ nhất, n-1 con còn lại bị giảm sản lượng. Sau đó vật sửa con bỏ thứ hai thì n-2 con còn lại bị giảm sản lượng.... Bạn hầy giúp anh Bo tính xem thứ tự vật sửa bỏ như thể não để số lượng sửa vật được là nhiều nhất nhẹ.

Input Format

• Dòng thứ nhất là số nguyên là số lượng con bò.

\- Đồng thứ hai gồm n số nguyên a1, a2,..., an là sản lượng sửa của các con bò.

Constraints

1<=n<=10^5; 1<=a[i]<=10^6

Output Format

Số nguyên xác định số lít sửa nhiều nhất mà anh Bo có thể vật được.

Sample Input 0

4
4 4 4 4

Sample Output 0

10

## [Sắp xếp - Tìm Kiểm]. Bài 17. Cặp số có tổng bằng K

Problem

Submissions

Discussions

Cho màng a gồm n phần tử và số nguyên dương k. Đếm số lượng cập số ai, aj (i != j) có tổng bằng k.

Goi ý : Sắp xếp màng tăng đàn sau đó với mỗi phần tử a[i] trong màng tìm xem trong đoạn [i + 1, n - 1] có bao nhiêu phần tử có giả trị là k - a[i], bằng cách tìm vị trí đầu tiên và vị trí cuối cùng của phần tử có giả trị là k - a[i] => Số lượng

Input Format

Dòng thứ 1 là số lượng phần tử trong màng và số nguyên dương k; Dòng thứ 2 là n phần tử trong màng

Constraints

2<=n<=10^6; 1<=k<=10^6; 0<=a[i]<=10^6;

Output Format

In ra số lượng cập số có tổng bằng k

Sample Input 0

Sample Output 0

## [Sắp xếp - Tìm Kiểm]. Bài 18. Cặp số có tổng nhỏ hơn K

```txt
Problem	Submissions	Discussions

Cho màng a gồm n phần tử và số nguyên dương k. Đếm số lượng cặp số ai, aj (i != j) có tổng nhỏ hơn k.

Input Format

Dòng thứ 1 là số lượng phần tử trong màng và số nguyên dương k: Dòng thứ 2 là n phần tử trong màng

Constraints

2<=n<=10^6;

1<=k<=10^6;

0<=a[i]<=10^6;

Output Format

In ra số lượng cặp số có tổng nhỏ hơn k

Sample Input 0

4 5
2 2 2 2

Sample Output 0

6
```

## [Sắp xếp - Tìm Kiểm]. Bài 19. Cặp số có tổng lớn hơn k

```txt
Problem	Submissions	Discussions

Cho màng a gồm n phần tử và số nguyên dương k. Đếm số lượng cặp số ai, aj (i != j) có tổng lớn hơn k.
Goi ý : Sử dụng binary_search, đối với mỗi phần tử a[i] đểm số lượng phần tử trong màng (đã sắp xếp) > k - a[i]
bằng cách tìm vị trí đầu tiên của phần tử > k - a[i], từ vị trí này tới cuối đầy sẽ đều là các phần tử > k - a[i]

Input Format

Dòng thứ 1 là số lượng phần tử trong màng và số nguyên dương k; Đồng thứ 2 là n phần tử trong màng

Constraints

2<=n<=10^6; 1<=k<=10^6; 0<=a[i]<=10^6;

Output Format

In ra số lượng cặp số có tổng lớn hơn k

Sample Input 0

4 5
2 3 4 5

Sample Output 0

5
txt
Problem	Submissions	Discussions

Cho mảng A[] gồm n số nguyên dưỡng. Gọi L, R là min và max các phần tử của A[]. Nhiệm vụ của bạn là tìm số phần tử cần thiết cần thêm vào mảng để mảng có đầy đủ các số trong khoảng [L, R]. Ví dụ A[] = {5, 7, 9, 3, 6, 2} ta nhận được kết quả là 2 tương ứng với các số còn thiếu là 4, 8.

Input Format

Dòng đầu tiên đưa vào n, tương ứng với số phần tử của mảng A[]; dòng tiếp theo là n số A[i] ; các số được viết cách nhau một vài khoảng trống.

Constraints

1=n<=10^6; 0<=a[i]<=10^6;

Output Format

In ra số lượng số còn thiếu

Sample Input 0

5
4 5 3 8 6

Sample Output 0

1
```

## [Sắp xếp - Tìm Kiểm]. Bài 20. Điền số còn thiếu

## [Sắp xếp - Tìm Kiểm]. Bài 26. Tìm kiểm cặp số có hiệu bằng X

```txt
Problem	Submissions	Discussions

Cho mảng A[] gồm N phần tử và số X. Nhiệm vụ của bạn là tìm cấp phần tử A[i] - A[j] = X. Nếu tồn tại A[i] - A[j] = X đưa ra 1, ngược lại đưa ra -1.

Input Format

Dòng thứ nhất là cặp số N, X; Dòng tiếp theo là N số A[i] là các phần tử của mảng A[].

Constraints

1≤ N ≤10^5; 1≤ X, A[i] ≤10^5.

Output Format

In ra 1 nếu tìm thấy một cặp số có hiệu bằng X, ngược lại in ra -1.

Sample Input 0

5 3
1 1 2 3 5

Sample Output 0

1
```

## [Sắp xếp - Tìm Kiếm]. Bài 30. Đèn lỏng

```txt
Problem	Submissions	Discussions

Vanya đi bộ vào ban đêm dọc theo một con đường thẳng dài có độ dài l, được thấp sáng bối n chiếc đèn lồng.
Xét hệ trục toa độ với điểm đầu của đường phố tương ứng với điểm 0 và điểm cuối của nó tương ứng với điểm
l. Khi đó đèn lồng thứ i ở điểm ai. Đèn lồng chiếu sáng tất cả các điểm trên đường phố cách nó nhiều nhất là d,
trong đó d là một số dương, chung cho tất cả các đèn lồng. Vanya tự hồi: bán kính ánh sáng tối thiểu d mà
những chiếc đèn lồng phải có để thấp sáng cả con phố?

Input Format

Dòng đầu tiên chứa hai số nguyên n, l (1 ≤ n ≤ 10^5, 1 ≤ l ≤ 10^9) - số lượng đèn lồng và chiều dài đường phố
tương ứng. Dòng tiếp theo chứa n số nguyên ai (0 ≤ ai ≤ l). Nhiều đèn lồng có thể được đặt tại cùng một điểm.
Đèn lồng có thể nằm ở cuối phố.

Constraints

1 ≤ n ≤ 10^5, 1 ≤ l ≤ 10^9; 0 ≤ ai ≤ l;

Output Format

In bán kính ánh sáng tối thiểu d, cần thiết để chiếu sáng cả đường phố. In ra kết quả với độ chính xác là 10 số
sau dấu phầy

Sample Input 0

7 15
15 5 3 7 9 14 0

Sample Output 0

2.5000000000
```

<table><tr><td>Problem</td><td>Submissions</td><td>Discussions</td></tr><tr><td colspan="3">Kirito đang bị mắc kết ở cấp độ của MMORPG mà anh ấy đang chơi hiện tại. Đế tiếp tục trò chơi, anh ta phải đánh bại tất cả n con ròng sống ở cấp độ này. Kirito và những con ròng có sức mạnh, được biểu thị bằng một số nguyên. Trong cuộc độ sức giữa hai đối thú, kết quả của cuộc độ sức được quyết định bởi sức mạnh của họ. Ban đầu, sức mạnh của Kirito bảng s.Nếu Kirito bắt đầu đầu tay đổi với ròng thứ i (1 ≤ i ≤ n) và sức mạnh của Kirito không lớn hơn sức mạnh của ròng có sức mạnh là xi, thì Kirito thua trận đầu và chết. Nhưng nếu sức mạnh của Kirito lớn hơn sức mạnh của con ròng, thì anh ta sẽ đánh bại con ròng và được tăng thêm sức mạnh theo là yi.Kirito có thể chiến đấu với những con ròng theo bắt kỳ thứ tự nào. Xác định xem liệu anh ta có thể chuyển sang cấp độ tiếp theo của trò chơi hay không, tức là đánh bại tất cả những con ròng mà không bị thua một lần nào.</td></tr><tr><td colspan="3">Input FormatDòng đầu tiên chứa hai số nguyên được phân tách bằng đầu cách n và s (1 ≤ s ≤ 10^6, 1 ≤ n ≤ 10^5).Sau đó n dòng tiếp theo: dòng thứ i chứa các số nguyên được phân tách bằng đầu cách là xi và yi (1 ≤ xi ≤ 10^4, 0 ≤ yi ≤ 10^4) - sức mạnh của con ròng thứ i và sức mạnh được tăng thêm khi đánh bại nó.</td></tr><tr><td colspan="3">Constraints1 ≤ s ≤ 10^6, 1 ≤ n ≤ 10^51 ≤ xi ≤ 10^4, 0 ≤ yi ≤ 10^4</td></tr><tr><td colspan="3">Output FormatTrên một dòng duy nhất in &quot;YES&quot; (không có dấu ngoặc kép), nếu Kirito có thể chuyển sang cấp độ tiếp theo và in &quot;NO&quot; (không có dấu ngoặc kép), nếu anh ta không thể.</td></tr><tr><td colspan="3">Sample Input 0</td></tr><tr><td colspan="3">2 21 99100 0</td></tr><tr><td colspan="3">Sample Output 0</td></tr><tr><td colspan="3">YES</td></tr></table>

## [Sắp xếp - Tìm Kiểm]. Bài 31. Dragon

## [Sắp xếp - Tìm Kiếm]. Bài 35. Xếp trẻ

Problem

Submissions

Discussions

Có n đứa trẻ muốn đi đầu quay, và nhiệm vụ của bạn là tìm một chiếc thuyền gondola cho mỗi đứa trẻ. Mỗi chiếc gondola có thể có một hoặc hai người trong đó và ngoài ra, tổng trọng lượng của một chiếc gondola không được vượt quá x. Bạn biết cân nặng của mọi đứa trẻ. Số lượng thuyền gondola tối thiểu cần thiết cho trẻ em là bao nhiêu?

Input Format

Dòng nhập đầu tiên chứa hai số nguyên n và x: số đứa trẻ và trọng lượng tối đa cho phép. Dòng tiếp theo chứa n số nguyên p1, p2,..., pn: trọng lượng của mỗi đứa trẻ

Constraints

$1 \leq n \leq 2.10^{5}; 1 \leq x \leq 10^{9}; 1 \leq pi \leq x;$

Output Format

In một số nguyên: số lượng thuyền gondola tối thiểu.

Sample Input 0

4 10
7 2 3 9

Sample Output 0

# [Sắp xếp - Tìm Kiểm]. Bài 24. Biểu thức nhỏ nhất

Problem

Submissions

Discussions

Một đầy gồm n số nguyên không âm a1, a2,..., an được viết thành một hàng ngang, giữa hai số liên tiếp có một khoảng trắng, như vậy có tất cả (n-1) khoảng trắng. Người ta muốn đặt k dấu cộng và (n-1-k) dấu trừ vào (n-1) khoảng trắng đó để nhận được một biểu thức có giá trị lớn nhất. Ví dụ, với đầy gồm 5 số nguyên 28, 9, 5, 1, 69 và k = 2 thì cách đặt 28+9-5-1+69 là biểu thức có giá trị lớn nhất. Yêu cầu: Cho đầy gồm n số nguyên không âm a1, a2,..., an và số nguyên dương k, hấy tìm cách đặt k dấu cộng và (n-1-k) dấu trừ vào (n-1) khoảng trắng để nhận được một biểu thức có giá trị lớn nhất.

Input Format

Dòng đầu chứa hai số nguyên dương n, k; Dòng thứ hai chứa n số nguyên không âm a1, a2,..., an;

Constraints

1<= k < n ≤ 10^5; 0 <= a[i] ≤ 10^6

Output Format

In ra giá trị lớn nhất của biểu thức

Sample Input 0

6 3
9560 5571 9008 3649 1473 3782

Sample Output 0

22799