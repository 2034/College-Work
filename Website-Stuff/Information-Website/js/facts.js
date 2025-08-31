const facts = [
    "Fact 1",
    "Fact 2",
    "Fact 3",
    "Fact 4",
    "Fact 5",
    "Fact 6",
]

/* 

Last Edited: 25/04/25

Explaination: Quite simple js file that just adds facts to the grid instead of just having lines and lines of html
*/

document.addEventListener("DOMContentLoaded", () => {
    const factsGrid = document.querySelector(".facts-grid");
    facts.forEach((fact) => {
        const factBox = document.createElement("div");
        factBox.className = "fact-box";
        factBox.textContent = fact;
        factsGrid.appendChild(factBox);
    });
});