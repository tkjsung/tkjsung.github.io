// collapse_expand.js
// Purpose: Enables item list expansion and collapse
// Side Note: This file is used for Food Compatibility Project

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        }
        else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}

// Uncomment and add expAll id to html if this is used.
// var expA = document.getElementById("expAll");
// expA.addEventListener('click', function () {
//     expandFunction(true);
// }, false);

var collA = document.getElementById("collAll");
collA.addEventListener('click', function () {
    expandFunction(false);
}, false);

function expandFunction(x) {
    var details = document.getElementsByClassName("collapsible");
    Array.from(details).forEach(span => {
        var content = span.nextElementSibling;
        var condition;
        var result;
        switch (x) {
            case false:
            condition = content.style.maxHeight == content.scrollHeight + "px";
            result = null;
            break;
            case true:
            condition = content.style.maxHeight == null || content.style.maxHeight == "";
            result = content.scrollHeight + "px";
            break;
            default:
        }
        if (condition) {
            span.classList.toggle("active");
            content.style.maxHeight = result;
        }
    });
}