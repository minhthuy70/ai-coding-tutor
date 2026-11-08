# Java Modern Features: Generics, Lambdas & Functional Streams Guide

## Java Generics & Type Safety

# Generics

Generics allow you to write classes, interfaces, and methods where the type is a parameter, defined by the caller rather than hard-coded. They were introduced in Java 5 to solve a fundamental problem: code that needed to be reusable across many types had no way to enforce type safety at compile time. Generics give you that reusability and that safety at the same time.

```

Think of it like this:
  A Box class without generics can hold anything — but when you take something out,
  you have to guess what it is and cast it, and if you guess wrong, the program crashes.
  A Box<T> class tells you exactly what is inside before you even open it.
  The type is checked when you put the item in, not when you take it out.

```

## 1. The Problem Generics Solve

Before generics, a reusable container had to hold `Object`. This meant every retrieval required a cast, and a wrong cast would compile just fine but crash at runtime.

```java
// Pre-generics: a Box that holds Object
public class Box {
    private Object value;

    public Box(Object value) {
        this.value = value;
    }

    public Object getValue() {
        return value;
    }
}

```

```java
Box stringBox = new Box("Hello");
Box intBox    = new Box(42);

// You must cast to get a usable type
String s = (String) stringBox.getValue(); // Works fine
Integer i = (Integer) intBox.getValue();  // Works fine

// But nothing stops this mistake at compile time:
String bad = (String) intBox.getValue();
// Output: Exception in thread "main" java.lang.ClassCastException:
//         class java.lang.Integer cannot be cast to class java.lang.String

```

The ClassCastException only appears at runtime, potentially deep inside production code. With generics, the same mistake becomes a compiler error — it never reaches production.

```java
// Generic version: the type is a parameter
public class Box<T> {
    private T value;

    public Box(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }
}

```

```java
Box<String>  stringBox = new Box<>("Hello");
Box<Integer> intBox    = new Box<>(42);

String s  = stringBox.getValue(); // No cast required
Integer i = intBox.getValue();    // No cast required

// This now fails at compile time, not runtime:
// String bad = (String) intBox.getValue(); // Compiler error: incompatible types

```

The error moved from runtime to compile time. That is the core value proposition of generics.

## 2. Generic Classes

A generic class declares one or more type parameters in angle brackets after the class name. Those parameters act as placeholders that are replaced with a real type when the class is instantiated.

**Syntax:** `public class ClassName<T> { ... }`

```java
public class Box<T> {
    private T value;

    public Box(T value) {
        this.value = value;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return "Box[" + value + "]";
    }
}

```

```java
Box<String>  nameBox  = new Box<>("Alice");
Box<Integer> ageBox   = new Box<>(30);
Box<Double>  priceBox = new Box<>(19.99);

System.out.println(nameBox);   // Output: Box[Alice]
System.out.println(ageBox);    // Output: Box[30]
System.out.println(priceBox);  // Output: Box[19.99]

// The compiler enforces the type — this does not compile:
// ageBox.setValue("oops"); // Compiler error: incompatible types: String cannot be converted to Integer

```

`T` is simply a name for "whatever type the caller chooses." When you write `Box<String>`, every `T` in that class becomes `String` for that instance. When you write `Box<Integer>`, every `T` becomes `Integer`.

## 3. Type Parameter Naming Conventions

Type parameter names are single uppercase letters by convention. These letters are not enforced by the compiler, but every Java developer follows them, and the standard library uses them throughout.

| Letter | Convention                  |
|--------|-----------------------------|
| T      | Type (general purpose)      |
| E      | Element (collections)       |
| K      | Key (maps)                  |
| V      | Value (maps)                |
| N      | Number                      |
| R      | Return type                 |

These are conventions, not rules, but following them makes generic code immediately readable to any Java developer. When you see `Map<K, V>` or `List<E>`, the intent is clear without needing to read the full class.

## 4. Generic Methods

A method can declare its own type parameter independent of the class it belongs to. This is useful for utility methods that need to work across types without requiring the entire class to be generic.

**Syntax:** `public static <T> ReturnType methodName(T arg) { ... }`

```java
public class ArrayUtils {

    // Swaps two elements in an array of any type
    public static <T> void swap(T[] arr, int i, int j) {
        T temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Returns the first element that equals the target, or null if not found
    public static <T> T findFirst(T[] arr, T target) {
        for (T element : arr) {
            if (element.equals(target)) {
                return element;
            }
        }
        return null;
    }
}

```

```java
String[] names = {"Alice", "Bob", "Carol", "Diana"};
System.out.println(java.util.Arrays.toString(names));
// Output: [Alice, Bob, Carol, Diana]

ArrayUtils.swap(names, 0, 3);
System.out.println(java.util.Arrays.toString(names));
// Output: [Diana, Bob, Carol, Alice]

String found = ArrayUtils.findFirst(names, "Carol");
System.out.println(found);
// Output: Carol

Integer[] numbers = {10, 20, 30, 40, 50};
ArrayUtils.swap(numbers, 1, 3);
System.out.println(java.util.Arrays.toString(numbers));
// Output: [10, 40, 30, 20, 50]

```

Notice that the type is never specified explicitly at the call site. The compiler infers `T` from the arguments passed in — `String[]` makes `T` become `String`, and `Integer[]` makes `T` become `Integer`.

## 5. Multiple Type Parameters

A class or method can declare more than one type parameter, separated by commas. This is common for containers that hold two related but potentially different values.

```java
public class Pair<A, B> {
    private A first;
    private B second;

    public Pair(A first, B second) {
        this.first  = first;
        this.second = second;
    }

    public A getFirst()  { return first;  }
    public B getSecond() { return second; }

    // Returns a new Pair with the positions swapped
    public Pair<B, A> swap() {
        return new Pair<>(second, first);
    }

    @Override
    public String toString() {
        return "(" + first + ", " + second + ")";
    }
}

```

```java
Pair<String, Integer> nameAndAge = new Pair<>("Alice", 30);
System.out.println(nameAndAge);
// Output: (Alice, 30)

Pair<Integer, String> swapped = nameAndAge.swap();
System.out.println(swapped);
// Output: (30, Alice)

Pair<String, Boolean> config = new Pair<>("darkMode", true);
System.out.println(config.getFirst() + " = " + config.getSecond());
// Output: darkMode = true

```

`Map<K, V>` in the Java standard library follows exactly this pattern. `K` is the key type and `V` is the value type, and both are independently chosen by the caller.

## 6. Bounded Type Parameters

Sometimes you need to restrict what types can be used as a type argument. Bounds let you require that `T` be a specific type or a subclass of it.

### Upper bound: extends

`<T extends Number>` means T must be `Number` or any subclass of it (`Integer`, `Double`, `Long`, etc.). This grants access to methods defined on `Number` inside the generic code.

```java
import java.util.List;

public class MathUtils {

    // T must be a Number — so .doubleValue() is available
    public static <T extends Number> double sum(List<T> list) {
        double total = 0;
        for (T element : list) {
            total += element.doubleValue();
        }
        return total;
    }
}

```

```java
List<Integer> ints    = java.util.Arrays.asList(1, 2, 3, 4, 5);
List<Double>  doubles = java.util.Arrays.asList(1.5, 2.5, 3.0);

System.out.println(MathUtils.sum(ints));
// Output: 15.0

System.out.println(MathUtils.sum(doubles));
// Output: 7.0

// This does not compile — String does not extend Number:
// List<String> strings = java.util.Arrays.asList("a", "b");
// MathUtils.sum(strings); // Compiler error: String is not within bounds

```

### Multiple bounds

A type parameter can be required to satisfy more than one constraint using `&`. The class bound (if any) must come first, followed by interface bounds.

```java
import java.io.Serializable;
import java.util.Arrays;

public class Sorter {

    // T must implement both Comparable<T> and Serializable
    public static <T extends Comparable<T> & Serializable> T findMax(T[] arr) {
        if (arr == null || arr.length == 0) {
            throw new IllegalArgumentException("Array must not be empty");
        }
        T max = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (arr[i].compareTo(max) > 0) {
                max = arr[i];
            }
        }
        return max;
    }
}

```

```java
String[] words   = {"banana", "apple", "cherry", "date"};
Integer[] values = {3, 1, 4, 1, 5, 9, 2, 6};

System.out.println(Sorter.findMax(words));
// Output: date

System.out.println(Sorter.findMax(values));
// Output: 9

```

`String` and `Integer` both implement `Comparable` and `Serializable`, so both calls compile. A custom class that did not implement both would be rejected at compile time.

## 7. Wildcards

Wildcards use `?` as a type argument when you do not need to name the type but still want flexibility. They appear in method parameters, not in class declarations.

### Unbounded wildcard: `<?>`

`List<?>` accepts a list of any type. Use this when you only need to read elements and treat them as `Object`, and the specific type does not matter.

```java
import java.util.List;

public class Printer {

    public static void printList(List<?> list) {
        for (Object element : list) {
            System.out.print(element + " ");
        }
        System.out.println();
    }
}

```

```java
List<String>  names   = java.util.Arrays.asList("Alice", "Bob", "Carol");
List<Integer> numbers = java.util.Arrays.asList(1, 2, 3);
List<Double>  prices  = java.util.Arrays.asList(9.99, 14.99, 4.99);

Printer.printList(names);
// Output: Alice Bob Carol

Printer.printList(numbers);
// Output: 1 2 3

Printer.printList(prices);
// Output: 9.99 14.99 4.99

```

### Upper bounded wildcard: `<? extends T>`

`List<? extends Number>` accepts `List<Integer>`, `List<Double>`, `List<Long>`, or any other list whose element type is a subtype of `Number`. Use this when you are **reading** from the list (the list is a producer of values).

```java
import java.util.List;

public class Statistics {

    public static double average(List<? extends Number> list) {
        double sum = 0;
        for (Number n : list) {
            sum += n.doubleValue();
        }
        return sum / list.size();
    }
}

```

```java
List<Integer> scores  = java.util.Arrays.asList(80, 90, 75, 95);
List<Double>  ratings = java.util.Arrays.asList(4.5, 3.8, 5.0, 4.2);

System.out.printf("Average score:  %.2f%n", Statistics.average(scores));
// Output: Average score:  85.00

System.out.printf("Average rating: %.2f%n", Statistics.average(ratings));
// Output: Average rating: 4.38

```

### Lower bounded wildcard: `<? super T>`

`List<? super Integer>` accepts `List<Integer>`, `List<Number>`, or `List<Object>` — any list whose element type is a supertype of `Integer`. Use this when you are **writing** to the list (the list is a consumer of values).

```java
import java.util.List;

public class Filler {

    public static void addNumbers(List<? super Integer> list) {
        for (int i = 1; i <= 5; i++) {
            list.add(i); // Safe — Integer is always compatible with a supertype of Integer
        }
    }
}

```

```java
List<Integer> intList    = new java.util.ArrayList<>();
List<Number>  numList    = new java.util.ArrayList<>();
List<Object>  objectList = new java.util.ArrayList<>();

Filler.addNumbers(intList);
Filler.addNumbers(numList);
Filler.addNumbers(objectList);

System.out.println(intList);
// Output: [1, 2, 3, 4, 5]

System.out.println(numList);
// Output: [1, 2, 3, 4, 5]

System.out.println(objectList);
// Output: [1, 2, 3, 4, 5]

```

### The PECS mnemonic

**Producer Extends, Consumer Super.**

- If a structure **produces** values you will read, use `<? extends T>`.
- If a structure **consumes** values you will write, use `<? super T>`.

```java
// src produces T values — use extends (you are reading from it)
// dest consumes T values — use super (you are writing into it)
public static <T> void copy(List<? extends T> src, List<? super T> dest) {
    for (T item : src) {
        dest.add(item);
    }
}

```

```java
List<Integer> source      = java.util.Arrays.asList(1, 2, 3);
List<Number>  destination = new java.util.ArrayList<>();

copy(source, destination);
System.out.println(destination);
// Output: [1, 2, 3]

```

## 8. Generic Interfaces

Interfaces can also be parameterized with type parameters. A class that implements a generic interface substitutes a concrete type for each parameter, creating a type-safe contract.

```java
public interface Repository<T, ID> {
    T findById(ID id);
    void save(T entity);
    void delete(ID id);
}

```

```java
public class User {
    private Long id;
    private String name;
    private String email;

    public User(Long id, String name, String email) {
        this.id    = id;
        this.name  = name;
        this.email = email;
    }

    public Long getId()    { return id;    }
    public String getName()  { return name;  }
    public String getEmail() { return email; }

    @Override
    public String toString() {
        return "User{id=" + id + ", name='" + name + "', email='" + email + "'}";
    }
}

```

```java
import java.util.HashMap;
import java.util.Map;

public class UserRepository implements Repository<User, Long> {
    private Map<Long, User> store = new HashMap<>();

    @Override
    public User findById(Long id) {
        return store.get(id);
    }

    @Override
    public void save(User user) {
        store.put(user.getId(), user);
    }

    @Override
    public void delete(Long id) {
        store.remove(id);
    }
}

```

```java
UserRepository repo = new UserRepository();

repo.save(new User(1L, "Alice", "alice@example.com"));
repo.save(new User(2L, "Bob",   "bob@example.com"));

System.out.println(repo.findById(1L));
// Output: User{id=1, name='Alice', email='alice@example.com'}

System.out.println(repo.findById(2L));
// Output: User{id=2, name='Bob', email='bob@example.com'}

repo.delete(1L);
System.out.println(repo.findById(1L));
// Output: null

```

This pattern is exactly how Spring Data JPA works. `JpaRepository<User, Long>` is a generic interface — Spring generates the implementation automatically, and your repository inherits type-safe methods like `findById(Long id)` and `save(User entity)` without writing a single line of persistence code.

## 9. Type Erasure

Generics exist only at compile time. The compiler uses the type information to verify correctness and insert casts where needed, but then **removes** all type parameters from the compiled bytecode. At runtime, `Box<String>` and `Box<Integer>` are both just `Box`. This process is called type erasure.

The erasure rule: `T` is replaced with `Object` (or the upper bound if one was declared — `<T extends Number>` becomes `Number` at runtime).

This design preserved backward compatibility with pre-generics Java code, but it has three important consequences.

```java
import java.util.ArrayList;
import java.util.List;

public class TypeErasureDemo {

    public static void main(String[] args) {

        // Consequence 1: Cannot use instanceof with a parameterized type.
        // At runtime the type parameter is gone, so the check is meaningless.
        List<String> list = new ArrayList<>();
        // if (list instanceof List<String>) { }
        // Compiler error: illegal generic type for instanceof
        // You can only check: if (list instanceof List) { } — without the type argument

        // Consequence 2: Cannot create an instance of a type parameter.
        // new T() is not allowed because the compiler cannot know the constructor to call.
        // public static <T> T create() {
        //     return new T(); // Compiler error: cannot instantiate type T
        // }
        // Workaround: pass a Class<T> token or a Supplier<T> to the method.

        // Consequence 3: Cannot create a generic array directly.
        // T[] arr = new T[10]; // Compiler error: generic array creation
        // Workaround: cast an Object array (with an unchecked warning).
        // T[] arr = (T[]) new Object[10];
    }
}

```

Understanding type erasure explains why certain patterns that seem logical in Java are forbidden by the compiler. The information simply does not exist at runtime.

## 10. Complete Example

```java
import java.util.Arrays;

public class Stack<T> {
    private T[] elements;
    private int size;
    private static final int DEFAULT_CAPACITY = 10;

    @SuppressWarnings("unchecked")
    public Stack() {
        // Generic array creation is not directly allowed — cast an Object array instead
        elements = (T[]) new Object[DEFAULT_CAPACITY];
        size = 0;
    }

    public void push(T item) {
        if (size == elements.length) {
            elements = Arrays.copyOf(elements, elements.length * 2);
        }
        elements[size++] = item;
    }

    public T pop() {
        if (isEmpty()) {
            throw new java.util.EmptyStackException();
        }
        T item = elements[--size];
        elements[size] = null; // Allow garbage collection
        return item;
    }

    public T peek() {
        if (isEmpty()) {
            throw new java.util.EmptyStackException();
        }
        return elements[size - 1];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    @Override
    public String toString() {
        return "Stack" + Arrays.toString(Arrays.copyOf(elements, size));
    }
}

```

```java
public class MathUtils {

    // Works with any type that can be compared to itself
    public static <T extends Comparable<T>> T max(T a, T b) {
        return a.compareTo(b) >= 0 ? a : b;
    }
}

```

```java
public class Main {
    public static void main(String[] args) {

        // Stack<String>
        Stack<String> wordStack = new Stack<>();
        wordStack.push("first");
        wordStack.push("second");
        wordStack.push("third");

        System.out.println(wordStack);
        // Output: Stack[first, second, third]

        System.out.println("Peek: " + wordStack.peek());
        // Output: Peek: third

        System.out.println("Pop: " + wordStack.pop());
        // Output: Pop: third

        System.out.println(wordStack);
        // Output: Stack[first, second]

        // Stack<Integer>
        Stack<Integer> intStack = new Stack<>();
        intStack.push(10);
        intStack.push(20);
        intStack.push(30);

        System.out.println(intStack);
        // Output: Stack[10, 20, 30]

        while (!intStack.isEmpty()) {
            System.out.print(intStack.pop() + " ");
        }
        System.out.println();
        // Output: 30 20 10

        // Stack<Double>
        Stack<Double> doubleStack = new Stack<>();
        doubleStack.push(1.1);
        doubleStack.push(2.2);
        doubleStack.push(3.3);

        System.out.println("Size: " + doubleStack.size());
        // Output: Size: 3

        // MathUtils.max with different types
        System.out.println(MathUtils.max(42, 99));
        // Output: 99

        System.out.println(MathUtils.max("apple", "mango"));
        // Output: mango

        System.out.println(MathUtils.max(3.14, 2.71));
        // Output: 3.14
    }
}

```

## 11. Key Takeaways

- Generics move type errors from runtime to compile time — the single most important reason to use them
- A type parameter (`T`, `E`, `K`, `V`) is a placeholder replaced by the caller's chosen type at instantiation
- Generic classes, generic methods, and generic interfaces each declare type parameters independently
- Upper bounds (`<T extends Number>`) restrict what types are allowed and unlock the bound type's methods inside the generic code
- Wildcards (`<?>`, `<? extends T>`, `<? super T>`) provide flexibility at call sites; use PECS to remember which to choose
- Type erasure removes all generic type information at runtime, which is why `instanceof` with parameterized types and `new T()` are both forbidden
- `@SuppressWarnings("unchecked")` is the correct way to acknowledge a deliberate, safe unchecked cast (such as `(T[]) new Object[n]`)
- Generic interfaces like `Repository<T, ID>` are the foundation of patterns like Spring Data JPA
- Naming conventions (`T`, `E`, `K`, `V`, `N`, `R`) are not enforced but are universally followed — use them

---

Generics are what make the Collections framework and Spring's APIs readable and type-safe — every `List<E>`, `Map<K, V>`, `Optional<T>`, and `JpaRepository<T, ID>` you use daily is built on exactly the concepts covered here.

---

## Java Lambda Expressions & Functional Interfaces

# Lambdas

A lambda expression is a concise way to represent an anonymous function — a block of behavior that can be stored in a variable, passed to a method, or returned from a method. Lambdas did not replace anything in Java; they gave you a shorter syntax for something the language already supported through anonymous classes. Understanding that connection is the key to understanding lambdas completely.

```

Think of it like this:
  You need to tell a sorting method HOW to compare two strings.
  Old way: write an entire anonymous class with a single method — five lines of ceremony for one line of logic.
  Lambda way: (a, b) -> a.compareTo(b)
  Same instruction, fraction of the noise.

```

## 1. The Problem Lambdas Solve

Before lambdas, passing behavior to a method required an anonymous class. The syntax was verbose for something conceptually simple.

```java
// Passing behavior with an anonymous class — Runnable
Runnable printHello = new Runnable() {
    @Override
    public void run() {
        System.out.println("Hello from a thread!");
    }
};

// Passing behavior with an anonymous class — Comparator<String>
Comparator<String> byLength = new Comparator<String>() {
    @Override
    public int compare(String a, String b) {
        return Integer.compare(a.length(), b.length());
    }
};

```

Five lines of boilerplate to express one line of logic. The anonymous class syntax forces you to name the interface, override the method, open and close braces — all before reaching the actual behavior. Lambdas strip all of that away.

```java
// The same two expressions as lambdas
Runnable printHello = () -> System.out.println("Hello from a thread!");

Comparator<String> byLength = (a, b) -> Integer.compare(a.length(), b.length());

```

The behavior is identical. The lambda is not a different mechanism — it compiles to the same thing. It is simply a shorter way to write it.

## 2. Functional Interfaces

A **functional interface** is any interface that has exactly one abstract method. That single method is what the lambda implements. The `@FunctionalInterface` annotation asks the compiler to enforce this constraint and will produce an error if you accidentally add a second abstract method.

```java
@FunctionalInterface
public interface Transformer<T> {
    T transform(T input);
}

```

`Transformer<T>` has one abstract method: `transform`. You can implement it three ways, all of which produce an object of type `Transformer<String>`.

**Anonymous class:**

```java
Transformer<String> shout = new Transformer<String>() {
    @Override
    public String transform(String input) {
        return input.toUpperCase();
    }
};

```

**Lambda:**

```java
Transformer<String> shout = input -> input.toUpperCase();

```

**Method reference:**

```java
Transformer<String> shout = String::toUpperCase;

```

All three produce a `Transformer<String>` object. A lambda is not something new — it is an instance of a functional interface written in a shorter form. When you write `input -> input.toUpperCase()`, Java creates an object that implements `Transformer` and whose `transform` method executes that body.

```java
System.out.println(shout.transform("hello"));
// Output: HELLO

```

## 3. Lambda Syntax

Lambda syntax scales from a single expression to a full method body. Every variation is shown below.

**No parameters:**

```java
Runnable greet = () -> System.out.println("Hello");
greet.run();
// Output: Hello

```

**One parameter — parentheses are optional:**

```java
Transformer<String> upper = name -> name.toUpperCase();
System.out.println(upper.transform("alice"));
// Output: ALICE

```

**One parameter — with parentheses:**

```java
Transformer<String> upper = (name) -> name.toUpperCase();

```

**Two parameters:**

```java
// Using a standard functional interface from java.util.function
java.util.function.BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
System.out.println(add.apply(3, 4));
// Output: 7

```

**Multi-line body — requires braces and an explicit return:**

```java
java.util.function.BiFunction<Integer, Integer, Integer> add = (a, b) -> {
    int sum = a + b;
    return sum;
};
System.out.println(add.apply(10, 20));
// Output: 30

```

**Explicit parameter types:**

```java
java.util.function.BiFunction<String, Integer, String> repeat = (String s, int n) -> s.repeat(n);
System.out.println(repeat.apply("ab", 3));
// Output: ababab

```

The rule: if the body is a single expression, omit the braces and `return`. If the body is multiple statements, use braces and `return` explicitly. Parameter types are always optional because the compiler infers them from the functional interface.

## 4. Built-in Functional Interfaces (java.util.function)

Java ships a set of general-purpose functional interfaces in `java.util.function`. You will use these constantly. Learning them means you rarely need to define your own.

| Interface            | Signature          | What it does                    |
|----------------------|--------------------|---------------------------------|
| `Predicate<T>`       | `T -> boolean`     | Tests a condition               |
| `Function<T, R>`     | `T -> R`           | Transforms a value              |
| `Consumer<T>`        | `T -> void`        | Consumes a value, no return     |
| `Supplier<T>`        | `() -> T`          | Produces a value, no input      |
| `BiFunction<T,U,R>`  | `(T, U) -> R`      | Transforms two values into one  |
| `BiPredicate<T,U>`   | `(T, U) -> boolean`| Tests two values                |
| `UnaryOperator<T>`   | `T -> T`           | Transforms a value of same type |
| `BinaryOperator<T>`  | `(T, T) -> T`      | Combines two values of same type|

**Predicate<T> — T -> boolean**

Tests whether a value satisfies a condition. Used for filtering.

```java
import java.util.function.Predicate;

Predicate<Integer> isEven = n -> n % 2 == 0;
System.out.println(isEven.test(4));   // Output: true
System.out.println(isEven.test(7));   // Output: false

Predicate<String> isNonBlank = s -> !s.isBlank();
System.out.println(isNonBlank.test("hello"));  // Output: true
System.out.println(isNonBlank.test("   "));    // Output: false

```

**Function<T, R> — T -> R**

Transforms a value of type T into a value of type R.

```java
import java.util.function.Function;

Function<String, Integer> getLength = s -> s.length();
System.out.println(getLength.apply("lambda"));  // Output: 6

Function<String, String> toUpperCase = s -> s.toUpperCase();
System.out.println(toUpperCase.apply("hello")); // Output: HELLO

```

**Consumer<T> — T -> void**

Consumes a value and produces no result. Used for side effects like printing or writing.

```java
import java.util.function.Consumer;
import java.util.ArrayList;
import java.util.List;

Consumer<String> print = s -> System.out.println(s);
print.accept("hello");  // Output: hello

List<String> collected = new ArrayList<>();
Consumer<String> saveToList = s -> collected.add(s);
saveToList.accept("alpha");
saveToList.accept("beta");
System.out.println(collected); // Output: [alpha, beta]

```

**Supplier<T> — () -> T**

Takes no input and produces a value. Used for lazy evaluation or default values.

```java
import java.util.function.Supplier;
import java.util.Random;

Supplier<String> defaultName = () -> "Unknown";
System.out.println(defaultName.get()); // Output: Unknown

Supplier<Integer> randomInt = () -> new Random().nextInt(100);
System.out.println(randomInt.get()); // Output: (a random number 0–99)

```

**BiFunction<T, U, R> — (T, U) -> R**

Takes two inputs of potentially different types and produces a result.

```java
import java.util.function.BiFunction;

BiFunction<String, Integer, String> repeat = (s, n) -> s.repeat(n);
System.out.println(repeat.apply("ha", 3)); // Output: hahaha

```

**BiPredicate<T, U> — (T, U) -> boolean**

Tests a condition over two inputs.

```java
import java.util.function.BiPredicate;

BiPredicate<String, String> startsWith = (s, prefix) -> s.startsWith(prefix);
System.out.println(startsWith.test("lambda", "lam")); // Output: true
System.out.println(startsWith.test("lambda", "xyz")); // Output: false

```

**UnaryOperator<T> — T -> T**

A specialization of `Function` where the input and output type are the same.

```java
import java.util.function.UnaryOperator;

UnaryOperator<Integer> doubleIt = n -> n * 2;
System.out.println(doubleIt.apply(5)); // Output: 10

UnaryOperator<String> reverse = s -> new StringBuilder(s).reverse().toString();
System.out.println(reverse.apply("hello")); // Output: olleh

```

**BinaryOperator<T> — (T, T) -> T**

A specialization of `BiFunction` where both inputs and the output are the same type.

```java
import java.util.function.BinaryOperator;

BinaryOperator<Integer> add = (a, b) -> a + b;
System.out.println(add.apply(6, 4)); // Output: 10

BinaryOperator<String> concat = (a, b) -> a + b;
System.out.println(concat.apply("Hello, ", "World")); // Output: Hello, World

```

## 5. Method References

A method reference is a shorthand for a lambda that does nothing but call an existing method. The syntax `ClassName::methodName` or `object::methodName` replaces a lambda whose entire body is a single method call. There are four forms.

**Static method reference — `ClassName::staticMethod`**

Use when the lambda just calls a static method, passing through its argument.

```java
import java.util.function.Function;

// Lambda version
Function<String, Integer> parse = s -> Integer.parseInt(s);

// Method reference version
Function<String, Integer> parse = Integer::parseInt;

System.out.println(parse.apply("42")); // Output: 42

// Another example
Function<Integer, Integer> abs = n -> Math.abs(n);
Function<Integer, Integer> abs = Math::abs;
System.out.println(abs.apply(-7)); // Output: 7

```

**Bound instance method reference — `object::instanceMethod`**

Use when the lambda calls a method on a specific, already-known instance.

```java
import java.util.function.Consumer;

// Lambda version
Consumer<String> print = s -> System.out.println(s);

// Method reference version
Consumer<String> print = System.out::println;

print.accept("bound reference"); // Output: bound reference

// Another example
String prefix = "Hello, ";
Function<String, String> greet = name -> prefix.concat(name);
Function<String, String> greet = prefix::concat;
System.out.println(greet.apply("Alice")); // Output: Hello, Alice

```

**Unbound instance method reference — `ClassName::instanceMethod`**

Use when the lambda takes an instance as its first argument and calls a method on it. The instance is not fixed ahead of time.

```java
import java.util.function.Function;

// Lambda version
Function<String, String> upper = s -> s.toUpperCase();

// Method reference version
Function<String, String> upper = String::toUpperCase;

System.out.println(upper.apply("hello")); // Output: HELLO

Function<String, Integer> length = s -> s.length();
Function<String, Integer> length = String::length;
System.out.println(length.apply("lambda")); // Output: 6

```

**Constructor reference — `ClassName::new`**

Use when the lambda creates a new instance.

```java
import java.util.function.Supplier;
import java.util.function.Function;
import java.util.ArrayList;

// Lambda version
Supplier<ArrayList<String>> makeList = () -> new ArrayList<>();

// Method reference version
Supplier<ArrayList<String>> makeList = ArrayList::new;

ArrayList<String> list = makeList.get();
list.add("test");
System.out.println(list); // Output: [test]

// Constructor reference with an argument
Function<String, StringBuilder> makeBuilder = s -> new StringBuilder(s);
Function<String, StringBuilder> makeBuilder = StringBuilder::new;
System.out.println(makeBuilder.apply("hello")); // Output: hello

```

The decision rule: if a lambda body is exactly `args -> SomeMethod(args)`, replace it with a method reference. If the lambda has any additional logic, keep it as a lambda.

## 6. Variable Capture

Lambdas can read variables from the enclosing scope. This is called **capturing** a variable.

```java
String greeting = "Hello";
Consumer<String> greet = name -> System.out.println(greeting + ", " + name + "!");

greet.accept("Alice"); // Output: Hello, Alice!
greet.accept("Bob");   // Output: Hello, Bob!

```

The lambda captured `greeting` from the surrounding scope. The rule is that captured local variables must be **effectively final** — they do not need the `final` keyword explicitly, but they must never be reassigned after the point they are captured. The compiler enforces this.

```java
String greeting = "Hello";
greeting = "Hi"; // This reassignment makes greeting NOT effectively final

// Compiler error on the line below:
// Variable used in lambda expression should be final or effectively final
Consumer<String> greet = name -> System.out.println(greeting + ", " + name);

```

This restriction exists because lambdas may execute later or in a different thread, and allowing the variable to change would create unpredictable behavior.

**Instance fields and static fields have no such restriction.** They can be freely read and written inside a lambda because they live on the heap, not on the stack.

```java
public class Counter {
    private int count = 0; // instance field — no restriction

    public void run() {
        Runnable increment = () -> count++; // reading and writing instance field is fine
        increment.run();
        increment.run();
        System.out.println(count); // Output: 2
    }
}

```

## 7. Chaining Functional Interfaces

Predicate and Function both provide default methods for composing multiple operations into a pipeline.

**Predicate chaining — `and()`, `or()`, `negate()`**

```java
import java.util.function.Predicate;

Predicate<String> isNonNull  = s -> s != null;
Predicate<String> isNonBlank = s -> !s.isBlank();
Predicate<String> isLongEnough = s -> s.length() >= 8;

// All three conditions must pass
Predicate<String> isValidPassword = isNonNull.and(isNonBlank).and(isLongEnough);

System.out.println(isValidPassword.test("secret99"));  // Output: true
System.out.println(isValidPassword.test("short"));     // Output: false
System.out.println(isValidPassword.test(""));          // Output: false

// or() — either condition is enough
Predicate<Integer> isNegative = n -> n < 0;
Predicate<Integer> isZero = n -> n == 0;
Predicate<Integer> isNonPositive = isNegative.or(isZero);

System.out.println(isNonPositive.test(-3)); // Output: true
System.out.println(isNonPositive.test(0));  // Output: true
System.out.println(isNonPositive.test(5));  // Output: false

// negate() — flip the result
Predicate<String> isBlank = String::isBlank;
Predicate<String> isNotBlank = isBlank.negate();

System.out.println(isNotBlank.test("hello")); // Output: true
System.out.println(isNotBlank.test("   "));   // Output: false

```

**Function chaining — `andThen()`, `compose()`**

`andThen(f)` applies `f` after the current function. `compose(f)` applies `f` before the current function.

```java
import java.util.function.Function;

Function<String, Integer> parseToInt = Integer::parseInt;
Function<Integer, Integer> doubleIt  = n -> n * 2;
Function<Integer, String>  toString  = n -> "Result: " + n;

// Pipeline: parse -> double -> label
Function<String, String> pipeline = parseToInt.andThen(doubleIt).andThen(toString);

System.out.println(pipeline.apply("21")); // Output: Result: 42

// compose() applies the argument BEFORE the receiver
Function<Integer, Integer> addOne   = n -> n + 1;
Function<Integer, Integer> triple   = n -> n * 3;

// triple.compose(addOne) means: first addOne, then triple
Function<Integer, Integer> addThenTriple = triple.compose(addOne);
System.out.println(addThenTriple.apply(4)); // Output: 15  (4+1=5, 5*3=15)

// triple.andThen(addOne) means: first triple, then addOne
Function<Integer, Integer> tripleThenAdd = triple.andThen(addOne);
System.out.println(tripleThenAdd.apply(4)); // Output: 13  (4*3=12, 12+1=13)

```

## 8. Lambdas with Collections

This is where lambdas pay off immediately. The standard collection methods accept functional interfaces directly.

**`List.sort()` with a Comparator lambda**

```java
import java.util.ArrayList;
import java.util.List;

List<String> names = new ArrayList<>(List.of("Charlie", "Alice", "Bob", "Diana"));

// Sort alphabetically
names.sort((a, b) -> a.compareTo(b));
System.out.println(names); // Output: [Alice, Bob, Charlie, Diana]

// Sort by length, then alphabetically for ties
names.sort((a, b) -> {
    int byLength = Integer.compare(a.length(), b.length());
    return byLength != 0 ? byLength : a.compareTo(b);
});
System.out.println(names); // Output: [Bob, Alice, Diana, Charlie]

```

**`List.removeIf()` with a Predicate lambda**

```java
List<Integer> numbers = new ArrayList<>(List.of(1, 2, 3, 4, 5, 6, 7, 8));

numbers.removeIf(n -> n % 2 == 0);  // Remove all even numbers
System.out.println(numbers); // Output: [1, 3, 5, 7]

```

**`List.forEach()` with a Consumer lambda**

```java
List<String> items = List.of("apple", "banana", "cherry");

items.forEach(item -> System.out.println(item.toUpperCase()));
// Output:
// APPLE
// BANANA
// CHERRY

```

**`Map.forEach()` with a BiConsumer lambda**

```java
import java.util.Map;

Map<String, Integer> scores = Map.of("Alice", 95, "Bob", 82, "Carol", 78);

scores.forEach((name, score) -> System.out.println(name + " scored " + score));
// Output (order may vary):
// Alice scored 95
// Bob scored 82
// Carol scored 78

```

**`Map.computeIfAbsent()` with a Function lambda**

```java
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Map;
import java.util.List;

Map<String, List<String>> groups = new HashMap<>();

// If the key is absent, the Function creates a new list for it
groups.computeIfAbsent("fruits", key -> new ArrayList<>()).add("apple");
groups.computeIfAbsent("fruits", key -> new ArrayList<>()).add("banana");
groups.computeIfAbsent("veggies", key -> new ArrayList<>()).add("carrot");

System.out.println(groups);
// Output: {fruits=[apple, banana], veggies=[carrot]}

```

## 9. Complete Example

An employee filtering and reporting system built entirely with lambdas and functional interfaces — no Streams.

```java
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Consumer;
import java.util.ArrayList;
import java.util.List;

public class Employee {
    private String name;
    private String department;
    private double salary;
    private int yearsExperience;

    public Employee(String name, String department, double salary, int yearsExperience) {
        this.name = name;
        this.department = department;
        this.salary = salary;
        this.yearsExperience = yearsExperience;
    }

    public String getName()         { return name; }
    public String getDepartment()   { return department; }
    public double getSalary()       { return salary; }
    public int getYearsExperience() { return yearsExperience; }

    @Override
    public String toString() {
        return name + " [" + department + ", $" + salary + ", " + yearsExperience + " yrs]";
    }
}

```

```java
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.ArrayList;
import java.util.List;

public class EmployeeReport {

    public static List<Employee> filterEmployees(List<Employee> list, Predicate<Employee> filter) {
        List<Employee> result = new ArrayList<>();
        for (Employee e : list) {
            if (filter.test(e)) {
                result.add(e);
            }
        }
        return result;
    }

    public static List<String> transformEmployees(List<Employee> list, Function<Employee, String> mapper) {
        List<String> result = new ArrayList<>();
        for (Employee e : list) {
            result.add(mapper.apply(e));
        }
        return result;
    }

    public static void main(String[] args) {
        List<Employee> employees = new ArrayList<>(List.of(
            new Employee("Alice",   "Engineering", 95000, 7),
            new Employee("Bob",     "Marketing",   62000, 3),
            new Employee("Carol",   "Engineering", 80000, 5),
            new Employee("David",   "HR",          58000, 2),
            new Employee("Eve",     "Engineering", 72000, 4),
            new Employee("Frank",   "Marketing",   74000, 6)
        ));

        // Find all employees in Engineering
        Predicate<Employee> inEngineering = e -> e.getDepartment().equals("Engineering");
        List<Employee> engineers = filterEmployees(employees, inEngineering);
        System.out.println("Engineering team:");
        engineers.forEach(e -> System.out.println("  " + e));
        // Output:
        // Engineering team:
        //   Alice [Engineering, $95000.0, 7 yrs]
        //   Carol [Engineering, $80000.0, 5 yrs]
        //   Eve [Engineering, $72000.0, 4 yrs]

        // Find employees earning over 70000
        Predicate<Employee> highEarner = e -> e.getSalary() > 70000;
        List<Employee> highEarners = filterEmployees(employees, highEarner);
        System.out.println("\nHigh earners (salary > 70000):");
        highEarners.forEach(e -> System.out.println("  " + e));
        // Output:
        // High earners (salary > 70000):
        //   Alice [Engineering, $95000.0, 7 yrs]
        //   Carol [Engineering, $80000.0, 5 yrs]
        //   Eve [Engineering, $72000.0, 4 yrs]
        //   Frank [Marketing, $74000.0, 6 yrs]

        // Combine predicates: Engineering AND high earner
        List<Employee> seniorEngineers = filterEmployees(employees, inEngineering.and(highEarner));
        System.out.println("\nSenior Engineers (Engineering + salary > 70000):");
        seniorEngineers.forEach(e -> System.out.println("  " + e));
        // Output:
        // Senior Engineers (Engineering + salary > 70000):
        //   Alice [Engineering, $95000.0, 7 yrs]
        //   Carol [Engineering, $80000.0, 5 yrs]
        //   Eve [Engineering, $72000.0, 4 yrs]

        // Get a list of all names
        Function<Employee, String> toName = e -> e.getName();
        List<String> names = transformEmployees(employees, toName);
        System.out.println("\nAll employee names: " + names);
        // Output:
        // All employee names: [Alice, Bob, Carol, David, Eve, Frank]

        // Get formatted summary strings
        Function<Employee, String> toSummary = e ->
            e.getName() + " earns $" + e.getSalary() + " with " + e.getYearsExperience() + " years of experience";
        List<String> summaries = transformEmployees(employees, toSummary);
        System.out.println("\nEmployee summaries:");
        summaries.forEach(s -> System.out.println("  " + s));
        // Output:
        // Employee summaries:
        //   Alice earns $95000.0 with 7 years of experience
        //   Bob earns $62000.0 with 3 years of experience
        //   Carol earns $80000.0 with 5 years of experience
        //   David earns $58000.0 with 2 years of experience
        //   Eve earns $72000.0 with 4 years of experience
        //   Frank earns $74000.0 with 6 years of experience

        // Print all employees using forEach with a Consumer lambda
        System.out.println("\nFull employee roster:");
        employees.forEach(e -> System.out.println("  " + e));
        // Output:
        // Full employee roster:
        //   Alice [Engineering, $95000.0, 7 yrs]
        //   Bob [Marketing, $62000.0, 3 yrs]
        //   Carol [Engineering, $80000.0, 5 yrs]
        //   David [HR, $58000.0, 2 yrs]
        //   Eve [Engineering, $72000.0, 4 yrs]
        //   Frank [Marketing, $74000.0, 6 yrs]
    }
}

```

## 10. Key Takeaways

- A lambda is an instance of a functional interface — it is not a new concept, it is a shorter syntax for an anonymous class with one method
- A functional interface has exactly one abstract method; `@FunctionalInterface` makes the compiler enforce this
- Lambda syntax scales from `() -> expression` up to `(Type a, Type b) -> { multiple; statements; return value; }`
- The eight interfaces in `java.util.function` — `Predicate`, `Function`, `Consumer`, `Supplier`, `BiFunction`, `BiPredicate`, `UnaryOperator`, `BinaryOperator` — cover the vast majority of use cases
- Method references (`Class::method`, `object::method`, `Class::new`) are shorthand for lambdas whose entire body is a single method call
- Captured local variables must be effectively final; instance fields and static fields have no such restriction
- `Predicate.and()`, `or()`, `negate()` and `Function.andThen()`, `compose()` let you build readable pipelines without nesting
- `List.sort()`, `List.removeIf()`, `List.forEach()`, `Map.forEach()`, and `Map.computeIfAbsent()` all accept functional interfaces directly — lambdas slot in immediately

---

Lambdas are the foundation that makes Streams, the Optional API, and Spring's functional-style configurations readable — once you are fluent with lambdas and the `java.util.function` interfaces, those higher-level APIs become a natural extension of the same ideas.

---

## Java Stream API (filter, map, reduce, collectors)

# Streams

A Stream is a pipeline of operations on a sequence of elements that allows you to express complex data processing queries in a declarative, readable style. Unlike a collection, a stream does not store data — it processes data from a source on demand. You already know lambdas and collections; streams are where those two concepts combine into their most powerful form.

```

Think of it like this:
  A collection is a bucket of water — it holds the water.
  A stream is a pipe — water flows through it and you apply
  filters, transformers, and collectors along the way.
  The pipe itself holds nothing. It only defines what happens
  to each drop of water as it passes through.

```

## 1. What Is a Stream?

A `Stream<T>` represents a sequence of elements that supports sequential and parallel aggregate operations. Three properties define how streams behave, and understanding them is essential before writing a single line of stream code.

**Laziness** — intermediate operations (filter, map, sorted, etc.) do not execute when you call them. They build up a description of the pipeline. Execution only begins when a terminal operation is called. This means if you chain five operations but the terminal operation only needs the first two elements, Java may never evaluate the remaining three operations on most elements.

**Single-use** — once a terminal operation has been called on a stream, the stream is consumed and cannot be reused. Attempting to reuse it throws `IllegalStateException`.

**Non-mutating** — a stream never modifies its source collection. You always get a new result; the original list remains unchanged.

```java
List<String> names = List.of("Alice", "Bob", "Carol");

// This creates a stream — it does NOT modify names
Stream<String> stream = names.stream();

// The stream is consumed here. names is still ["Alice", "Bob", "Carol"].
long count = stream.filter(n -> n.startsWith("A")).count();

System.out.println(count); // Output: 1
System.out.println(names); // Output: [Alice, Bob, Carol]

```

Collection vs. Stream at a glance:

| Question | Collection | Stream |
|---|---|---|
| Does it store elements? | Yes | No |
| Can you iterate it more than once? | Yes | No |
| Does it evaluate lazily? | No | Yes |
| Does it modify its source? | Possible | Never |

## 2. Creating Streams

There are several ways to obtain a stream depending on where your data lives.

**From a collection** — every `Collection` has a `.stream()` method.

```java
List<String> cities = List.of("London", "Tokyo", "Cairo");
Stream<String> cityStream = cities.stream();

```

**From an array** — use `Arrays.stream()`.

```java
int[] numbers = {1, 2, 3, 4, 5};
IntStream numberStream = Arrays.stream(numbers);

String[] words = {"hello", "world"};
Stream<String> wordStream = Arrays.stream(words);

```

**From explicit values** — use `Stream.of()`.

```java
Stream<String> stream = Stream.of("red", "green", "blue");

```

**Empty stream** — useful as a safe default return value.

```java
Stream<String> empty = Stream.empty();

```

**Infinite streams** — streams that generate elements on demand. Always pair them with `limit()` or they will run forever.

```java
// Produces 0, 1, 2, 3, 4 ...
Stream<Integer> naturals = Stream.iterate(0, n -> n + 1);

// Produces random doubles endlessly
Stream<Double> randoms = Stream.generate(Math::random);

// Safe — take only the first 10
List<Integer> firstTen = Stream.iterate(0, n -> n + 1)
        .limit(10)
        .collect(Collectors.toList());
// Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

```

**Primitive streams** — `IntStream`, `LongStream`, and `DoubleStream` avoid the boxing overhead of `Stream<Integer>`. Covered in depth in section 7.

```java
IntStream oneToTen = IntStream.range(1, 11);       // 1 to 10 (exclusive end)
IntStream oneToTenInclusive = IntStream.rangeClosed(1, 10); // 1 to 10 (inclusive end)

```

## 3. Intermediate Operations

Intermediate operations return a new `Stream` and are lazy — they do not execute until a terminal operation is called. Each operation describes one step in the pipeline.

### filter(Predicate)

Keeps only the elements that match the condition.

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

List<Integer> evens = numbers.stream()
        .filter(n -> n % 2 == 0)
        .collect(Collectors.toList());

System.out.println(evens);
// Output: [2, 4, 6, 8, 10]

```

### map(Function)

Transforms each element into something else. The output stream can be a different type.

```java
List<String> names = List.of("alice", "bob", "carol");

List<String> upper = names.stream()
        .map(String::toUpperCase)
        .collect(Collectors.toList());

System.out.println(upper);
// Output: [ALICE, BOB, CAROL]

```

### flatMap(Function)

Used when each element maps to a collection or stream of elements. `flatMap` flattens all those inner streams into a single stream.

```java
List<String> sentences = List.of("the quick brown fox", "jumps over the lazy dog");

List<String> words = sentences.stream()
        .flatMap(sentence -> Arrays.stream(sentence.split(" ")))
        .collect(Collectors.toList());

System.out.println(words);
// Output: [the, quick, brown, fox, jumps, over, the, lazy, dog]

```

Without `flatMap`, you would get a `Stream<String[]>` — a stream of arrays. `flatMap` collapses the nesting.

### distinct()

Removes duplicate elements using `equals()`.

```java
List<Integer> withDupes = List.of(3, 1, 4, 1, 5, 9, 2, 6, 5, 3);

List<Integer> unique = withDupes.stream()
        .distinct()
        .collect(Collectors.toList());

System.out.println(unique);
// Output: [3, 1, 4, 5, 9, 2, 6]

```

### sorted() and sorted(Comparator)

`sorted()` uses the element's natural ordering. `sorted(Comparator)` accepts a custom ordering.

```java
List<String> names = List.of("Charlie", "Alice", "Bob");

// Natural order (alphabetical)
List<String> alphabetical = names.stream()
        .sorted()
        .collect(Collectors.toList());
System.out.println(alphabetical);
// Output: [Alice, Bob, Charlie]

// Custom order — longest name first
List<String> byLength = names.stream()
        .sorted(Comparator.comparingInt(String::length).reversed())
        .collect(Collectors.toList());
System.out.println(byLength);
// Output: [Charlie, Alice, Bob]

```

### peek(Consumer)

Performs an action on each element without modifying the stream. Its primary purpose is debugging — it lets you observe elements at a specific point in the pipeline.

```java
List<Integer> result = List.of(1, 2, 3, 4, 5).stream()
        .peek(n -> System.out.println("Before filter: " + n))
        .filter(n -> n % 2 == 0)
        .peek(n -> System.out.println("After filter: " + n))
        .collect(Collectors.toList());

// Output:
// Before filter: 1
// Before filter: 2
// After filter: 2
// Before filter: 3
// Before filter: 4
// After filter: 4
// Before filter: 5

```

### limit(n) and skip(n)

`limit(n)` keeps only the first `n` elements. `skip(n)` discards the first `n` elements and keeps the rest.

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

List<Integer> page = numbers.stream()
        .skip(3)    // skip the first 3
        .limit(4)   // keep only the next 4
        .collect(Collectors.toList());

System.out.println(page);
// Output: [4, 5, 6, 7]

```

### Multi-Step Pipeline Example

Intermediate operations can be chained freely. Each step receives the output of the previous step.

```java
List<String> words = List.of(
        "stream", "lambda", "map", "filter", "stream",
        "collect", "map", "optional", "reduce"
);

List<String> result = words.stream()
        .filter(w -> w.length() > 3)          // keep words longer than 3 chars
        .map(String::toUpperCase)              // uppercase them
        .distinct()                            // remove duplicates
        .sorted()                              // sort alphabetically
        .limit(4)                              // take the first 4
        .collect(Collectors.toList());

System.out.println(result);
// Output: [COLLECT, FILTER, LAMBDA, OPTIONAL]

```

## 4. Terminal Operations

Terminal operations trigger the entire pipeline and produce a result. After a terminal operation completes, the stream is consumed.

### forEach(Consumer)

Iterates over each element and performs an action. Returns `void`.

```java
List<String> names = List.of("Alice", "Bob", "Carol");
names.stream().forEach(System.out::println);
// Output:
// Alice
// Bob
// Carol

```

### collect(Collector)

Gathers the stream elements into a container. This is the most commonly used terminal operation. Collectors are covered in depth in section 5.

```java
List<Integer> evens = List.of(1, 2, 3, 4, 5, 6).stream()
        .filter(n -> n % 2 == 0)
        .collect(Collectors.toList());

System.out.println(evens);
// Output: [2, 4, 6]

```

### count()

Returns the number of elements in the stream as a `long`.

```java
long count = List.of("a", "bb", "ccc", "dddd").stream()
        .filter(s -> s.length() >= 2)
        .count();

System.out.println(count);
// Output: 3

```

### reduce(identity, BinaryOperator)

Folds all elements into a single value by repeatedly applying a combining function.

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5);

// Sum: starts at 0, adds each element
int sum = numbers.stream()
        .reduce(0, Integer::sum);
System.out.println(sum);
// Output: 15

// Product: starts at 1, multiplies each element
int product = numbers.stream()
        .reduce(1, (a, b) -> a * b);
System.out.println(product);
// Output: 120

// Concatenation
String joined = List.of("Java", "is", "expressive").stream()
        .reduce("", (a, b) -> a.isEmpty() ? b : a + " " + b);
System.out.println(joined);
// Output: Java is expressive

```

### findFirst() and findAny()

Both return an `Optional<T>`. `findFirst()` returns the first element in encounter order. `findAny()` may return any element and is more efficient in parallel streams.

```java
Optional<String> first = List.of("apple", "banana", "cherry").stream()
        .filter(s -> s.startsWith("b"))
        .findFirst();

first.ifPresent(System.out::println);
// Output: banana

```

### anyMatch, allMatch, noneMatch

Short-circuit predicates that return `boolean`. They stop processing as soon as the answer is known.

```java
List<Integer> numbers = List.of(2, 4, 6, 7, 8);

boolean anyOdd   = numbers.stream().anyMatch(n -> n % 2 != 0);
boolean allEven  = numbers.stream().allMatch(n -> n % 2 == 0);
boolean noneNeg  = numbers.stream().noneMatch(n -> n < 0);

System.out.println(anyOdd);  // Output: true
System.out.println(allEven); // Output: false
System.out.println(noneNeg); // Output: true

```

### min(Comparator) and max(Comparator)

Return an `Optional<T>` containing the smallest or largest element according to the given comparator.

```java
List<String> words = List.of("apple", "fig", "banana", "kiwi");

Optional<String> shortest = words.stream()
        .min(Comparator.comparingInt(String::length));

Optional<String> longest = words.stream()
        .max(Comparator.comparingInt(String::length));

shortest.ifPresent(s -> System.out.println("Shortest: " + s));
longest.ifPresent(s -> System.out.println("Longest: " + s));
// Output:
// Shortest: fig
// Longest: banana

```

### toList() (Java 16+)

A shorthand for `collect(Collectors.toList())`. Returns an unmodifiable list.

```java
List<String> result = Stream.of("x", "y", "z")
        .map(String::toUpperCase)
        .toList();

System.out.println(result);
// Output: [X, Y, Z]

```

## 5. Collectors

The `Collectors` class provides factory methods for the most common collection strategies. You pass a `Collector` to the `collect()` terminal operation.

### Basic Collectors

```java
List<String> names = List.of("Alice", "Bob", "Alice", "Carol", "Bob");

// Collect to a mutable list
List<String> asList = names.stream().collect(Collectors.toList());

// Collect to a set (removes duplicates)
Set<String> asSet = names.stream().collect(Collectors.toSet());
System.out.println(asSet);
// Output: [Alice, Bob, Carol]  (order not guaranteed)

// Collect to an unmodifiable list
List<String> immutable = names.stream().collect(Collectors.toUnmodifiableList());

```

### Collectors.toMap

```java
List<String> words = List.of("apple", "fig", "banana");

Map<String, Integer> wordLengths = words.stream()
        .collect(Collectors.toMap(
                word -> word,          // key: the word itself
                String::length         // value: its length
        ));

System.out.println(wordLengths);
// Output: {apple=5, fig=3, banana=6}

```

### Collectors.joining

Concatenates stream elements into a single `String`.

```java
List<String> names = List.of("Alice", "Bob", "Carol");

String csv = names.stream()
        .collect(Collectors.joining(", "));
System.out.println(csv);
// Output: Alice, Bob, Carol

String formatted = names.stream()
        .collect(Collectors.joining(", ", "[", "]"));
System.out.println(formatted);
// Output: [Alice, Bob, Carol]

```

### Collectors.counting, summingInt, averagingInt

```java
List<String> words = List.of("a", "bb", "ccc", "dd", "e");

long count = words.stream().collect(Collectors.counting());
int totalLength = words.stream().collect(Collectors.summingInt(String::length));
double avgLength = words.stream().collect(Collectors.averagingInt(String::length));

System.out.println(count);       // Output: 5
System.out.println(totalLength); // Output: 9
System.out.println(avgLength);   // Output: 1.8

```

### Collectors.groupingBy

Groups elements by a classifier function and returns a `Map<K, List<V>>`. This is one of the most powerful collectors.

```java
record Employee(String name, String department, double salary) {}

List<Employee> employees = List.of(
        new Employee("Alice",   "Engineering", 95000),
        new Employee("Bob",     "Engineering", 88000),
        new Employee("Carol",   "Marketing",   72000),
        new Employee("Dave",    "Marketing",   68000),
        new Employee("Eve",     "HR",          64000)
);

// Group employees by department
Map<String, List<Employee>> byDept = employees.stream()
        .collect(Collectors.groupingBy(Employee::department));

byDept.forEach((dept, emps) -> {
    System.out.println(dept + ": " + emps.stream()
            .map(Employee::name)
            .collect(Collectors.joining(", ")));
});
// Output:
// Engineering: Alice, Bob
// Marketing: Carol, Dave
// HR: Eve

```

**groupingBy with a downstream collector** — you can apply a second collector to each group.

```java
// Count employees per department
Map<String, Long> countByDept = employees.stream()
        .collect(Collectors.groupingBy(
                Employee::department,
                Collectors.counting()
        ));

System.out.println(countByDept);
// Output: {Engineering=2, Marketing=2, HR=1}

// Average salary per department
Map<String, Double> avgSalaryByDept = employees.stream()
        .collect(Collectors.groupingBy(
                Employee::department,
                Collectors.averagingDouble(Employee::salary)
        ));

System.out.println(avgSalaryByDept);
// Output: {Engineering=91500.0, Marketing=70000.0, HR=64000.0}

```

### Collectors.partitioningBy

Splits the stream into exactly two groups — those that match the predicate (`true`) and those that do not (`false`). Returns a `Map<Boolean, List<T>>`.

```java
Map<Boolean, List<Employee>> partition = employees.stream()
        .collect(Collectors.partitioningBy(e -> e.salary() >= 80000));

System.out.println("High earners: " + partition.get(true).stream()
        .map(Employee::name).collect(Collectors.joining(", ")));
System.out.println("Others: " + partition.get(false).stream()
        .map(Employee::name).collect(Collectors.joining(", ")));
// Output:
// High earners: Alice, Bob
// Others: Carol, Dave, Eve

```

## 6. Stream Pipeline: Lazy Evaluation

Intermediate operations do not execute immediately. Java builds a pipeline description and only pulls elements through when a terminal operation demands them. This is called lazy evaluation and has real performance implications.

The following example uses `peek()` to make the execution order visible.

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

System.out.println("Building pipeline...");

List<Integer> result = numbers.stream()
        .peek(n  -> System.out.println("  source:  " + n))
        .filter(n -> n % 2 == 0)
        .peek(n  -> System.out.println("  filtered:" + n))
        .map(n   -> n * n)
        .peek(n  -> System.out.println("  mapped:  " + n))
        .collect(Collectors.toList());

System.out.println("Result: " + result);
// Output:
// Building pipeline...
//   source:  1
//   source:  2
//   filtered:2
//   mapped:  4
//   source:  3
//   source:  4
//   filtered:4
//   mapped:  16
//   source:  5
//   source:  6
//   filtered:6
//   mapped:  36
//   source:  7
//   source:  8
//   filtered:8
//   mapped:  64
//   source:  9
//   source:  10
//   filtered:10
//   mapped:  100
// Result: [4, 16, 36, 64, 100]

```

Notice that each element travels through the entire pipeline before the next element enters. The stream processes vertically (per element), not horizontally (per operation).

**limit() cuts off processing entirely** — elements beyond the limit are never touched.

```java
List<Integer> numbers = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

List<Integer> firstThreeEvens = numbers.stream()
        .peek(n -> System.out.println("Checking: " + n))
        .filter(n -> n % 2 == 0)
        .limit(3)
        .collect(Collectors.toList());

System.out.println("Result: " + firstThreeEvens);
// Output:
// Checking: 1
// Checking: 2
// Checking: 3
// Checking: 4
// Checking: 5
// Checking: 6
// Result: [2, 4, 6]
// Elements 7, 8, 9, 10 were never examined at all.

```

## 7. Primitive Streams

`Stream<Integer>` boxes each `int` into an `Integer` object. For large numeric workloads this creates unnecessary heap allocations. `IntStream`, `LongStream`, and `DoubleStream` operate directly on primitive values with no boxing.

They also provide numeric convenience methods (`sum()`, `average()`, `min()`, `max()`) that are not available on `Stream<T>`.

### Creating Primitive Streams

```java
IntStream range    = IntStream.range(1, 6);         // 1, 2, 3, 4, 5  (exclusive end)
IntStream closed   = IntStream.rangeClosed(1, 5);   // 1, 2, 3, 4, 5  (inclusive end)
LongStream longs   = LongStream.range(0L, 1_000_000L);
DoubleStream dubs  = DoubleStream.of(1.1, 2.2, 3.3);

```

### Built-In Numeric Operations

```java
IntStream scores = IntStream.of(88, 92, 75, 96, 84);

System.out.println(scores.sum());               // Output: 435
// (Must recreate — stream is consumed)

System.out.println(IntStream.of(88, 92, 75, 96, 84).average()); // Output: OptionalDouble[87.0]
System.out.println(IntStream.of(88, 92, 75, 96, 84).min());     // Output: OptionalInt[75]
System.out.println(IntStream.of(88, 92, 75, 96, 84).max());     // Output: OptionalInt[96]
System.out.println(IntStream.of(88, 92, 75, 96, 84).count());   // Output: 5

```

### Converting Between Stream Types

`mapToInt()` and `mapToDouble()` convert a `Stream<T>` to a primitive stream. `boxed()` converts back to an object stream.

```java
List<String> words = List.of("hello", "world", "streams");

// Convert Stream<String> -> IntStream to use sum()
int totalChars = words.stream()
        .mapToInt(String::length)
        .sum();
System.out.println(totalChars);
// Output: 18

// Convert IntStream -> Stream<Integer> when you need object stream methods
List<Integer> boxed = IntStream.rangeClosed(1, 5)
        .boxed()
        .collect(Collectors.toList());
System.out.println(boxed);
// Output: [1, 2, 3, 4, 5]

```

### Stream vs IntStream for Summing — Side by Side

```java
List<Integer> numbers = List.of(10, 20, 30, 40, 50);

// Using Stream<Integer> with reduce — verbose, involves boxing
int sumWithReduce = numbers.stream()
        .reduce(0, Integer::sum);
System.out.println(sumWithReduce);
// Output: 150

// Using IntStream — cleaner, no boxing
int sumWithIntStream = numbers.stream()
        .mapToInt(Integer::intValue)
        .sum();
System.out.println(sumWithIntStream);
// Output: 150

```

For small lists the difference is negligible. For millions of elements, `IntStream` is meaningfully faster.

## 8. Stream vs Collection

| Feature | Collection | Stream |
|---|---|---|
| Stores data | Yes | No |
| Reusable | Yes | No (single-use) |
| Lazy | No | Yes |
| Modifies source | Possible | Never |
| External iteration | Yes (for-each) | No (internal) |
| Size known upfront | Yes | Not always (infinite streams) |
| Numeric shortcuts | No | Yes (IntStream, etc.) |

A collection is the right choice when you need to store, access, and modify data repeatedly. A stream is the right choice when you need to describe a transformation or query over that data.

## 9. Complete Example

The following example builds an employee reporting system that demonstrates how multiple stream operations work together in a realistic codebase.

```java
import java.util.*;
import java.util.stream.*;

public record Employee(
        String name,
        String department,
        double salary,
        int yearsExperience
) {}

```

```java
public class EmployeeReport {
    public static void main(String[] args) {

        List<Employee> employees = List.of(
                new Employee("Alice",   "Engineering", 105000, 8),
                new Employee("Bob",     "Engineering",  92000, 5),
                new Employee("Carol",   "Engineering",  88000, 12),
                new Employee("Dave",    "Marketing",    74000, 3),
                new Employee("Eve",     "Marketing",    69000, 7),
                new Employee("Frank",   "HR",           62000, 11),
                new Employee("Grace",   "HR",           58000, 2),
                new Employee("Hank",    "Engineering",  97000, 9)
        );

        // All Engineering employees sorted by salary descending
        List<Employee> engineers = employees.stream()
                .filter(e -> e.department().equals("Engineering"))
                .sorted(Comparator.comparingDouble(Employee::salary).reversed())
                .collect(Collectors.toList());

        System.out.println("Engineering by salary (desc):");
        engineers.forEach(e ->
                System.out.printf("  %-8s $%.0f%n", e.name(), e.salary()));
        // Output:
        //   Alice    $105000
        //   Hank     $97000
        //   Bob      $92000
        //   Carol    $88000

        // Average salary across the whole company
        double avgSalary = employees.stream()
                .mapToDouble(Employee::salary)
                .average()
                .orElse(0.0);

        System.out.printf("%nCompany average salary: $%.2f%n", avgSalary);
        // Output:
        // Company average salary: $80625.00

        // Map of department -> list of employee names
        Map<String, List<String>> namesByDept = employees.stream()
                .collect(Collectors.groupingBy(
                        Employee::department,
                        Collectors.mapping(Employee::name, Collectors.toList())
                ));

        System.out.println("\nNames by department:");
        namesByDept.forEach((dept, names) ->
                System.out.println("  " + dept + ": " + names));
        // Output:
        //   Engineering: [Alice, Bob, Carol, Hank]
        //   Marketing: [Dave, Eve]
        //   HR: [Frank, Grace]

        // Highest paid employee
        Optional<Employee> highestPaid = employees.stream()
                .max(Comparator.comparingDouble(Employee::salary));

        highestPaid.ifPresent(e ->
                System.out.println("\nHighest paid: " + e.name() + " ($" + e.salary() + ")"));
        // Output:
        // Highest paid: Alice ($105000.0)

        // Whether any employee has more than 10 years experience
        boolean hasVeteran = employees.stream()
                .anyMatch(e -> e.yearsExperience() > 10);

        System.out.println("\nAny employee with 10+ years: " + hasVeteran);
        // Output:
        // Any employee with 10+ years: true

        // Total salary bill
        double totalSalary = employees.stream()
                .mapToDouble(Employee::salary)
                .sum();

        System.out.printf("%nTotal salary bill: $%.0f%n", totalSalary);
        // Output:
        // Total salary bill: $645000

        // Formatted report string — all names joined
        String allNames = employees.stream()
                .map(Employee::name)
                .collect(Collectors.joining(", "));

        System.out.println("\nAll employees: " + allNames);
        // Output:
        // All employees: Alice, Bob, Carol, Dave, Eve, Frank, Grace, Hank
    }
}

```

## 10. Key Takeaways

- A Stream is a pipeline that processes data from a source; it does not store data and does not modify its source
- Intermediate operations (`filter`, `map`, `flatMap`, `sorted`, `distinct`, `peek`, `limit`, `skip`) are lazy and return a new `Stream`
- Terminal operations (`collect`, `forEach`, `count`, `reduce`, `findFirst`, `anyMatch`, `min`, `max`, `toList`) trigger the pipeline and consume the stream
- A stream can only be used once; calling a terminal operation twice throws `IllegalStateException`
- `Collectors.groupingBy` and `Collectors.partitioningBy` are among the most powerful tools in the API — they transform flat lists into structured maps with a single expression
- `IntStream`, `LongStream`, and `DoubleStream` eliminate boxing overhead and provide built-in numeric operations like `sum()` and `average()`
- Lazy evaluation means elements that are never needed (due to `limit()` or short-circuit operations) are never processed — this is a genuine performance benefit, not just a theoretical one
- Infinite streams (`Stream.iterate`, `Stream.generate`) are valid and safe as long as they are paired with a limiting terminal condition

---

Streams are the most expressive way to process collections in modern Java, and fluency with them is essential for reading and writing Spring Boot service layer code, where stream-based data transformations appear in nearly every repository or data access method.

---