
let name = 'Ayesha'; //defining a variable 
//declare each vatiable on its one line 
let approved = true;


const interestRate = 0.3; //defining a constant
console.log(interestRate); 

//javascript is a dynamic language
//the typeof each variable is determined at run time based on the variable 
//assigned to it 

//reference types

//objects object literal, add the key value pairs 
let person = {
    name: 'Mosh',
    age: 30
};
console.log(person); 
//accessing the object properties 
person.name = 'John'; 
console.log(person); 
console.log(person['name']); 

//arrays and lists > 
let selectedColors = ['red', 'blue']; //assigns the indexes 
selectedColors[2] = 'green'; //length is dynamic 
selectedColors[3] = 10; //types of objects are dynamic 
console.log(selectedColors); 

//javascript arrays have built in operations 
console.log(selectedColors.length); 

//functions 
function greet(name){
    //defining some logic 
    console.log("Hello " + name); 
}

greet("Ayesha"); //calls the function 

//calculating values 
function square(number){
    return number * number; 
}

console.log(square(2)); 


