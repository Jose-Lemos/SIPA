const selectBtn3 = document.querySelector(".select-btn-3"),
    items3 = document.querySelectorAll(".item-3");

selectBtn3.addEventListener("click", () =>
{
    selectBtn3.classList.toggle("open-3");
});

items3.forEach(item3 => {
    item3.addEventListener("click", () => {
        item3.classList.toggle("checked-3");

    let checked3 = document.querySelectorAll(".checked-3"),
        btnText3 = document.querySelector(".btn-text-3");

        if(checked3 && checked3.length > 0)
        {
            btnText3.innerText = `Paises: ${checked3.length}`;
        }else{
            btnText3.innerText = "Paises: Todos";
        }
    });
})