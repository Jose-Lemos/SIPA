const selectBtn = document.querySelector(".select-btn-1"),
    items = document.querySelectorAll(".item-1");

selectBtn.addEventListener("click", () =>
{
    selectBtn.classList.toggle("open");
});
items.forEach(item => {
    item.addEventListener("click", () => {
        item.classList.toggle("checked");

    let checked = document.querySelectorAll(".checked"),
        btnText = document.querySelector(".btn-text");

        if(checked && checked.length > 0)
        {
            btnText.innerText = `Categorias: ${checked.length}`;
        }else{
            btnText.innerText = "Categorias: Todas";
        }
    });
})

