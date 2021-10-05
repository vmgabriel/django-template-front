document.addEventListener("DOMContentLoaded", (event) => {
  const showNavbar = (toggleId, navId, bodyId, headerId) => {
    const toggle = document.getElementById(toggleId);
    const nav = document.getElementById(navId);
    const bodypd = document.getElementById(bodyId);
    const headerpd = document.getElementById(headerId);
    const menu = document.getElementById("menu");
    const profile = document.getElementById("profile");

    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd) {
      toggle.addEventListener("click", () => {
        nav.classList.toggle("show");
        toggle.classList.toggle("bi-x-lg");
        bodypd.classList.toggle("body-pd");
        headerpd.classList.toggle("body-pd");
      });
    }
  };

  showNavbar("header-toggle", "nav-bar", "body-pd", "header");
  const linkColor = document.querySelectorAll(".nav_link");

  function colorLink() {
    if(linkColor) {
      linkColor.forEach(l => l.classList.remove("active"));
      this.classList.add("active");
    }
  }

  linkColor.forEach(l => l.addEventListener("click", colorLink));
});
