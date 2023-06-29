let cerrarModalModify = document.querySelectorAll(".btn-cancel-modify")[0];
let abrirModalModify = document.querySelectorAll(".button-modify");
let modalModify = document.querySelectorAll(".modal-modify")[0];
let modalContainerModify = document.querySelectorAll(".modal-container-modify")[0];

abrirModalModify.forEach(function(click)
{
   click.addEventListener("click", function(e){

        e.preventDefault();
        modalContainerModify.style.opacity = "1";
        modalContainerModify.style.visibility = "visible";
        modalModify.classList.toggle("modal-modify-close");
        
    })
})

cerrarModalModify.addEventListener("click", function()
{
    modalModify.classList.toggle("modal-modify-close");
   
    setTimeout(function()
    {
        modalContainerModify.style.opacity = "0";
        modalContainerModify.style.visibility = "hidden";
    },300)
});

window.addEventListener("click", function(e){
    if(e.target == modalContainerModify){
        modalModify.classList.toggle("modal-modify-close");
   
        setTimeout(function()
        {
            modalContainerModify.style.opacity = "0";
            modalContainerModify.style.visibility = "hidden";
        },300)
    }
})

