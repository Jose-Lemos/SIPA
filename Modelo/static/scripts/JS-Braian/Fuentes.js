const selectBtn2 = document.querySelector(".select-btn-2"),
    items2 = document.querySelectorAll(".item-2");

selectBtn2.addEventListener("click", () =>
{
    selectBtn2.classList.toggle("open-2");
});
items2.forEach(item2 => {
    item2.addEventListener("click", () => {
        item2.classList.toggle("checked-2");

    let checked2 = document.querySelectorAll(".checked-2"),
        btnText2 = document.querySelector(".btn-text-2");

        if(checked2 && checked2.length > 0)
        {
            btnText2.innerText = `Fuentes: ${checked2.length}`;
        }else{
            btnText2.innerText = "Fuentes: Todas";
        }
    });
})
// cambia el nombre de las variables