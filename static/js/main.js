function toggleMenu() {
  const nav = document.getElementById("navMenu");
  const isOpen = nav.classList.toggle("active");

  document.documentElement.classList.toggle("no-scroll", isOpen);
  document.body.classList.toggle("no-scroll", isOpen);
}
document.querySelectorAll(".nav-links a").forEach(link => {
  link.addEventListener("click", () => {
    document.getElementById("navMenu").classList.remove("active");
    document.documentElement.classList.remove("no-scroll");
    document.body.classList.remove("no-scroll");
  });
});
const inputs = document.querySelectorAll("input, textarea");
const menuBtn = document.querySelector(".menu-btn");

inputs.forEach(el => {
  el.addEventListener("focus", () => {
    menuBtn.style.opacity = "0";
    menuBtn.style.pointerEvents = "none";
  });

  el.addEventListener("blur", () => {
    menuBtn.style.opacity = "1";
    menuBtn.style.pointerEvents = "auto";
  });
});

