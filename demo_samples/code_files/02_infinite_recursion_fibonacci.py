def fib(n):
    # Lỗi: Thiếu điều kiện cơ sở (base case) khi n <= 1
    return fib(n - 1) + fib(n - 2)

print('Tính số Fibonacci thứ 5:')
print(fib(5))