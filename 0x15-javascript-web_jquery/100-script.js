// Select the header element and update its text color to red
  document.addEventListener("DOMContentLoaded", function() {
  var header = document.querySelector("header");
  if (header) {
    header.style.color = "#FF0000";
  } else {
    console.error("Header element not found!");
  }
});
