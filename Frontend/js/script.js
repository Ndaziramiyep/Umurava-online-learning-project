const navs = document.querySelectorAll("a");
 navs.forEach((nav) =>{
     nav.addEventListener("click", (event)=>{
        event.preventDefault();
        navs.forEach((nav) => nav.classList.remove("active"));
         nav.classList.add("active")
    });
});

// -------------------making #mobile (menu) clickable ----------

const bar = document.getElementById("bar");
const nav = document.getElementById("navbar");

if (bar){
    bar.addEventListener("click", () => {
        nav.classList.add('active');
    })
}