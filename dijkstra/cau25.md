## 1. Ý tưởng cốt lõi (Bất biến tham lam)

Thuật toán Dijkstra hoạt động theo kiểu "tham lam" (greedy). Trong quá trình chạy, đồ thị được chia làm 2 phần:
* Tập $S$: Gồm các đỉnh đã được duyệt xong và chốt khoảng cách (đã lôi ra khỏi Heap, đánh dấu `visited = True`).
* Tập còn lại ($V \setminus S$): Các đỉnh chưa chốt, khoảng cách hiện tại mới chỉ là ước lượng tạm thời.

**Khẳng định cần chứng minh (Bất biến):** Mỗi khi ta chọn đỉnh $u$ có khoảng cách tạm thời nhỏ nhất trong Heap để lôi ra và bỏ vào tập $S$, thì giá trị `dist[u]` lúc đó chắc chắn đã là khoảng cách ngắn nhất thực tế từ gốc ($\text{start}$) đến $u$. Tức là không bao giờ có chuyện sau này tìm được đường khác ngắn hơn nữa.

---

## 2. Chứng minh bằng phản chứng

Giả sử thuật toán chạy sai. Gọi $u$ là đỉnh **đầu tiên** bị thuật toán tính sai khi lôi ra khỏi Heap để cho vào tập $S$. 
Vì tính sai nên khoảng cách thuật toán tìm được (`dist[u]`) lớn hơn khoảng cách thực tế tối ưu ($d(\text{start}, u)$):
$$\text{dist}[u] > d(\text{start}, u)$$

Gọi $P$ là đường đi ngắn nhất thực tế từ $\text{start}$ đến $u$. 
* Điểm đầu của đường đi này ($\text{start}$) nằm trong tập $S$ (đã chốt).
* Điểm cuối của đường đi ($u$) nằm ngoài tập $S$ (chưa chốt).

Vì đường đi $P$ chạy từ trong tập $S$ ra ngoài tập $S$, nên trên con đường này chắc chắn phải có một chỗ bước qua ranh giới. Gọi cạnh bước qua ranh giới đó là $x \rightarrow y$ (với $x$ nằm trong $S$, còn $y$ nằm ngoài $S$). Đỉnh $y$ có thể nằm dọc đường hoặc trùng luôn với $u$.

### Phân tích các bước logic:
1. Vì $x$ thuộc tập $S$ và $u$ là đỉnh đầu tiên bị tính sai, nên đỉnh $x$ trước đó đã được tính đúng:
   $$\text{dist}[x] = d(\text{start}, x)$$

2. Khi $x$ được cho vào tập $S$, thuật toán đã cập nhật (relax) các đỉnh kề của nó, trong đó có $y$. Do đó, khoảng cách tạm thời của $y$ ít nhất phải bằng hoặc tốt hơn đường đi qua $x$:
   $$\text{dist}[y] \le \text{dist}[x] + w(x, y) = d(\text{start}, x) + w(x, y)$$

3. Vì cạnh $x \rightarrow y$ nằm ngay trên đường đi ngắn nhất thực tế $P$, nên tổng chi phí từ gốc đến $x$ rồi cộng thêm cạnh $x \rightarrow y$ chính bằng khoảng cách tối ưu đến $y$:
   $$d(\text{start}, x) + w(x, y) = d(\text{start}, y)$$
   Từ (2) và (3) suy ra `dist[y]` không thể lớn hơn thực tế, mà ước lượng thì không thể nhỏ hơn thực tế, nên:
   $$\text{dist}[y] = d(\text{start}, y)$$

4. Đường đi từ gốc đến $y$ chỉ là một đoạn ngắn nằm trên tổng đường đi từ gốc đến $u$. Vì **tất cả các cạnh của đồ thị đều không âm ($w \ge 0$)**, nên đi tiếp từ $y$ đến $u$ chỉ có thể bằng hoặc tốn thêm chi phí, chứ không thể bớt đi:
   $$d(\text{start}, y) \le d(\text{start}, u)$$

### Kết nối lại để tìm điểm mâu thuẫn:
Từ các điều trên, ta có một chuỗi so sánh:
$$\text{dist}[y] = d(\text{start}, y) \le d(\text{start}, u) < \text{dist}[u] \implies \text{dist}[y] < \text{dist}[u]$$

Theo đúng nguyên lý của Heap, đỉnh nào có khoảng cách tạm thời nhỏ hơn (`dist`) thì phải được lôi ra trước. Kết quả trên chỉ ra `dist[y] < dist[u]`, nghĩa là đáng lẽ ra $y$ phải được lôi ra trước $u$. 

Điều này mâu thuẫn hoàn toàn với giả thiết ở trên là ta đang lôi $u$ ra khỏi Heap trước $y$.

**Kết luận:** Giả sử ban đầu là sai. Thuật toán Dijkstra luôn chọn đúng khoảng cách ngắn nhất.

---

## 3. Tại sao bắt buộc trọng số phải không âm?

Hãy nhìn kỹ lại **Bước 4** ở phần chứng minh:
$$d(\text{start}, y) \le d(\text{start}, u)$$

Phép suy luận này chỉ đúng khi và chỉ khi đoạn đường đi tiếp từ $y \rightarrow u$ không có cạnh nào âm. Nếu đồ thị có cạnh âm, việc đi tiếp từ $y$ đến $u$ có thể làm tổng chi phí giảm mạnh xuống, khiến cho $d(\text{start}, y) > d(\text{start}, u)$.

Khi đó, `dist[u]` lúc ở trong Heap có thể nhỏ hơn `dist[y]`, thuật toán sẽ lôi $u$ ra trước để chốt chặn và đánh dấu đã duyệt xong. Sau này khi loang đến nhánh của $y$ rồi đi qua cạnh âm, thuật toán mới phát hiện ra đường đi vòng qua $y$ để đến $u$ rẻ hơn. Nhưng vì $u$ đã bị chốt (đánh dấu `visited = True`), cơ chế tham lam của Dijkstra sẽ **bỏ qua luôn và không cập nhật lại $u$ nữa**, dẫn đến kết quả bị sai.