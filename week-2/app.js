
/* 要求一  ------------------------------------------------------ */

  function calculate(min,max,step){
    let number=0
    for(let i=min;i<=max;i+=step){
       number+=i
      }
      console.log(number)
    }
    
 calculate(1, 3, 1); // 你的程式要能夠計算 1+2+3，最後印出 6
 calculate(4, 8, 2); // 你的程式要能夠計算 4+6+8，最後印出 18    
 calculate(-1, 2, 2);  // 你的程式要能夠計算 -1+1，最後印出 0

/* 要求二---------------------------------------------------------- */

function avg(data){
     
   let array=data.employees.length
   let total=0
   let count=0
   let average=0
   
   for(let i=0;i<array;i++){
       let manager=data.employees[i].manager;
       let salary=data.employees[i].salary;
       if(manager!=true){
           total+=salary
           count++
       }
        
   }
   average = total/count;
   console.log(average)
}
  
   avg({
   "employees":[
   {
   "name":"John",
   "salary":30000,
   "manager":false },
   {
   "name":"Bob",
   "salary":60000,
   "manager":true },
   {
   "name":"Jenny",
   "salary":50000,
   "manager":false },
   {
   "name":"Tony",
   "salary":40000,
   "manager":false }
   ]
   }); // 呼叫 avg 函式





/* 要求三-------------------------------------------------------- */

 function func(a){
      return function(b,c){
         let answer=a+(b*c)
        console.log(answer)  
     }
  }
 func(2)(3, 4); // 你補完的函式能印出 2+(3*4) 的結果 14 
 func(5)(1, -5); // 你補完的函式能印出 5+(1*-5) 的結果 0 
 func(-3)(2, 9); // 你補完的函式能印出 -3+(2*9) 的結果 15 // 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

/* 要求四------------------------------------------------------------ */

function maxProduct(nums){
    let max=nums[0]*nums[1]
    for(let i=0;i<nums.length;i++){
        for(let j=0;j<nums.length;j++){
              if(nums[i]*nums[j]>max && i!==j){
                max=nums[i]*nums[j]
              }
        }
    }
    console.log(max) 
   
}
maxProduct([5, 20, 2, 6]) // 得到 120 
maxProduct([10, -20, 0, 3]) // 得到 30 
maxProduct([10, -20, 0, -3]) // 得到 60 
maxProduct([-1, 2]) // 得到 -2 
maxProduct([-1, 0, 2]) // 得到 0 或 -0 
maxProduct([5, -1, -2, 0]) // 得到 2 
maxProduct([-5, -2]) // 得到 10 */

/*  要求五--------------------------------------------------------------- */

function twoSum(nums, target){
     let result=[]
     for(let i=0;i<nums.length;i++){
        for(let j=0;j<nums.length;j++){
            if(nums[i]+nums[j]==target && i!=j){
                result.push(i)
            }
        }
     }
     return result
}

let result=twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9


/*  要求六---------------------------------------------------------------- */

function maxZeros(nums){
   let count=0;
   let result=0;
   for(let i=0;i<nums.length;i++){
         if(nums[i]==1)
             count=0;
         else{
             count++;
             result=Math.max(result,count)
         }    

      }
     console.log(result)
   }


maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4 
maxZeros([1, 1, 1, 1, 1]); // 得到 0 
maxZeros([0, 0, 0, 1, 1]) // 得到 3

