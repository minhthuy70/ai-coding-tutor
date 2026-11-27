def append_item(val, target_list=[]):
    # Lỗi kinh điển trong Python: Default argument là một mutable object (list)
    target_list.append(val)
    return target_list

print('Lần gọi 1:', append_item('Apple'))
print('Lần gọi 2:', append_item('Banana'))
print('Lần gọi 3:', append_item('Cherry'))
# Kết quả bất ngờ: ['Apple', 'Banana', 'Cherry'] thay vì ['Cherry']