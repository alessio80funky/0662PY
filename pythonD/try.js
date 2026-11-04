
try{
    let age = Number("alessio");

    if (isNaN(age)) {
        throw new Error("無効な入力です。整数を入力してください。");
    }
    
    console.log(`あなたの年齢は ${age} 歳です。`);
}catch(error){
    console.error(error.message);
}