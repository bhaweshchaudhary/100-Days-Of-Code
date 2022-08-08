function ham () {
    // by default list is hidden
    // on click this function list class is shown
    document.getElementById("mobile-menu").style.display = "block";
    document.getElementById("ham").style.display = "none";
    document.getElementById("cross").style.display = "block";

}

function cross() {
    document.getElementById("mobile-menu").style.display = "none";
    document.getElementById("ham").style.display = "block";
    document.getElementById("cross").style.display = "none";
}