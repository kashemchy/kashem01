// if else conditin

// if (condition){
//     //code block
// } else if () {
//     // code block
// } else {
//     // code block
// }


 let age = 90;

 if (age >= 18){
    console.log("You can Vote");
 } else {
    console.log("You cannot Vote")
 }

 let score = 50;

 if (score >= 90) {
    console.log("Grade A")
 } else if (score >= 80) {
    console.log("Greade B")
 } else if (score >= 70) {
    console.log("Greade c")
 }else if (score >= 60) {
    console.log("Greade d")
 }else {
    console.log("Greade F")
 }


// logical operators   || and !

// logical and 
// both condition need to be correct
let math = 46;
let science = 70;

if (math >= 50 && science >= 50) {
    console.log("You are passed")
}else {
    console.log("You are failed")
}


// logical ||  
// any one condition true then it will check and print the result
let member = false;
let coupon = true;

if (member || coupon) {
    console.log("YOU CAN ENROLL MY COURSE")
} else {
    console.log("YOU CANnot ENROLL MY COURSE")
}

//logical not: positive thakle eta negative kore fele ar negatice korle  eta positive kore dibe

let isLoggedIn = false;

if (!isLoggedIn){
    console.log("Please log in")
}else {
    console.log("welcome back!")
}


let proMember = true;
let loggedIn = true;

let accessCode = false;

if ((proMember && loggedIn) || accessCode) {
   console.log("You can enjoy web development course")
} else {
   console.log("access denied! plese buy")
}



// how to define function

// function functionName (parameter) {
//    //logic here
// }

function greet(){
   console.log("Ha are you!")
}

greet();

function greetuser(names){
   console.group(`Hello ${names}! how are you?`)
}

greetuser("kashem");
greetuser("Rubel");
greetuser("kashem","lambu");

// function for add numbers

function assNumbers (num1,num2) {
   return num1 + num2;
}

let result = assNumbers(5,10);

console.log(`Result is: ${result}`);

// arrow functin

// let functionName = () => {

// }

// let multiply = (num1,num2) => num1 * num2   another way to rite arrow functin

let multiply = (num1,num2) => {
   return num1 * num2
}

console.log("The result is ", + multiply(5,2))


// function expression    put function into variable

let diff = (a,b) => a-b;
let result3= diff(5,2)
console.log("The result is: ",result3)

// anonymous callback fucntion: je function er kunu name thakbena

let fri = ["rubel","lambu","kashem"] ;
fri.forEach((fri) => console.log(`Welcome, ${fri}`));
fri.forEach((fri) =>  {
   return "welcome" + fri;
});


// js basic array starting from here 
// wht is array . what 

const students = ["Alex", "Mamun", "Joy", "Jhon", "Mithu"];




