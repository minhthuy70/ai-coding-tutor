students = ['An', 'Binh', 'Cuong', 'Dung']

# Lỗi: Duyệt vượt biên len(students) + 1
for i in range(len(students) + 1):
    print(f'Học sinh {i + 1}: {students[i]}')