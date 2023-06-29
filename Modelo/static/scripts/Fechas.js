const selectBtn4 = document.querySelector(".select-btn-4"),
    items4 = document.querySelectorAll(".item-4");

selectBtn4.addEventListener("click", () =>
{
    selectBtn4.classList.toggle("open-4");
});
items4.forEach(item4 => {
    item4.addEventListener("click", () => {
        item4.classList.toggle("checked-4");

    let checked4 = document.querySelectorAll(".checked-4"),
        btnText4 = document.querySelector(".btn-text-4");
        if(checked4 && checked4.length > 0)
        {
            btnText4.innerText = `Fechas: ${checked4.length}`;
        }else{
            btnText4.innerText = "Fechas: Todas";
        }
    });
})