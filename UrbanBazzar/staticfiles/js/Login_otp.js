// document.addEventListener("DOMContentLoaded", function () {
//     const otpInputs = document.querySelectorAll(".input-field input");
//     const popupContainer = document.getElementById("popupContainer");
//     const form = document.getElementById("otpForm");
  
//     otpInputs.forEach((input, index) => {
//       // Move focus to the next input field if the current input is filled
//       input.addEventListener("input", function () {
//         if (input.value.length === input.maxLength) {
//           const nextInput = otpInputs[index + 1];
//           if (nextInput) {
//             nextInput.focus();
//           }
//         }
//       });
  
//       // Handle backspace key press to move focus to the previous input field
//       input.addEventListener("keydown", function (event) {
//         if (event.key === "Backspace" && input.value === "") {
//           const previousInput = otpInputs[index - 1];
//           if (previousInput) {
//             previousInput.focus();
//             previousInput.value = ""; // Clear the previous input value
//           }
//         }
//       });
//     });
  
//     // Function to create popups
//     function showPopup(message, type) {
//       const popup = document.createElement("div");
//       popup.className = `popup ${type}`;
//       popup.innerHTML = message;
//       popupContainer.appendChild(popup);
  
//       setTimeout(() => {
//         popup.classList.add("slide-up");
//         setTimeout(() => popup.remove(), 500);
//       }, 3000);
//     }
  
//     // Remove existing popups after 3 seconds (even success messages)
//     const existingPopups = document.querySelectorAll(".popup");
//     existingPopups.forEach(popup => {
//       setTimeout(() => {
//         popup.classList.add("slide-up");
//         setTimeout(() => popup.remove(), 500);
//       }, 3000);
//     });
  
//     // Form submit event listener
//     form.addEventListener("submit", function (event) {
//       event.preventDefault(); // Prevent form submission
  
//       // Check if all inputs are filled
//       let allFilled = true;
//       otpInputs.forEach((input) => {
//         if (!input.value) {
//           allFilled = false;
//           input.focus();
//           return;
//         }
//       });
  
//       if (allFilled) {
//         if (loader) loader.style.display = "flex";
//         form.submit(); // Allow form submission
//       } else {
//         showPopup("Please fill all OTP fields.", "error");
//       }
//     });
//     // Show loader on Resend OTP click
//     if (resendLink) {
//       resendLink.addEventListener("click", function (e) {
//         e.preventDefault(); // Stop immediate navigation
//         if (loader) loader.style.display = "flex";
//         setTimeout(() => {
//           window.location.href = resendLink.href;
//         }, 300); // Small delay to show loader
//       });
//     }
//   });


document.addEventListener("DOMContentLoaded", function () {
  const otpInputs = document.querySelectorAll(".input-field input");
  const popupContainer = document.getElementById("popupContainer");
  const form = document.getElementById("otpForm");
  const loader = document.getElementById("loader");
  const resendLink = document.querySelector('a[href*="Resend_otp"]');

  // Hide loader by default
  loader.style.display = "none";

  otpInputs.forEach((input, index) => {
    input.addEventListener("input", function () {
      if (input.value.length === input.maxLength) {
        const nextInput = otpInputs[index + 1];
        if (nextInput) {
          nextInput.focus();
        }
      }
    });

    input.addEventListener("keydown", function (event) {
      if (event.key === "Backspace" && input.value === "") {
        const previousInput = otpInputs[index - 1];
        if (previousInput) {
          previousInput.focus();
          previousInput.value = "";
        }
      }
    });
  });

  // Function to create popups
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

  // Remove existing popups after 3 seconds (even success messages)
  const existingPopups = document.querySelectorAll(".popup");
  existingPopups.forEach(popup => {
    setTimeout(() => {
      popup.classList.add("slide-up");
      setTimeout(() => popup.remove(), 500);
    }, 3000);
  });

  // Form submit event listener
  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission

    // Check if all inputs are filled
    let allFilled = true;
    otpInputs.forEach((input) => {
      if (!input.value) {
        allFilled = false;
        input.focus();
        return;
      }
    });

    if (allFilled) {
      if (loader) loader.style.display = "flex";
      form.submit(); // Allow form submission
    } else {
      showPopup("Please fill all OTP fields.", "error");
    }
  });

  // Show loader on Resend OTP click
  if (resendLink) {
    resendLink.addEventListener("click", function (e) {
      e.preventDefault(); // Stop immediate navigation
      if (loader) loader.style.display = "flex"; // Show loader when "Resend OTP" is clicked

      // Simulate delay and then navigate (you can adjust the delay as needed)
      setTimeout(() => {
        window.location.href = resendLink.href; // Navigate after a short delay
      }, 500); // Adjust the delay time (500ms) for smoother loader display
    });
  }

  // Ensure the loader is hidden after the page reloads
  window.addEventListener('load', function () {
    loader.style.display = "none"; // Hide loader after page load
  });
});
