//比較演算子

a = 10;
b = 20;

console.log(a === b); //等しいかどうか -> false
console.log(a !== b); //等しくないかどうか -> true
console.log(a > b); //大きいかどうか -> false
console.log(a < b); //小さいかどうか ->  true                      
console.log(a >= b); //大きいか等しいかどうか -> false
console.log(a <= b); //小さいか等しいかどうか -> true

//論理演算子

console.log(a > 5 && b < 30); //両方の条件がtrue -> true

console.log(a > 5 || b < 30); //どちらかの条件がtrue -> true

console.log(!(a > 5)); //条件がtrueならfalse、falseならtrue -> false


age = 17;
score = 80;

if (age >= 18 && score >= 70) {
    console.log("合格");    
}

if (age < 18 || score < 70) {
    console.log("不合格");
}