# Carnegie Mellon University (CMU 15-445) C++ Memory & Smart Pointers


## Smart Pointers 1

## Smart Pointers I — unique_ptr

- `unique_ptr` is a smart pointer with exclusive ownership. Its characteristics include automatic management of dynamically allocated memory, ensuring only one owner per object, automatic memory release at end of scope, and zero-overhead abstraction (virtually no performance penalty).
- `unique_ptr`'s copy constructor is implicitly deleted (`= delete`), so it does not support copy semantics, but it does support move semantics.
- If a function only temporarily uses the object, pass by reference (`std::unique_ptr<T> &`). If the function needs to take ownership, use move semantics (`std::move(ptr)`).
- `make_unique` is used to create `unique_ptr` objects and is the recommended approach over direct construction.


---


## Smart Pointers 2

## Smart Pointers II — shared_ptr

- `shared_ptr` is a smart pointer with shared ownership, allowing multiple pointer instances to jointly own and manage the same object. It supports reference counting and automatic memory management.
- The key difference between ordinary references and rvalue references is that the latter "hints" that resources may be "stolen" (though no actual move occurs in this program). Summary:

| Feature              | Ordinary Reference (&) | Rvalue Reference (&&)                        |
| -------------------- | ---------------------- | -------------------------------------------- |
| **Accepts**          | Lvalues (variables)    | Rvalues (temporaries, std::move results)     |
| **Call syntax**      | `func(var)`            | `func(std::move(var))` or `func(temp_obj)`   |
| **Reference count**  | Unchanged              | Unchanged                                    |
| **Semantic meaning** | Borrowed use           | Preparing to transfer ownership              |
| **Source state**     | Unchanged              | May be "moved from" (depends on impl)        |

- `make_shared` is a template function for creating `shared_ptr`. Compared to the traditional approach (`std::shared_ptr<int> ptr(new int(42));`), it is more memory-efficient and exception-safe. Summary:

| Feature              | make_shared           | shared_ptr(new T) |
| -------------------- | --------------------- | ----------------- |
| **Memory efficiency** | High (single alloc)  | Low (two allocs)  |
| **Exception safety** | Yes                   | Potentially unsafe |
| **Code brevity**     | Yes                   | More verbose      |
| **Custom deleter**   | Not supported         | Supported         |
| **Memory release**   | May be delayed        | Timely            |

- Differences between `shared_ptr`, `unique_ptr`, and `weak_ptr`:

| Feature            | shared_ptr  | unique_ptr  | weak_ptr       |
| ------------------ | ----------- | ----------- | -------------- |
| **Ownership**      | Shared      | Exclusive   | Non-owning     |
| **Copyable**       | Yes         | No          | Yes            |
| **Reference count**| Yes         | No          | Does not increment |
| **Performance**    | Higher      | Very low    | Low            |


---

