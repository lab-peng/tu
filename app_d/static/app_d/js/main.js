// toggle lefter
const toggleLefter = () => {
    const lefter = document.querySelector(".lefter")
    if (lefter.style.display !== 'none') {
        lefter.style.display = 'none';
        document.querySelector(".main").style.marginLeft = "0";
    } else {
        lefter.style.width = "300px";
        lefter.style.display = 'block';
        document.querySelector(".main").style.marginLeft = "300px";
    }
}