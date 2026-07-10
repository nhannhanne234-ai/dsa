Thuật toán tìm kiếm tuyến tính:
- Hoạt động bằng cách duyệt lần lượt từng phần tử trong mảng từ đầu đến cuối để kiểm tra phần tử cần tìm có xuất hiện trong mảng hay không
- Khi duyệt gặp phần từ bằng giá trị cần tìm thì trả về vị trí của phần tử đó
- Khi duyệt hết mảng vẫn không tìm thấy sẽ trả kết luận phần tử không tồn tại trong mảng

Input: 
- Mảng a = [2, 4, 7, 9, 10, 12, 14, 23]
- Giá trị cần tìm x = 12

Output: 
- Vị trí của giá trị x trong mảng nếu tìm thấy.
- Nếu không tìm thấy sẽ trả về -1

---> Vị trí của giá trị 12 trong mảng nếu tìm thấy là: 5

Thuật toán dừng: 
- Thuật toán sẽ dừng trong hai trường hợp:
	+ Trường hợp 1: Tìm thấy phần tử
	+ Trường hợp 2: Duyệt hết mảng nhưng không tìm thấy phần tử