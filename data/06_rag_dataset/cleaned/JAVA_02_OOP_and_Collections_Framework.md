# Comprehensive Java Object-Oriented Programming (OOP) & Collections Framework Guide

## OOP - OOP

# Introduction to Object-Oriented Programming (OOP)

Object-Oriented Programming is a programming paradigm that organizes software design around **objects** rather than functions and logic. An object is a self-contained unit that combines **data** (attributes) and **behavior** (methods) into a single entity. Java is a class-based, object-oriented language, meaning everything in Java revolves around classes and objects.

## 1. Classes and Objects

A **class** is a blueprint or template that defines the structure and behavior of objects. An **object** is a concrete instance of a class that exists in memory at runtime.

```

Think of it like this:
  Class  = Blueprint of a house
  Object = The actual house built from that blueprint

```

### Defining a Class

```java
public class Car {
    // Attributes (fields/instance variables)
    private String brand;
    private String model;
    private int year;

    // Constructor
    public Car(String brand, String model, int year) {
        this.brand = brand;
        this.model = model;
        this.year = year;
    }

    // Methods (behavior)
    public void start() {
        System.out.println(brand + " " + model + " is starting.");
    }

    public void stop() {
        System.out.println(brand + " " + model + " has stopped.");
    }
}

```

### Creating Objects

```java
public class Main {
    public static void main(String[] args) {
        // Creating objects from the Car class
        Car car1 = new Car("Toyota", "Corolla", 2020);
        Car car2 = new Car("Honda", "Civic", 2022);

        // Calling methods on objects
        car1.start();  // Output: Toyota Corolla is starting.
        car2.start();  // Output: Honda Civic is starting.
    }
}

```

## 2. Anatomy of a Class

A Java class typically consists of the following components:

```java
public class Student {
    // 1. Fields (instance variables) - the data
    private String name;
    private int age;
    private double gpa;

    // 2. Constructors - initialize the object
    public Student(String name, int age, double gpa) {
        this.name = name;
        this.age = age;
        this.gpa = gpa;
    }

    // 3. Methods - the behavior
    public void study(String subject) {
        System.out.println(name + " is studying " + subject);
    }

    // 4. Getters and Setters - controlled access to fields
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // 5. toString() - string representation of the object
    @Override
    public String toString() {
        return "Student{name='" + name + "', age=" + age + ", gpa=" + gpa + "}";
    }
}

```

## 3. Constructors

A **constructor** is a special method that is called when an object is created. It has the same name as the class and no return type.

### Default Constructor
If you do not define any constructor, Java provides a **default constructor** that initializes fields to their default values (0, null, false, etc.).

```java
public class Animal {
    private String name;
    private String color;

    // No-argument constructor
    public Animal() {
        name = "Unknown";
        color = "Unknown";
    }
}

// Usage
Animal a = new Animal();
System.out.println(a.getName()); // Output: Unknown

```

### Parameterized Constructor
Accepts arguments to initialize fields with specific values.

```java
public class Animal {
    private String name;
    private String color;

    public Animal(String name, String color) {
        this.name = name;
        this.color = color;
    }
}

// Usage
Animal dog = new Animal("Rex", "Brown");

```

### Constructor Overloading
A class can have multiple constructors with different parameter lists.

```java
public class Animal {
    private String name;
    private String color;

    public Animal() {
        this.name = "Unknown";
        this.color = "Unknown";
    }

    public Animal(String name) {
        this.name = name;
        this.color = "Unknown";
    }

    public Animal(String name, String color) {
        this.name = name;
        this.color = color;
    }
}

```

### Constructor Chaining with `this()`
One constructor can call another constructor in the same class using `this()`.

```java
public class Animal {
    private String name;
    private String color;

    public Animal() {
        this("Unknown", "Unknown"); // Calls the two-argument constructor
    }

    public Animal(String name) {
        this(name, "Unknown"); // Calls the two-argument constructor
    }

    public Animal(String name, String color) {
        this.name = name;
        this.color = color;
    }
}

```

## 4. The `this` Keyword

The `this` keyword refers to the current object instance. It is used to:

- **Distinguish** instance variables from parameters with the same name
- **Call** another constructor in the same class
- **Pass** the current object as an argument to a method

```java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name; // this.name = instance variable, name = parameter
    }

    public void introduce() {
        System.out.println("Hi, I am " + this.name);
    }
}

```

## 5. Getters and Setters

**Getters** retrieve the value of a private field. **Setters** modify the value of a private field. Together they provide controlled access to an object's data.

```java
public class BankAccount {
    private String owner;
    private double balance;

    public BankAccount(String owner, double balance) {
        this.owner = owner;
        this.balance = balance;
    }

    // Getter
    public double getBalance() {
        return balance;
    }

    // Setter with validation
    public void setBalance(double balance) {
        if (balance >= 0) {
            this.balance = balance;
        } else {
            System.out.println("Balance cannot be negative.");
        }
    }

    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }
}

```

## 6. The `toString()` Method

Every class in Java inherits from `Object`, which provides a `toString()` method. By default, it returns the class name and memory address. Override it to provide a meaningful string representation.

```java
public class Book {
    private String title;
    private String author;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
    }

    @Override
    public String toString() {
        return "Book{title='" + title + "', author='" + author + "'}";
    }
}

// Usage
Book book = new Book("Clean Code", "Robert Martin");
System.out.println(book); // Output: Book{title='Clean Code', author='Robert Martin'}
// Without override: Book@1b6d3586

```

## 7. Access Modifiers

Access modifiers control the visibility of classes, fields, and methods.

| Modifier    | Same Class | Same Package | Subclass | Everywhere |
|-------------|------------|--------------|----------|------------|
| `public`    | Yes        | Yes          | Yes      | Yes        |
| `protected` | Yes        | Yes          | Yes      | No         |
| default     | Yes        | Yes          | No       | No         |
| `private`   | Yes        | No           | No       | No         |

**Rule of thumb**: Make fields `private` and provide `public` getters and setters. This is the foundation of encapsulation.

## 8. Static vs Instance Members

### Instance Members
Belong to individual objects. Each object has its own copy.

```java
public class Student {
    private String name; // Each student has their own name

    public void setName(String name) {
        this.name = name;
    }
}

```

### Static Members
Belong to the class itself. Shared across all objects.

```java
public class Student {
    private String name;
    private static int studentCount = 0; // Shared across all Student objects

    public Student(String name) {
        this.name = name;
        studentCount++; // Incremented each time a Student is created
    }

    public static int getStudentCount() {
        return studentCount;
    }
}

// Usage
Student s1 = new Student("Alice");
Student s2 = new Student("Bob");
System.out.println(Student.getStudentCount()); // Output: 2

```

## 9. The Four Pillars of OOP

Object-Oriented Programming is built on four fundamental principles:

1. **Encapsulation** - Bundling data and methods together, restricting direct access to internal state
2. **Inheritance** - Creating new classes based on existing classes, inheriting their fields and methods
3. **Polymorphism** - The ability of objects to take on many forms, responding differently to the same method call
4. **Abstraction** - Hiding complex implementation details and exposing only the essential features

Each of these pillars is covered in detail in its own dedicated document.

## 10. Best Practices

- Use meaningful class names that represent real-world entities (nouns)
- Use meaningful method names that describe actions (verbs)
- Keep fields `private` and provide access through getters and setters
- Override `toString()` for every class to aid debugging
- Follow the Single Responsibility Principle: a class should have one reason to change
- Use constructor overloading to provide flexibility in object creation
- Prefer composition over inheritance when the relationship is "has-a" rather than "is-a"

---

This guide covers the foundational concepts of OOP in Java. Each of the four pillars is explored in depth in its own separate document.

---

## OOP - ENCAPSULATION

# Encapsulation

Encapsulation is the practice of **bundling data (fields) and the methods that operate on that data into a single unit (class)**, while **restricting direct access** to the internal state of the object. It is the most fundamental pillar of OOP and the basis for writing secure, maintainable code.

The core idea is simple: an object should control how its data is accessed and modified. Outside code should never be able to put an object into an invalid state.

## 1. Why Encapsulation Matters

Without encapsulation:

```java
public class BankAccount {
    public double balance; // Anyone can modify this directly
}

// Dangerous - no validation, no control
BankAccount account = new BankAccount();
account.balance = -5000; // Invalid state, no one stopped it

```

With encapsulation:

```java
public class BankAccount {
    private double balance; // Only accessible through methods

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Insufficient funds or invalid amount.");
        }
    }

    public double getBalance() {
        return balance;
    }
}

```

Now the balance can never be set to a negative value. The class **controls its own state**.

## 2. How to Achieve Encapsulation

Encapsulation in Java follows a straightforward pattern:

1. Declare fields as `private`
2. Provide `public` getter methods to read field values
3. Provide `public` setter methods to modify field values (with validation if needed)

```java
public class Employee {
    // Step 1: Private fields
    private String name;
    private double salary;
    private String department;

    // Step 2: Constructor
    public Employee(String name, double salary, String department) {
        this.name = name;
        setSalary(salary);       // Use setter for validation even in constructor
        this.department = department;
    }

    // Step 3: Getters
    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public String getDepartment() {
        return department;
    }

    // Step 4: Setters with validation
    public void setName(String name) {
        if (name != null && !name.isEmpty()) {
            this.name = name;
        }
    }

    public void setSalary(double salary) {
        if (salary >= 0) {
            this.salary = salary;
        } else {
            System.out.println("Salary cannot be negative.");
        }
    }

    public void setDepartment(String department) {
        this.department = department;
    }
}

```

## 3. Getters and Setters In Depth

### Read-Only Fields
Sometimes a field should be set once and never changed. Provide only a getter, no setter.

```java
public class Student {
    private final String studentId; // final ensures it cannot be reassigned
    private String name;

    public Student(String studentId, String name) {
        this.studentId = studentId;
        this.name = name;
    }

    // Getter only - no setter for studentId
    public String getStudentId() {
        return studentId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

```

### Computed Getters
A getter does not need to return a field directly. It can compute a value.

```java
public class Rectangle {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    // Computed getter - no corresponding field
    public double getArea() {
        return width * height;
    }

    // Computed getter
    public double getPerimeter() {
        return 2 * (width + height);
    }
}

```

### Defensive Copying
When a getter returns a mutable object (like an array or list), return a copy to prevent external code from modifying internal state.

```java
import java.util.Arrays;

public class Gradebook {
    private int[] grades;

    public Gradebook(int[] grades) {
        this.grades = Arrays.copyOf(grades, grades.length); // Defensive copy in
    }

    public int[] getGrades() {
        return Arrays.copyOf(grades, grades.length); // Defensive copy out
    }
}

```

## 4. Encapsulation with Behavior

Encapsulation is not just about getters and setters. It is about exposing **meaningful operations** rather than raw data access.

### Poor Encapsulation (Data-Centric)

```java
public class Timer {
    private int seconds;

    public int getSeconds() { return seconds; }
    public void setSeconds(int seconds) { this.seconds = seconds; }
}

// Client code must manage the logic
Timer timer = new Timer();
timer.setSeconds(timer.getSeconds() + 60); // Adding a minute
timer.setSeconds(timer.getSeconds() - 10); // Subtracting 10 seconds

```

### Good Encapsulation (Behavior-Centric)

```java
public class Timer {
    private int seconds;

    public int getSeconds() {
        return seconds;
    }

    public void addMinutes(int minutes) {
        if (minutes > 0) {
            seconds += minutes * 60;
        }
    }

    public void subtractSeconds(int amount) {
        if (amount > 0 && amount <= seconds) {
            seconds -= amount;
        }
    }

    public void reset() {
        seconds = 0;
    }

    public String getFormattedTime() {
        int mins = seconds / 60;
        int secs = seconds % 60;
        return mins + "m " + secs + "s";
    }
}

// Client code uses meaningful operations
Timer timer = new Timer();
timer.addMinutes(5);
timer.subtractSeconds(10);
System.out.println(timer.getFormattedTime()); // Output: 4m 50s

```

## 5. Access Modifier Levels

Encapsulation relies on access modifiers to enforce boundaries.

| Modifier    | Visibility                              | Use Case                          |
|-------------|-----------------------------------------|-----------------------------------|
| `private`   | Same class only                         | Fields, internal helper methods   |
| default     | Same package only                       | Package-internal utility classes  |
| `protected` | Same package + subclasses               | Fields/methods meant for subclasses |
| `public`    | Everywhere                              | API methods, constructors         |

**General rule**: Use the most restrictive access level that makes sense.

## 6. Complete Example

```java
public class Product {
    private String name;
    private double price;
    private int quantity;

    public Product(String name, double price, int quantity) {
        this.name = name;
        setPrice(price);
        setQuantity(quantity);
    }

    // Getters
    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    // Setters with validation
    public void setName(String name) {
        if (name != null && !name.isEmpty()) {
            this.name = name;
        }
    }

    public void setPrice(double price) {
        if (price >= 0) {
            this.price = price;
        }
    }

    public void setQuantity(int quantity) {
        if (quantity >= 0) {
            this.quantity = quantity;
        }
    }

    // Behavior methods
    public double getTotalValue() {
        return price * quantity;
    }

    public void restock(int amount) {
        if (amount > 0) {
            quantity += amount;
        }
    }

    public boolean sell(int amount) {
        if (amount > 0 && amount <= quantity) {
            quantity -= amount;
            return true;
        }
        return false;
    }

    public void applyDiscount(double percentage) {
        if (percentage > 0 && percentage <= 100) {
            price -= price * (percentage / 100);
        }
    }

    @Override
    public String toString() {
        return "Product{name='" + name + "', price=" + price + ", quantity=" + quantity + "}";
    }
}

```

```java
// Usage
Product laptop = new Product("Laptop", 999.99, 50);
laptop.sell(3);
laptop.applyDiscount(10);
System.out.println(laptop);
// Output: Product{name='Laptop', price=899.991, quantity=47}
System.out.println("Total stock value: " + laptop.getTotalValue());

```

## 7. Key Takeaways

- Encapsulation protects the internal state of an object from uncontrolled access
- Always declare fields as `private`
- Provide getters and setters to control how fields are accessed and modified
- Add validation in setters to prevent invalid state
- Prefer exposing meaningful behavior over raw data access
- Use `final` for fields that should not change after construction
- Return copies of mutable objects to prevent external modification

---

Encapsulation is the foundation upon which the other three pillars are built. Without encapsulation, inheritance and polymorphism become unreliable because any code could corrupt an object's internal state.

---

## OOP - INHERITANCE

# Inheritance

Inheritance is a mechanism that allows a new class (**subclass/child class**) to inherit the fields and methods of an existing class (**superclass/parent class**). It establishes an **"is-a" relationship** between classes and promotes code reuse.

```

Think of it like this:
  Animal (parent)
    ├── Dog (child) - is an Animal
    ├── Cat (child) - is an Animal
    └── Bird (child) - is an Animal

```

A Dog **is an** Animal. It has everything an Animal has, plus its own specific characteristics.

## 1. Basic Inheritance Syntax

In Java, inheritance is achieved using the `extends` keyword.

```java
// Parent class (superclass)
public class Animal {
    private String name;
    private int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void eat() {
        System.out.println(name + " is eating.");
    }

    public void sleep() {
        System.out.println(name + " is sleeping.");
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

```

```java
// Child class (subclass)
public class Dog extends Animal {
    private String breed;

    public Dog(String name, int age, String breed) {
        super(name, age); // Calls the parent constructor
        this.breed = breed;
    }

    // Dog-specific method
    public void bark() {
        System.out.println(getName() + " says: Woof!");
    }

    public String getBreed() {
        return breed;
    }
}

```

```java
// Usage
Dog dog = new Dog("Rex", 5, "German Shepherd");
dog.eat();   // Inherited from Animal
dog.sleep(); // Inherited from Animal
dog.bark();  // Defined in Dog

```

## 2. The `super` Keyword

The `super` keyword refers to the parent class. It is used to:

### Call the Parent Constructor
The first statement in a child constructor must be `super()` if you want to call the parent constructor explicitly.

```java
public class Cat extends Animal {
    private boolean isIndoor;

    public Cat(String name, int age, boolean isIndoor) {
        super(name, age); // Must be the first statement
        this.isIndoor = isIndoor;
    }
}

```

### Call a Parent Method
When you override a method but still want to use the parent's version.

```java
public class Dog extends Animal {
    private String breed;

    public Dog(String name, int age, String breed) {
        super(name, age);
        this.breed = breed;
    }

    @Override
    public void eat() {
        super.eat(); // Call the parent's eat() method first
        System.out.println(getName() + " wags tail while eating.");
    }
}

```

## 3. What Is Inherited

| Inherited                          | Not Inherited              |
|------------------------------------|----------------------------|
| `public` methods                   | `private` fields (exist but not directly accessible) |
| `protected` methods                | `private` methods          |
| `public` fields (if any)           | Constructors               |
| `protected` fields                 |                            |

**Important**: Private fields are not accessible directly in the subclass, but they still exist in the object. Access them through inherited getters and setters.

```java
public class Animal {
    private String name; // Not directly accessible in Dog

    public String getName() { // This IS accessible in Dog
        return name;
    }
}

public class Dog extends Animal {
    public void printName() {
        // System.out.println(name);      // Compilation error - private
        System.out.println(getName());     // Works - using inherited public getter
    }
}

```

## 4. Method Overriding

A subclass can provide its own implementation of a method defined in the parent class. This is called **method overriding**.

**Rules for Overriding:**
- Method must have the same name, return type, and parameters
- Access modifier cannot be more restrictive than the parent
- Use the `@Override` annotation to signal intent (recommended)
- Cannot override `final` or `static` methods

```java
public class Animal {
    public void makeSound() {
        System.out.println("Some generic sound");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof! Woof!");
    }
}

public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow!");
    }
}

```

```java
// Usage
Animal animal = new Animal();
Dog dog = new Dog();
Cat cat = new Cat();

animal.makeSound(); // Output: Some generic sound
dog.makeSound();    // Output: Woof! Woof!
cat.makeSound();    // Output: Meow!

```

## 5. The `protected` Access Modifier

The `protected` modifier is designed for inheritance. A `protected` member is accessible within the same package and by subclasses in any package.

```java
public class Vehicle {
    protected int speed;        // Accessible in subclasses
    private String engineType;  // Not accessible in subclasses

    public Vehicle(int speed, String engineType) {
        this.speed = speed;
        this.engineType = engineType;
    }

    protected void accelerate(int amount) {
        speed += amount;
    }
}

public class Car extends Vehicle {
    public Car(int speed, String engineType) {
        super(speed, engineType);
    }

    public void boost() {
        accelerate(50);                      // Can call protected method
        System.out.println("Speed: " + speed); // Can access protected field
    }
}

```

## 6. Constructor Chaining in Inheritance

When an object of a subclass is created, constructors execute from the top of the hierarchy down.

```java
public class Animal {
    public Animal() {
        System.out.println("Animal constructor");
    }
}

public class Dog extends Animal {
    public Dog() {
        super(); // Automatically inserted by Java if omitted
        System.out.println("Dog constructor");
    }
}

public class Puppy extends Dog {
    public Puppy() {
        super();
        System.out.println("Puppy constructor");
    }
}

// Creating a Puppy
Puppy p = new Puppy();
// Output:
// Animal constructor
// Dog constructor
// Puppy constructor

```

If the parent class has no no-argument constructor, the child class **must** explicitly call a parent constructor with `super(args)`.

## 7. The `final` Keyword in Inheritance

### Final Class
A `final` class cannot be extended.

```java
public final class MathConstants {
    public static final double PI = 3.14159;
    // No class can extend MathConstants
}

```

### Final Method
A `final` method cannot be overridden by subclasses.

```java
public class Account {
    public final void closeAccount() {
        // This implementation cannot be changed by subclasses
        System.out.println("Account closed.");
    }
}

```

## 8. The `Object` Class

Every class in Java implicitly extends `java.lang.Object`. This means every object has access to the methods defined in `Object`:

- `toString()` - String representation of the object
- `equals(Object obj)` - Checks equality
- `hashCode()` - Returns a hash code value
- `getClass()` - Returns the runtime class

```java
public class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Person{name='" + name + "'}";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Person person = (Person) obj;
        return name.equals(person.name);
    }
}

```

## 9. Single Inheritance in Java

Java supports **single inheritance** only. A class can extend exactly one parent class.

```java
// Valid
public class Dog extends Animal { }

// Invalid - Java does not allow multiple inheritance of classes
// public class Dog extends Animal, Pet { }  // Compilation error

```

To achieve similar behavior, Java provides **interfaces**, which a class can implement multiple of.

## 10. Multilevel Inheritance

A class can inherit from a class that itself inherits from another class, forming a chain.

```java
public class Animal {
    public void breathe() {
        System.out.println("Breathing...");
    }
}

public class Mammal extends Animal {
    public void feedMilk() {
        System.out.println("Feeding milk...");
    }
}

public class Dog extends Mammal {
    public void bark() {
        System.out.println("Barking...");
    }
}

// Dog inherits from Mammal AND Animal
Dog dog = new Dog();
dog.breathe();   // From Animal
dog.feedMilk();  // From Mammal
dog.bark();      // From Dog

```

## 11. Complete Example

```java
public class Shape {
    private String color;

    public Shape(String color) {
        this.color = color;
    }

    public double getArea() {
        return 0;
    }

    public String getColor() {
        return color;
    }

    @Override
    public String toString() {
        return "Shape{color='" + color + "', area=" + getArea() + "}";
    }
}

```

```java
public class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public String toString() {
        return "Circle{color='" + getColor() + "', radius=" + radius + ", area=" + getArea() + "}";
    }
}

```

```java
public class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() {
        return width * height;
    }

    @Override
    public String toString() {
        return "Rectangle{color='" + getColor() + "', width=" + width
                + ", height=" + height + ", area=" + getArea() + "}";
    }
}

```

```java
// Usage
Shape circle = new Circle("Red", 5.0);
Shape rectangle = new Rectangle("Blue", 4.0, 6.0);

System.out.println(circle);
// Output: Circle{color='Red', radius=5.0, area=78.53981633974483}
System.out.println(rectangle);
// Output: Rectangle{color='Blue', width=4.0, height=6.0, area=24.0}

```

## 12. When to Use Inheritance

**Use inheritance when:**
- There is a clear "is-a" relationship (Dog is an Animal)
- Subclasses genuinely share behavior and state with the parent
- You want to leverage polymorphism

**Avoid inheritance when:**
- The relationship is "has-a" (a Car has an Engine, not a Car is an Engine)
- You only need to reuse a few methods (prefer composition)
- The parent class was not designed for extension

## 13. Key Takeaways

- Inheritance establishes an "is-a" relationship between classes
- Use `extends` to inherit from a parent class
- Use `super` to call parent constructors and methods
- Private fields are inherited but not directly accessible
- Use `@Override` annotation when overriding methods
- Java supports single inheritance only (one parent class)
- Every class implicitly extends `Object`
- Use `final` to prevent a class from being extended or a method from being overridden
- Prefer composition over inheritance when the relationship is not genuinely "is-a"

---

Inheritance works hand-in-hand with polymorphism. Once you understand how subclasses extend parent classes, the next step is understanding how Java decides which version of a method to call at runtime.

---

## OOP - POLYMORPHISM

# Polymorphism

Polymorphism means **"many forms."** It is the ability of a single interface or method call to behave differently depending on the actual type of the object it is operating on. In Java, polymorphism allows you to write code that works with a parent type but automatically executes the correct behavior for each subclass.

```

Think of it like this:
  You call makeSound() on an Animal reference.
  If the actual object is a Dog  -> "Woof!"
  If the actual object is a Cat  -> "Meow!"
  If the actual object is a Bird -> "Tweet!"
  Same method call, different behavior.

```

## 1. Types of Polymorphism

Java supports two types of polymorphism:

| Type                | Also Known As            | Resolved At    | Mechanism          |
|---------------------|--------------------------|----------------|--------------------|
| Compile-time        | Static polymorphism      | Compilation    | Method overloading |
| Runtime             | Dynamic polymorphism     | Execution      | Method overriding  |

## 2. Compile-Time Polymorphism (Method Overloading)

Method overloading allows multiple methods in the same class to share a name but differ in their parameter lists. The compiler determines which method to call based on the arguments provided.

```java
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }

    public String add(String a, String b) {
        return a + b; // String concatenation
    }
}

```

```java
Calculator calc = new Calculator();
System.out.println(calc.add(2, 3));           // Calls add(int, int) -> 5
System.out.println(calc.add(2.5, 3.5));       // Calls add(double, double) -> 6.0
System.out.println(calc.add(1, 2, 3));        // Calls add(int, int, int) -> 6
System.out.println(calc.add("Hello", " World")); // Calls add(String, String) -> Hello World

```

**Rules for Overloading:**
- Methods must have the same name
- Methods must differ in parameter type, number, or order
- Return type alone is not sufficient to distinguish overloaded methods

## 3. Runtime Polymorphism (Method Overriding)

Runtime polymorphism occurs when a subclass overrides a method from its parent class. The JVM determines which version to execute based on the **actual object type** at runtime, not the reference type.

```java
public class Animal {
    public void makeSound() {
        System.out.println("Some generic sound");
    }

    public void describe() {
        System.out.println("I am an animal.");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Woof! Woof!");
    }

    @Override
    public void describe() {
        System.out.println("I am a dog.");
    }
}

public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow!");
    }

    @Override
    public void describe() {
        System.out.println("I am a cat.");
    }
}

```

```java
// The reference type is Animal, but the actual objects are Dog and Cat
Animal myDog = new Dog();
Animal myCat = new Cat();

myDog.makeSound(); // Output: Woof! Woof!   (Dog's version)
myCat.makeSound(); // Output: Meow!          (Cat's version)

```

This is the essence of runtime polymorphism: the method that runs depends on the **object**, not the **variable type**.

## 4. Upcasting and Downcasting

### Upcasting
Assigning a subclass object to a parent class reference. This is done **implicitly** and is always safe.

```java
Animal animal = new Dog("Rex", 5, "Labrador"); // Upcasting (implicit)
animal.makeSound(); // Calls Dog's makeSound()
// animal.bark();   // Compilation error - Animal reference cannot see Dog-specific methods

```

After upcasting, you can only call methods defined in the parent class. However, if the method is overridden, the subclass version executes.

### Downcasting
Casting a parent class reference back to a subclass type. This must be done **explicitly** and can fail at runtime.

```java
Animal animal = new Dog("Rex", 5, "Labrador");

// Explicit downcast
Dog dog = (Dog) animal;
dog.bark(); // Now we can access Dog-specific methods

// Dangerous downcast - will throw ClassCastException at runtime
// Cat cat = (Cat) animal; // Runtime error: Dog cannot be cast to Cat

```

### Safe Downcasting with `instanceof`
Always check the type before downcasting.

```java
Animal animal = new Dog("Rex", 5, "Labrador");

if (animal instanceof Dog) {
    Dog dog = (Dog) animal;
    dog.bark(); // Safe
}

if (animal instanceof Cat) {
    Cat cat = (Cat) animal; // This block will not execute
    cat.purr();
}

```

### Pattern Matching for `instanceof` (Java 16+)

```java
if (animal instanceof Dog dog) {
    dog.bark(); // dog is already cast, no explicit cast needed
}

```

## 5. Polymorphism with Arrays and Collections

One of the most powerful uses of polymorphism is storing different subclass objects in a single array or collection of the parent type.

```java
Animal[] animals = new Animal[3];
animals[0] = new Dog("Rex", 5, "Labrador");
animals[1] = new Cat("Whiskers", 3, true);
animals[2] = new Bird("Tweety", 1, true);

// Same method call, different behavior for each object
for (Animal animal : animals) {
    animal.makeSound();
}
// Output:
// Woof! Woof!
// Meow!
// Tweet! Tweet!

```

## 6. Polymorphism with Method Parameters

Methods can accept a parent type as a parameter and work with any subclass.

```java
public class Veterinarian {
    // Accepts any Animal - Dog, Cat, Bird, etc.
    public void examine(Animal animal) {
        System.out.println("Examining: " + animal.getName());
        animal.makeSound();
    }
}

```

```java
Veterinarian vet = new Veterinarian();
vet.examine(new Dog("Rex", 5, "Labrador"));   // Works with Dog
vet.examine(new Cat("Whiskers", 3, true));     // Works with Cat
vet.examine(new Bird("Tweety", 1, true));      // Works with Bird

```

This means you can write methods that work with **any current or future subclass** of Animal without modifying the method.

## 7. Polymorphism with Return Types

Methods can return a parent type while actually returning subclass instances.

```java
public class AnimalFactory {
    public static Animal createAnimal(String type) {
        if (type.equals("dog")) {
            return new Dog("Default Dog", 1, "Mixed");
        } else if (type.equals("cat")) {
            return new Cat("Default Cat", 1, false);
        } else {
            return new Animal("Unknown", 0);
        }
    }
}

```

```java
Animal pet = AnimalFactory.createAnimal("dog");
pet.makeSound(); // Output: Woof! Woof!

```

## 8. The `@Override` Annotation

The `@Override` annotation tells the compiler that a method is intended to override a parent method. It is not required, but strongly recommended.

```java
public class Dog extends Animal {
    @Override
    public void makeSound() {     // Compiler verifies this overrides a parent method
        System.out.println("Woof!");
    }

    // @Override
    // public void makeSond() { }  // Compiler error - typo caught because of @Override
}

```

Without `@Override`, a typo in the method name would silently create a new method instead of overriding the intended one.

## 9. Complete Example

```java
public class Shape {
    private String color;

    public Shape(String color) {
        this.color = color;
    }

    public double getArea() {
        return 0;
    }

    public String getColor() {
        return color;
    }

    public void displayInfo() {
        System.out.println("Shape: " + getClass().getSimpleName()
                + ", Color: " + color
                + ", Area: " + String.format("%.2f", getArea()));
    }
}

```

```java
public class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
}

```

```java
public class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() {
        return width * height;
    }
}

```

```java
public class Triangle extends Shape {
    private double base;
    private double height;

    public Triangle(String color, double base, double height) {
        super(color);
        this.base = base;
        this.height = height;
    }

    @Override
    public double getArea() {
        return 0.5 * base * height;
    }
}

```

```java
// Polymorphism in action
public class Main {
    public static void printAllAreas(Shape[] shapes) {
        for (Shape shape : shapes) {
            shape.displayInfo(); // Each shape calculates its own area
        }
    }

    public static double totalArea(Shape[] shapes) {
        double total = 0;
        for (Shape shape : shapes) {
            total += shape.getArea();
        }
        return total;
    }

    public static void main(String[] args) {
        Shape[] shapes = {
            new Circle("Red", 5),
            new Rectangle("Blue", 4, 6),
            new Triangle("Green", 3, 8)
        };

        printAllAreas(shapes);
        // Output:
        // Shape: Circle, Color: Red, Area: 78.54
        // Shape: Rectangle, Color: Blue, Area: 24.00
        // Shape: Triangle, Color: Green, Area: 12.00

        System.out.println("Total area: " + String.format("%.2f", totalArea(shapes)));
        // Output: Total area: 114.54
    }
}

```

## 10. Key Takeaways

- Polymorphism allows one interface to serve multiple underlying forms
- **Compile-time polymorphism** (overloading) is resolved by the compiler based on method signatures
- **Runtime polymorphism** (overriding) is resolved by the JVM based on the actual object type
- Upcasting is implicit and safe; downcasting requires an explicit cast and should use `instanceof`
- Polymorphism enables writing flexible code that works with parent types and automatically handles any subclass
- Use `@Override` to catch errors and communicate intent
- Arrays and collections of a parent type can hold any mix of subclass objects

---

Polymorphism is what makes OOP truly powerful. It allows you to write extensible code that handles new subclasses without modification, which is the foundation of the Open/Closed Principle in software design.

---

## OOP - ABSTRACTION

# Abstraction

Abstraction is the principle of **hiding complex implementation details and exposing only the essential features** of an object. It allows you to define **what** an object does without specifying **how** it does it. In Java, abstraction is achieved through **abstract classes** and **interfaces**.

```

Think of it like this:
  When you drive a car, you use the steering wheel, pedals, and gear shift.
  You do not need to know how the engine combustion cycle works.
  The car abstracts away the complexity and gives you a simple interface.

```

## 1. Abstract Classes

An **abstract class** is a class that cannot be instantiated on its own. It serves as a base class that defines a common structure for its subclasses. It can contain both **abstract methods** (no implementation) and **concrete methods** (with implementation).

### Declaring an Abstract Class

```java
public abstract class Shape {
    private String color;

    public Shape(String color) {
        this.color = color;
    }

    // Abstract method - no body, must be implemented by subclasses
    public abstract double getArea();

    // Abstract method
    public abstract double getPerimeter();

    // Concrete method - has implementation, inherited as-is
    public String getColor() {
        return color;
    }

    public void displayInfo() {
        System.out.println("Shape: " + getClass().getSimpleName());
        System.out.println("Color: " + color);
        System.out.println("Area: " + String.format("%.2f", getArea()));
        System.out.println("Perimeter: " + String.format("%.2f", getPerimeter()));
    }
}

```

### Implementing an Abstract Class

```java
public class Circle extends Shape {
    private double radius;

    public Circle(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }
}

public class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() {
        return width * height;
    }

    @Override
    public double getPerimeter() {
        return 2 * (width + height);
    }
}

```

```java
// Usage
// Shape shape = new Shape("Red");  // Compilation error - cannot instantiate abstract class
Shape circle = new Circle("Red", 5);
Shape rectangle = new Rectangle("Blue", 4, 6);

circle.displayInfo();
// Output:
// Shape: Circle
// Color: Red
// Area: 78.54
// Perimeter: 31.42

```

### Rules for Abstract Classes
- Cannot be instantiated with `new`
- Can have constructors (called by subclasses via `super()`)
- Can have both abstract and concrete methods
- Can have fields (instance variables)
- A subclass **must** implement all abstract methods, or itself be declared abstract
- Can have `static` methods

## 2. Interfaces

An **interface** is a contract that defines a set of abstract methods a class must implement. It specifies **what** a class must do, but not **how** it does it. Interfaces define capabilities that can be shared across unrelated classes.

### Declaring an Interface

```java
public interface Drawable {
    void draw();         // Abstract by default (public abstract)
    void resize(double factor);
}

```

### Implementing an Interface
A class uses the `implements` keyword to implement an interface and must provide implementations for all its methods.

```java
public class Circle implements Drawable {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.println("Drawing a circle with radius " + radius);
    }

    @Override
    public void resize(double factor) {
        radius *= factor;
    }
}

```

### Multiple Interface Implementation
Unlike classes, a class can implement **multiple interfaces**.

```java
public interface Drawable {
    void draw();
}

public interface Resizable {
    void resize(double factor);
}

public interface Printable {
    void print();
}

// A class can implement all three
public class Circle implements Drawable, Resizable, Printable {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.println("Drawing circle");
    }

    @Override
    public void resize(double factor) {
        radius *= factor;
    }

    @Override
    public void print() {
        System.out.println("Circle with radius: " + radius);
    }
}

```

## 3. Interface Features (Java 8+)

### Default Methods
Interfaces can provide a default implementation using the `default` keyword. Classes that implement the interface can use the default implementation or override it.

```java
public interface Loggable {
    void performAction();

    // Default method with implementation
    default void log(String message) {
        System.out.println("[LOG] " + message);
    }
}

public class UserService implements Loggable {
    @Override
    public void performAction() {
        log("Performing user action"); // Uses default implementation
    }
}

```

### Static Methods
Interfaces can have static utility methods.

```java
public interface MathOperations {
    double calculate(double a, double b);

    static double square(double value) {
        return value * value;
    }
}

// Usage
double result = MathOperations.square(5); // 25.0

```

### Constants
All fields in an interface are implicitly `public static final`.

```java
public interface GameConstants {
    int MAX_PLAYERS = 4;       // public static final by default
    int MAX_LEVEL = 100;
    String DEFAULT_NAME = "Player";
}

```

## 4. Abstract Class vs Interface

| Feature              | Abstract Class                        | Interface                            |
|----------------------|---------------------------------------|--------------------------------------|
| Instantiation        | Cannot be instantiated                | Cannot be instantiated               |
| Methods              | Abstract and concrete                 | Abstract, default, and static        |
| Fields               | Any type (private, protected, etc.)   | Only `public static final` constants |
| Constructors         | Yes                                   | No                                   |
| Inheritance          | Single (extends one class)            | Multiple (implements many)           |
| Access modifiers     | Any                                   | Methods are `public` by default      |
| Use case             | Shared state and behavior among related classes | Defining capabilities across unrelated classes |

### When to Use Which

**Use an abstract class when:**
- Subclasses share common state (fields) and behavior
- You want to provide a partial implementation
- The classes have a clear "is-a" relationship

**Use an interface when:**
- You want to define a capability that unrelated classes can share
- You need multiple inheritance of type
- You want to define a contract without any state

## 5. Combining Abstract Classes and Interfaces

A class can extend one abstract class and implement multiple interfaces simultaneously.

```java
public abstract class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public abstract void makeSound();

    public String getName() {
        return name;
    }
}

public interface Swimmable {
    void swim();
}

public interface Trainable {
    void learnTrick(String trick);
}

// Dog extends Animal AND implements two interfaces
public class Dog extends Animal implements Swimmable, Trainable {
    public Dog(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + " says: Woof!");
    }

    @Override
    public void swim() {
        System.out.println(getName() + " is swimming.");
    }

    @Override
    public void learnTrick(String trick) {
        System.out.println(getName() + " learned: " + trick);
    }
}

```

```java
// Usage - polymorphism with interfaces
Dog dog = new Dog("Rex");
dog.makeSound();               // Woof!
dog.swim();                    // Rex is swimming.
dog.learnTrick("Shake hands"); // Rex learned: Shake hands

// Can be referenced by any of its types
Animal animal = dog;
Swimmable swimmer = dog;
Trainable trainable = dog;

```

## 6. Interface as a Type

Interfaces can be used as reference types, enabling polymorphism across unrelated classes.

```java
public interface Payable {
    double getPaymentAmount();
}

public class Employee implements Payable {
    private String name;
    private double salary;

    public Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }

    @Override
    public double getPaymentAmount() {
        return salary;
    }
}

public class Invoice implements Payable {
    private String description;
    private double amount;

    public Invoice(String description, double amount) {
        this.description = description;
        this.amount = amount;
    }

    @Override
    public double getPaymentAmount() {
        return amount;
    }
}

```

```java
// Employee and Invoice are unrelated but both are Payable
Payable[] payables = {
    new Employee("Alice", 5000),
    new Invoice("Office Supplies", 250),
    new Employee("Bob", 6000),
    new Invoice("Server Hosting", 1200)
};

double total = 0;
for (Payable p : payables) {
    total += p.getPaymentAmount();
}
System.out.println("Total payments: " + total); // Output: Total payments: 12450.0

```

## 7. Complete Example

```java
// Abstract class for common vehicle state and behavior
public abstract class Vehicle {
    private String brand;
    private int year;

    public Vehicle(String brand, int year) {
        this.brand = brand;
        this.year = year;
    }

    // Abstract methods - subclasses must implement
    public abstract void start();
    public abstract void stop();
    public abstract double getFuelEfficiency();

    // Concrete method
    public String getBrand() {
        return brand;
    }

    public int getYear() {
        return year;
    }

    @Override
    public String toString() {
        return brand + " (" + year + ")";
    }
}

```

```java
// Interface for electric vehicle capability
public interface Electric {
    double getBatteryLevel();
    void charge(double hours);
}

// Interface for GPS capability
public interface GPSEnabled {
    void navigateTo(String destination);
}

```

```java
public class ElectricCar extends Vehicle implements Electric, GPSEnabled {
    private double batteryLevel;

    public ElectricCar(String brand, int year) {
        super(brand, year);
        this.batteryLevel = 100.0;
    }

    @Override
    public void start() {
        System.out.println(getBrand() + " silently starts.");
    }

    @Override
    public void stop() {
        System.out.println(getBrand() + " stops.");
    }

    @Override
    public double getFuelEfficiency() {
        return 0; // Electric cars don't use fuel
    }

    @Override
    public double getBatteryLevel() {
        return batteryLevel;
    }

    @Override
    public void charge(double hours) {
        batteryLevel = Math.min(100, batteryLevel + (hours * 20));
        System.out.println(getBrand() + " charged to " + batteryLevel + "%");
    }

    @Override
    public void navigateTo(String destination) {
        System.out.println(getBrand() + " navigating to " + destination);
    }
}

```

```java
public class GasCar extends Vehicle implements GPSEnabled {
    private double fuelLevel;

    public GasCar(String brand, int year) {
        super(brand, year);
        this.fuelLevel = 100.0;
    }

    @Override
    public void start() {
        System.out.println(getBrand() + " engine roars to life.");
    }

    @Override
    public void stop() {
        System.out.println(getBrand() + " engine shuts off.");
    }

    @Override
    public double getFuelEfficiency() {
        return 12.5; // km per liter
    }

    @Override
    public void navigateTo(String destination) {
        System.out.println(getBrand() + " navigating to " + destination);
    }
}

```

```java
// Usage
public class Main {
    public static void main(String[] args) {
        Vehicle[] vehicles = {
            new ElectricCar("Tesla", 2024),
            new GasCar("Toyota", 2023)
        };

        for (Vehicle v : vehicles) {
            v.start();
        }
        // Output:
        // Tesla silently starts.
        // Toyota engine roars to life.

        // Using interface type
        GPSEnabled[] gpsDevices = {
            new ElectricCar("Tesla", 2024),
            new GasCar("Toyota", 2023)
        };

        for (GPSEnabled gps : gpsDevices) {
            gps.navigateTo("Nairobi");
        }
    }
}

```

## 8. Key Takeaways

- Abstraction hides complexity and exposes only what is necessary
- **Abstract classes** provide partial implementation and shared state for related classes
- **Interfaces** define contracts (capabilities) that unrelated classes can implement
- A class can extend one abstract class but implement multiple interfaces
- Abstract methods have no body and must be overridden by concrete subclasses
- Interfaces can have default and static methods (Java 8+)
- Use abstract classes for "is-a" relationships with shared state
- Use interfaces to define capabilities that cut across class hierarchies

---

Abstraction ties together with the other three pillars. Encapsulation hides internal data, inheritance shares structure, polymorphism enables flexible behavior, and abstraction defines clean contracts that make all of this work together.

---

## OOP - INTERFACES

# Interfaces as a Design Tool

An interface is more than just a list of methods a class must implement. It is a formal agreement between the code that defines a capability and the code that uses it, enforced at compile time. Understanding how to design with interfaces — not just how to write the syntax — is one of the most important skills in professional Java development.

```

Think of it like this:
  A power outlet is an interface.
  It defines exactly what shape the plug must be and what voltage it delivers.
  Any device that follows that contract can plug in.
  The outlet does not care if it is a lamp, a phone charger, or a laptop.
  Interfaces work the same way: the caller does not care what is on the other end,
  only that it honors the contract.

```

## 1. Interface as a Contract

When you define an interface, you are writing a contract. Every class that implements that interface promises to provide a working implementation of every method declared in it. The compiler holds classes to that promise — if a method is missing, the code will not compile.

```java
public interface Exportable {
    String toJson();
    byte[] toCsv();
}

// Compiler error: Report does not implement toCsv()
public class Report implements Exportable {
    @Override
    public String toJson() {
        return "{ \"title\": \"Q1 Report\" }";
    }
    // Missing toCsv() — compile-time error
}

```

This matters enormously when working in teams or building APIs. If you publish an interface as part of a library, every consumer who implements it is guaranteed to have those methods available. You can write code that calls `toJson()` on any `Exportable` and know with certainty, before the program ever runs, that the method exists. The contract is checked at build time, not discovered at runtime.

## 2. Programming to an Interface

Programming to an interface means declaring variables, parameters, and return types using the interface type rather than the concrete implementation type. This is one of the most practical design principles in Java.

```java
// Tightly coupled to a specific implementation
ArrayList<String> names = new ArrayList<>();

// Programmed to the interface
List<String> names = new ArrayList<>();

```

The second approach lets you swap the implementation without touching any code that uses `names`. If you later decide a `LinkedList` performs better for your access pattern, one line changes:

```java
// Only this one line changes
List<String> names = new LinkedList<>();

// All code that uses names stays identical
names.add("Alice");
names.add("Bob");
System.out.println(names.get(0)); // Output: Alice

```

The same principle applies to method signatures:

```java
// Bad: forces callers to pass an ArrayList specifically
public void printAll(ArrayList<String> items) { ... }

// Good: accepts any List implementation
public void printAll(List<String> items) { ... }

```

When a method accepts `List<String>`, callers can pass an `ArrayList`, a `LinkedList`, an unmodifiable list from `Collections.unmodifiableList()`, or any other `List` implementation. The method works with all of them because it only calls methods defined on the `List` interface.

## 3. Functional Interfaces (Java 8+)

A functional interface is an interface that declares exactly one abstract method. This single requirement is what allows the interface to be used with a lambda expression, because a lambda is simply a compact way to provide that one method's implementation.

The `@FunctionalInterface` annotation is optional but strongly recommended. It tells the compiler to enforce the one-abstract-method rule, so if you accidentally add a second abstract method, you get a clear error instead of silent behavior change.

```java
@FunctionalInterface
public interface Transformer {
    String transform(String input);
}

```

You can implement this interface using an anonymous class or a lambda:

```java
// Anonymous class — verbose but explicit
Transformer upper = new Transformer() {
    @Override
    public String transform(String input) {
        return input.toUpperCase();
    }
};

// Lambda — same result, far less noise
Transformer upper = input -> input.toUpperCase();

System.out.println(upper.transform("hello")); // Output: HELLO

```

Functional interfaces are the foundation of Java's `java.util.function` package (`Function<T,R>`, `Predicate<T>`, `Consumer<T>`, `Supplier<T>`) and the entire Streams API. Every time you write a lambda in Java, you are implementing a functional interface.

## 4. Default Methods (Java 8+)

Default methods allow an interface to provide a method implementation directly, using the `default` keyword. Their primary purpose is to evolve an existing interface without breaking all the classes that already implement it.

Suppose you have a `Logger` interface used across dozens of classes in a codebase:

```java
public interface Logger {
    void log(String message);
}

```

A year later you want to add a convenience method `logError`. Without default methods, adding an abstract method to `Logger` would force every implementing class to add that method or fail to compile. With a default method, existing classes keep working unchanged:

```java
public interface Logger {
    void log(String message);

    // New method added without breaking existing implementations
    default void logError(String message) {
        log("[ERROR] " + message);
    }
}

```

Any existing class that implements `Logger` automatically inherits `logError` for free. A class that wants custom behavior can override it:

```java
public class FileLogger implements Logger {
    @Override
    public void log(String message) {
        System.out.println("FILE: " + message);
    }

    // Uses the default logError — no need to override
}

public class AlertLogger implements Logger {
    @Override
    public void log(String message) {
        System.out.println("ALERT: " + message);
    }

    @Override
    public void logError(String message) {
        System.out.println("CRITICAL ALERT: " + message.toUpperCase());
    }
}

```

```java
Logger file = new FileLogger();
Logger alert = new AlertLogger();

file.logError("Disk full");     // Output: FILE: [ERROR] Disk full
alert.logError("Disk full");    // Output: CRITICAL ALERT: DISK FULL

```

## 5. Static Methods in Interfaces

Interfaces can declare static methods. These are utility or factory methods that logically belong to the interface's concept but do not operate on an instance.

```java
public interface Color {
    int getRed();
    int getGreen();
    int getBlue();

    static Color of(int red, int green, int blue) {
        return new Color() {
            public int getRed()   { return red; }
            public int getGreen() { return green; }
            public int getBlue()  { return blue; }
        };
    }

    static Color fromHex(String hex) {
        int r = Integer.parseInt(hex.substring(1, 3), 16);
        int g = Integer.parseInt(hex.substring(3, 5), 16);
        int b = Integer.parseInt(hex.substring(5, 7), 16);
        return of(r, g, b);
    }
}

```

```java
Color red = Color.of(255, 0, 0);
Color blue = Color.fromHex("#0000FF");

System.out.println(red.getRed());    // Output: 255
System.out.println(blue.getBlue());  // Output: 255

```

Static methods in interfaces are not inherited by implementing classes. You call them directly on the interface name (`Color.of(...)`), not on an instance or subtype. This differs from static methods in abstract classes, which are inherited and can be called on subclass names. Interface static methods are strictly namespaced to the interface itself.

## 6. Private Methods (Java 9+)

When two or more default methods in an interface share logic, you can extract that shared logic into a private method. This avoids duplicating code while keeping the helper invisible to implementing classes.

```java
public interface AuditLogger {
    void logCreate(String entityName, long id);
    void logDelete(String entityName, long id);

    default void logCreate(String entityName, long id, String user) {
        writeAuditEntry("CREATE", entityName, id, user);
    }

    default void logDelete(String entityName, long id, String user) {
        writeAuditEntry("DELETE", entityName, id, user);
    }

    private void writeAuditEntry(String action, String entity, long id, String user) {
        String entry = String.format("[AUDIT] %s on %s#%d by %s", action, entity, id, user);
        System.out.println(entry);
    }
}

```

```java
public class DatabaseAuditLogger implements AuditLogger {
    @Override
    public void logCreate(String entityName, long id) {
        logCreate(entityName, id, "system");
    }

    @Override
    public void logDelete(String entityName, long id) {
        logDelete(entityName, id, "system");
    }
}

```

```java
AuditLogger logger = new DatabaseAuditLogger();
logger.logCreate("User", 42, "admin");
// Output: [AUDIT] CREATE on User#42 by admin
logger.logDelete("Order", 7, "admin");
// Output: [AUDIT] DELETE on Order#7 by admin

```

The private method `writeAuditEntry` is only visible inside the interface. Implementing classes cannot call or override it.

## 7. Interface Segregation

The Interface Segregation Principle states that a class should not be forced to implement methods it does not use. A large, catch-all interface creates unnecessary coupling and forces implementors to write empty or stub methods.

Consider a fat interface that tries to represent all office machine capabilities:

```java
// Bad: one interface for everything
public interface OfficeMachine {
    void print(String document);
    void scan(String fileName);
    void fax(String number, String document);
    void staple(int copies);
}

// A simple inkjet printer cannot fax or staple,
// but it is forced to implement those methods anyway
public class BasicPrinter implements OfficeMachine {
    @Override
    public void print(String document) {
        System.out.println("Printing: " + document);
    }

    @Override
    public void scan(String fileName) {
        throw new UnsupportedOperationException("Scanner not available");
    }

    @Override
    public void fax(String number, String document) {
        throw new UnsupportedOperationException("Fax not available");
    }

    @Override
    public void staple(int copies) {
        throw new UnsupportedOperationException("Stapler not available");
    }
}

```

The better design splits the fat interface into focused, single-purpose interfaces:

```java
// Good: each interface represents one capability
public interface Printer {
    void print(String document);
}

public interface Scanner {
    void scan(String fileName);
}

public interface FaxMachine {
    void fax(String number, String document);
}

public interface Stapler {
    void staple(int copies);
}

// A basic printer only implements what it actually supports
public class BasicPrinter implements Printer {
    @Override
    public void print(String document) {
        System.out.println("Printing: " + document);
    }
}

// An all-in-one machine implements everything it can do
public class AllInOnePrinter implements Printer, Scanner, FaxMachine, Stapler {
    @Override
    public void print(String document) {
        System.out.println("Printing: " + document);
    }

    @Override
    public void scan(String fileName) {
        System.out.println("Scanning to: " + fileName);
    }

    @Override
    public void fax(String number, String document) {
        System.out.println("Faxing to " + number + ": " + document);
    }

    @Override
    public void staple(int copies) {
        System.out.println("Stapling " + copies + " copies");
    }
}

```

Code that only needs to print accepts a `Printer`. Code that needs to scan accepts a `Scanner`. Neither caller is exposed to methods it does not use.

## 8. Marker Interfaces

A marker interface is an interface with no methods at all. It communicates a property or capability through the type system itself, not through any method signature.

```java
// From the Java standard library
public interface Serializable {
    // No methods
}

public interface Cloneable {
    // No methods
}

```

When a class implements `Serializable`, it is telling the JVM's object serialization mechanism: "You are allowed to convert instances of this class to a byte stream." The interface adds no behavior — it adds a type that can be checked at runtime with `instanceof` or by frameworks using reflection.

```java
public class UserProfile implements java.io.Serializable {
    private String username;
    private int age;

    public UserProfile(String username, int age) {
        this.username = username;
        this.age = age;
    }
}

```

```java
Object obj = new UserProfile("alice", 30);

if (obj instanceof java.io.Serializable) {
    System.out.println("This object can be serialized"); // Output: This object can be serialized
}

```

Marker interfaces are less common today because annotations (like `@Entity` in JPA) can serve the same purpose with more flexibility. However, they remain valuable when the type check needs to be performed at compile time, which an annotation alone cannot do.

## 9. Commonly Used Built-in Interfaces

Java's standard library defines many interfaces that unlock language features or framework integration.

### Comparable\<T\>

Defines a class's natural ordering. Implementing it allows objects to be sorted by `Collections.sort()` and `Arrays.sort()` without any additional configuration.

```java
public class Student implements Comparable<Student> {
    private String name;
    private double gpa;

    public Student(String name, double gpa) {
        this.name = name;
        this.gpa = gpa;
    }

    @Override
    public int compareTo(Student other) {
        // Negative: this comes before other
        // Zero: equal
        // Positive: this comes after other
        return Double.compare(other.gpa, this.gpa); // Descending by GPA
    }

    @Override
    public String toString() {
        return name + " (" + gpa + ")";
    }
}

```

```java
List<Student> students = new ArrayList<>();
students.add(new Student("Carol", 3.5));
students.add(new Student("Alice", 3.9));
students.add(new Student("Bob", 3.7));

Collections.sort(students);
System.out.println(students);
// Output: [Alice (3.9), Bob (3.7), Carol (3.5)]

```

### Comparator\<T\>

Defines an external ordering strategy that is separate from the class itself. Use `Comparator` when you need multiple different orderings, or when you cannot modify the class you are sorting.

```java
public class StudentNameComparator implements Comparator<Student> {
    @Override
    public int compare(Student a, Student b) {
        return a.getName().compareTo(b.getName());
    }
}

```

```java
List<Student> students = new ArrayList<>();
students.add(new Student("Carol", 3.5));
students.add(new Student("Alice", 3.9));
students.add(new Student("Bob", 3.7));

students.sort(new StudentNameComparator());
System.out.println(students);
// Output: [Alice (3.9), Bob (3.7), Carol (3.5)]  <- sorted by name A-Z

```

### Iterable\<T\>

Implementing `Iterable<T>` allows your custom class to work in a for-each loop. You must implement the `iterator()` method, which returns an `Iterator<T>`.

```java
public class NumberRange implements Iterable<Integer> {
    private final int start;
    private final int end;

    public NumberRange(int start, int end) {
        this.start = start;
        this.end = end;
    }

    @Override
    public java.util.Iterator<Integer> iterator() {
        return new java.util.Iterator<Integer>() {
            int current = start;

            public boolean hasNext() { return current <= end; }
            public Integer next()    { return current++; }
        };
    }
}

```

```java
for (int n : new NumberRange(1, 5)) {
    System.out.print(n + " ");
}
// Output: 1 2 3 4 5

```

### AutoCloseable

Implementing `AutoCloseable` allows objects to be used in a try-with-resources block. The `close()` method is called automatically when the block exits, even if an exception is thrown.

```java
public class DatabaseConnection implements AutoCloseable {
    private final String url;

    public DatabaseConnection(String url) {
        this.url = url;
        System.out.println("Connection opened: " + url);
    }

    public void query(String sql) {
        System.out.println("Executing: " + sql);
    }

    @Override
    public void close() {
        System.out.println("Connection closed: " + url);
    }
}

```

```java
try (DatabaseConnection conn = new DatabaseConnection("jdbc:mysql://localhost/mydb")) {
    conn.query("SELECT * FROM users");
}
// Output:
// Connection opened: jdbc:mysql://localhost/mydb
// Executing: SELECT * FROM users
// Connection closed: jdbc:mysql://localhost/mydb

```

The connection is closed automatically at the end of the try block, with no explicit call needed.

## 10. Interface vs Abstract Class

| Feature              | Interface                                       | Abstract Class                             |
|----------------------|-------------------------------------------------|--------------------------------------------|
| Instantiation        | Cannot be instantiated                          | Cannot be instantiated                     |
| Fields               | Only `public static final` constants            | Any access modifier, instance state allowed |
| Constructors         | Not allowed                                     | Allowed, called by subclasses via `super()` |
| Abstract methods     | All methods abstract by default (pre-Java 8)    | Explicitly declared with `abstract`        |
| Concrete methods     | Via `default` keyword (Java 8+)                 | Any regular method                         |
| Inheritance          | A class can implement many interfaces           | A class can extend only one abstract class |
| Access modifiers     | Methods implicitly `public`                     | Methods can be any access level            |
| Private methods      | Allowed as helpers for default methods (Java 9+)| Always allowed                             |
| Use case             | Define a capability shared across unrelated types | Share state and behavior among related types |

When to choose an interface:

- You are defining a capability or role (`Printable`, `Serializable`, `Payable`) rather than a type hierarchy
- Unrelated classes need to fulfill the same contract
- You need a class to fulfill multiple contracts simultaneously
- You are designing a public API that others will implement

When to choose an abstract class:

- Subclasses share common state (instance fields) that would be duplicated otherwise
- You want to enforce a template structure with some steps already implemented
- The relationship is clearly "is-a" and a single hierarchy makes sense
- You need a constructor to initialize shared state

## 11. Complete Example

This example builds a small payment processing system using multiple interfaces and polymorphic processing.

```java
public interface Payable {
    void processPayment(double amount);
    String getPaymentMethod();
}

```

```java
public interface Refundable {
    void processRefund(double amount);
}

```

```java
public class CreditCardPayment implements Payable, Refundable {
    private final String cardNumber;
    private double balance;

    public CreditCardPayment(String cardNumber, double initialBalance) {
        this.cardNumber = cardNumber;
        this.balance = initialBalance;
    }

    @Override
    public void processPayment(double amount) {
        balance -= amount;
        System.out.println("Credit card " + cardNumber + ": charged $" + amount
                + " | Remaining balance: $" + balance);
    }

    @Override
    public String getPaymentMethod() {
        return "Credit Card (" + cardNumber + ")";
    }

    @Override
    public void processRefund(double amount) {
        balance += amount;
        System.out.println("Credit card " + cardNumber + ": refunded $" + amount
                + " | New balance: $" + balance);
    }
}

```

```java
public class BankTransfer implements Payable {
    private final String accountNumber;

    public BankTransfer(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    @Override
    public void processPayment(double amount) {
        System.out.println("Bank transfer from account " + accountNumber
                + ": transferred $" + amount);
    }

    @Override
    public String getPaymentMethod() {
        return "Bank Transfer (" + accountNumber + ")";
    }
}

```

```java
public class PaymentProcessor {
    public void processAll(Payable[] payments, double amount) {
        for (Payable payment : payments) {
            System.out.println("Processing via: " + payment.getPaymentMethod());
            payment.processPayment(amount);

            // Only attempt refunds on payment methods that support it
            if (payment instanceof Refundable) {
                Refundable refundable = (Refundable) payment;
                System.out.println("This payment method supports refunds. Issuing partial refund.");
                refundable.processRefund(amount * 0.1);
            }

            System.out.println("---");
        }
    }
}

```

```java
public class Main {
    public static void main(String[] args) {
        Payable[] payments = {
            new CreditCardPayment("4111-1111-1111-1111", 1000.00),
            new BankTransfer("ACC-789456"),
            new CreditCardPayment("5500-0000-0000-0004", 500.00)
        };

        PaymentProcessor processor = new PaymentProcessor();
        processor.processAll(payments, 150.00);
    }
}

```

```java
// Output:
// Processing via: Credit Card (4111-1111-1111-1111)
// Credit card 4111-1111-1111-1111: charged $150.0 | Remaining balance: $850.0
// This payment method supports refunds. Issuing partial refund.
// Credit card 4111-1111-1111-1111: refunded $15.0 | New balance: $865.0
// ---
// Processing via: Bank Transfer (ACC-789456)
// Bank transfer from account ACC-789456: transferred $150.0
// ---
// Processing via: Credit Card (5500-0000-0000-0004)
// Credit card 5500-0000-0000-0004: charged $150.0 | Remaining balance: $350.0
// This payment method supports refunds. Issuing partial refund.
// Credit card 5500-0000-0000-0004: refunded $15.0 | New balance: $365.0
// ---

```

`PaymentProcessor` knows nothing about credit cards or bank transfers. It only works with `Payable`. The `instanceof` check for `Refundable` is a deliberate design decision: it lets the processor take advantage of an optional capability without requiring every payment method to support it.

## 12. Key Takeaways

- An interface is a compile-time enforced contract: every declared method must be implemented or the code does not compile
- Program to interfaces, not implementations: declare variables and parameters as the interface type so implementations can be swapped freely
- A functional interface has exactly one abstract method and can be implemented with a lambda expression; annotate it with `@FunctionalInterface` to make the constraint explicit
- Default methods allow interfaces to evolve — new methods can be added without breaking existing implementors
- Static methods in interfaces are utility methods scoped to the interface name and are not inherited
- Private methods in interfaces (Java 9+) let you eliminate code duplication inside default methods
- Follow the Interface Segregation Principle: many small, focused interfaces are better than one large interface
- Marker interfaces communicate a type-level property that can be checked with `instanceof` or reflection, even though they carry no method signatures
- `Comparable<T>` defines natural ordering; `Comparator<T>` defines an external ordering strategy; `Iterable<T>` enables for-each; `AutoCloseable` enables try-with-resources
- Prefer an interface when defining a capability; prefer an abstract class when sharing state and behavior among closely related types

---

Interfaces are the backbone of Spring Boot's dependency injection: every service, repository, and component you write as an interface lets Spring swap, mock, or decorate the implementation without touching any of the code that depends on it.

---

## OOP - EQUALS-HASHCODE

# equals() and hashCode()

Every Java class inherits two methods from `Object`: `equals()` and `hashCode()`. By default, `equals()` checks whether two variables point to the same object in memory, and `hashCode()` returns a number derived from the object's memory address. For many classes — particularly value-holding data classes — this default behaviour is wrong. This guide explains how to override them correctly and what happens when you do not.

---

## 1. The Problem: Default equals() Compares Identity, Not Value

When you create two `Point` objects with the same coordinates, the default `equals()` returns `false` because they are two different objects, even though they represent the same logical value.

```java
public class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

```

```java
Point p1 = new Point(3, 4);
Point p2 = new Point(3, 4);

System.out.println(p1 == p2);       // Output: false — different objects in memory
System.out.println(p1.equals(p2));  // Output: false — same result as == by default

```

This is the correct behaviour for some classes (like database connections or locks), but wrong for value objects like coordinates, money amounts, or user records, where equality should be based on field values.

---

## 2. Overriding equals() — the Five Properties

A correct `equals()` implementation must satisfy five properties defined in the Java specification. Violating any of them produces subtle, hard-to-diagnose bugs.

| Property | Meaning |
|---|---|
| Reflexive | `a.equals(a)` must be `true` |
| Symmetric | If `a.equals(b)` is `true`, then `b.equals(a)` must also be `true` |
| Transitive | If `a.equals(b)` and `b.equals(c)`, then `a.equals(c)` must be `true` |
| Consistent | Multiple calls to `a.equals(b)` return the same result (assuming no mutation) |
| Null-safe | `a.equals(null)` must return `false`, never throw |

The standard idiom for overriding `equals()`:

```java
import java.util.Objects;

public class Point {
    private final int x;
    private final int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        // 1. Reflexive: an object is always equal to itself.
        if (this == obj) return true;

        // 2. Null-safe and type check: null and wrong types are never equal.
        if (!(obj instanceof Point other)) return false;

        // 3. Compare all fields that define value equality.
        return this.x == other.x && this.y == other.y;
    }
}

```

```java
Point p1 = new Point(3, 4);
Point p2 = new Point(3, 4);
Point p3 = new Point(0, 0);

System.out.println(p1.equals(p2));    // Output: true
System.out.println(p1.equals(p3));    // Output: false
System.out.println(p1.equals(null));  // Output: false (null-safe)
System.out.println(p1.equals("xy"));  // Output: false (type-safe)

```

---

## 3. The equals/hashCode Contract

The Java specification states a strict contract:

> **If `a.equals(b)` is `true`, then `a.hashCode()` must equal `b.hashCode()`.**

The converse is not required: two objects can have the same hash code without being equal (this is called a hash collision and is expected). But the forward direction is absolute.

This contract is what makes `HashMap` and `HashSet` work. When you put an object into a `HashMap`, Java uses its hash code to find the right bucket, then uses `equals()` to find the exact key within that bucket. If equal objects have different hash codes, they will end up in different buckets and the map will never find one when you look up the other.

---

## 4. Overriding hashCode() — the Formula Pattern

The simplest correct approach is `Objects.hash(field1, field2, ...)`, which combines the hash codes of the listed fields in a well-distributed way.

```java
import java.util.Objects;

public class Point {
    private final int x;
    private final int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Point other)) return false;
        return this.x == other.x && this.y == other.y;
    }

    @Override
    public int hashCode() {
        // Objects.hash() calls hashCode() on each argument and combines the results.
        // Use the same fields as equals() — no more, no less.
        return Objects.hash(x, y);
    }
}

```

```java
Point p1 = new Point(3, 4);
Point p2 = new Point(3, 4);

System.out.println(p1.equals(p2));              // Output: true
System.out.println(p1.hashCode() == p2.hashCode()); // Output: true — contract satisfied

```

The rule is simple: **use the same set of fields in both `equals()` and `hashCode()`.**

---

## 5. Why Violating the Contract Breaks HashMap and HashSet

Here is a concrete demonstration of what goes wrong when `equals()` is overridden but `hashCode()` is not.

```java
// A Point class with equals() overridden but hashCode() NOT overridden.
// hashCode() still returns a memory-address-based value — different for each object.
public class BrokenPoint {
    int x;
    int y;

    public BrokenPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof BrokenPoint other)) return false;
        return this.x == other.x && this.y == other.y;
    }
    // hashCode() NOT overridden — still returns identity-based hash code.
}

```

```java
import java.util.HashSet;
import java.util.HashMap;

BrokenPoint a = new BrokenPoint(1, 2);
BrokenPoint b = new BrokenPoint(1, 2); // "equal" to a according to equals()

// HashSet stores objects by their hash code bucket.
HashSet<BrokenPoint> set = new HashSet<>();
set.add(a);

// a.equals(b) is true, so we expect the set to contain b.
System.out.println(set.contains(b)); // Output: false — contract violation!
// a and b have different hash codes, so the set looks in the wrong bucket.

// Same problem with HashMap.
HashMap<BrokenPoint, String> map = new HashMap<>();
map.put(a, "value");
System.out.println(map.get(b)); // Output: null — can never find the key!

```

The `HashSet` reports that it does not contain `b`, even though `b` is "equal" to the stored element `a`. The contract violation made the collection unreliable. This is one of the most common sources of subtle bugs in Java code.

---

## 6. Mutable Fields in equals/hashCode — the Danger

If a field used in `equals()` or `hashCode()` is mutable and you change it after the object has been added to a hash-based collection, the object ends up in the wrong bucket and the collection can never find it again.

```java
import java.util.HashSet;
import java.util.Objects;

public class MutablePoint {
    int x;
    int y;

    // Constructor, equals, hashCode using both fields...
    @Override public boolean equals(Object o) {
        if (!(o instanceof MutablePoint p)) return false;
        return x == p.x && y == p.y;
    }
    @Override public int hashCode() { return Objects.hash(x, y); }
}

```

```java
MutablePoint p = new MutablePoint();
p.x = 1; p.y = 2;

HashSet<MutablePoint> set = new HashSet<>();
set.add(p);

System.out.println(set.contains(p)); // Output: true — found in the correct bucket.

// Mutate a field that is part of the hash code.
p.x = 99;

// The set still holds p, but now p.hashCode() returns a different value.
// The set looks in the wrong bucket and cannot find the object it already holds.
System.out.println(set.contains(p)); // Output: false — the object is lost!

```

The standard advice: prefer immutable fields in classes that override `equals()` and `hashCode()`. If you must use mutable classes as map keys or set members, never mutate them while they are in the collection.

---

## 7. Records Automatically Generate Correct equals/hashCode

Java records (Java 16+) automatically generate `equals()`, `hashCode()`, and `toString()` based on all record components. The generated implementations are correct and satisfy the contract.

```java
record Point(int x, int y) {}

```

```java
Point p1 = new Point(3, 4);
Point p2 = new Point(3, 4);

System.out.println(p1.equals(p2));                  // Output: true
System.out.println(p1.hashCode() == p2.hashCode()); // Output: true
System.out.println(p1);                             // Output: Point[x=3, y=4]

```

For data classes with no custom logic, records are the preferred way to get correct `equals()` and `hashCode()` without writing any code.

---

## 8. IDE Generation vs Manual vs Objects.hash()

| Approach | Recommendation |
|---|---|
| IDE generation (`Generate > equals() and hashCode()`) | Good starting point; generates correct boilerplate |
| Manual implementation using `instanceof` pattern + `Objects.hash()` | Recommended for custom classes that cannot be records |
| `java.util.Objects.hash(fields...)` | Always use this for hashCode — do not implement the bit-shifting yourself |
| Records | Best for simple data classes — zero boilerplate, automatically correct |

---

## 9. Complete Example: Product in a HashSet and HashMap

```java
import java.util.HashMap;
import java.util.HashSet;
import java.util.Objects;

public class Product {
    private final String sku;
    private final String name;
    private double price; // Mutable — we deliberately do NOT include this in equals/hashCode.

    public Product(String sku, String name, double price) {
        this.sku   = sku;
        this.name  = name;
        this.price = price;
    }

    // Identity is based on SKU and name only.
    // Price is excluded because products are "the same product" regardless of price changes.
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof Product other)) return false;
        return Objects.equals(this.sku, other.sku)
            && Objects.equals(this.name, other.name);
    }

    @Override
    public int hashCode() {
        // Use the same fields as equals(). Objects.equals handles null safely.
        return Objects.hash(sku, name);
    }

    public void setPrice(double price) { this.price = price; }
    public double getPrice()           { return price; }
    public String getSku()             { return sku; }

    @Override
    public String toString() {
        return "Product{sku='" + sku + "', name='" + name + "', price=" + price + "}";
    }
}

```

```java
import java.util.HashMap;
import java.util.HashSet;

public class ProductDemo {
    public static void main(String[] args) {

        Product p1 = new Product("SKU-001", "Widget", 9.99);
        Product p2 = new Product("SKU-001", "Widget", 9.99); // Logically the same product.
        Product p3 = new Product("SKU-002", "Gadget", 24.99);

        // HashSet correctly deduplicates equal products.
        HashSet<Product> catalogue = new HashSet<>();
        catalogue.add(p1);
        catalogue.add(p2); // This is a duplicate — p1.equals(p2) is true.
        catalogue.add(p3);

        System.out.println("Catalogue size: " + catalogue.size()); // Output: 2 (not 3)
        System.out.println("Contains p2: " + catalogue.contains(p2)); // Output: true

        // HashMap correctly stores and retrieves by product key.
        HashMap<Product, Integer> stock = new HashMap<>();
        stock.put(p1, 100);
        stock.put(p3, 50);

        // Retrieve using p2 (a different object with the same SKU/name).
        // This works because p1.equals(p2) and p1.hashCode() == p2.hashCode().
        System.out.println("Stock for p2 (= p1): " + stock.get(p2)); // Output: 100

        // Price changes do not affect map lookup because price is not in equals/hashCode.
        p1.setPrice(12.99);
        System.out.println("Stock after price change: " + stock.get(p1)); // Output: 100
    }
}

```

---

## 10. Common Mistakes

### Using == inside a custom equals()
Using `==` to compare object fields compares references, not values. Use `Objects.equals(a, b)` for nullable fields (it handles null safely) or `.equals()` for non-nullable fields.

```java
// Wrong: compares String references — may fail even for equal strings.
return this.name == other.name;

// Correct: compares String contents, null-safe.
return Objects.equals(this.name, other.name);

```

### Including mutable fields in hashCode
If a field is included in `hashCode()` and its value changes, the object's hash code changes. Objects in hash-based collections with changed hash codes become permanently unreachable.

### Overriding equals() without overriding hashCode()
The most common mistake in this area. `equals()` and `hashCode()` must always be overridden together.

### Using a subset of fields in hashCode but all fields in equals
If `hashCode()` considers fewer fields than `equals()`, two objects that `equals()` considers different could still share a hash code. This is allowed (collisions are expected) but hurts performance. More importantly, the reverse (more fields in `hashCode()` than `equals()`) violates the contract.

---

## 11. Key Takeaways

- The default `equals()` compares identity (same object); override it for classes where value equality is meaningful
- A correct `equals()` must be reflexive, symmetric, transitive, consistent, and null-safe
- **If `a.equals(b)` then `a.hashCode() == b.hashCode()` — this contract is absolute and must not be violated**
- Always override `hashCode()` whenever you override `equals()` — use `Objects.hash(fields...)` for the implementation
- Use the same set of fields in both `equals()` and `hashCode()`
- Mutable fields in `equals()`/`hashCode()` are dangerous when objects are used as map keys or set members
- Records automatically provide correct `equals()`, `hashCode()`, and `toString()` — prefer records for simple data classes

---

Correct `equals()` and `hashCode()` are the foundation of reliable `HashMap` and `HashSet` usage, which are the two most commonly used data structures in enterprise Java applications. Getting them right once is far easier than debugging the subtle failures that occur when they are wrong.

---

## COLLECTIONS - COLLECTIONS

# The Collections Framework

The Collections Framework is a unified architecture for storing, retrieving, and manipulating groups of objects in Java. It replaces the need for hand-rolled data structures by providing a set of well-tested interfaces and implementations that cover almost every data management scenario you will encounter. Understanding it is essential because real applications are rarely about single variables — they are about managing collections of data efficiently.

```

Think of it like this:
  You have a list of students, a set of unique cities, and a lookup table of IDs.
  Arrays could technically hold all of this, but they fight you every step of the way.
  The Collections Framework gives you the right tool for each job,
  all sharing the same familiar interface so you only need to learn the pattern once.

```

## 1. The Collections Framework Overview

The framework is built around a hierarchy of interfaces. Each interface defines a contract, and multiple classes implement each contract with different performance trade-offs.

```

Iterable
└── Collection
    ├── List  (ordered, allows duplicates)
    ├── Set   (no duplicates)
    └── Queue (FIFO ordering)
Map (key-value pairs, not a Collection)

```

Arrays fall short in several important ways:

- **Fixed size.** Once created, an array cannot grow or shrink. Adding a new element requires creating a new array and copying everything over.
- **No built-in search or sort methods.** You must write them yourself or call a separate utility class.
- **No remove operation.** Removing an element from the middle of an array means manually shifting every element after it.
- **No type-safe key-value storage.** There is no array equivalent of a dictionary or map.

The Collections Framework solves all of these problems with clean, generic interfaces.

## 2. List — ArrayList

`ArrayList` is the most commonly used collection in Java. It is a resizable array under the hood: it allocates a backing array and doubles its capacity automatically when that array fills up.

**Declaration — program to the interface, not the implementation:**

```java
List<String> cities = new ArrayList<>();

```

By declaring the variable as `List<String>` instead of `ArrayList<String>`, you can swap the implementation later without changing any other code.

**Core operations:**

```java
List<String> cities = new ArrayList<>();

// Adding elements
cities.add("Austin");           // appends to the end
cities.add("Boston");
cities.add("Chicago");
cities.add(1, "Denver");        // inserts at index 1, shifts others right

System.out.println(cities);
// Output: [Austin, Denver, Boston, Chicago]

// Reading elements
System.out.println(cities.get(0));      // Output: Austin
System.out.println(cities.size());      // Output: 4
System.out.println(cities.isEmpty());   // Output: false
System.out.println(cities.contains("Boston")); // Output: true

// Updating elements
cities.set(2, "Baltimore");
System.out.println(cities.get(2));      // Output: Baltimore

// Removing elements
cities.remove(0);               // removes by index
cities.remove("Denver");        // removes by object value
System.out.println(cities);
// Output: [Baltimore, Chicago]

```

**Iterating an ArrayList:**

```java
List<String> names = new ArrayList<>();
names.add("Alice");
names.add("Bob");
names.add("Carol");

// For-each loop (preferred when you do not need the index)
for (String name : names) {
    System.out.println(name);
}
// Output:
// Alice
// Bob
// Carol

// Traditional for loop (use when you need the index)
for (int i = 0; i < names.size(); i++) {
    System.out.println(i + ": " + names.get(i));
}
// Output:
// 0: Alice
// 1: Bob
// 2: Carol

```

**When to use ArrayList:** When you need fast random access by index, when reads far outnumber writes, or when you simply need an ordered list with duplicates allowed.

## 3. List — LinkedList

`LinkedList` implements the same `List` interface, but internally it stores each element in a separate node that holds a reference to the next and previous node. There is no backing array.

```java
LinkedList<String> tasks = new LinkedList<>();

tasks.add("Write tests");
tasks.add("Review PR");
tasks.add("Deploy");

// LinkedList-specific methods for working at the ends
tasks.addFirst("Plan sprint");      // inserts at the front
tasks.addLast("Send report");       // inserts at the back

System.out.println(tasks.peekFirst()); // Output: Plan sprint  (does not remove)
System.out.println(tasks.peekLast());  // Output: Send report  (does not remove)

tasks.removeFirst();  // removes and returns "Plan sprint"
tasks.removeLast();   // removes and returns "Send report"

System.out.println(tasks);
// Output: [Write tests, Review PR, Deploy]

```

**ArrayList vs LinkedList — a quick comparison:**

| Operation              | ArrayList                  | LinkedList                  |
|------------------------|----------------------------|-----------------------------|
| Access by index        | O(1) — fast                | O(n) — must walk the chain  |
| Insert / remove at end | O(1) amortized             | O(1)                        |
| Insert / remove middle | O(n) — must shift elements | O(n) — must walk to position|
| Memory per element     | Lower (packed array)       | Higher (node + two pointers)|

**When to use LinkedList:** When you frequently add or remove elements at the front or back of the list, such as implementing a queue or a double-ended task buffer. For almost everything else, `ArrayList` is the better default.

## 4. Set — HashSet

A `Set` is a collection that never contains duplicate elements. `HashSet` is the most common implementation. It stores elements in a hash table, which gives it very fast add, remove, and lookup operations, but it provides no guarantee about the order of iteration.

```java
Set<String> tags = new HashSet<>();

tags.add("java");
tags.add("programming");
tags.add("java");       // duplicate — silently ignored
tags.add("backend");

System.out.println(tags.size());            // Output: 3  (not 4)
System.out.println(tags.contains("java"));  // Output: true

tags.remove("backend");
System.out.println(tags);
// Output: [programming, java]  (order is not guaranteed)

```

**Eliminating duplicates from a List:**

```java
List<String> withDuplicates = new ArrayList<>();
withDuplicates.add("red");
withDuplicates.add("blue");
withDuplicates.add("red");
withDuplicates.add("green");
withDuplicates.add("blue");

Set<String> unique = new HashSet<>(withDuplicates);
System.out.println(unique);
// Output: [red, green, blue]  (order may vary)

```

**When to use HashSet:** When all you need to know is whether something is in a group (membership testing), and order does not matter. It is the fastest `Set` implementation.

## 5. Set — LinkedHashSet and TreeSet

When you need a `Set` with a predictable order, Java provides two alternatives.

**LinkedHashSet** maintains elements in the order they were inserted, without allowing duplicates.

**TreeSet** keeps elements sorted in their natural order (or by a `Comparator` you provide). It implements `NavigableSet`, which adds methods for range queries.

```java
List<String> input = Arrays.asList("banana", "apple", "cherry", "apple", "date");

// HashSet: no duplicates, unpredictable order
Set<String> hashSet = new HashSet<>(input);

// LinkedHashSet: no duplicates, insertion order preserved
Set<String> linkedHashSet = new LinkedHashSet<>(input);

// TreeSet: no duplicates, sorted alphabetically
Set<String> treeSet = new TreeSet<>(input);

System.out.println("HashSet:       " + hashSet);
// Output: HashSet:       [banana, cherry, apple, date]  (order varies)

System.out.println("LinkedHashSet: " + linkedHashSet);
// Output: LinkedHashSet: [banana, apple, cherry, date]

System.out.println("TreeSet:       " + treeSet);
// Output: TreeSet:       [apple, banana, cherry, date]

```

**TreeSet range operations:**

```java
TreeSet<String> fruits = new TreeSet<>();
fruits.add("apple");
fruits.add("banana");
fruits.add("cherry");
fruits.add("date");
fruits.add("elderberry");

System.out.println(fruits.first());              // Output: apple
System.out.println(fruits.last());               // Output: elderberry
System.out.println(fruits.headSet("cherry"));    // Output: [apple, banana]  (exclusive)
System.out.println(fruits.tailSet("cherry"));    // Output: [cherry, date, elderberry]  (inclusive)

```

## 6. Map — HashMap

A `Map` stores key-value pairs. Every key is unique, and each key maps to exactly one value. `HashMap` is the most common implementation, using a hash table for O(1) average-case lookups.

**Declaration:**

```java
Map<String, Integer> scores = new HashMap<>();

```

**Core operations:**

```java
Map<String, Integer> scores = new HashMap<>();

// Adding and updating entries
scores.put("Alice", 92);
scores.put("Bob", 85);
scores.put("Carol", 90);
scores.put("Alice", 95);    // overwrites the previous value for "Alice"

// Reading values
System.out.println(scores.get("Bob"));          // Output: 85
System.out.println(scores.get("Dave"));         // Output: null  (key does not exist)
System.out.println(scores.getOrDefault("Dave", 0)); // Output: 0

// Checking membership
System.out.println(scores.containsKey("Carol"));    // Output: true
System.out.println(scores.containsValue(85));        // Output: true

// Conditional insertion
scores.putIfAbsent("Bob", 99);   // ignored because "Bob" already exists
System.out.println(scores.get("Bob")); // Output: 85

// Removing an entry
scores.remove("Carol");
System.out.println(scores.size()); // Output: 2

```

**Iterating a Map:**

```java
Map<String, Integer> scores = new HashMap<>();
scores.put("Alice", 95);
scores.put("Bob", 85);
scores.put("Carol", 90);

// Iterate over keys only
for (String name : scores.keySet()) {
    System.out.println(name);
}

// Iterate over values only
for (int score : scores.values()) {
    System.out.println(score);
}

// Iterate over key-value pairs (most common)
for (Map.Entry<String, Integer> entry : scores.entrySet()) {
    System.out.println(entry.getKey() + " -> " + entry.getValue());
}
// Output (order may vary):
// Alice -> 95
// Bob -> 85
// Carol -> 90

```

**When to use HashMap:** Any time you need to look up a value by a known key in constant time — configuration tables, caches, frequency counters, index structures.

## 7. Map — LinkedHashMap and TreeMap

Just like with sets, Java provides ordered map implementations when insertion order or sorted order matters.

**LinkedHashMap** preserves the order in which entries were inserted.

**TreeMap** keeps entries sorted by key in natural order (or by a supplied `Comparator`).

**Building a word-frequency counter, then printing alphabetically:**

```java
String[] words = {"banana", "apple", "cherry", "apple", "banana", "apple"};

// Count frequencies with HashMap (fast, unordered)
Map<String, Integer> frequency = new HashMap<>();
for (String word : words) {
    frequency.put(word, frequency.getOrDefault(word, 0) + 1);
}

System.out.println("HashMap (unordered): " + frequency);
// Output: HashMap (unordered): {banana=2, cherry=1, apple=3}  (order varies)

// Print alphabetically by passing the HashMap into a TreeMap
Map<String, Integer> sorted = new TreeMap<>(frequency);
System.out.println("TreeMap (sorted):    " + sorted);
// Output: TreeMap (sorted):    {apple=3, banana=2, cherry=1}

```

**LinkedHashMap preserving insertion order:**

```java
Map<String, String> config = new LinkedHashMap<>();
config.put("host", "localhost");
config.put("port", "8080");
config.put("timeout", "30");

for (Map.Entry<String, String> entry : config.entrySet()) {
    System.out.println(entry.getKey() + " = " + entry.getValue());
}
// Output:
// host = localhost
// port = 8080
// timeout = 30

```

## 8. Queue and Deque — ArrayDeque

A `Queue` processes elements in FIFO (first-in, first-out) order. A `Deque` (double-ended queue) supports insertion and removal at both ends, which means it can serve as both a queue and a stack.

`ArrayDeque` is the recommended implementation for both. It is backed by a resizable array and is generally faster than `LinkedList` for queue and stack operations.

**Queue interface method pairs:**

| Action  | Throws exception | Returns null/false |
|---------|------------------|--------------------|
| Insert  | `add(e)`         | `offer(e)`         |
| Remove  | `remove()`       | `poll()`           |
| Examine | `element()`      | `peek()`           |

Prefer the safe variants (`offer`, `poll`, `peek`) to avoid unchecked exceptions on empty collections.

**ArrayDeque as a queue (FIFO):**

```java
Deque<String> queue = new ArrayDeque<>();

queue.offer("first");
queue.offer("second");
queue.offer("third");

System.out.println(queue.peek());   // Output: first  (does not remove)
System.out.println(queue.poll());   // Output: first  (removes it)
System.out.println(queue.poll());   // Output: second
System.out.println(queue);
// Output: [third]

```

**ArrayDeque as a stack (LIFO):**

```java
Deque<String> stack = new ArrayDeque<>();

stack.push("page1");    // same as addFirst
stack.push("page2");
stack.push("page3");

System.out.println(stack.peek());   // Output: page3  (top of stack, not removed)
System.out.println(stack.pop());    // Output: page3  (removes from top)
System.out.println(stack.pop());    // Output: page2
System.out.println(stack);
// Output: [page1]

```

**When to use ArrayDeque:** Any time you need to process items in arrival order (task queues, BFS traversal), or when you need an undo/redo stack. Prefer it over the legacy `Stack` class, which is synchronized and slower.

## 9. Choosing the Right Collection

| Need                                               | Use            |
|----------------------------------------------------|----------------|
| Ordered list, duplicates allowed, fast random access | ArrayList      |
| Ordered list, fast insert/remove at ends           | LinkedList     |
| No duplicates, fast lookup, no order needed        | HashSet        |
| No duplicates, insertion order preserved           | LinkedHashSet  |
| No duplicates, sorted order                        | TreeSet        |
| Key-value lookup, no order needed                  | HashMap        |
| Key-value, insertion order preserved               | LinkedHashMap  |
| Key-value, sorted by key                           | TreeMap        |
| FIFO queue or LIFO stack                           | ArrayDeque     |

## 10. The Collections Utility Class

`java.util.Collections` (note the plural) is a utility class containing only static methods that operate on collections. It is distinct from the `Collection` interface.

```java
List<Integer> numbers = new ArrayList<>(Arrays.asList(5, 2, 8, 1, 9, 3));

// Sort ascending (natural order)
Collections.sort(numbers);
System.out.println(numbers);
// Output: [1, 2, 3, 5, 8, 9]

// Reverse the order
Collections.reverse(numbers);
System.out.println(numbers);
// Output: [9, 8, 5, 3, 2, 1]

// Shuffle randomly
Collections.shuffle(numbers);
System.out.println(numbers);
// Output: [3, 9, 1, 8, 5, 2]  (order varies)

// Find min and max
Collections.sort(numbers); // sort first for clarity
System.out.println(Collections.min(numbers)); // Output: 1
System.out.println(Collections.max(numbers)); // Output: 9

// Count occurrences of an element
List<String> colors = Arrays.asList("red", "blue", "red", "green", "red");
System.out.println(Collections.frequency(colors, "red")); // Output: 3

// Create a read-only view of a list
List<String> mutable = new ArrayList<>(Arrays.asList("a", "b", "c"));
List<String> readOnly = Collections.unmodifiableList(mutable);
// readOnly.add("d"); // throws UnsupportedOperationException at runtime
System.out.println(readOnly); // Output: [a, b, c]

```

## 11. Complete Example

This example builds a simple student registry using three collections together, each chosen for a different purpose.

**The Student class:**

```java
public class Student {
    private String id;
    private String name;
    private String city;

    public Student(String id, String name, String city) {
        this.id = id;
        this.name = name;
        this.city = city;
    }

    public String getId()   { return id; }
    public String getName() { return name; }
    public String getCity() { return city; }

    @Override
    public String toString() {
        return name + " (" + id + ") from " + city;
    }
}

```

**The StudentRegistry class:**

```java
import java.util.*;

public class StudentRegistry {

    // Ordered list — preserves enrollment order, allows iterating all students
    private List<Student> enrollmentList = new ArrayList<>();

    // Set of unique cities — automatically deduplicates
    private Set<String> cities = new HashSet<>();

    // Map for fast ID lookup — O(1) access by student ID
    private Map<String, Student> idIndex = new HashMap<>();

    public void enroll(Student student) {
        enrollmentList.add(student);
        cities.add(student.getCity());
        idIndex.put(student.getId(), student);
    }

    public void remove(String id) {
        Student student = idIndex.remove(id);
        if (student != null) {
            enrollmentList.remove(student);
            // Rebuild city set after removal to ensure accuracy
            cities.clear();
            for (Student s : enrollmentList) {
                cities.add(s.getCity());
            }
            System.out.println("Removed: " + student.getName());
        } else {
            System.out.println("Student not found: " + id);
        }
    }

    public Student findById(String id) {
        return idIndex.getOrDefault(id, null);
    }

    public void printAll() {
        System.out.println("--- All Students (enrollment order) ---");
        for (Student s : enrollmentList) {
            System.out.println("  " + s);
        }
    }

    public void printStats() {
        System.out.println("--- Registry Stats ---");
        System.out.println("Total students : " + enrollmentList.size());
        System.out.println("Unique cities  : " + cities.size());
        System.out.println("Cities         : " + new TreeSet<>(cities)); // sorted for display
    }

    public static void main(String[] args) {
        StudentRegistry registry = new StudentRegistry();

        // Populate from a common data source
        registry.enroll(new Student("S001", "Alice",   "Austin"));
        registry.enroll(new Student("S002", "Bob",     "Boston"));
        registry.enroll(new Student("S003", "Carol",   "Austin"));   // same city as Alice
        registry.enroll(new Student("S004", "Dave",    "Chicago"));
        registry.enroll(new Student("S005", "Eve",     "Boston"));   // same city as Bob

        registry.printAll();
        // Output:
        // --- All Students (enrollment order) ---
        //   Alice (S001) from Austin
        //   Bob (S002) from Boston
        //   Carol (S003) from Austin
        //   Dave (S004) from Chicago
        //   Eve (S005) from Boston

        registry.printStats();
        // Output:
        // --- Registry Stats ---
        // Total students : 5
        // Unique cities  : 3
        // Cities         : [Austin, Boston, Chicago]

        // Fast lookup by ID
        Student found = registry.findById("S003");
        System.out.println("Found: " + found);
        // Output: Found: Carol (S003) from Austin

        // Lookup of a non-existent ID
        System.out.println("Found: " + registry.findById("S999"));
        // Output: Found: null

        // Remove a student and verify stats update
        registry.remove("S002");
        // Output: Removed: Bob

        registry.printStats();
        // Output:
        // --- Registry Stats ---
        // Total students : 4
        // Unique cities  : 3   (Boston still has Eve)
        // Cities         : [Austin, Boston, Chicago]
    }
}

```

## 12. Key Takeaways

- The Collections Framework provides a unified set of interfaces (`List`, `Set`, `Queue`, `Map`) and multiple implementations for each, letting you choose the right trade-off for your use case.
- Always declare collection variables using the interface type (`List`, `Set`, `Map`) rather than the concrete class to keep code flexible.
- `ArrayList` is the default general-purpose list; reach for `LinkedList` only when you have frequent insertions or removals at the ends.
- `HashSet` offers the fastest membership testing; use `LinkedHashSet` to preserve insertion order and `TreeSet` for sorted order.
- `HashMap` is the default map; `LinkedHashMap` preserves insertion order and `TreeMap` sorts by key.
- `ArrayDeque` is the recommended implementation for both queues and stacks; prefer `offer`/`poll`/`peek` over the exception-throwing variants.
- The `Collections` utility class provides ready-made algorithms — sort, reverse, shuffle, min, max, frequency, and unmodifiable wrappers — so you rarely need to write them yourself.
- Mixing collection types in a single class (as in the student registry) is common and expected: use each type where its strengths apply.

---

The Collections Framework is the backbone of nearly every real Java application — once you internalize which collection fits which problem, you will spend less time fighting your data structures and more time solving the actual problem at hand.

---

## COLLECTIONS - COMPARATOR

# Comparator and Comparable

Sorting is one of the most common operations in any application. Java provides two interfaces for defining order: `Comparable` for an object's natural order and `Comparator` for any alternative ordering you need on the fly. Understanding both — and knowing when to use each — is essential for writing clean, flexible code.

---

## 1. The Two Interfaces at a Glance

```

Think of it like this:
  Comparable is like a person's name — it defines the one natural way to order the object.
  Comparator is like a sorting rule you hand to a filing clerk — it defines an ordering
  for a specific situation without changing the object itself.
  You can have one natural order (Comparable) and as many Comparators as you need.

```

| | `Comparable<T>` | `Comparator<T>` |
|---|---|---|
| Lives in | The class being sorted | A separate object or lambda |
| Method | `compareTo(T other)` | `compare(T a, T b)` |
| Number of orderings | One (the natural order) | Unlimited |
| Used by | `Collections.sort(list)`, `TreeSet`, `TreeMap` (no arg) | `Collections.sort(list, comparator)`, `list.sort(comparator)` |

---

## 2. Comparable — Natural Ordering

Implement `Comparable<T>` when the class has one obvious, canonical ordering that applies everywhere.

`compareTo` must return:
- A **negative** integer if `this` is less than `other`.
- **Zero** if `this` equals `other`.
- A **positive** integer if `this` is greater than `other`.

```java
public class Student implements Comparable<Student> {
    private final String name;
    private final double gpa;
    private final int    graduationYear;

    public Student(String name, double gpa, int graduationYear) {
        this.name           = name;
        this.gpa            = gpa;
        this.graduationYear = graduationYear;
    }

    // Natural order: alphabetical by name.
    @Override
    public int compareTo(Student other) {
        return this.name.compareTo(other.name);
    }

    @Override
    public String toString() {
        return name + " (GPA: " + gpa + ", Year: " + graduationYear + ")";
    }

    public String getName()        { return name; }
    public double getGpa()         { return gpa; }
    public int    getGraduationYear() { return graduationYear; }
}

```

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

List<Student> students = new ArrayList<>(List.of(
    new Student("Charlie", 3.5, 2025),
    new Student("Alice",   3.8, 2024),
    new Student("Bob",     3.2, 2026)
));

// Collections.sort uses compareTo — the natural order defined by Comparable.
Collections.sort(students);

for (Student s : students) {
    System.out.println(s);
}
// Output:
// Alice (GPA: 3.8, Year: 2024)
// Bob (GPA: 3.2, Year: 2026)
// Charlie (GPA: 3.5, Year: 2025)

```

### Integer.compare() and Double.compare()

Never compute the difference of two numbers to implement `compareTo`. For integers, the subtraction can overflow if the values are extreme. Use the static compare methods instead.

```java
// Wrong: integer subtraction overflows for large negative values.
// return this.graduationYear - other.graduationYear;

// Correct: Integer.compare handles all values safely.
// return Integer.compare(this.graduationYear, other.graduationYear);

// Correct: Double.compare handles NaN and -0.0 correctly.
// return Double.compare(this.gpa, other.gpa);

```

---

## 3. Comparator — Custom Ordering

`Comparator<T>` defines an ordering without modifying the class. Use it when:
- The class does not implement `Comparable`.
- You need an ordering different from the natural order.
- You need multiple different orderings.

### Classic anonymous-class style (pre-Java 8)

```java
import java.util.Comparator;

Comparator<Student> byGpa = new Comparator<Student>() {
    @Override
    public int compare(Student a, Student b) {
        return Double.compare(b.getGpa(), a.getGpa()); // Descending: higher GPA first.
    }
};

students.sort(byGpa);

```

### Lambda style (Java 8+)

A `Comparator` is a functional interface — it has one abstract method (`compare`). Use a lambda.

```java
// Ascending by GPA.
students.sort((a, b) -> Double.compare(a.getGpa(), b.getGpa()));

// Descending by GPA (swap a and b).
students.sort((a, b) -> Double.compare(b.getGpa(), a.getGpa()));

// Ascending by graduation year.
students.sort((a, b) -> Integer.compare(a.getGraduationYear(), b.getGraduationYear()));

```

---

## 4. Comparator Factory Methods (Java 8+)

`Comparator` provides static and default methods that build comparators cleanly without explicit lambda logic.

### Comparator.comparing()

`Comparator.comparing(keyExtractor)` takes a method reference that extracts the sort key. It handles null-safety and consistent comparison automatically.

```java
import java.util.Comparator;

// Sort by name using a method reference — cleaner than a lambda.
Comparator<Student> byName = Comparator.comparing(Student::getName);
students.sort(byName);

// Sort by GPA in ascending order.
Comparator<Student> byGpa = Comparator.comparingDouble(Student::getGpa);
students.sort(byGpa);

// Sort by graduation year.
Comparator<Student> byYear = Comparator.comparingInt(Student::getGraduationYear);
students.sort(byYear);

```

### reversed()

`.reversed()` flips an existing comparator.

```java
// Descending by GPA (highest first).
Comparator<Student> byGpaDesc = Comparator.comparingDouble(Student::getGpa).reversed();
students.sort(byGpaDesc);

for (Student s : students) {
    System.out.println(s);
}
// Output (example, starting with highest GPA):
// Alice (GPA: 3.8, Year: 2024)
// Charlie (GPA: 3.5, Year: 2025)
// Bob (GPA: 3.2, Year: 2026)

```

### thenComparing() — multi-level sort

Chain `.thenComparing()` to sort by a secondary key when the primary keys are equal.

```java
// Primary: ascending graduation year.
// Secondary (tie-break): descending GPA.
Comparator<Student> byYearThenGpa = Comparator
        .comparingInt(Student::getGraduationYear)
        .thenComparing(Comparator.comparingDouble(Student::getGpa).reversed());

students.sort(byYearThenGpa);

for (Student s : students) {
    System.out.println(s);
}
// Output (sorted by year, then highest GPA first within each year):
// Alice (GPA: 3.8, Year: 2024)
// Charlie (GPA: 3.5, Year: 2025)
// Bob (GPA: 3.2, Year: 2026)

```

### Comparator.naturalOrder() and Comparator.reverseOrder()

```java
// naturalOrder() uses the class's compareTo method.
List<String> names = new ArrayList<>(List.of("Charlie", "Alice", "Bob"));
names.sort(Comparator.naturalOrder());
System.out.println(names); // Output: [Alice, Bob, Charlie]

// reverseOrder() is the reverse of natural order.
names.sort(Comparator.reverseOrder());
System.out.println(names); // Output: [Charlie, Bob, Alice]

```

### nullsFirst() and nullsLast()

```java
List<String> withNulls = new ArrayList<>(List.of("Charlie", null, "Alice", null, "Bob"));

withNulls.sort(Comparator.nullsFirst(Comparator.naturalOrder()));
System.out.println(withNulls); // Output: [null, null, Alice, Bob, Charlie]

withNulls.sort(Comparator.nullsLast(Comparator.naturalOrder()));
System.out.println(withNulls); // Output: [Alice, Bob, Charlie, null, null]

```

---

## 5. Sorted Collections: TreeSet and TreeMap

`TreeSet` and `TreeMap` maintain elements in sorted order. They use `Comparable` by default, or a `Comparator` supplied at construction.

```java
import java.util.TreeSet;
import java.util.TreeMap;

// TreeSet — uses Student's natural order (alphabetical by name).
TreeSet<Student> sortedStudents = new TreeSet<>(students);
for (Student s : sortedStudents) {
    System.out.println(s.getName()); // Output: Alice, Bob, Charlie (alphabetical)
}

// TreeSet with a custom Comparator — sorted by GPA descending.
TreeSet<Student> byGpa = new TreeSet<>(
        Comparator.comparingDouble(Student::getGpa).reversed()
);
byGpa.addAll(students);
for (Student s : byGpa) {
    System.out.println(s.getName() + ": " + s.getGpa());
}
// Output:
// Alice: 3.8
// Charlie: 3.5
// Bob: 3.2

// TreeMap — keys sorted by natural order.
TreeMap<String, Student> byName = new TreeMap<>();
for (Student s : students) {
    byName.put(s.getName(), s);
}
System.out.println(byName.firstKey()); // Output: Alice
System.out.println(byName.lastKey());  // Output: Charlie

```

---

## 6. Using Comparator with Streams

`sorted()` in the Streams API accepts a `Comparator`.

```java
import java.util.List;
import java.util.stream.Collectors;

// All students with GPA >= 3.4, sorted by GPA descending.
List<Student> honour = students.stream()
        .filter(s -> s.getGpa() >= 3.4)
        .sorted(Comparator.comparingDouble(Student::getGpa).reversed())
        .collect(Collectors.toList());

honour.forEach(System.out::println);
// Output:
// Alice (GPA: 3.8, Year: 2024)
// Charlie (GPA: 3.5, Year: 2025)

// Min and max using a Comparator.
students.stream()
        .max(Comparator.comparingDouble(Student::getGpa))
        .ifPresent(s -> System.out.println("Top student: " + s.getName())); // Output: Top student: Alice

students.stream()
        .min(Comparator.comparingInt(Student::getGraduationYear))
        .ifPresent(s -> System.out.println("Earliest graduate: " + s.getName())); // Output: Earliest graduate: Alice

```

---

## 7. Complete Example: Product Catalogue Sorting

```java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class ProductSortDemo {

    record Product(String name, String category, double price, int stock) {}

    public static void main(String[] args) {

        List<Product> catalogue = new ArrayList<>(List.of(
            new Product("Widget",    "Hardware", 9.99,  150),
            new Product("Gadget",    "Electronics", 24.99, 80),
            new Product("Doohickey", "Hardware", 4.49,  200),
            new Product("Gizmo",     "Electronics", 14.99, 60),
            new Product("Thingamajig", "Hardware", 19.99, 45)
        ));

        // Sort by price ascending.
        catalogue.sort(Comparator.comparingDouble(Product::price));
        System.out.println("-- By price (ascending) --");
        catalogue.forEach(p -> System.out.printf("%-15s $%.2f%n", p.name(), p.price()));
        // Output:
        // Doohickey       $4.49
        // Widget          $9.99
        // Gizmo           $14.99
        // Thingamajig     $19.99
        // Gadget          $24.99

        // Sort by category, then by price descending within each category.
        Comparator<Product> byCategoryThenPriceDesc = Comparator
                .comparing(Product::category)
                .thenComparing(Comparator.comparingDouble(Product::price).reversed());

        catalogue.sort(byCategoryThenPriceDesc);
        System.out.println("\n-- By category, then price desc --");
        catalogue.forEach(p ->
                System.out.printf("%-12s %-15s $%.2f%n", p.category(), p.name(), p.price()));
        // Output:
        // Electronics  Gadget          $24.99
        // Electronics  Gizmo           $14.99
        // Hardware     Thingamajig     $19.99
        // Hardware     Widget          $9.99
        // Hardware     Doohickey       $4.49
    }
}

```

---

## 8. Common Mistakes

### Using subtraction for compareTo

Subtracting two integers to implement `compareTo` is a common but dangerous shortcut. It overflows for large values and produces incorrect ordering.

```java
// Wrong: overflows when a is Integer.MIN_VALUE and b is positive.
public int compareTo(IntWrapper other) {
    return this.value - other.value;
}

// Correct.
public int compareTo(IntWrapper other) {
    return Integer.compare(this.value, other.value);
}

```

### Inconsistent compareTo and equals

If `a.compareTo(b) == 0`, it should be true that `a.equals(b)`. `TreeSet` and `TreeMap` use `compareTo` for membership, not `equals`. An inconsistency means an element present by `equals` may not be found in a `TreeSet`.

```java
// If compareTo is by GPA but equals is by name, a TreeSet keyed on GPA
// will treat two students with the same GPA as duplicates,
// even if their names differ. This is almost always a bug.

```

### Forgetting to chain thenComparing for stable multi-key sorts

If two elements are equal on the primary key, the sort is unstable without a `thenComparing` chain. `Collections.sort` and `List.sort` are guaranteed stable (equal elements preserve their original relative order), but adding explicit tie-breaking makes intent clear.

```java
// Without thenComparing, ties in category are ordered arbitrarily.
catalogue.sort(Comparator.comparing(Product::category));

// With thenComparing, ties in category are broken by name.
catalogue.sort(Comparator.comparing(Product::category)
                         .thenComparing(Product::name));

```

---

## 9. Key Takeaways

- Implement `Comparable<T>` for the natural, canonical ordering of a class; use `compareTo` to define it
- Always use `Integer.compare()`, `Double.compare()`, or delegate to `String.compareTo()` — never compute differences
- Use `Comparator` when you need an ordering that is separate from the class, or when you need multiple orderings
- `Comparator.comparing(KeyExtractor)` with method references is the cleanest way to build comparators
- Chain `.thenComparing()` for multi-level sorts and call `.reversed()` to flip any comparator
- `TreeSet` and `TreeMap` require either `Comparable` elements or a `Comparator` at construction
- `Comparator.nullsFirst()` and `nullsLast()` handle null elements without manual null checks
- The Streams `sorted(Comparator)`, `min(Comparator)`, and `max(Comparator)` methods all accept the same comparators

---

Sorting is one of those operations that looks trivial and turns complex the moment you need multi-key or null-safe ordering. The `Comparator` builder methods — `comparing`, `thenComparing`, `reversed`, `nullsFirst` — cover virtually every sorting requirement you will encounter in practice.

---

## COLLECTIONS - ITERATORS

# Iterators and the Iterable Contract

The enhanced for loop (`for (String s : list)`) looks simple, but underneath it uses a protocol called the **Iterator pattern**. Understanding this protocol explains why some types work with the enhanced for loop and others do not, how to remove elements while iterating safely, and how to make your own classes work with the enhanced for loop.

---

## 1. What the Enhanced For Loop Actually Does

```

Think of it like this:
  An Iterator is a bookmark that moves through a book one page at a time.
  hasNext() asks "are there more pages?"
  next() turns to the next page and returns its content.
  The enhanced for loop is syntactic sugar that creates the bookmark and calls these
  two methods in a loop — so you never have to write the loop machinery yourself.

```

The enhanced for loop:

```java
List<String> names = List.of("Alice", "Bob", "Carol");

for (String name : names) {
    System.out.println(name);
}

```

is compiled by the Java compiler into exactly:

```java
Iterator<String> it = names.iterator();
while (it.hasNext()) {
    String name = it.next();
    System.out.println(name);
}
// Output:
// Alice
// Bob
// Carol

```

The enhanced for loop works with any class that implements `Iterable<T>`, which includes all `Collection` types (`List`, `Set`, `Queue`, `Deque`) and arrays.

---

## 2. The Iterator Interface

`java.util.Iterator<T>` has three methods:

| Method | Description |
|---|---|
| `boolean hasNext()` | Returns `true` if the iteration has more elements |
| `T next()` | Returns the next element and advances the cursor |
| `void remove()` | Removes the last element returned by `next()` from the underlying collection (optional operation) |

`remove()` is the only safe way to remove elements from a collection while iterating. All other approaches throw `ConcurrentModificationException`.

```java
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

List<String> names = new ArrayList<>(List.of("Alice", "Bob", "Carol", "Dave"));

// Remove all names with length <= 3 while iterating.
Iterator<String> it = names.iterator();
while (it.hasNext()) {
    String name = it.next();
    if (name.length() <= 3) {
        it.remove(); // Safe: removes through the iterator, not directly from the list.
    }
}

System.out.println(names); // Output: [Alice, Carol, Dave]

```

---

## 3. ConcurrentModificationException

Modifying a collection directly while iterating over it with a for-each loop or an explicit iterator throws `ConcurrentModificationException`. Collections maintain a modification count; the iterator checks this count on every `next()` call.

```java
List<String> names = new ArrayList<>(List.of("Alice", "Bob", "Carol"));

// Wrong: removing from the list directly while the enhanced for loop runs.
for (String name : names) {
    if (name.equals("Bob")) {
        names.remove(name); // Throws ConcurrentModificationException.
    }
}

```

Safe alternatives:

```java
// Option 1: use Iterator.remove().
Iterator<String> it = names.iterator();
while (it.hasNext()) {
    if (it.next().equals("Bob")) {
        it.remove(); // Safe.
    }
}
System.out.println(names); // Output: [Alice, Carol]

// Option 2: use List.removeIf() (Java 8+) — cleaner for simple conditions.
names.removeIf(name -> name.equals("Bob"));
System.out.println(names); // Output: [Alice, Carol]

// Option 3: collect into a new list.
List<String> filtered = names.stream()
        .filter(name -> !name.equals("Bob"))
        .collect(java.util.stream.Collectors.toList());
System.out.println(filtered); // Output: [Alice, Carol]

```

---

## 4. ListIterator — Bidirectional Iteration

`ListIterator<T>` extends `Iterator<T>` with the ability to iterate backwards, access the current index, and replace elements in place. It is available only for `List` types.

```java
import java.util.ArrayList;
import java.util.List;
import java.util.ListIterator;

List<String> names = new ArrayList<>(List.of("alice", "bob", "carol"));

// Capitalise each name in place using ListIterator.set().
ListIterator<String> lit = names.listIterator();
while (lit.hasNext()) {
    String name = lit.next();
    String capitalised = name.substring(0, 1).toUpperCase() + name.substring(1);
    lit.set(capitalised); // Replace the element that was just returned by next().
}

System.out.println(names); // Output: [Alice, Bob, Carol]

// Iterate in reverse using hasPrevious() and previous().
while (lit.hasPrevious()) {
    System.out.println(lit.previous());
}
// Output:
// Carol
// Bob
// Alice

```

---

## 5. The Iterable Interface

`java.lang.Iterable<T>` has one abstract method:

```java
public interface Iterable<T> {
    Iterator<T> iterator();
}

```

Any class that implements `Iterable<T>` can be used in an enhanced for loop. Implementing it requires implementing a corresponding `Iterator<T>`.

---

## 6. Implementing Iterable on Your Own Class

To make a custom class work with the enhanced for loop, implement `Iterable<T>` and provide a nested `Iterator<T>` implementation.

```java
import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * A fixed-size circular buffer that supports iteration in insertion order.
 * Elements are stored in an array; when the buffer is full, new elements
 * overwrite the oldest ones.
 */
public class CircularBuffer<T> implements Iterable<T> {

    private final Object[] data;
    private int head  = 0;    // Index of the oldest element.
    private int size  = 0;    // Number of elements currently stored.
    private final int capacity;

    public CircularBuffer(int capacity) {
        this.capacity = capacity;
        this.data     = new Object[capacity];
    }

    /** Add an element, overwriting the oldest if full. */
    public void add(T element) {
        int tail = (head + size) % capacity; // Where to write.
        data[tail] = element;
        if (size < capacity) {
            size++;
        } else {
            head = (head + 1) % capacity; // Oldest slot is now the next slot.
        }
    }

    public int size() { return size; }

    /** Return an iterator that visits elements in insertion order, oldest first. */
    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {

            private int remaining = size;       // How many elements are left to return.
            private int cursor    = head;       // Index of the next element to return.

            @Override
            public boolean hasNext() {
                return remaining > 0;
            }

            @Override
            @SuppressWarnings("unchecked")
            public T next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                T element = (T) data[cursor];
                cursor    = (cursor + 1) % capacity; // Advance, wrapping at capacity.
                remaining--;
                return element;
            }
        };
    }
}

```

```java
CircularBuffer<Integer> buffer = new CircularBuffer<>(3);
buffer.add(1);
buffer.add(2);
buffer.add(3);
buffer.add(4); // Overwrites 1 — the oldest element.

// The enhanced for loop works because CircularBuffer implements Iterable.
for (int value : buffer) {
    System.out.println(value);
}
// Output:
// 2
// 3
// 4

```

---

## 7. Iterator vs forEach vs Streams

Three ways to process every element of a collection:

```java
List<String> names = List.of("Alice", "Bob", "Carol");

// 1. Iterator — most explicit; necessary when you need to remove elements.
Iterator<String> it = names.iterator();
while (it.hasNext()) {
    System.out.println(it.next());
}

// 2. forEach (Iterable.forEach, Java 8+) — concise for simple processing.
names.forEach(System.out::println);

// 3. Stream — for transforming, filtering, or collecting results.
names.stream()
     .filter(name -> name.length() > 3)
     .map(String::toUpperCase)
     .forEach(System.out::println);
// Output: ALICE CAROL

```

**When to use each:**

| Approach | Best for |
|---|---|
| Iterator | Removing elements while iterating; fine-grained cursor control; bidirectional traversal (ListIterator) |
| Enhanced for | Simple read-only traversal; clearest and least verbose for the common case |
| `forEach` | Simple processing with a method reference; slightly more concise than enhanced for |
| Stream | Filtering, transforming, reducing, or collecting results; multi-step pipelines |

---

## 8. Common Mistakes

### Calling next() without checking hasNext()

`next()` throws `NoSuchElementException` if the iteration is exhausted. Always check `hasNext()` first.

```java
Iterator<String> it = List.of("Alice").iterator();
it.next();           // Returns "Alice".
it.next();           // Throws NoSuchElementException — no more elements.

```

### Calling remove() before next()

`remove()` removes the element most recently returned by `next()`. Calling it before any `next()` call, or calling it twice in a row, throws `IllegalStateException`.

```java
Iterator<String> it = new ArrayList<>(List.of("Alice", "Bob")).iterator();
it.remove(); // IllegalStateException — next() has not been called yet.

```

### Modifying the collection while using an enhanced for loop

As shown in Section 3, this always causes `ConcurrentModificationException`. Use `removeIf` or an explicit `Iterator.remove()` instead.

### Using Iterator on concurrent collections without synchronisation

Standard iterators are fail-fast: they detect structural modification and throw immediately. `ConcurrentHashMap` and `CopyOnWriteArrayList` provide weakly-consistent iterators that do not throw but may not reflect all concurrent modifications. Know which collection you are using before assuming iterator behaviour.

---

## 9. Key Takeaways

- The enhanced for loop compiles to an explicit `Iterator` loop; it works with any `Iterable<T>`
- `Iterator` provides `hasNext()`, `next()`, and `remove()` — the only three methods you need
- `Iterator.remove()` is the only safe way to remove elements from a collection during iteration
- Direct modification of a collection during iteration causes `ConcurrentModificationException`
- `ListIterator` extends `Iterator` with backward traversal and in-place replacement via `set()`
- Implementing `Iterable<T>` on a custom class requires providing a nested `Iterator<T>` that implements `hasNext()` and `next()`
- For simple traversal, prefer the enhanced for loop; for element removal, use `removeIf()` or an explicit iterator; for transformation pipelines, use streams

---

The Iterator pattern is the foundation that all Java collection traversal is built on. Once you understand what the enhanced for loop compiles to, the whole design becomes transparent — and the rules about when you can and cannot modify a collection while iterating follow naturally.

---