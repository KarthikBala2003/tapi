document.addEventListener("DOMContentLoaded", function () {
    const jsonDataFile = "/static/menu_data.json";
    const menuList = document.getElementById("menuList");

    fetch(jsonDataFile)
        .then(response => response.json())
        .then(jsonData => {
            for (const category in jsonData) {
                const categoryItem = document.createElement("li");
                const link = document.createElement("a");
                link.href = "#";
                link.textContent = category;
                categoryItem.appendChild(link);

                const submenu = document.createElement("div");
                submenu.classList.add("submenu");

                for (const item of jsonData[category]) {
                    const menuItem = document.createElement("a");
                    menuItem.href = `/reference/${item}`;
                    menuItem.textContent = item.replace(/_/g, ' ').toUpperCase();
                    submenu.appendChild(menuItem);
                }

                categoryItem.appendChild(submenu);
                menuList.appendChild(categoryItem);
            }
        })
        .catch(error => console.error("Error loading JSON data:", error));
});