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