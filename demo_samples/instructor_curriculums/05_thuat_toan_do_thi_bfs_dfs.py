"""
Module: Graph Algorithms - Breadth-First Search (BFS) & Depth-First Search (DFS)
Giáo trình chuẩn Giải thuật trên Đồ thị - Ngôn ngữ Python
"""

from collections import deque
from typing import Dict, List, Set, Optional

# Biểu diễn đồ thị bằng Danh sách kề (Adjacency List)
Graph = Dict[str, List[str]]

def breadth_first_search(graph: Graph, start_node: str) -> List[str]:
    """
    Thuật toán Tìm kiếm theo chiều rộng (BFS):
    - Sử dụng Hàng đợi (Queue FIFO - collections.deque).
    - Thăm tất cả các đỉnh lân cận ở khoảng cách k trước khi chuyển sang khoảng cách k+1.
    - Tìm đường đi ngắn nhất trên đồ thị không có trọng số.
    - Độ phức tạp: O(V + E) thời gian, O(V) không gian bộ nhớ.
    """
    visited: Set[str] = set()
    queue: deque[str] = deque([start_node])
    traversal_order: List[str] = []

    visited.add(start_node)

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def depth_first_search(graph: Graph, start_node: str, visited: Optional[Set[str]] = None) -> List[str]:
    """
    Thuật toán Tìm kiếm theo chiều sâu (DFS):
    - Khám phá sâu nhất có thể theo từng nhánh trước khi quay lui (Backtracking).
    - Sử dụng Ngăn xếp (Call Stack thông qua Đệ quy hoặc collections.deque).
    - Ứng dụng: Duyệt đồ thị, phát hiện chu trình, sắp xếp Tô-pô (Topological Sort).
    - Độ phức tạp: O(V + E) thời gian, O(V) bộ nhớ ngăn xếp.
    """
    if visited is None:
        visited = set()

    visited.add(start_node)
    traversal: List[str] = [start_node]

    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            traversal.extend(depth_first_search(graph, neighbor, visited))

    return traversal