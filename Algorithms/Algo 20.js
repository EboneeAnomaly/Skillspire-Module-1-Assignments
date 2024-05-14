let arr = [1,2,1,3,4,2,1]
function removeDuplicates(arr){
   if (arr.length <= 1){
    return arr;
   }
   let unique= {};
   let result = [];
   
   for (let i = 0; i < arr.length; i++){
    if (!unique[arr[i]]) {
        unique[arr[i]] = true;

        result.push(arr[i]);
    }
   }
   return result;
}

console.log(removeDuplicates(arr))