/* 
    Last Edited: 25/04/25

    Explaination: This is a simple js file that just adds date to the footer of each page.
    Uses toLocaleDateString to format the date to dd/mm/yyyy.
*/

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('current-date').textContent = new Date().toLocaleDateString('en-GB');
});