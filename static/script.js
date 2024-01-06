document.addEventListener("DOMContentLoaded", function () {
    function changeCase(str) {
        return str.replace(/[\s_](.)/g, (match, group1) => ' ' + group1.toUpperCase())
            .replace(/^(.)/, (match, group1) => group1.toUpperCase());
    }

//document.getElementById('redirectButton').addEventListener('click', function () {
//    window.location.href = '/';
//});

    const jsonDataFile = "/static/menu_data.json";
    const menuList = document.getElementById("menuList");

    fetch(jsonDataFile)
        .then(response => response.json())
        .then(jsonData => {
            for (const category in jsonData) {
                const categoryItem = document.createElement("li");
                const link = document.createElement("a");
                link.href = "#";

                link.textContent = changeCase(category);
                categoryItem.appendChild(link);

                const submenu = document.createElement("div");
                submenu.classList.add("submenu");

                for (const item of jsonData[category]) {
                    const menuItem = document.createElement("a");
                    menuItem.href = `/reference/${item}`;
                    menuItem.textContent = changeCase(item);

                    submenu.appendChild(menuItem);
                }

                categoryItem.appendChild(submenu);
                menuList.appendChild(categoryItem);
            }
        })
        .catch(error => console.error("Error loading JSON data:", error));

    var footer = document.getElementById("pageFooter");
    var isFooterVisible = false;

    window.addEventListener("scroll", function () {
        
        var isBottom = window.innerHeight + window.scrollY >= document.body.offsetHeight;

        
        var isTop = window.scrollY === 0;

        
        if (isBottom && !isFooterVisible) {
            footer.style.opacity = 1;
            isFooterVisible = true;
        } else if ((!isBottom || isTop) && isFooterVisible) {
            footer.style.opacity = 0;
            isFooterVisible = false;
        }
    });
});
window.addEventListener('beforeunload', function (event) {
    // Notify the server when the tab or browser is closed
    fetch('/logout', { method: 'POST' });
});