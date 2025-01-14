// ? Navbar Start --->
const add = document.querySelector("#add");
const elans = document.querySelector(".elans");
const elan1 = document.querySelector(".elan1");
const elan2 = document.querySelector(".elan2");

add.addEventListener("click", () => {
  console.log("s");
  elans.classList.toggle("elansDisplay");
  add.classList.toggle("addDisplay");
});
elan1.addEventListener("click", () => {
  console.log("s");
  elans.classList.toggle("elansDisplay");
  add.classList.toggle("addDisplay");
});
elan2.addEventListener("click", () => {
  console.log("s");
  elans.classList.toggle("elansDisplay");
  add.classList.toggle("addDisplay");
});
// ! Navbar End  --->
