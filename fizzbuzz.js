const x = 100
const fizz = 3
const buzz = 5

for(let i =1; i<=(x+1); i++){

    let output = ""
    if(i%fizz==0){
        output+="fizz"
    }
    if(i%buzz==0){
        output+="buzz"
    }
    if(output==""){
        output = i
    }
    console.log(output)
}

