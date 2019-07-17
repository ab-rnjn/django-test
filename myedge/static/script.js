function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "0";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
// slideer imgs next and prev.

var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs((slideIndex += n));
}
function currentDiv(n) {
  showDivs((slideIndex = n));
}
function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  if (n > x.length) {
    slideIndex = 1;
  }
  if (n < 1) {
    slideIndex = x.length;
  }
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" w3-white", "");
  }
  x[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " w3-white";
}

// automatic slider

var myIndex = 0;
carousel();

function carousel() {
  var i;
  var y = document.getElementsByClassName("mySlides");
  var dot = document.getElementsByClassName("demo");
  for (i = 0; i < y.length; i++) {
    y[i].style.display = "none";
  }
  for (i = 0; i < dot.length; i++) {
    dot[i].className = dot[i].className.replace(" w3-white", "");
  }
  myIndex++;
  if (myIndex > y.length) {
    myIndex = 1;
  }
  y[myIndex - 1].style.display = "block";
  dot[myIndex - 1].className += " w3-white";
  setTimeout(carousel, 4000); // Change image every 2 seconds
}
