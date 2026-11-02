//javascriptのターミナルの出力のコマンド
console.log("hello");
//javascriptの変数
let name = "アレッシオ";
let age = 36;

console.log(name);
console.log(age);
//javascriptのテンプレート文字列
console.log(`${name}さんは${age}才です`);

//関数
function sayHello(){
    console.log(name);
};
sayHello();

function tsuika(a, b){
    return a + b;
};

let kekka = tsuika(10,5)

console.log(kekka)//15