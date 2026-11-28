<!-- page: 1 -->

## [Xâu ký tự]. Bài 1. Đếm số loại ký tự trong xâu.

```txt
Problem	Submissions	Discussions

Cho một xấu kí tự, hay đếm số lượng kí tự là chữ cái, chữ số và kí tự đặc biệt(Các kí tự không phải là chữ cái và chữ số).

Input Format

Xâu kí tự S.

Constraints

1≤len(S)≤1000.

Output Format

In ra số lượng chữ cái, chữ số, và kì tự đặc biệt xuất hiện trong xấu

Sample Input 0

abcd123 $%^ a

Sample Output 0

5 3 5
```

<!-- page: 2 -->

## [Xâu ký tự]. Bài 2. In hoa, in thường.

Problem

Submissions

Discussions

Cho một xấu kí tự, hây viết hoa và viết thường các kí tự là chữ cái trong xấu, các kí tự không phải là chữ cái thì không thay đổi.

Input Format

Xâu kí tự 5.

Constraints

1≤len(S)≤1000.

Output Format

Dòng đầu tiên in ra xâu sau khi thay đổi mọi kí tự thường trong xâu thành ký tự hoa. Dòng thứ 2 in ra xâu sau khi thay đổi mọi kí tự hoa trong xâu thành ký tự thường.

Sample Input 0

abcd ABCD

Sample Output 0

ABCD ABCD abcd abcd

<!-- page: 3 -->

## [Xâu ký tự]. Bài 3. Tần suất xuất hiện của ký tự

<table><tr><td>Problem</td><td>Submissions</td><td>Discussions</td></tr><tr><td colspan="3">Cho một xấu kí tự, hấy đêm tần suất xuất hiện của các ký tự trong xấu và in ra theo yêu cầu.</td></tr><tr><td colspan="3">Input Format</td></tr><tr><td colspan="3">Xâu kí tự S chỉ bao gồm chữ cái in hoa và in thường.</td></tr><tr><td colspan="3">Constraints</td></tr><tr><td colspan="3">1≤len(S)≤100000.</td></tr><tr><td colspan="3">Output Format</td></tr><tr><td colspan="3">Đầu tiên in ra các ký tự và tần suất xuất hiện của các ký tự ở trong xấu theo thứ tự từ diễn tăng dần, sau đó cách ra một dòng và in ra tần suất xuất hiện của các ký tự theo thứ tự xuất hiện trong xấu(chú ý mỗi ký tự chỉ in 1 lần)</td></tr><tr><td colspan="3">Sample Input 0</td></tr><tr><td colspan="3">abcdabcdA</td></tr><tr><td colspan="3">Sample Output 0</td></tr><tr><td colspan="3">A 1</td></tr><tr><td colspan="3">a 2</td></tr><tr><td colspan="3">b 2</td></tr><tr><td colspan="3">c 2</td></tr><tr><td colspan="3">d 2</td></tr><tr><td colspan="3">a 2</td></tr><tr><td colspan="3">b 2</td></tr><tr><td colspan="3">c 2</td></tr><tr><td colspan="3">d 2</td></tr><tr><td colspan="3">A 1</td></tr></table>

<!-- page: 4 -->

<table><tr><td>Problem</td><td>Submissions</td><td>Discussions</td></tr><tr><td colspan="3">Cho một xấu kí tự, hãy tìm kí tự có số lần xuất hiện ít nhất trong xấu và kí tự có số lần xuất hiện nhiều nhất ở trong xấu. Trong trường hợp có nhiều kí tự có cùng số lần xuất hiện lớn nhất hoặc nhỏ nhất thì in ra kí tự có thứ tự từ điện lớn nhất.</td></tr><tr><td colspan="3">Input Format</td></tr><tr><td colspan="3">Xâu kí tự S chỉ bao gồm chữ cái in hoa và in thường.</td></tr><tr><td colspan="3">Constraints</td></tr><tr><td colspan="3">1≤len(S)≤100000.</td></tr><tr><td colspan="3">Output Format</td></tr><tr><td colspan="3">Dòng đầu tiên in ra kí tự có số lần xuất hiện nhiều nhất, trong trường hợp có nhiều kí tự có cùng số lần xuất hiện nhiều nhất thì chọn kí tự có thứ tự từ điện lớn nhất. Dòng thứ 2 in ra kí tự có số lần xuất hiện nhỏ nhất nhất, trong trường hợp có nhiều kí tự có cùng số lần xuất hiện nhỏ nhất thì chọn kí tự có thứ tự từ điện lớn nhất.</td></tr><tr><td colspan="3">Sample Input 0</td></tr><tr><td colspan="3">qEQtEEuAQcSWfFRfWRnKKeCZeUYlSGrXWvOGqEXsWMxLRtQPxBMtEHdPGbGKvKFiQLxUSuSZtMIjXEhUZtAZdBInYLeH WfWUwCVo</td></tr><tr><td colspan="3">Sample Output 0</td></tr><tr><td colspan="3">W 6w 1</td></tr></table>

## [Xâu ký tự]. Bài 4. Ký tự xuất hiện nhiều nhất trong xây.

<!-- page: 5 -->

## [Xâu ký tự]. Bài 5. Ký tự xuất hiện ở cả 2 xâu.

Cho 2 xâu kí tự S1 và S2, hấy in ra các kí tự xuất hiện ở cả 2 xâu theo thứ tự từ điện, chú ý mỗi kí tự chỉ liệt kê một lần. Sau đó tiếp tục liệt kê các kí tự xuất hiện ở 1 trong 2 xâu theo thứ tự từ điện.

Input Format

Dòng đầu tiên là xâu S1. Dòng thứ 2 là xâu S2. Các ký tự trong 2 xâu chỉ bao gồm chữ cái in hoa hoặc in thường.

Constraints

$1 \leq \text{len}(S1) \leq 100000; 1 \leq \text{len}(S2) \leq 100000.$

Output Format

Dòng 1 in ra các ký tự xuất hiện ở cả 2 xấu theo thứ tự từ diễn tăng dần. Dòng 2 in ra các ký tự xuất hiện ở 1 trong 2 xấu theo thứ tự từ diễn tăng dần.

Sample Input 0

nTOhOGvRBk
bUJtZSoONh

Sample Output 0

BGJNORSTUZbhknotv

<!-- page: 6 -->

## [Xâu ký tự]. Bài 6. Ký tự xuất hiện ở 2 xây 2.

Problem

Submissions

Discussions

Cho 2 xấu kí tự S1 và S2 chỉ bao gồm chữ cái in hoa và in thường, hấy tìm các kí tự xuất hiện trong xâu S1 mà không xuất hiện trong xâu S2, và các kí tự chỉ xuất hiện trong xâu S2 mà không xuất hiện trong xâu S1. Các ký tự được in ra theo thứ tự từ điện và chỉ liệt kê mỗi ký tự một lần.

Input Format

Dòng đầu tiên là xâu S1. Dòng thứ 2 là xâu S2.

Constraints

$1 \leq \text{len}(S1) \leq 100000; 1 \leq \text{len}(S2) \leq 100000.$

Output Format

Dòng đầu tiên in ra các ký tự chỉ xuất hiện trong S1 mà không xuất hiện trong S2. Dòng thứ 2 in ra các ký tự chỉ xuất hiện trong S2 mà không xuất hiện trong S1.

Sample Input 0

fAOxTUeAIs
aVUkULeRYw

Sample Output 0

AIOTfsx
LRVYakw

<!-- page: 7 -->

## [Xâu ký tự]. Bài 7. Xâu đối xứng.

Problem

Submissions

Discussions

Cho một xấu ký tự 5 chỉ bao gồm các chữ cái, hảy kiểm tra xem xấu nhập vào có phải là xấu đối xứng hay không?

Input Format

Dòng duy nhất là xâu S

Constraints

1≤len(S)≤100000;

Output Format

In ra YES nếu S đối xúng, ngược lại in NO.

Sample Input 0

cBGkXXqKWqqWKqXXkGBc

Sample Output 0

<!-- page: 8 -->

## [Xâu ký tự]. Bài 8. Xâu pangram 1

Problem

Submissions

Discussions

Xâu pangram là xâu có chứa đầy đủ các kí tự từ A tới Z không phân biệt chữ hoa hay thường. Nhập vào xâu S và kiểm tra xem xâu S có phải là xâu pangram hay không?

Input Format

Xâu kí tự S chỉ bao gồm các kí tự in hoa hoặc in thường.

Constraints

1≤len(S)≤100000;

Output Format

In ra YES nếu S là xấu pangram, ngược lại in NO.

Sample Input 0

abcdefghijklmnopqrstuvwxyz

Sample Output 0

<!-- page: 9 -->

## [Xâu ký tự]. Bài 9. Đếm số lượng từ trong xâu

Problem

Submissions

Discussions

Cho một xấu kí tự S bao gồm các chữ cái và dấu cách, một từ được định nghĩa là các kí tự liên tiếp không chứa dấu cách, hây đêm số lượng từ xuất hiện trong xấu S.

Input Format

Dòng duy nhất chứa xâu 5.

Constraints

1≤len(S)≤100000;

Output Format

In ra số lượng từ xuất hiện trong xấu S.

Sample Input 0

ngon ngu lap trình java, python

Sample Output 0

<!-- page: 10 -->

## [Xâu ký tự]. Bài 10. Liệt kê các từ khác nhau trong xây.

Problem

Submissions

Discussions

Cho một xấu kí tự S bao gồm các chữ cái và dấu cách, một từ được định nghĩa là các kí tự liên tiếp không chứa dấu cách, hãy liệt kê các từ khác nhau trong xấu S, đầu tiên hãy liệt kê các từ khác nhau theo thứ tự từ diễn tăng dần, sau đó liệt kê các từ theo thứ tự xuất hiện trong xấu.

Input Format

Dòng duy nhất chứa xâu S.

Constraints

1≤len(S)≤100000;

Output Format

Dòng đầu tiên in ra các trong xâu theo thứ tự từ điện. Dòng thứ hai in ra các từ theo thứ tự xuất hiện trong xâu. Chú ý không in dấu cách thừa sau từ cuối cùng của từng dòng.

Sample Input 0

python java php php java python

Sample Output 0

java php python
python java php

<!-- page: 11 -->

## [Xâu ký tự]. Bài 11. Sắp xếp các từ trong xâu 1

Problem

Submissions

Discussions

Cho một xấu kí tự S bao gồm các chữ cái và dấu cách, một từ được định nghĩa là các kí tự liên tiếp không chứa dấu cách, đầu tiên hãy sắp xếp các từ trong xấu theo thứ tự từ điện tăng dần, sau đó sắp xếp các từ trong xấu theo thứ tự chiều dài tăng dần, trong trường hợp có nhiều từ có cùng chiều dài thì từ nào có thứ tự từ diễn nhỏ hơn sẽ in ra trước.

Input Format

Dòng duy nhất chứa xâu S.

Constraints

1≤len(S)≤100000;

Output Format

Dòng đầu tiên in ra các từ trong xâu theo thứ tự từ điển tăng dần. Dòng thứ 2 in ra các từ trong xâu theo thứ tự chiều dài tăng dần, trong trường hợp có nhiều từ có cùng chiều dài thì từ nào có thứ tự từ diễn nhỏ hơn sẽ in ra trước. Các từ được in cách nhau một dấu cách.

Sample Input 0

hoc lap trinh php

Sample Output 0

hoc lap php trinh
hoc lap php trinh

<!-- page: 12 -->

## [Xâu ký tự]. Bài 12. Sắp xếp các từ trong xâu 2

Problem

Submissions

Discussions

Cho một xấu kí tự S bao gồm các chữ cái và dấu cách, một từ được định nghĩa là các kí tự liên tiếp không chứa dấu cách, hấy sắp xếp các từ thuận nghịch khác nhau trong xấu theo thứ tự từ chiều dài tăng dần, nếu 2 từ thuận nghịch có cùng chiều dài thì từ nào xuất hiện trước sẽ được in ra trước.

Input Format

Dòng duy nhất chứa xây S.

Constraints

1≤len(S)≤100000;

Output Format

In ra các từ theo thứ tự sắp xếp yêu cầu, các từ được in cách nhau một dấu cách.

Sample Input 0

php aba aaaa nguyen huu hoc pop

Sample Output 0

php aba pop aaaa

<!-- page: 13 -->

<table><tr><td>Problem</td><td>Submissions</td><td>Discussions</td></tr><tr><td colspan="3">Cho một xấu kí tự S bao gồm các chữ cái và dấu cách, một từ được định nghĩa là các kí tự liên tiếp không chứa dấu cách, hây đêm xem mỗi từ trong xấu xuất hiện bao nhiêu lần, đầu tiên hây liệt kê các từ trong xấu kèm theo tần suất của mỗi từ theo thứ tự từ điện, sau đó liệt kê các từ trong xấu theo thứ tự xuất hiện.</td></tr><tr><td colspan="3">Input Format</td></tr><tr><td colspan="3">Dòng duy nhất chứa xấu S.</td></tr><tr><td colspan="3">Constraints</td></tr><tr><td colspan="3">1≤len(S)≤100000;</td></tr><tr><td colspan="3">Output Format</td></tr><tr><td colspan="3">Đầu tiên in ra các từ trong xấu và tần suất của nó theo thứ tự từ điện. Sau đó bổ trống 1 dòng và in ra các từ trong xấu và tần suất của nó theo thứ tự xuất hiện trong xấu.</td></tr><tr><td colspan="3">Sample Input 0</td></tr><tr><td colspan="3">bb aa bb cc aa bb cc</td></tr><tr><td colspan="3">Sample Output 0</td></tr><tr><td>aa 2</td><td></td><td></td></tr><tr><td>bb 3</td><td></td><td></td></tr><tr><td>cc 2</td><td></td><td></td></tr><tr><td>bb 3</td><td></td><td></td></tr><tr><td>aa 2</td><td></td><td></td></tr><tr><td>cc 2</td><td></td><td></td></tr></table>

## [Xâu ký tự]. Bài 13. Tần suất các từ xuất hiện trong xây.

<!-- page: 14 -->

## [Xâu ký tự]. Bài 14. Từ xuất hiện nhiều nhất, ít nhất

Problem

Submissions

Discussions

Cho một xấu kí tự S bao gồm các chữ cái và dấu cách, một từ được định nghĩa là các kí tự liên tiếp không chứa dấu cách. Hây tìm từ có số lần xuất hiện nhiều nhất và ít nhất trong xấu, nếu có nhiều từ có cùng số lần xuất hiện nhiều nhất hoặc ít nhất thì chọn từ có thứ tự từ diễn lớn nhất làm kết quả.

Input Format

Dòng duy nhất chứa xâu S.

Constraints

1≤len(S)≤100000;

Output Format

Dòng đầu tiên in ra từ có số lần xuất hiện nhiều nhất. Dòng thứ 2 in ra từ có số lần xuất hiện ít nhất.

Sample Input 0

aa bb cc aa bb aa aa cc

Sample Output 0

aa 4
cc 2

<!-- page: 15 -->

## [Xâu ký tự]. Bài 15. Kiểm tra xây con

Problem

Submissions

Discussions

Cho 2 xấu S và T chỉ bao gồm các chữ cái in hoa, in thường và dấu cách. Hấy kiểm tra xem xâu T có phải là xâu con của xấu S hay không?

Input Format

Dòng đầu tiên là xâu S. Dòng thứ 2 là xâu T.

Constraints

1≤len(S)≤100000; 1≤len(T)≤100000;

Output Format

In ra YES nếu xấu T xuất hiện trong xấu S, ngược lại in ra NO.

Sample Input 0

aabcacbdaa
cacb

Sample Output 0

<!-- page: 16 -->

## [Xâu ký tự]. Bài 16. Chuẩn hóa tên 1

Problem

Submissions

Discussions

Cho một xấu là tên người chỉ bao gồm các kí tự là chữ cái và dấu cách, giữa các từ trong câu có thể tôn tại nhiều dấu cách hãy chuẩn hóa tên người bằng cách viết hoa chữ cái đầu tiên của từng từ và viết thường các chữ cái còn lại. Xâu tiếp theo là ngày sinh của người này, bao gồm ngày tháng năm phân cách nhau bằng dấuprime, hãy chuẩn hóa ngày sinh của người này về đúng dạng dd/mm/yyyy.

## Input Format

Dòng đầu tiên là tên người; Dòng thứ 2 là ngày sinh;

Constraints

Xâu kí tự tên người có không quá 2000 kí tự; Xâu ngày sinh có không quá 10 kí tự. Dữ liệu đảm bảo có dấu '7' giữa ngày, tháng, năm.

Output Format

Dòng đầu tiên in ra tên người sau khi chuẩn hóa. Dòng thứ 2 in ra ngày sinh sau khi đưa về dạng chuẩn dd/mm/yyyy.

Sample Input 0

NgUYEN Van TECH28
1/1/2022

Sample Output 0

Nguyen Van Tech28
01/01/2022

<!-- page: 17 -->

## [Xâu ký tự]. Bài 17. Chuẩn hóa tên 2.

Problem

Submissions

Discussions

Cho một xấu là tên người chỉ bao gồm các kí tự là chữ cái và dấu cách, giữa các từ trong câu có thể tôn tại nhiều dấu cách hãy chuẩn hóa tên người theo 2 mẫu được yêu cầu trước. Xem output để rõ hơn về cách chuẩn hóa.

Input Format

Dòng duy nhất là tên người.

Constraints

Xâu kí tự tên người có không quá 1000 kí tự;

Output Format

Dòng đầu tiên in ra theo mẫu chuẩn hóa 1. Dòng thứ 2 in ra theo mẫu chuẩn hóa 2.

Sample Input 0

tRAN

Sample Output 0

Tran Van, TECH28
TECH28, Tran Van

<!-- page: 18 -->

## [Xâu ký tự]. Bài 18. Tạo email và mật khẩu.

Problem

Submissions

Discussions

Hiện tại trường đại học XYZ tổ chức cấp email cho sinh viên mới nhập học. Email và mật khấu sẽ được cấp dựa trên tên của sinh viên và ngày sinh của sinh viên đó. Bạn hấy viết chương trình để cấp tài khoản theo yêu cầu như sau, tên email được tạo bằng cách lấy tên của sinh viên và ghép với các chữ cái đầu tiên của họ và tên đêm, tất các ký tự trong email đều ở dạng in thường, ví dụ sinh viên có tên "Nguyen Van Long" sẽ được cấp email "longnv@xyz.edu.vn". Một khấu sẽ dựa trên ngày sinh của sinh viên đó, bằng cách ghép ngày tháng nằm lại với nhau, ví dụ sinh viên sinh ngày 27/04/2002 sẽ có mật khấu là 2742002.

## Input Format

Dòng đầu tiên là số lượng sinh viên cần cấp email N. N dòng tiếp theo, mỗi dòng gồm 2 phần là họ tên và ngày sinh, ngày sinh của sinh viên đã ở dạng chuẩn dd/mm/yyyy. Giữa các tử có thể có nhiều dấu cách, từ cuối cùng trong dòng là thông tin ngày sinh của sinh viên(xâu kí tự không có dấu cách chuẩn dd/mm/yyyy).

## Constraints

1≤N≤5000; Dòng thông tin của sinh viên không quá 1000 ký tự, dữ liệu đảm bảo thông tin cuối cùng trong dòng là ngày sinh của sinh viên.

## Output Format

Đối với mỗi sinh viên in ra thông tin trên 2 dòng, dòng thứ 1 là tên email, dòng thứ 2 là mật khẩu.

## Sample Input 0

```asm
1
nguyen   VAN   NAM    22/07/2002
```

## Sample Output 0

namnv@xyz.edu.vn
2272002

<!-- page: 19 -->

## [Xâu ký tự]. Bài 19. Tạo email và mật khẩu 2.

Problem

Submissions

Discussions

\- Trường đại học ABC tổ chức cấp email cho sinh viên mới nhập học. Email và mật khẩu sẽ được cấp dựa trên tên của sinh viên và ngày sinh của sinh viên đó. Bạn hấy viết chương trình để cấp tài khoản theo yêu cầu như sau, tên email được tạo bằng cách lấy tên của sinh viên và ghép với các chữ cái đầu tiên của họ và tên đêm tất các ký tự trong email đều ở dạng in thường, ví dụ sinh viên có tên "Nguyen Van Long" sẽ được cấp email "longnv@xyz.edu.vn".

\- Mặt khấu sẽ dựa trên ngày sinh của sinh viên đó, bằng cách ghép ngày tháng nằm lại với nhau, ví dụ sinh viên sinh ngày 27/04/2002 sẽ có mật khấu là 2742002. Ngoài ra sẽ có những trường hợp sinh viên bị trùng tên email, ví dụ, sinh viên "Nguyen Van Long" sẽ được cấp email "longnv@xyz.edu.vn", sinh viên tên "Ngo Van Long" cũng sẽ được cấp email "longnv@xyz.edu.vn", vì thế nhà trường quy định, theo thứ tự tên trong danh sách, nếu email được cấp của sinh viên hiện tại đã được cấp cho một sinh viên trước đó thì thêm số thứ tự vào tên email.

## Input Format

\- Dòng đầu tiên là số lượng sinh viên cần cấp email N.

\- N dòng tiếp theo, mỗi dòng gồm 2 phần là họ tên và ngày sinh, ngày sinh của sinh viên đã ở dạng chuẩn dd/mm/yyyy. Giữa các tử có thể có nhiều dấu cách, từ cuối cùng trong dòng là thông tin ngày sinh của sinh viên(xâu ký tự không có dấu cách chuẩn dd/mm/yyyy).

Constraints

\- $1 \leq N \leq 5000$

\- Đồng thông tin của sinh viên không quá 1000 kí tư, dữ liệu đảm bảo thông tin cuối cùng trong dòng là ngày sinh của sinh viên.

## Output Format

In ra ra email và mật khấu được cấp của mỗi sinh viên trên 2 dòng. Chủ ý các sinh viên email bị trùng tên sẽ được thêm số thứ tự vào sau.

<!-- page: 20 -->

## Sample Input 0

4
nguyen van LONG 20/10/2002
ngo Vang Long 20/12/2002
Nguyen Vu Long 22/12/2003
ho van nam 17/09/2002

## Sample Output 0

longnv@xyz.edu.vn
20102002
longnv2@xyz.edu.vn
20122002
longnv3@xyz.edu.vn
22122003
namhv@xyz.edu.vn
1792002

<!-- page: 21 -->

## [Xâu ký tự]. Bài 20. Ngôn ngữ lập trình Python.

Problem

Submissions

Discussions

Trong giờ học ngôn ngữ lập trình Python, thấy giáo có đưa ra một bài toán cho Tèo, bài toán như sau "Cho một xấu kí tự S, Tèo hây xác định xem liệu rằng có thể xóa đi bất kì một kí tự nào trong xấu S ở một vị trí bất kì và xấu S trở thành từ "python" được hay không? Biết rằng Tèo có thể xóa bất kì một kí tự nào nhưng không thể hoán đối vị trí các kí tự trong xấu S ban đầu". Hiện nay vì Tèo đang bạn gói bánh chung phụ thấy mẹ nên nhờ bạn giải giúp. Hy vọng bạn có thể giúp được Tèo !!!

## Input Format

Một xấu kí tự S chỉ bao gồm các kí tự in hoa hoặc in thường.

## Constraints

Xâu 5 có độ dài không quá 1000 ký tự.

## Output Format

In ra YES nếu có thể tạo ra xâu "python" bằng cách xóa đi các kí tự trong xâu, ngược lại in NO.

<!-- page: 22 -->

rRMssizYyAbYPbfYPwaamZFTLSoWSqCewiGIKymcnlVUuQqpXGinxSuPooRfUljsZhjncyvWeDdgoOrDHeXLMbkNvThv DZLnFITEaOnWapaPjmHBFlqEwkWRWTSzZnyKkpNTpidcXxxptIenHGKovBporbkaoPjyLBZNrCzxGtZPMoQmgrpiihYR dGYUSRChscdQpVZYdaTAqyDBfSrBmqsEDjeSysMKIuQdggYOxXuMqleEigpllWAyPOGjHlRCraPTuPgByGDokiPcoFHL hhVlIeGvzssrOWVetiknhtuerNysZhcCcZyIuPUjhBOIvYnHYopsUZuptCQoxYBSodMAtxERREaGgNxtSjuOdyQCFLxY gGxsswbDhHWErcNjzdycpZYfCsvPPVgNqFNbLHegCSBNbDzhSDjGoPKLZCQDvfKeHokfDKWQwOZKhTfTXGDCHtpopuyX abGgbyncHVKlPzrqtlGRUZDKKvGkZaeZaVRZvfeznbzBgwnNwprUEQuupkVKrzzHENzLZCITPGYsZPwgwmzcDCBkIVpr SFWpISLGjAmZbcyIUOfmmuNDdDDDPGziCzztviOsHGjIzysPLyTczfWrWalbeLgnfLVhzLPfXhoQwIjVMjBAxyVbSczF hUXaRzBVmeWvlIgpQBDgZFtgeHLHZWMIRxiscYqTyKNuzucMczdycPWMYNYUHCVBUZZktqxtxNWyjyTQFAcPoKteBGTx hcdezFVzuNaziplGPtzZpNFVQaxEQwxbdatBjRCnccjjYLTfWbVgeiraCDLGtEpgkOoWnGvawBXvtTUMAAnsWPmxFZqe LCQiPRzXuMhQMSUaslbNNgplnrVnpcbWcyZREbKSCArfKYblBLATNuycAQEXuf

Sample Output 0

YES

Sample Input 1

pyoooooonnnnnthhhhhyonnn

Sample Output 1

<!-- page: 23 -->

## [Xâu ký tự]. Bài 21. Tập từ chung của 2 xây

Problem

Submissions

Discussions

Cho 2 xãu kí tự S và T. Hãy liệt kê các từ xuất hiện ở cả 2 xãu mà không phân biệt hoa thường, mỗi từ được liệt kê một lần theo thứ tự từ diễn tăng dần. Gọi ý : Chuyển hết các kí tự S, T về in thường rời xét từ.

Cách 1 : Dùng 2 cái set, set1 lưu các từ khác nhau trong S, set2 lưu các từ khác nhau trong T. Sau đó duyệt set1 và kiểm tra sự tôn tại của từ trong set2, nếu có thì in ra

Cách 2 : Dùng map, đánh dấu các từ trong S = 1, sau đó duyệt từ trong T và kiểm tra nếu đã được đánh dấu là 1, thì đánh dấu thành 2. Cuối cùng in ra các từ trong map được đánh dấu là 2.

## Input Format

Dòng đầu tiên chứa xâu S. Dòng thứ hai chứa xâu T.

Constraints

1≤len(S)≤10000; 1≤len(T)≤10000; Xâu S và T chỉ bao gồm chữ cái và dấu cách.

## Output Format

In ra các từ xuất hiện ở cả 2 xấu theo thứ tự từ diễn tăng dần, mỗi từ được liệt kê 1 lần và in ra ở dạng chữ in thường.

Sample Input 0

abc abc abcd abcd AB
abC CD ZAH abd ABcD

Sample Output 0

abc abcd

<!-- page: 24 -->

## [Xâu ký tự]. Bài 22. Tập từ riêng của 2 xãu.

Problem

Submissions

Discussions

Cho 2 xấu kí tự S và T. Hấy liệt kê các từ xuất hiện ở xấu S và không xuất hiện ở xấu T mà không phân biệt hoa thường, mỗi từ được liệt kê một lần theo thứ tự từ diễn tăng dần.

Input Format

Dòng đầu tiên chứa xâu S. Dòng thứ hai chứa xâu T.

Constraints

1≤len(S)≤10000; 1≤len(T)≤10000; Xâu S và T chỉ bao gồm chữ cái và dấu cách.

Output Format

In ra các từ theo thứ tự từ điện, các từ cách nhau một dấu cách và in theo thứ tự từ điện tăng dần.

Sample Input 0

aa AA abc abcd zzaA
ABc ABCd uuzka aka opl

Sample Output 0

aa zzaa

<!-- page: 25 -->

## [Xâu ký tự]. Bài 23. Ghép xâu

Problem

Submissions

Discussions

Cho các từ chỉ bao gồm chữ cái in hoa và in thường, bạn được yêu cầu ghép các từ này lại với nhau sao cho từ được ghép lại sau cùng có thứ tự từ diễn lớn nhất.

## Input Format

Dòng đầu tiên là số nguyên dương N - số lượng tử; Dòng thứ 2 gồm N từ, mỗi từ cách nhau một dấu cách.

Constraints

1≤N≤1000;

Output Format

In ra xâu sau khi ghép.

Sample Input 0

4
ab abc abcd aa

Sample Output 0

abcdabcabaa

<!-- page: 26 -->

## [Xâu ký tự]. Bài 24. Xâu có đầu cuối giống nhau.

Problem

Submissions

Discussions

Cho xấu S chỉ bao gồm các kí tự in thường, hấy đêm số lượng xâu con (xâu ký tự chứa các chữ cái liên tiếp) mà có kí tự đầu và kí tự cuối giống nhau.

Input Format

Một dòng duy nhất chứa xâu S chỉ bao gồm chữ cái in thường.

Constraints

1≤len(S)≤100000;

Output Format

In ra đáp án của bài toán.

Sample Input 0

abcda

Sample Output 0

6

Explanation 0

Các xấu con có kí tự đầu cuối giống nhau : a, b, c, d, a, abcda

<!-- page: 27 -->

## [Xâu ký tự]. Bài 25. Số lớn nhất, nhỏ nhất.

```txt
Problem	Submissions	Discussions

Cho số tự nhiên m và số nguyên s không âm. Nhiệm vụ của bạn là tìm số bé nhất và lớn nhất có m chữ số và tổng chữ số bằng s.

Input Format

Một dòng gồm 2 số m và s

Constraints

1 ≤ m ≤ 100; 0 ≤ s ≤ 900

Output Format

In ra số bé nhất, lớn nhất có thể đạt được, mỗi số in ra trên 1 dòng. Nếu không có đáp ăn thì in ra 1 dòng "NOT FOUND".

Sample Input 0

2 15

Sample Output 0

69
96

Sample Input 1

2 30

Sample Output 1

NOT FOUND
```

<!-- page: 28 -->

## [Xâu ký tự]. Bài 26. Xâu con liên tiếp các kí tự giống nhau.

Problem

Submissions

Discussions

Cho một xấu kí tự S chỉ bao gồm các chữ cái in thường, hấy tìm xấu con liên tiếp chứa các kí tự giống nhau dài nhất, nếu có nhiều xấu con thỏa mãn thì chọn xấu con có thứ tự từ diễn lớn nhất.

Input Format

Một dòng duy nhất chứa xấu S.

Constraints

1≤len(S)≤100000;

Output Format

In ra xâu con tìm được.

Sample Input 0

zzaabc

Sample Output 0

<!-- page: 29 -->

## [Xâu ký tự]. Bài 27. Xâu con liên tiếp các kí tự khác nhau.

Problem

Submissions

Discussions

Cho một xấu kí tự S chỉ bao gồm các chữ cải in thường, hấy tìm xấu con liên tiếp sao cho không có 2 kí tự nào liên kè giống nhau có độ dài lớn nhất, nếu có nhiều xấu con thỏa mặn thì chọn xấu con có thứ tự từ điện lớn nhất.

Input Format

Một dòng duy nhất chứa xây S.

Constraints

1≤len(5)≤100000;

Output Format

In ra xâu con là kết quả của bài toán

Sample Input 0

zzaabc

Sample Output 0

abc

<!-- page: 30 -->

## [Xâu ký tự]. Bài 28. Số lớn nhất xuất hiện trong xấu.

Problem

Submissions

Discussions

Cho một xấu kí tự S chỉ bao gồm các chữ cái và chữ số, hấy tìm số lớn nhất xuất hiện trong xấu. Ví dụ S = "28techabc123bba567ajsj50kkf099" thì số lớn nhất xuất hiện trong xấu là số 567, chú ý trong trường hợp một số có các số 0 đúng trước thì ta loại bổ các số 0 ở đầu, trong ví dụ số 099 ta tính là số 99,000 ta tính là số 0.

Input Format

Một dòng duy nhất chứa xâu S.

Constraints

1≤len(S)≤100000;

Output Format

In ra số lớn nhất xuất hiện trong xãu, dữ liệu đảm bảo có ít nhất 1 số xuất hiện trong xãu.

Sample Input 0

abc123bba567ajsj50kkf099

Sample Output 0

567

<!-- page: 31 -->

## [Xâu ký tự]. Bài 29. Tính tổng các số xuất hiện trong xấu.

Problem

Submissions

Discussions

Cho một xấu kí tự S chỉ bao gồm các chữ cái và chữ số, hây tìm tổng các số xuất hiện trong xấu. Ví dụ xấu kí tư "abcd123aad22a05" có tổng các số trong xấu là 123 + 22 + 5 = 150. Trong trường hợp các số bắt đầu bằng số 0 thì ta loại bỏ các số đó, dữ liệu đảm bảo tổng các số xuất hiện trong xấu không vượt quá 10^18.

Input Format

Một dòng duy nhất chứa xây S.

Constraints

1≤len(S)≤100000;

Output Format

In ra tổng các số trong xâu.

Sample Input 0

abcd123aad22a05

Sample Output 0

150

<!-- page: 32 -->

## [Xâu ký tự]. Bài 30. Ghép số.

Problem

Submissions

Discussions

Cho một xấu kí tự S chỉ bao gồm các chữ cái và chữ số, hãy thực hiện tách các số xuất hiện trong xấu ra và ghép lại với nhau để tạo thành một số tự nhiên lớn nhất. Ví dụ với xấu S = "123abcda234kkf11" thì ta sẽ tách được các số 123, 234 và 11, trong trường hợp các số bắt đầu bằng chữ số 0 thì ta loại bỏ các số 0 vô nghĩa này. Sau đó ghép lại với nhau thành số 23412311 là số lớn nhất có thể đạt được.

Input Format

Một dòng duy nhất chứa xâu S.

Constraints

1≤len(S)≤100000;

Output Format

In ra số lớn nhất ghép được.

Sample Input 0

123abcda234kkf11

Sample Output 0

23412311

<!-- page: 33 -->

## [Xâu ký tự]. Bài 31. Tổng chữ số của số nguyên

Problem

Submissions

Discussions

Cho một số nguyên không âm N, hây tính tổng các chữ số của N.

Input Format

Số nguyên không âm N.

Constraints

N có không quá 1000 chữ số.

Output Format

In ra tổng các chữ số của N.

Sample Input 0

123456789

Sample Output 0

45

<!-- page: 34 -->

## [Xâu ký tự]. Bài 32. Số đẹp 1

Problem

Submissions

Discussions

Một số được coi là số đẹp nếu nó có tất cả các chữ số là số nguyên tố và tổng các chữ số của nó cũng là số nguyên tố. Hây viết chương trình kiểm tra số nguyên dương N cho trước có phải là số đẹp hay không?

Input Format

Số nguyên dương N

Constraints

N có không quá 1000 chữ số.

Output Format

In ra YES nếu N là số đẹp, ngược lại in ra NO.

Sample Input 0

373

Sample Output 0

<!-- page: 35 -->

## [Xâu ký tự]. Bài 33. Số đẹp 2

Problem

Submissions

Discussions

Một số được coi là số đẹp nếu nó là số thuận nghịch và chứa ít nhất 1 chữ số 6. Hãy viết chương trình kiểm tra số nguyên dương N cho trước có phải là số đẹp hay không?

Input Format

Số nguyên dương N

Constraints

N có không quá 1000 chữ số.

Output Format

In ra YES nếu N là số đẹp, ngược lại in ra NO.

Sample Input 0

6433987866217635596629171229463963223693649221719266955367126687893346

Sample Output 0

<!-- page: 36 -->

```txt
Problem	Submissions	Discussions

Một số được coi là số đẹp nếu nó có các chữ số không giảm từ trái qua phải hoặc không tăng từ trái quá phải, ví dụ số 1233333345 là số không giảm, số 5555555543 là số không tăng. Hấy viết chương trình kiểm tra số nguyên dương N cho trước có phải là số đẹp hay không?

Input Format

Số nguyên dương N.

Constraints

N có không quá 1000 chữ số.

Output Format

In ra YES nếu N là số đẹp ngược lại lại ra NO.

Sample Input 0

12377788888888888888888888888888888888888888889

Sample Output 0

YES

Sample Input 1

8128777888888889

Sample Output 1

NO
```

## [Xâu ký tự]. Bài 34. Số đẹp 3

<!-- page: 37 -->

## [Xâu ký tự]. Bài 35. Số chia hết cho 6

Problem

Submissions

Discussions

Kiểm tra một số nguyên N có phải là số chia hết cho 6 hay không? Số chia hết cho 6 nếu nó chia hết cho cả 2 và 3.

Input Format

Số nguyên dương N.

Constraints

N có không quá 1000 chữ số.

Output Format

In YES nếu N là số chia hết cho 6, ngược lại in NO.

Sample Input 0

360

Sample Output 0

<!-- page: 38 -->

## [Xâu ký tự]. Bài 36. Số chia hết cho 4

Problem

Submissions

Discussions

Kiểm tra xem một số nguyên không âm N có chia hết cho 4 hay không, số chia hết cho 4 là số có nhiều hơn 1 chữ số mà có 2 chữ số tận cùng chia hết cho 4 hoặc là số có 1 chữ số chia hết cho 4.

Input Format

Số nguyên không âm N.

Constraints

N có không quá 1000 chữ số.

Output Format

In ra YES nếu N là số chia hết cho 4, ngược lại in ra NO.

Sample Input 0

516

Sample Output 0

<!-- page: 39 -->

## [Xâu ký tự]. Bài 37. Số chia hết cho 15

```txt
Problem	Submissions	Discussions

Kiểm tra xem một số nguyên không âm N có chia hết cho 15 hay không? Số chia hết cho 15 nếu nó chia hết cho cả 3 và 5.

Input Format

Số nguyên không âm N.

Constraints

N có không quả 1000 chữ số.

Output Format

In ra YES nếu N chia hết cho 15, ngược lại in ra NO.

Sample Input 0

150

Sample Output 0

YES
```

<!-- page: 40 -->

## [Xâu ký tự]. Bài 38. Số chia hết cho 25

Problem

Submissions

Discussions

Kiểm tra xem một số nguyên không âm N có chia hết cho 25 hay không? Số chia hết cho 25 nếu nó có 2 chữ số tận cùng là 2 số 0 hoặc là số chia hết cho 25.

Input Format

Số nguyên không âm N.

Constraints

N có không quá 1000 chữ số.

Output Format

In ra YES nếu N chia hết cho 25, ngược lại in ra NO.

Sample Input 0

150

Sample Output 0

YES

<!-- page: 41 -->

```txt
Problem	Submissions	Discussions

Kiểm tra xem một số nguyên không âm N có chia hết cho 11 hay không? Đế kiểm tra 1 số có chia hết cho 11 hay không bạn chỉ cần tính tổng các chữ số ở vị trí chẩn, tổng các chữ số ở vị trí lẻ và lấy độ chênh lệch của 2 tổng này chia cho 11, nếu độ chênh lệch này chia hết thì số ban đầu chia hết cho 11. Ví dụ số N = 8580 có tổng các số ở vị trí chẩn là 5, tổng các số ở vị trí lẻ là 16, độ chênh lệch giữa 2 tổng này là 11 vì thể số 8580 chia hết cho 11.

Input Format

Số nguyên không âm N.

Constraints

N có không quá 1000 chữ số.

Output Format

In ra YES nếu N chia hết cho 11 ngược lại in ra NO.

Sample Input 0

121

Sample Output 0

YES
```

## [Xâu ký tự]. Bài 39. Số chia hết cho 11

<!-- page: 42 -->

## [Xâu ký tự]. Bài 40. Số nhị phân chia hết cho 5

<table><tr><td>Problem</td><td>Submissions</td><td>Discussions</td></tr><tr><td colspan="3">Cho số nhị phân N, hây kiểm tra xem N có chia hết cho 5 hay không.</td></tr><tr><td colspan="3">Input Format</td></tr><tr><td colspan="3">Số N ở dạng nhị phân</td></tr><tr><td colspan="3">Constraints</td></tr><tr><td colspan="3">N có không quá 1000 bit.</td></tr><tr><td colspan="3">Output Format</td></tr><tr><td colspan="3">In ra YES nếu N chia hết cho 5, ngược lại in ra NO.</td></tr><tr><td colspan="3">Sample Input 0</td></tr><tr><td colspan="3">1010</td></tr><tr><td colspan="3">Sample Output 0</td></tr><tr><td colspan="3">YES</td></tr><tr><td colspan="3">Sample Input 1</td></tr><tr><td colspan="3">1010</td></tr><tr><td colspan="3">Sample Output 1</td></tr><tr><td colspan="3">YES</td></tr><tr><td colspan="3">Sample Input 2</td></tr><tr><td colspan="3">1010</td></tr><tr><td colspan="3">Sample Output 2</td></tr><tr><td colspan="3">YES</td></tr></table>
