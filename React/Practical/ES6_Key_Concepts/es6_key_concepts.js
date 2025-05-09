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



// ES6 Array Methods - map, filter, find, some, every, includes, indexOf, findIndex

const personsArray = [
    {
        name: 'Person 01',
        age: 30, 
        country: "USA",
    },
    {
        name: 'Person 1',
        age: 30, 
        country: "USA",
    },
    {
        name: 'Person 2',
        age: 40, 
        country: "RUSSIA",
    },
    {
        name: 'Person 3',
        age: 50, 
        country: "INDIA",
    }
]

// map: Transforms each element in the array and returns a new array.
const getAllNames = personsArray.map((person, index) => {
    console.log(person, index)
    return `${person.name} age is ${person.age}`
})
console.log(getAllNames)

// find: Returns the first element that satisfies the condition.
let getPersonFromUSA = personsArray.find((person, index) => {
    console.log(person, index)
    return person.country === "USA"
})
console.log(getPersonFromUSA)

// filter: Returns a new array with all elements that satisfy the condition.
let getAllPersonsFromUSA = personsArray.filter((person, index) => {
    console.log(person, index)
    return person.country === "USA"
})
console.log(getAllPersonsFromUSA)

// some: Checks if at least one element satisfies the condition.
let checkSomePerson = personsArray.some((person, index) => {
    console.log(person, index)
    return person.age >= 40
})
console.log(checkSomePerson)

// every: Checks if all elements satisfy the condition.
let checkEveryPerson = personsArray.every((person, index) => {
    console.log(person, index)
    return person.age > 30
})
console.log(checkEveryPerson)

// includes: Checks if an array contains a specific value.
const fruitsArray = ["apple", "banana", "orange"]
console.log(fruitsArray.includes("apple")) // true

// indexOf: Returns the index of the first occurrence of a value in the array.
console.log(fruitsArray.indexOf("banana")) // 1

console.log("-----------------")

// findIndex: Returns the index of the first element that satisfies the condition.
let getIndexofPerson = personsArray.findIndex((person, index) => {
    return person.country == "INDIA"
})
console.log(getIndexofPerson) 



// async await API call example
let getListOfProductsElement = document.querySelector('.list-of-products')
 
function renderProducts(getProducts){
    getListOfProductsElement.innerHTML = getProducts.map(
        (singleProductItem) => `<p>${singleProductItem.title}<p>`
    ).join(' ')
}       

async function fetchListOfProducts(){
    try {
        const apiResponse = await fetch('https://dummyjson.com/products', {
            method: 'GET'
        })

        const result = await apiResponse.json();
        console.log(result)

        if(result?.products?.length > 0) renderProducts(result?.products)
    }catch(e){
        console.log(e)
    }
}

fetchListOfProducts()