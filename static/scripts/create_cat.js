document.getElementById("bg-color").addEventListener("input", function() {
    document.getElementById("colorful-object").style.backgroundColor = this.value;
    document.getElementById("created_category").style.backgroundColor = this.value;
});
