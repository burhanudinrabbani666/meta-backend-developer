# Programming Paradigm

Procedural Programming Basics

- Procedural programming involves writing step-by-step instructions organized into procedures or subroutines.
- It helps structure code logically, making it easier to update and add new functionality.

---

Functions and Reusability

- Functions accept parameters and return results, allowing code reuse with different inputs.
- The DRY (Don't Repeat Yourself) principle encourages reducing code duplication by creating reusable functions.

Example: Calculating Bill and Tax

- The example demonstrates functions for calculating a bill total and tax, each performing specific tasks.
- Functions call one another to reuse code, reducing the overall code footprint and improving maintainability.

---

Advantages of Procedural Programming

- Easy for beginners to learn and understand.
- Procedures can be reused across different parts of the program, enhancing code organization.

---

Disadvantages of Procedural Programming

- Can be difficult to maintain and extend for larger programs.
- Does not always model real-world objects well, and data is often exposed throughout the program.

---

Understanding Algorithms

- An algorithm is a series of steps to complete a task or solve a problem, similar to following a recipe.
- Algorithms break problems into smaller parts to build step-by-step solutions that work consistently.

---

Example: Palindrome Checking Algorithm

- A palindrome is a word that reads the same forwards and backwards, such as "racecar."
- The algorithm compares characters from the start and end of the string moving inward to check if they match.

---

Implementing the Algorithm in Code

- Define a function that takes a string as input and uses indices to compare characters from both ends.
- Use a loop to iterate through the string, returning false if any characters don’t match, otherwise true if all match.
- Testing the function with "racecar" returns true, while "racecars" returns false, confirming the algorithm works as intended.

---

Big O notation is a key concept in computer science used to describe the efficiency of algorithms by expressing how their runtime or resource usage grows with input size.

Understanding Big O Notation

- Big O notation represents the upper bound or worst-case time complexity of an algorithm, written as O(f(n)), where f(n) relates input size to runtime.
- It helps analyze how an algorithm scales as input data increases, enabling comparison and optimization.

---

Common Big O Examples

- O(1) (Constant Time): Runtime does not change with input size, e.g., accessing an array element by index.
- O(n) (Linear Time): Runtime grows linearly with input size, e.g., searching an unsorted list.
- O(n^2) (Quadratic Time): Runtime grows with the square of input size, e.g., bubble sort.
- O(log n) (Logarithmic Time): Runtime grows logarithmically, e.g., binary search in a sorted list.

---

Importance of Big O Notation

- It allows objective comparison of algorithms and helps optimize performance and scalability.
- Understanding Big O is essential for coding interviews and managing resources in constrained environments.

---

Analyzing Code with Big O

- Identify input size and loops, count operations inside loops, combine complexities for nested loops, and focus on the dominant term.
- Simplify expressions by removing constants to determine overall time complexity.

---

Functional Programming Basics

- Functional programming is a paradigm that uses functions to process data without changing the input or external state.
- Pure functions always produce the same output for the same input and do not modify global variables or data outside their scope.

---

Differences Between Traditional and Pure Functions

- Traditional functions can access and modify global state, while pure functions cannot.
- Pure functions depend solely on their input to produce output, ensuring consistency and predictability.

---

Python and Functional Programming

- Python treats functions as first-class citizens, meaning functions can be assigned to variables, passed as arguments, and returned from other functions.
- Built-in Python functions like sorted, map, and filter support functional programming by enabling reusable, clean, and efficient code.

---

Practical Example

- The course demonstrates creating a custom function to reverse strings and using the map function to apply it to a list, showcasing how functional programming simplifies data processing tasks.
