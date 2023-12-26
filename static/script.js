<<<<<<< HEAD
// Toggle submenus in the sidebar
document.addEventListener("DOMContentLoaded", function () {
    var dropdowns = document.getElementsByClassName("dropdown-btn");
    for (var i = 0; i < dropdowns.length; i++) {
        dropdowns[i].addEventListener("click", function () {
            this.classList.toggle("active");
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === "block") {
                dropdownContent.style.display = "none";
            } else {
                dropdownContent.style.display = "block";
            }
        });
    }
});
=======
$(document).ready(function () {
    
    let list = $('<li/>').appendTo('#menu1');

    $('<a />')
        .text('Features')
        .attr('href', '#')
        .appendTo(list);

    
    let sub_ul = $('<ul/>').appendTo(list);

    
    $.getJSON('/static/menu_data.json', function (jsonData) {
        $.each(jsonData, function (category, subcategories) {
            
            let sub_li = $('<li/>').appendTo(sub_ul);
            $('<a />')
                .text(category + ' + ')
                .attr('href', '#')
                .appendTo(sub_li);

            let sub_sub_ul = $('<ul/>').appendTo(sub_li);

            $.each(subcategories, function (index, subcategory) {
                let sub_sub_li = $('<li/>').appendTo(sub_sub_ul);
                $('<a />')
                    .text(subcategory)
                    .attr('href', '#')
                    .appendTo(sub_sub_li);
            });
        });
    });
});
>>>>>>> 597ff7c12305622436d0bb3879bede87afeb228d
