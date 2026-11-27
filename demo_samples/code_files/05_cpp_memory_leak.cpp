#include <iostream>

void process_data() {
    for (int i = 0; i < 10000; i++) {
        // Lỗi: Cấp phát động bằng new nhưng không dùng delete[] để giải phóng
        int* buffer = new int[500];
        buffer[0] = i;
    }
}

int main() {
    std::cout << "Dang xu ly du lieu..." << std::endl;
    process_data();
    std::cout << "Xu ly xong!" << std::endl;
    return 0;
}