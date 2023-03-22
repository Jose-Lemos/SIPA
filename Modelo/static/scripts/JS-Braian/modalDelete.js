let cerrarModalDelete = document.querySelectorAll(".btn-cancel-delete")[0];
let abrirModalDelete = document.querySelectorAll(".button-trash");
let modalDelete = document.querySelectorAll(".modal-delete")[0];
let modalContainer = document.querySelectorAll(".modal-container-delete")[0];

abrirModalDelete.forEach(function(click)
{
    click.addEventListener("click", function(e){
        
        e.preventDefault();
        modalContainer.style.opacity = "1";
        modalContainer.style.visibility = "visible";
        modalDelete.classList.toggle("modal-delete-close");
    })
    
    
})

cerrarModalDelete.addEventListener("click", function()
{
    modalDelete.classList.toggle("modal-delete-close");
   
    setTimeout(function()
    {
        modalContainer.style.opacity = "0";
        modalContainer.style.visibility = "hidden";
    },300)
});

window.addEventListener("click", function(e){
    if(e.target == modalContainer){
        modalDelete.classList.toggle("modal-delete-close");
   
        setTimeout(function()
        {
            modalContainer.style.opacity = "0";
            modalContainer.style.visibility = "hidden";
        },300)
    }
})