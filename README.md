# FoodSpot 📍 - Dự án đã dừng phát triển

## ⚠️ Thông báo quan trọng
**Dự án này đã bị dừng lại do không thể lấy được dữ liệu từ Shopee Food.**

## Tổng quan ứng dụng

FoodSpot là một ứng dụng được thiết kế để hỗ trợ nhà đầu tư/kinh doanh tìm kiếm mặt bằng mở quán ăn, đồng thời phân tích đối thủ cạnh tranh trong khu vực. Ứng dụng tập trung vào việc cung cấp thông tin chi tiết và phân tích dữ liệu để hỗ trợ quyết định kinh doanh.

## Chức năng dự kiến

### 1. Chọn vị trí
- Lọc theo tỉnh/thành phố → quận/huyện
- Tìm kiếm theo địa chỉ hoặc vị trí cụ thể trên bản đồ

### 2. Danh sách quán ăn hiện hữu (đối thủ)
- Thông tin hiển thị: tên quán – vị trí – đánh giá – lượng review
- Show trực tiếp trên map và trong dashboard

### 3. Phân tích đối thủ
- Xem chi tiết từng quán: menu, mức giá, review, đánh giá
- Thống kê: mật độ quán ăn trong bán kính X km
- Phân loại theo: quán bình dân, quán cao cấp, thương hiệu lớn/chuỗi

### 4. Tổng quan & xuất báo cáo
- Chọn một hoặc nhiều khu vực → xuất báo cáo phân tích thị trường
- Gồm: mật độ đối thủ, mức độ cạnh tranh, đánh giá trung bình, nhóm món ăn phổ biến
- Có thể xuất file PDF/Excel để tiện trình bày kế hoạch

## Điểm khác biệt dự kiến

- **Không chỉ tìm quán** → mà tập trung hỗ trợ ra quyết định chọn mặt bằng kinh doanh
- **Trực quan bằng bản đồ** + thống kê số liệu
- **Có khả năng so sánh khu vực** (ví dụ Quận 1 vs Quận 3)

## Cấu trúc dự án

```
├── datascientist/          # Module xử lý và phân tích dữ liệu
│   ├── main.py            # Script chính cho data processing
│   ├── process_data.ipynb # Jupyter notebook để phân tích dữ liệu
│   └── shoppe_data/       # Dữ liệu từ Shopee Food (bị giới hạn)
├── frontend/              # Giao diện người dùng (Next.js)
│   ├── src/
│   ├── public/
│   └── package.json
└── main.py               # Entry point chính của ứng dụng
```

## Lý do dừng phát triển

Dự án đã gặp phải những hạn chế nghiêm trọng trong việc thu thập dữ liệu:

1. **Không thể truy cập API Shopee Food**: Shopee Food không cung cấp API công khai để lấy dữ liệu quán ăn
2. **Hạn chế web scraping**: Shopee Food có các biện pháp chống bot và crawling nghiêm ngặt
3. **Vấn đề pháp lý**: Việc crawl dữ liệu có thể vi phạm điều khoản sử dụng của Shopee Food

---

**Liên hệ**: Nếu bạn có ý tưởng hoặc giải pháp để tiếp tục dự án này, vui lòng mở issue hoặc pull request.
