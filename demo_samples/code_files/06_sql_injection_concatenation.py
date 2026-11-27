import sqlite3

def find_user_by_username(user_input):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Lỗi bảo mật nghiêm trọng: Nối chuỗi trực tiếp vào câu lệnh SQL trong ứng dụng Python
    query = f"SELECT * FROM accounts WHERE username = '{user_input}'"
    print('Executing query:', query)
    cursor.execute(query)
    return cursor.fetchall()

# Input hiểm độc: admin' OR '1'='1
result = find_user_by_username("admin' OR '1'='1")