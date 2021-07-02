# LocationShareServer
Hướng dẫn khi code trên các nhánh:
    - Chuyển sang nhánh dev: git checkout dev
    - Pull code mới nhất: git pull
    - Chuyển sang nhánh mình, ví dụ: git checkout huy
    - Merge từ dev về nhánh mình: git merge dev
    - Import file .sql, chỉnh sửa thông tin config trong file <i>config.py</i>
    - Bắt đầu code, tránh code trùng file dẫn đến conflict
    - Code xong commit rồi push lên remote repo.
    - Tạo merge request, merge nhánh của mình vào dev: Pull request -> new pull request, chọn nhánh nguồn và nhánh đích phù hợp

Cấu trúc mã nguồn:
    - config.py: chứa config cho database (luôn xem lại trước khi chạy code)
    - models.py: 2 object chính của hệ thống: User và Key
    - main.py: luồng thực thi chính của server
    - LocateShareAPI.py: API "Chia sẻ vị trí" và "Tìm quanh đây"
    - UserManagerAPI.py: API "Đăng nhập" và "Đăng kí"
    - test.py: file test kết nối với database (chạy file test.py, nếu output ra kết quả thì connect DB thành công)
    - db_share_location.sql: file .sql database:
        mỗi khi pull về, import vào local MySQL
        sau khi code, không export phiên bản hiện tại trong MySQL (tránh conflict với phiên bản database trên máy local của thành viên khác)
Ingore:
    venv
    .vscode
    config.py
