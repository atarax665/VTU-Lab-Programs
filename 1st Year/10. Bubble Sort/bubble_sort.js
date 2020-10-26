function bubble_Sort(arrayToSort){
    var swapp;
    var length = arrayToSort.length-1;
    var x=arrayToSort;
    do {
        swapp = false;
        for (var i=0; i < length; i++)
        {
            if (x[i] < x[i+1])
            {
               var temp = x[i];
               x[i] = x[i+1];
               x[i+1] = temp;
               swapp = true;
            }
        }
        length--;
    } while (swapp);
 return x; 
}
console.log(bubble_Sort([12, 345, 4, 546, 122, 84, 98, 64, 9, 1, 3223, 455, 23, 234, 213]));
// Expected outcome is [ 3223, 546, 455, 345, 234, 213, 122, 98, 84, 64, 23, 12, 9, 4, 1 ]
