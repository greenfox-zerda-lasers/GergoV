var arr = ["apple","orange","apple","orange","pear","orange"];

function getWordCnt(){
    return arr.reduce(function(prev,next){
        prev[next] = (prev[next] + 1) || 1;
        return prev;
    },{});
}

console.log(getWordCnt());  
