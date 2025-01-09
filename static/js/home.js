
const filter= document.querySelector(".filterBtn");
const filterDiv=document.querySelector(".filterDiv")


filter.addEventListener("click",()=>{


    if (filterDiv.getAttribute("style")){
     
        filterDiv.removeAttribute("style");
        
    }
    else{
        filterDiv.setAttribute("style","display:none")
    }
    filter.classList.toggle("black")

})