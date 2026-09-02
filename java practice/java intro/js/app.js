console.log("this is my app and i am practicing java");
console.log(5+5);
console.log("I am not ok right now")
// alert("hi");
console.log(5 * 2); // this is a calculation her to understand
console.log("now I am alright how are you. are hou ok... i don't know")

var name = "kashem"; // it is old style
name = " joynul";
console.log(name)


let user = "ke koice";

let age = 35;

console.log(user)
console.log(age)

const cuntry = "Bangladesh";
console.log(cuntry)


let great = "hello everyone"
let message = "I am not very nice one"
let welcome_message = `Welcom, ${great}`

console.log(welcome_message)

const para = `Learning a little each day adds up. Research shows that students who make learning a habit are more likely to reach their goals. Set time aside to learn and get reminders using your learning scheduler.`

let grate = `are you ready to fuck`

console.log("your paragraph is :", para.length)

console.log("Uppercase", grate.toUpperCase())

let phrase = "welcome to java!"

console.log(phrase.slice(11, -1))
const subText = phrase.substring(11, 15)

console.log("Sub: ",subText)


let word = "    coding is my thing    "

const trimword = word.trim()
console.log(trimword)

// templet literal must nee to know 

let mine = " alice"
let agees = 30;

// my  name is Alice and my age is 30

let messages = `MY name is ${mine}, and I am ${age}`;

console.log(messages)

// multiline strings

let x1 = 50.5655, y1 = 10.5656;
let total_prices = x1 + y1;
let diff = x1 - y1

console.log(`Total sum is : ${x1 + y1}`)

console.log("Total price : ",total_prices.toFixed(2) )
console.log("Subtruct: ", diff);
console.log("Subtruct: ", diff);


// math.round()

let xp = 65.356;
let xy = 75.468;
let rendom_numverSet = Math.floor(Math.random() * 10);
let rendom_numverSet1_to100 = Math.floor(Math.random() * 100) + 1;

console.log(`Rounded value for ${xp}  IS: `, Math.round(xp)) // make it nearest integer .5 er beshi hole  upore jay  05 er niche hole niche chole ashe
console.log(`Random Number: `, Math.random())
console.log("Random namber is 1 to 10: ", rendom_numverSet)
console.log("Random namber is 1 to 100: ", rendom_numverSet1_to100)
console.log(`Amount for ${xp}: `,Math.ceil(xp));
console.log(`Amount for ${xy}: `, Math.floor(xy) ) //Math floor nicher number couant koere


//Math.Max() return largest value

let xz = 100;

let maxNumber = Math.max(xp, xy, xz )

console.log("Largest number is : ", maxNumber ) // if need to find higest score of something.

let numbers_arr = [89, 45,76,99, 35, 67]
let largetrs_num = Math.max(...numbers_arr )

console.log("the largest number is : ", largetrs_num)





// slice(), tofixed(), touppercase(), tolowercase(), trime(), subtracting(),
// Math.Round(), tofixed(), Mth.random(), Math.ciel(), Math.floor(), Math.max()


// numbers method: for number methods

// tofixed() convert to nubmer  for change data according to our data neded

let prices = 56.49645655;

let fixedThisNumber = prices.toFixed(2);
console.log("Fixed this number: ",fixedThisNumber ) 

// parseInt(): convert a string to a number or decimal not word ar letter
let strings1 = "50";
let strings2 = "jkh7850ksjds";
let strings3 = "90px";
console.log(parseInt(strings1))
console.log(parseInt(strings2))
console.log(parseInt(strings3))

//using redix parameter: binary to decimal . decimal base 10 and binary base 2 hexa descima bas 16

let bineryNumber = "1010001";
console.log("Decimal number is: ", parseInt(bineryNumber, 2))

let hexaNumber = "A"; // hexa number: 0-9, a b c d e f
let hexaNumberColor = "DC24";
console.log("Decimal number is: ", parseInt(hexaNumber, 16))
console.log("Decimal number is: ", parseInt(hexaNumberColor, 16)) //aita redix parameter

// parseFloot(), convert string to decimal nubmer

let str4 = "3.1415";
let str5 = "9.1415";
console.log(parseFloat(str4));

let totaPri = parseFloat(str4) + parseFloat(str5);

console.log(totaPri)

// primetive data types and non primitive data types in java

/*
//primitive data types: basic data types and immutable. you cannot change primitive data means variable name but value directly stor kora jay.

non primitive data refference data type like objects arrays and function
   

*/
// premitive example
let xyx = 10;
let xyxy = 20;
let yyx = xyxy;

console.log("X is : ", xyx)
xyxy = 30;
console.log("Y is : ", xyxy)
console.log("2 time Z is : ", yyx)

// non primitive example 

let obj1 = {
    a: 10,
    b: 20,
}
let obj2 = obj1;

console.log("The obj ", obj2)

obj2.a = 20;

console.log("2nd time The obj ", obj2)
console.log("3nd time The obj ", obj1)
















