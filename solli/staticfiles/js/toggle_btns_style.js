document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".toggle-button");

  buttons.forEach((btn) => {
    btn.addEventListener("click", function () {
      buttons.forEach((b) => b.classList.remove("selected")); // Remove de todos
      this.classList.add("selected"); // Adiciona no clicado
    });
  });
});

