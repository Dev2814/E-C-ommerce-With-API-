// document.addEventListener("DOMContentLoaded", function () {
//     const popupContainer = document.getElementById("popupContainer");

//     // Remove existing popups after 3 seconds
//     const existingPopups = document.querySelectorAll(".popup");
//     existingPopups.forEach(popup => {
//         setTimeout(() => {
//             popup.classList.add("slide-up");
//             setTimeout(() => popup.remove(), 500);
//         }, 3000);
//     });

//     // Function to create popups
//     function showPopup(message, type) {
//         const popup = document.createElement("div");
//         popup.className = `popup ${type}`;
//         popup.innerHTML = message;
//         popupContainer.appendChild(popup);

//         setTimeout(() => {
//             popup.classList.add("slide-up");
//             setTimeout(() => popup.remove(), 500);
//         }, 3000);
//     }
// });
document.addEventListener("DOMContentLoaded", function () {
    const popupContainer = document.getElementById("popupContainer");
    const form = document.getElementById("ForgetForm");
    const loader = document.getElementById("loader");

    // Remove existing popups after 3 seconds
    const existingPopups = document.querySelectorAll(".popup");
    existingPopups.forEach(popup => {
        setTimeout(() => {
            popup.classList.add("slide-up");
            setTimeout(() => popup.remove(), 500);
        }, 3000);
    });

    // Show loader on form submit
    if (form) {
        form.addEventListener("submit", function (event) {
            event.preventDefault();  // Prevent default form submission to show loader first

            // Show the loader
            if (loader) {
                loader.style.display = "flex"; // Show the loader
            }

            // You can either submit the form with a delay or immediately
            setTimeout(function () {
                form.submit();  // After showing the loader, submit the form
            }, 1000); // You can adjust the delay as needed (1 second here)
        });
    }

    // Function to create popups (optional use)
    function showPopup(message, type) {
        const popup = document.createElement("div");
        popup.className = `popup ${type}`;
        popup.innerHTML = message;
        popupContainer.appendChild(popup);

        setTimeout(() => {
            popup.classList.add("slide-up");
            setTimeout(() => popup.remove(), 500);
        }, 3000);
    }
});
