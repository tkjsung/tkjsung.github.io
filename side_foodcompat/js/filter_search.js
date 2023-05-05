// filter_search.js
// Purpose: Enables list filtering by setting style to "none" when the search keyword doesn't match the item in the list
// Side Note: This file is used for Food Compatibility Project

function page_loaded(){
    let btn = document.getElementsByClassName("collapsible");
    let btn_description = document.getElementsByClassName("content");
    let result_text = document.getElementById("text_results");
    for (let i=0; i<btn.length; i++){
        btn[i].style.display = "none";
        btn_description[i].style.display = "none";
        result_text.style.display = "none";
    }
}

// TODO: When search box is empty, do not display all entries.
function compat_search(){
    let usr_input = document.getElementById("compat_searchbox");
    let filter = usr_input.value.toUpperCase();
    let btn = document.getElementsByClassName("collapsible");
    let btn_description = document.getElementsByClassName("content");
    let result_text = document.getElementById("text_results");
    let j = 0;

    for(let i=0; i<btn.length; i++){
        let txtValue = btn[i].textContent || btn[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter)>-1){
            btn[i].style.display = "";
            btn_description[i].style.display = "";
        } else {
            btn[i].style.display = "none";
            btn_description[i].style.display = "none";
            j += 1;
        }
        if (j==btn.length){
            result_text.style.display = "none";
        }
        else{
            result_text.style.display = "";
        }
    }
}

function check_enter_key(e){
    // console.log(e)
    if (e.key === "Enter"){
        compat_search();
    }
}
