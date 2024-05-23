// Function definition
function greet(name) {
    const greeting = `Hello, ${name}!`; // Local scope
    return greeting;
}

// Scope and Closure
function outerFunction(outerVariable) {
    return function innerFunction(innerVariable) {
        console.log(`Outer Variable: ${outerVariable}`);
        console.log(`Inner Variable: ${innerVariable}`);
    };
}

const innerFunc = outerFunction(`outside`);
innerFunc('inside');

console.log(greet('Moses'));
