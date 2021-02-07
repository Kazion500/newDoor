export const deleteFunc = (endpoint, whatHasBeenDeleted, redirectUrl) => {
  const deleteBtns = document.querySelectorAll(".btn-delete");
  const confirmation = document.querySelector(".confirmation");
  const modalBody = document.querySelector(".modal-body");
  const show = document.querySelector(".show");
  const message = document.querySelector(".message");
  let url;

  deleteBtns.forEach((deleteBtn, index) => {
    deleteBtn.addEventListener("click", (e) => {
      const pk = deleteBtn.dataset.pk;
      const name = deleteBtn.dataset.name;
      modalBody.textContent = `Are you sure you want to delete ${name}?`;
      url = `${endpoint}/${pk}`;
    });
  });

  confirmation.addEventListener("click", (e) => {
    e.preventDefault();
    $.ajax({
      url: url,
      method: "GET",
      success(data) {
        show.style.display = "block";
        message.textContent = `Congratulations...! ${whatHasBeenDeleted} successfully deleted.`;
        setTimeout(() => {
          location.pathname = redirectUrl;
        }, 3000);
      },
    });
  });
};












