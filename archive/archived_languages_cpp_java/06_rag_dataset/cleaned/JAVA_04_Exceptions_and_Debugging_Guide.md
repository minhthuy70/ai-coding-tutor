# Java Exception Handling, Stack Traces & Debugging Guide

## EXCEPTIONS - EXCEPTIONS

# Exception Handling in Java

When a program encounters an unexpected situation — dividing by zero, reading a file that doesn't exist, accessing an index outside an array's bounds — it needs a way to signal that something went wrong and decide what to do about it. Java's answer is the **exception handling** mechanism.

```

Think of it like this:
  Your program is driving down a highway.
  An exception is an obstacle that suddenly appears on the road.
  Without handling, the car crashes (program terminates).
  With handling, there is a detour — the program recovers and continues.

```

---

## 1. What Is an Exception?

An **exception** is an event that disrupts the normal flow of a program's execution. When an error occurs inside a method, the method creates an **exception object** and hands it off to the runtime — this is called **throwing** an exception.

The exception object contains:
- The type of exception (e.g., `NullPointerException`)
- The error message describing what went wrong
- The **stack trace** — the chain of method calls that led to the error

If no code in the call stack handles the exception, the JVM prints the stack trace and terminates the program.

```java
public class Main {
    public static void main(String[] args) {
        int result = 10 / 0;  // Throws ArithmeticException
        System.out.println(result); // Never reached
    }
}
// Output:
// Exception in thread "main" java.lang.ArithmeticException: / by zero
//     at Main.main(Main.java:3)

```

---

## 2. The Exception Class Hierarchy

All exception types in Java form a class hierarchy rooted at `Throwable`.

```

Throwable
├── Error
│   ├── OutOfMemoryError
│   ├── StackOverflowError
│   └── VirtualMachineError
└── Exception
    ├── RuntimeException  (unchecked)
    │   ├── NullPointerException
    │   ├── ArrayIndexOutOfBoundsException
    │   ├── ClassCastException
    │   ├── ArithmeticException
    │   ├── IllegalArgumentException
    │   ├── NumberFormatException
    │   └── IllegalStateException
    └── IOException  (checked)
        ├── FileNotFoundException
        └── EOFException
    └── SQLException  (checked)
    └── ParseException  (checked)

```

### `Throwable`
The root of all errors and exceptions. Has two direct subclasses:

### `Error`
Represents serious problems that a **program should not try to recover from**. These are caused by the JVM environment, not by application logic.
- `OutOfMemoryError` — the JVM ran out of heap memory
- `StackOverflowError` — infinite recursion exhausted the call stack

You generally do not catch `Error` objects. They indicate conditions the application cannot realistically handle.

### `Exception`
Represents conditions that a **program might reasonably want to catch and handle**. Split into two major categories:

---

## 3. Checked vs Unchecked Exceptions

This is one of the most important distinctions in Java exception handling.

| Feature             | Checked Exceptions                    | Unchecked Exceptions                    |
|---------------------|---------------------------------------|-----------------------------------------|
| Superclass          | `Exception` (but not `RuntimeException`) | `RuntimeException` and its subclasses  |
| Compiler enforces?  | Yes — must catch or declare           | No — optional to handle                 |
| Typically caused by | External resources (files, network, DB) | Programming bugs (null, bad index, etc.) |
| Examples            | `IOException`, `SQLException`        | `NullPointerException`, `ArithmeticException` |

### Checked Exceptions
The compiler **forces** you to handle them. If you call a method that can throw a checked exception, you must either:
1. Surround it in a `try-catch` block, **or**
2. Declare the exception in the method signature with `throws`

```java
import java.io.FileReader;
import java.io.IOException;

// Option 1: handle it here
public void readFile(String path) {
    try {
        FileReader reader = new FileReader(path); // throws FileNotFoundException (checked)
    } catch (IOException e) {
        System.out.println("File not found: " + e.getMessage());
    }
}

// Option 2: declare and let the caller deal with it
public void readFile(String path) throws IOException {
    FileReader reader = new FileReader(path);
}

```

### Unchecked Exceptions
The compiler does **not** require you to handle them. They usually signal a bug in the program — null references, invalid indexes, bad casts.

```java
String name = null;
System.out.println(name.length()); // NullPointerException — unchecked, no compiler warning

```

---

## 4. The `try-catch` Block

The fundamental mechanism for handling exceptions. Code that might throw an exception goes inside `try`. Recovery logic goes inside `catch`.

### Basic syntax

```java
try {
    // Code that might throw an exception
} catch (ExceptionType e) {
    // Code that runs if ExceptionType (or a subclass) is thrown
}

```

```java
public class Division {
    public static int divide(int a, int b) {
        try {
            return a / b;
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero.");
            return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println(divide(10, 2));  // Output: 5
        System.out.println(divide(10, 0));  // Output: Cannot divide by zero. -> 0
    }
}

```

### Catching multiple exception types

**Option A: Separate catch blocks** — use when you want different handling for each type.

```java
try {
    String[] names = {"Alice", "Bob"};
    String result = names[5].toUpperCase();  // Could throw two exceptions
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("Index out of range: " + e.getMessage());
} catch (NullPointerException e) {
    System.out.println("Null value encountered: " + e.getMessage());
}

```

**Order matters**: Catch subclasses before superclasses. The JVM uses the first matching `catch` block.

```java
// WRONG — the second catch is unreachable
catch (Exception e)               { ... }
catch (ArithmeticException e)     { ... }  // Compiler error

// CORRECT — specific before general
catch (ArithmeticException e)     { ... }
catch (Exception e)               { ... }

```

**Option B: Multi-catch** (Java 7+) — use when the handling is identical.

```java
try {
    // risky code
} catch (ArithmeticException | ArrayIndexOutOfBoundsException e) {
    System.out.println("Something went wrong: " + e.getMessage());
}

```

### Catching a parent class
Catching `Exception` catches everything that extends it (all checked and unchecked exceptions).

```java
try {
    // risky code
} catch (Exception e) {
    System.out.println("Caught: " + e.getMessage());
}

```

This is convenient but generally discouraged — it hides exactly what went wrong. Prefer specific types.

---

## 5. The `finally` Block

Code inside `finally` **always runs**, whether an exception was thrown or not. It is the right place for cleanup — closing files, releasing database connections, freeing resources.

```java
try {
    // risky code
} catch (Exception e) {
    // handle error
} finally {
    // always runs — cleanup goes here
}

```

```java
public static void readData() {
    FileReader reader = null;
    try {
        reader = new FileReader("data.txt");
        // read from file...
    } catch (IOException e) {
        System.out.println("Error reading file: " + e.getMessage());
    } finally {
        System.out.println("Closing resources...");
        if (reader != null) {
            try {
                reader.close(); // even this can throw
            } catch (IOException e) {
                System.out.println("Error closing reader.");
            }
        }
    }
}

```

`finally` runs even if:
- The `try` block exits normally
- A `catch` block runs
- A `return` statement is hit inside `try` or `catch`

`finally` does **not** run if `System.exit()` is called or the JVM crashes.

---

## 6. Try-with-Resources (Java 7+)

Because the `finally`-based cleanup pattern above is verbose and error-prone, Java 7 introduced **try-with-resources**. Any object that implements `AutoCloseable` (or `Closeable`) is automatically closed at the end of the `try` block, even if an exception is thrown.

```java
try (ResourceType resource = new ResourceType()) {
    // use resource
} catch (Exception e) {
    // handle exception
}
// resource.close() is called automatically here

```

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public static void readFile(String path) {
    try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        String line;
        while ((line = reader.readLine()) != null) {
            System.out.println(line);
        }
    } catch (IOException e) {
        System.out.println("Could not read file: " + e.getMessage());
    }
    // reader is closed automatically — no finally block needed
}

```

You can declare multiple resources separated by semicolons. They are closed in reverse declaration order.

```java
try (
    FileReader fr = new FileReader("input.txt");
    BufferedReader br = new BufferedReader(fr)
) {
    // use both
}
// br closed first, then fr

```

---

## 7. The `throws` Keyword

A method that can throw a **checked** exception but does not handle it must declare this in its signature using `throws`. This passes the responsibility to the caller.

```java
public void loadConfig(String file) throws IOException {
    FileReader reader = new FileReader(file);  // checked — declared, not caught
    // ...
}

```

The caller must then either catch it or also declare `throws`:

```java
// Caller option 1: catch it
public void start() {
    try {
        loadConfig("config.txt");
    } catch (IOException e) {
        System.out.println("Config missing: " + e.getMessage());
    }
}

// Caller option 2: propagate further
public void start() throws IOException {
    loadConfig("config.txt");
}

```

`throws` is only required for checked exceptions. You may also declare unchecked exceptions in `throws` as documentation, but the compiler will not enforce it.

---

## 8. The `throw` Keyword

`throw` lets you **manually create and throw an exception** from anywhere in your code. You use it to signal that your code has encountered an invalid state.

```java
throw new ExceptionType("error message");

```

```java
public class BankAccount {
    private double balance;

    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        }
        if (amount > balance) {
            throw new IllegalStateException("Insufficient funds.");
        }
        balance -= amount;
    }
}

```

```java
BankAccount account = new BankAccount(100.0);
account.withdraw(-50);   // throws IllegalArgumentException
account.withdraw(200);   // throws IllegalStateException

```

The distinction between `throw` and `throws`:

| Keyword  | Purpose                                          |
|----------|--------------------------------------------------|
| `throw`  | Actually throws an exception object (action)     |
| `throws` | Declares that a method might throw an exception (declaration) |

---

## 9. Creating Custom Exceptions

You can create your own exception types by extending `Exception` (checked) or `RuntimeException` (unchecked). This makes your code's error signals more expressive and specific to your domain.

### Custom unchecked exception

```java
public class InsufficientFundsException extends RuntimeException {
    private double amount;

    public InsufficientFundsException(double amount) {
        super("Insufficient funds. Attempted to withdraw: " + amount);
        this.amount = amount;
    }

    public double getAmount() {
        return amount;
    }
}

```

### Custom checked exception

```java
public class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}

```

### Using your custom exceptions

```java
public class BankAccount {
    private double balance;

    public BankAccount(double balance) {
        this.balance = balance;
    }

    public void withdraw(double amount) {
        if (amount > balance) {
            throw new InsufficientFundsException(amount);
        }
        balance -= amount;
    }
}

```

```java
public class Person {
    private int age;

    public void setAge(int age) throws InvalidAgeException {
        if (age < 0 || age > 150) {
            throw new InvalidAgeException("Age " + age + " is not a valid value.");
        }
        this.age = age;
    }
}

```

```java
BankAccount account = new BankAccount(50.0);

try {
    account.withdraw(200.0);
} catch (InsufficientFundsException e) {
    System.out.println(e.getMessage());
    System.out.println("You tried to withdraw: " + e.getAmount());
}
// Output:
// Insufficient funds. Attempted to withdraw: 200.0
// You tried to withdraw: 200.0

```

### Naming convention
Custom exceptions always end in `Exception` — `InsufficientFundsException`, `InvalidAgeException`, `ProductNotFoundException`.

---

## 10. Exception Propagation

When an exception is thrown, Java walks back up the **call stack** looking for a matching `catch` block. If none is found, it moves to the caller of that method, then to that method's caller, and so on. This is called **propagation**.

```java
public class Main {
    public static void main(String[] args) {
        methodA();  // Exception propagates from C → B → A → main → JVM (crash)
    }

    static void methodA() {
        methodB();
    }

    static void methodB() {
        methodC();
    }

    static void methodC() {
        int[] arr = new int[3];
        arr[10] = 5;  // ArrayIndexOutOfBoundsException thrown here
    }
}

```

Stack trace output:

```

Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 10 out of bounds for length 3
    at Main.methodC(Main.java:15)
    at Main.methodB(Main.java:11)
    at Main.methodA(Main.java:7)
    at Main.main(Main.java:3)

```

Read the stack trace from **bottom to top** to trace the call sequence, and from **top to bottom** to find where the exception actually occurred.

### Catching at the right level
Catch an exception at the level where you have enough context to handle it meaningfully.

```java
// Too low — this method knows nothing about the user; generic message only
static void methodC() {
    try {
        arr[10] = 5;
    } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Error.");  // Not useful here
    }
}

// Better — catch at the level where you can explain what went wrong in context
static void main(String[] args) {
    try {
        methodA();
    } catch (ArrayIndexOutOfBoundsException e) {
        System.out.println("Data processing failed: " + e.getMessage());
    }
}

```

---

## 11. Exception Chaining

When you catch one exception and throw another, you can attach the original as the **cause**. This preserves the full picture of what happened.

```java
public void loadUserData(int userId) throws DataLoadException {
    try {
        // simulate a database read
        int[] data = new int[10];
        data[userId] = 1;  // throws ArrayIndexOutOfBoundsException
    } catch (ArrayIndexOutOfBoundsException e) {
        // wrap the low-level exception in a higher-level one
        throw new DataLoadException("Failed to load data for user: " + userId, e);
    }
}

```

```java
public class DataLoadException extends Exception {
    public DataLoadException(String message, Throwable cause) {
        super(message, cause);  // Throwable has a constructor that takes a cause
    }
}

```

```java
try {
    loadUserData(99);
} catch (DataLoadException e) {
    System.out.println(e.getMessage());
    System.out.println("Caused by: " + e.getCause().getMessage());
}
// Output:
// Failed to load data for user: 99
// Caused by: Index 99 out of bounds for length 10

```

---

## 12. The Most Common Built-in Exceptions

| Exception                           | When it occurs                                             |
|-------------------------------------|------------------------------------------------------------|
| `NullPointerException`              | Calling a method on a `null` reference                     |
| `ArrayIndexOutOfBoundsException`    | Accessing an array index that does not exist               |
| `ClassCastException`                | Casting an object to an incompatible type                  |
| `ArithmeticException`               | Illegal arithmetic (e.g. integer division by zero)         |
| `NumberFormatException`             | Parsing a string that is not a valid number                |
| `IllegalArgumentException`          | A method receives an argument it cannot accept             |
| `IllegalStateException`             | Calling a method when the object is not in a valid state   |
| `StackOverflowError`                | Infinite recursion exhausted the call stack                |
| `OutOfMemoryError`                  | JVM ran out of heap memory                                 |
| `IOException`                       | General I/O failure (file, network, stream)                |
| `FileNotFoundException`             | The specified file does not exist                          |

---

## 13. Complete Example

```java
// Custom exception
public class ProductNotFoundException extends RuntimeException {
    private String productId;

    public ProductNotFoundException(String productId) {
        super("Product not found: " + productId);
        this.productId = productId;
    }

    public String getProductId() {
        return productId;
    }
}

```

```java
// Product class
public class Product {
    private String id;
    private String name;
    private double price;

    public Product(String id, String name, double price) {
        if (price < 0) {
            throw new IllegalArgumentException("Price cannot be negative: " + price);
        }
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public String getId()    { return id; }
    public String getName()  { return name; }
    public double getPrice() { return price; }

    @Override
    public String toString() {
        return "Product{id='" + id + "', name='" + name + "', price=" + price + "}";
    }
}

```

```java
// Inventory class
public class Inventory {
    private Product[] products;
    private int count;

    public Inventory(int capacity) {
        products = new Product[capacity];
        count = 0;
    }

    public void addProduct(Product product) {
        if (count >= products.length) {
            throw new IllegalStateException("Inventory is full.");
        }
        products[count++] = product;
    }

    public Product findById(String id) {
        for (int i = 0; i < count; i++) {
            if (products[i].getId().equals(id)) {
                return products[i];
            }
        }
        throw new ProductNotFoundException(id);
    }

    public void updatePrice(String id, double newPrice) {
        if (newPrice < 0) {
            throw new IllegalArgumentException("New price cannot be negative.");
        }
        Product p = findById(id);  // throws ProductNotFoundException if not found
        // In a real implementation, price would be mutable
        System.out.println("Updated price of " + p.getName() + " to " + newPrice);
    }
}

```

```java
// Main — shows all mechanisms together
public class Main {
    public static void main(String[] args) {

        Inventory inventory = new Inventory(5);

        // --- Normal operation ---
        try {
            inventory.addProduct(new Product("P001", "Keyboard", 49.99));
            inventory.addProduct(new Product("P002", "Mouse", 29.99));
            System.out.println("Products added successfully.");
        } catch (IllegalStateException e) {
            System.out.println("Could not add product: " + e.getMessage());
        }

        // --- Illegal argument ---
        try {
            inventory.addProduct(new Product("P003", "Monitor", -200.0));
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid product data: " + e.getMessage());
        }

        // --- Finding an existing product ---
        try {
            Product found = inventory.findById("P001");
            System.out.println("Found: " + found);
        } catch (ProductNotFoundException e) {
            System.out.println(e.getMessage());
        }

        // --- Finding a non-existent product ---
        try {
            Product notFound = inventory.findById("P999");
            System.out.println(notFound);
        } catch (ProductNotFoundException e) {
            System.out.println(e.getMessage());
            System.out.println("Searched for ID: " + e.getProductId());
        }

        // --- Try-with-resources (simulated) ---
        System.out.println("\nTry-with-resources example:");
        try (java.io.StringReader reader = new java.io.StringReader("Hello, world")) {
            int ch;
            while ((ch = reader.read()) != -1) {
                System.out.print((char) ch);
            }
            System.out.println();
        } catch (java.io.IOException e) {
            System.out.println("Read error: " + e.getMessage());
        }
        // reader.close() called automatically
    }
}

```

```

Output:
Products added successfully.
Invalid product data: Price cannot be negative: -200.0
Found: Product{id='P001', name='Keyboard', price=49.99}
Product not found: P999
Searched for ID: P999

Try-with-resources example:
Hello, world

```

---

## 14. Best Practices

### Catch specific exceptions, not `Exception`

```java
// Avoid — hides the real problem
catch (Exception e) { ... }

// Prefer — you know exactly what went wrong
catch (NumberFormatException e) { ... }

```

### Never swallow exceptions silently

```java
// Never do this — the problem disappears with no trace
catch (IOException e) { }

// Always at minimum log the message
catch (IOException e) {
    System.out.println("File error: " + e.getMessage());
}

```

### Use custom exceptions to communicate intent
A method that throws `ProductNotFoundException` is far more expressive than one that throws a generic `RuntimeException` with a message you have to read to understand.

### Throw early, catch late
- **Throw early**: validate inputs at the start of a method and throw immediately if they are invalid
- **Catch late**: handle the exception at the layer that has enough context to do something meaningful with it

```java
// Good: throw early
public void setAge(int age) {
    if (age < 0) throw new IllegalArgumentException("Age cannot be negative.");
    this.age = age;
}

// Good: catch where you can respond sensibly
public void handleUserInput(String input) {
    try {
        int age = Integer.parseInt(input);
        person.setAge(age);
    } catch (NumberFormatException e) {
        System.out.println("Please enter a valid number.");
    } catch (IllegalArgumentException e) {
        System.out.println(e.getMessage());
    }
}

```

### Always clean up resources
Use try-with-resources for anything that implements `AutoCloseable`. If you cannot, use `finally`.

### Include useful information in exception messages

```java
// Unhelpful
throw new IllegalArgumentException("Invalid value.");

// Helpful
throw new IllegalArgumentException("Age must be between 0 and 150, but received: " + age);

```

---

## 15. Key Takeaways

- An **exception** is an event that disrupts normal program flow; an exception object carries the type, message, and stack trace
- **Checked exceptions** must be caught or declared with `throws`; the compiler enforces this
- **Unchecked exceptions** (subclasses of `RuntimeException`) do not require handling — they usually indicate bugs
- **Errors** (`OutOfMemoryError`, `StackOverflowError`) should not be caught; they indicate JVM-level failures
- Use `try-catch` to handle exceptions; use `finally` (or try-with-resources) to clean up resources
- Use `throw` to signal an error; use `throws` to declare that a method may propagate a checked exception
- Create **custom exceptions** by extending `Exception` (checked) or `RuntimeException` (unchecked)
- **Exception chaining** preserves the original cause when wrapping one exception in another
- Catch exceptions at the level where you have enough context to handle them meaningfully
- Never swallow exceptions silently — always at minimum log the message

---

Exception handling is not about hiding errors. It is about giving your program the information it needs to fail gracefully, recover when possible, and communicate clearly when it cannot.

---

## EXCEPTIONS - EXERCISE

# Exceptions Practice Exercises

Exception handling is not about hiding errors. It is about giving your program the information it needs to fail gracefully, recover when possible, and communicate clearly when it cannot. The exercises below build from basic try/catch through custom exceptions, exception chaining, and resource management. Work through each set in order.

---

## Exercise Set 1: try/catch/finally

### Exercise 1.1: Safe Division

Write a method `safeDivide(int a, int b)` that:
- Attempts `a / b` inside a `try` block
- Catches `ArithmeticException` and returns `0`, printing a message explaining why
- Prints `"Division attempted"` in a `finally` block every time, regardless of outcome

Call it with `(10, 2)`, `(10, 0)`, and `(-15, 3)`. Show that `finally` runs in all three cases.

### Exercise 1.2: Multiple Catch Blocks

Write a method `parseAndIndex(String[] arr, String indexStr)` that:
1. Parses `indexStr` to an integer using `Integer.parseInt`
2. Uses that integer to index into `arr`
3. Calls `.toUpperCase()` on the result

Use three separate `catch` blocks for `NumberFormatException`, `ArrayIndexOutOfBoundsException`, and `NullPointerException`, each printing a specific message. Call the method four times:
- Valid input
- A non-numeric string for the index
- An index that is out of range
- An index that points to a `null` element (put a `null` in the array)

### Exercise 1.3: Finally for Cleanup

Create a class `FakeConnection` (not a real I/O class — just a regular class with `open()`, `query()`, and `close()` methods that print messages). `query()` should throw a `RuntimeException` when called with a bad argument.

Write a method that opens the connection, calls `query()`, and always closes it in `finally`. Demonstrate that `close()` is called even when `query()` throws.

---

## Exercise Set 2: Checked vs Unchecked Exceptions

### Exercise 2.1: The Checked Exception Contract

Write a method `readConfig(String filename) throws java.io.IOException` that simulates reading a configuration file. If `filename` is `null` or empty, throw a new `java.io.IOException("No filename provided")`. Otherwise print `"Reading: " + filename`.

Write two callers:
- One that handles the `IOException` with a `try-catch`
- One that propagates it using `throws IOException` in its own signature

Show that a third method that calls `readConfig` without either handling or declaring the exception does not compile (write the error as a comment).

### Exercise 2.2: When to Use Unchecked

Write a class `BankAccount` with a `double balance` field and a method `withdraw(double amount)` that throws `IllegalArgumentException` if `amount <= 0` and `IllegalStateException` if `amount > balance`. Neither of these requires a `try-catch` at the call site.

Demonstrate: call `withdraw` with `-50`, then with an amount that exceeds the balance. Catch both exceptions at the call site and print specific messages for each. Explain in a comment why these are `RuntimeException` subclasses rather than checked exceptions.

### Exercise 2.3: Checked Exception Propagation Chain

Write three methods that call each other in sequence:
- `readLine()` throws `java.io.IOException`
- `processFile()` calls `readLine()` and declares `throws java.io.IOException`
- `loadData()` calls `processFile()` and handles the `IOException` in a `try-catch`

Inside `readLine()`, throw `new java.io.IOException("Disk read failure")`. Show the entire chain compiles and the exception is caught in `loadData()`.

---

## Exercise Set 3: Custom Exceptions

### Exercise 3.1: Custom Unchecked Exception

Create `InsufficientFundsException` extending `RuntimeException` with:
- A `private double amount` field storing the shortfall
- A constructor `InsufficientFundsException(double amount)` that calls `super` with a descriptive message
- A `getAmount()` accessor

Use it inside a `BankAccount.withdraw(double amount)` method. Catch it in `main`, print the message, and print the shortfall separately via `getAmount()`.

### Exercise 3.2: Custom Checked Exception

Create `InvalidAgeException` extending `Exception` with:
- A constructor accepting a `String message`
- A second constructor accepting `int age` that builds the message automatically: `"Age " + age + " is not valid (must be 0–150)."`

Use it inside a `Person.setAge(int age) throws InvalidAgeException` method. Demonstrate with a valid age and two invalid ages (`-5` and `200`).

### Exercise 3.3: Domain-Specific Exception Hierarchy

Create a small exception hierarchy:
- `AppException extends RuntimeException` — base class with a `String code` field and a constructor `AppException(String code, String message)`; add `getCode()`
- `UserNotFoundException extends AppException` — constructor takes a `long userId`, sets code `"USER_NOT_FOUND"` and builds a message
- `DuplicateEmailException extends AppException` — constructor takes a `String email`, sets code `"DUPLICATE_EMAIL"` and builds a message

Write a `UserService` class with `findUser(long id)` and `registerUser(String email)` that throw these exceptions. Catch them polymorphically with a single `catch (AppException e)` block and print both `e.getCode()` and `e.getMessage()`.

---

## Exercise Set 4: Exception Chaining and Re-throwing

### Exercise 4.1: Wrapping a Low-Level Exception

Write a method `loadUserData(int userId)` that accesses an array with `userId` as an index. If the index is out of bounds, catch the `ArrayIndexOutOfBoundsException` and wrap it in a custom `DataAccessException extends Exception`, passing the original as the cause.

In `main`, catch `DataAccessException`, print its message, then print the cause's message using `e.getCause().getMessage()`.

### Exercise 4.2: Re-throwing with Context

Write a method `parsePrice(String input)` that calls `Double.parseDouble(input)`. If a `NumberFormatException` is thrown, catch it and re-throw a new `IllegalArgumentException("Invalid price format: '" + input + "'", e)`, preserving the original exception as the cause.

In `main`, catch the `IllegalArgumentException`, print its message, and also print `e.getCause().getClass().getSimpleName()` to confirm the cause is still accessible.

### Exercise 4.3: Multi-level Exception Chain

Simulate a three-layer architecture where each layer wraps the exception from the layer below:

- `databaseLayer()` throws `java.sql.SQLException("Connection timeout")`
- `repositoryLayer()` catches it and throws a checked `RepositoryException extends Exception` with the `SQLException` as the cause
- `serviceLayer()` catches it and throws an unchecked `ServiceException extends RuntimeException` with the `RepositoryException` as the cause
- `main` catches `ServiceException`, prints its message, then follows the cause chain with `getCause()` twice to reach and print the original `SQLException` message

---

## Exercise Set 5: try-with-resources and AutoCloseable

### Exercise 5.1: Implementing AutoCloseable

Create a class `ManagedResource` that implements `AutoCloseable`:
- Constructor prints `"ManagedResource opened"`
- A method `process()` prints `"Processing..."`
- `close()` prints `"ManagedResource closed"`

Use it in a try-with-resources block. Show that `close()` is called automatically after the `try` block exits normally. Then repeat with `process()` throwing a `RuntimeException` — show that `close()` is still called before the exception propagates.

### Exercise 5.2: Multiple Resources in One Block

Create two classes `InputResource` and `OutputResource`, both implementing `AutoCloseable`. Each constructor prints `"Opened"` with its name. Each `close()` prints `"Closed"` with its name.

Declare both in a single try-with-resources statement. Show that they are closed in reverse declaration order (last declared, first closed). Do this for both the normal path and the exception path.

### Exercise 5.3: Suppressed Exceptions

Create a `BrokenResource` that implements `AutoCloseable`. Its `use()` method throws a `RuntimeException("Primary failure")`. Its `close()` method throws a `RuntimeException("Close failure")`.

Use it in a try-with-resources block. When both the body and `close()` throw, Java keeps the body exception as the primary and attaches the close exception as a suppressed exception. In the catch block, call `e.getSuppressed()` to retrieve and print the suppressed exceptions, demonstrating that neither exception is silently lost.

---

## Common Mistakes

### Catching Exception or Throwable too broadly

Catching the top of the hierarchy silences information you need. You lose the ability to handle different failure modes differently, and you may accidentally catch exceptions you had no intention of handling (including `OutOfMemoryError` if you catch `Throwable`).

```java
// Avoid — masks all possible failures with one generic handler.
try {
    processData();
} catch (Exception e) {
    System.out.println("Something went wrong.");
}

// Prefer — handle each failure mode explicitly.
try {
    processData();
} catch (IOException e) {
    System.out.println("I/O failure: " + e.getMessage());
} catch (IllegalArgumentException e) {
    System.out.println("Bad input: " + e.getMessage());
}

```

### Swallowing exceptions (empty catch blocks)

An empty catch block discards the exception entirely. The error silently disappears, the program continues in a potentially broken state, and there is no record of what went wrong. This is one of the most harmful patterns in Java code.

```java
// Never do this — the exception vanishes with no trace.
try {
    loadConfig("settings.json");
} catch (IOException e) {
    // nothing here
}

// At minimum, log the message. In production code, use a proper logger.
try {
    loadConfig("settings.json");
} catch (IOException e) {
    System.out.println("Config load failed: " + e.getMessage());
}

```

### Throwing exceptions from finally blocks

If both the `try` body and the `finally` block throw exceptions, the `finally` exception replaces the original. The first exception — the one that explains what actually went wrong — is permanently lost. There is no suppression mechanism for classic `finally` (unlike try-with-resources).

```java
// Dangerous: the IOException from the try block is silently discarded.
try {
    readFile(); // throws IOException
} finally {
    closeResource(); // also throws RuntimeException — this one wins.
}

// Safe: guard the finally block so it does not throw.
try {
    readFile();
} finally {
    try {
        closeResource();
    } catch (Exception ignored) {
        System.out.println("Close failed (original exception takes priority).");
    }
}

```

### Checking exception type with == instead of instanceof

Exception types form a class hierarchy. A `FileNotFoundException` IS an `IOException`. Using `==` checks for exact class identity and misses all subclasses, so subtype exceptions fall through uncaught.

```java
// Wrong: == only matches the exact class, not subclasses.
try {
    readFile();
} catch (IOException e) {
    if (e.getClass() == IOException.class) {
        // A FileNotFoundException would not match this — it would go unhandled.
    }
}

// Correct: instanceof respects the class hierarchy.
try {
    readFile();
} catch (IOException e) {
    if (e instanceof java.io.FileNotFoundException) {
        System.out.println("File not found: " + e.getMessage());
    } else {
        System.out.println("I/O error: " + e.getMessage());
    }
}

```

---

Solutions for these exercises are in the `solutions/` subfolder.

---