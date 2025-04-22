// mobile button toggler
document.getElementById("mobile-menu-button").addEventListener("click", function() {
    document.getElementById("mobile-menu").classList.toggle("hidden");
});  

// typewriter for banner
const typeText = (element, text, delay = 50, callback) => {
    let index = 0;
    const type = () => {
        if (index < text.length) {
        element.textContent += text.charAt(index);
        index++;
        setTimeout(type, delay);
        } else if (callback) {
        callback();
        }
    };
    type();
};

window.addEventListener("DOMContentLoaded", () => {
    const heading = document.getElementById("typewriter-heading");
    const paragraph = document.getElementById("typewriter-paragraph");

    if (heading || paragraph){
        typeText(heading, "Innovative Web & IT Solutions Tailored for You", 30, () => {
            setTimeout(() => {
            typeText(paragraph, "From idea to execution — we build for the business.", 30);
            }, 100);
        });
    }

    const toggleBtn = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');

    toggleBtn.addEventListener('click', () => {
      menu.classList.toggle('max-h-0');
      menu.classList.toggle('opacity-0');
      menu.classList.toggle('max-h-96');
      menu.classList.toggle('opacity-100');
    });
});


window.addEventListener('load', () => {
    document.getElementById("fade-out").id = "faded";
    console.log("fade-out element ID changed to faded");
  });

document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('mobile-menu-button');
    const menu = document.getElementById('mobile-menu');

    toggleBtn.addEventListener('click', () => {
        menu.classList.toggle('open');
    });
});


// tailwind font integration
tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
            Oranienbaum: ['Oranienbaum', 'serif']
        }
      }
    }
  }