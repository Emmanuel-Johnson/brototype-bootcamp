// Logical AND (&&) and Logical OR (||)

let a = true;
let b = false;

console.log(a && b); // false (both must be true for AND)

let c = true;
let d = false;

console.log(c || d); // true (at least one must be true for OR)

// Explanation:
// Logical AND (&&): Returns true if both operands are true, otherwise false.
// Logical OR (||): Returns true if at least one operand is true, otherwise false.



// Template Literals

let firstName = "John";
let lastName = "Doe";

console.log(`${firstName} ${lastName}`); // John Doe

// Explanation:
// Template literals allow embedding variables and expressions inside strings using backticks (`) and ${}.



// Ternary Operator

let flag = false;
console.log(flag ? "flag is true" : "flag is false"); // flag is false

// Explanation:
// The ternary operator is a shorthand for if-else.
// Syntax: condition ? value_if_true : value_if_false.



// Object and Array Destructuring

// Object creation with traditional property assignment
const id = 1;
const productName = "Smart Phone";
const rating = 5;

const product1 = {
    id: id,
    productName: productName,
    rating: rating,
};

console.log(product1); // { id: 1, productName: 'Smart Phone', rating: 5 }

// Object creation with shorthand property names
const product2 = { id, productName, rating };

console.log(product2); // { id: 1, productName: 'Smart Phone', rating: 5 }

// Adding additional properties
const product3 = {
    description: "Product 3 Description",
    id,
    productName,
    rating,
};

// Accessing properties using dot notation
console.log(product3.description); // Product 3 Description

// Accessing properties using destructuring
const { description } = product3;
console.log(description); // Product 3 Description

// Array destructuring
const array = [1, 2, 3];

// Accessing elements using index
let firstValue = array[0];
let secondValue = array[1];

console.log(firstValue, secondValue); // 1 2

// Accessing elements using destructuring
const [firstElement, secondElement] = array;

console.log(firstElement, secondElement); // 1 2

// Explanation:
// Object destructuring allows extracting properties into variables.
// Array destructuring allows extracting elements into variables.



// Default Parameters, Spread, and Rest Operators

// Default parameters
function multiply(num1 = 5, num2) {
    return num1 * num2;
}

console.log(multiply(undefined, 10)); // 50 (num1 defaults to 5)

// Spread operator
const array2 = [2, 3, 4];
const array3 = [10, 11, 12];

console.log(999, ...array2, 90, ...array3, 1000); 
// 999 2 3 4 90 10 11 12 1000

// Rest operator
function getInfo(a, b, c, ...rest) {
    console.log(a, b, c, rest); // 1 2 3 [4, 5]
    return "Yo";
}

console.log(getInfo(1, 2, 3, 4, 5)); // Yo

// Explanation:
// Default parameters provide default values for function arguments.
// Spread operator (...) expands arrays or objects into individual elements.
// Rest operator (...) collects remaining arguments into an array.