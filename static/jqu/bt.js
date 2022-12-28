
document.addEventListener("DOMContentLoaded", function(event) { 
var li = document.querySelector('#jku').value;
 
var nm = document.querySelector('#nma');

 var btn = document.querySelector('#btna');

 function senda() {
    
    const ba = document.createElement('li');
    //var b = document.createElement('li');
       ba.setAttribute("class", "small p-2 ms-3 mb-3 rounded-3");
        ba.setAttribute("style", "background-color: #f5f6f7;");

       var nma = document.querySelector('.nma').value;

         var n = document.createTextNode(nma)


              ba.append(n);


             li.append(ba);

  if (nm == "where is jku" || nm.includes("jku")) {
 
 
 var ds=document.querySelector('.div');
 ds.setAttribute("style","display:block");

 b.append(ds);
 li.append(b);
  var vb =setTimeout(function() {
         ds.setAttribute("style","display:none");


   var j = "jku is located at south";
   
   var b = document.createElement('li');
   b.setAttribute("class", "small p-2 ms-3 mb-3 rounded-3");
   b.setAttribute("style", "background-color: lightgreen;float:right");

   var n = document.createTextNode(j);
   b.append(n);
   li.append(b);
         }, 3000);
   
   btn.setAttribute("class", "btn btn-warning");
   btn.setAttribute("id", "bt");

   var btna = document.querySelector('#bt');
   btna.addEventListener('click', ()=> {
    var nm = document.querySelector('#nma');


    nm.setAttribute("class", "form-control");
    nm.setAttribute("id", "in");

    
    var b = document.createElement('li');
    b.setAttribute("class", "small p-2 ms-3 mb-3 rounded-3");
    b.setAttribute("style", "background-color: #f5f6f7;");

    var nma = document.querySelector('#in').value;

    var n = document.createTextNode(nma)


    b.append(n);


    li.append(b);

    if (nma.includes("cs")) {
     var j = "i love css";
     var b = document.createElement('li');
     b.setAttribute("class", "small p-2 ms-3 mb-3 rounded-3");
     b.setAttribute("style", "background-color: lightgreen;float:right");

     var n = document.createTextNode(j);
     b.append(n);
     li.append(b);
    }
   });


  } else if (nm == "how i employed at jku" || nm.includes("employed")) {

   var j = "if you need to employed at jku you have to apllay";
   var b = document.createElement('li');
   b.setAttribute("class", "small p-2 ms-3 mb-3 rounded-3");
   b.setAttribute("style", "background-color: lightgreen;float:right");

   var n = document.createTextNode(j)
   var a = document.createElement('br');
   b.append(n);
   b.append(a);
   li.append(b);
  }
 }});