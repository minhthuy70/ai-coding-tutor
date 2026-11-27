counter = 0

def increment():
    # Lỗi kinh điển trong Python: UnboundLocalError
    # Khi cố gắng thay đổi biến counter bên ngoài hàm mà thiếu từ khóa 'global'
    counter += 1
    return counter

print("Giá trị ban đầu:", counter)
print("Sau khi tăng:", increment())