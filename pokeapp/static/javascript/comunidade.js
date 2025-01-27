const Cards = document.querySelectorAll(".card")

Cards.forEach(card => {
    classe = card.querySelector("#classe").value
    console.log(classe)
    if (classe !== "Comunidade"){
        card.style.display = "none"
    }
});