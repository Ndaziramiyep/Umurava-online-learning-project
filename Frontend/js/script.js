const navs = document.querySelectorAll("a");
 navs.forEach((nav) =>{
     nav.addEventListener("click", (event)=>{
        event.preventDefault();
        navs.forEach((nav) => nav.classList.remove("active"));
         nav.classList.add("active")
    });
});