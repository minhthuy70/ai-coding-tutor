# Carnegie Mellon University (CMU 15-445) C++ STL Guide


## Vectors

## Vectors

- The `inline` keyword primarily suggests that the compiler perform inline optimization — expanding the function code directly at the call site instead of performing a function call, eliminating call overhead (stack push, jump, return, etc.). It also allows functions to be defined in header files, solving the multiple-definition problem.
- `inline` is suitable for frequently called, short functions or performance-sensitive scenarios.
- The `const` keyword on a function promises not to modify the object's state, and the compiler verifies that no members are indeed modified.
- `const` objects can only call `const` member functions.
- Analyzing this code:

```cpp
void print_int_vector(const std::vector<int> &vec) {
  for (const int &elem : vec) {
    std::cout << elem << " ";
  }
  std::cout << "\n";
}
```

1. Pass-by-reference instead of pass-by-value in the function parameter: if the vector has a large capacity, copying would be expensive.
2. The reference in the loop offers little performance benefit here since `int` is only 4 bytes and copying is cheap — modern compilers typically optimize away the difference. However, if `vec` were a vector of `string`, there would be a meaningful performance gain.
3. The `const` keyword in the loop ensures the function does not accidentally modify the original `vec` elements.

- `push_back` copies or moves an already-constructed object to the end of the container. It accepts object copies or rvalue references and is suitable when an existing object needs to be moved or when the original object must be preserved.
- `emplace_back` constructs the object in-place directly at the end of the container. It accepts constructor arguments and is suitable for complex objects or performance-sensitive scenarios.
- Lambda expressions are an important modern C++ feature, allowing us to define anonymous functions inline. For example:

```cpp
 point_vector.erase(
      std::remove_if(point_vector.begin(), point_vector.end(),
                     [](const Point &point) { return point.GetX() == 37; }),
      point_vector.end());
```

Here `[]` is the capture list (empty means no external variables are captured), `(const Point &point)` is the parameter list accepting a const Point reference, and `{ return point.GetX() == 37; }` is the function body returning a bool.

- `remove_if` works by scanning elements and moving those that don't satisfy the condition to the front, and those that do to the back, returning a partition iterator `new_end` (pointing to the "new logical end").
- `erase` deletes all elements from `new_end` to `end`.
- The erase-remove idiom is more efficient than naive deletion because it reduces the number of element moves.
- C++20 provides `std::erase_if` to simplify the above operation.


---


## Hash Maps

## Hash Maps

- `unordered_map` is essentially a **hash table**, using buckets and linked lists to handle collisions. It provides constant-time lookup performance in most cases, at the cost of higher memory overhead and unordered elements.
- The traversal order of `unordered_map` is unpredictable, influenced by the hash function, bucket array size, and the order of elements within buckets.
- The trade-off for being unordered is faster lookup speed, since the storage location can be computed directly via the hash function without needing multiple key comparisons as in a tree.


---


## Sets

## Sets

- Most standard library implementations (such as GCC's libstdc++ and Microsoft's MSVC library) use **red-black trees** as the underlying data structure for `std::set`.
- `std::set` chooses red-black trees as its underlying implementation because it offers the best balance between **lookup efficiency**, **insertion/deletion performance**, **memory usage**, and **implementation complexity**.
- Because the underlying implementation uses a red-black tree (a balanced binary search tree), `std::set` is an ordered set — elements are automatically kept in order upon insertion, and an in-order traversal naturally produces a sorted sequence.
- Default ordering is ascending; custom sort order can be specified via a comparison function.


---


## Iterators

## Iterators

- An iterator is a design pattern and programming concept that provides a uniform way to access elements in a container (arrays, linked lists, trees, etc.) without exposing the container's internal structure.
- The core value of iterators lies in abstraction, uniformity, flexibility, safety, and composability.
- Analyzing this code:

```cpp
for (DLLIterator iter = dll.Begin(); iter != dll.End(); ++iter) {
    std::cout << *iter << " ";
}
```

1. `dll.Begin()` returns not a pointer, but a newly constructed `DLLIterator` object that internally holds a pointer to the first node.
2. `dll.End()` returns an iterator representing "past-the-end" (`curr_` = `nullptr`). This is called on every loop condition check, incurring temporary object overhead.
3. The condition compares the iterator's `curr_` pointer against `nullptr` to determine if the end of the list has been reached.
4. Prefix `++iter` is recommended because it avoids creating a temporary object and is more efficient. Postfix `++` creates a temporary object each time, with extra construction/destruction overhead.
5. Best practice: prefer prefix `++iter` in for loops unless you explicitly need postfix `++` semantics (i.e., using the value before increment).

- `size_t` is an unsigned integer type in C++ (0 and positive integers), specifically designed to represent object sizes and array indices, avoiding safety issues from negative indices.
- `size_t` is 8 bytes on 64-bit systems and 4 bytes on 32-bit systems, providing portability.


---

