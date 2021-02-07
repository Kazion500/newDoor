
export function deleteFunc(whatToDelete, baseUrl, redirectUrl,completionMessage) {
    const deleteBtns = document.querySelectorAll(".btn-delete");
    const confirmation = document.querySelector(".confirmation");
    const modalBody = document.querySelector(".modal-body");
    const show = document.querySelector(".show");
    const message = document.querySelector(".message");
    let url;
  
    deleteBtns.forEach((deleteBtn, index) => {
      deleteBtn.addEventListener("click", (e) => {
        const pk = deleteBtn.dataset.pk;
        const name = deleteBtn.dataset.name
        // modalBody.textContent = `Are you sure you want to delete unit flat number ${name}?`;
        modalBody.textContent = `Are you sure you want to delete ${whatToDelete} ${name}?`;
        // url = `/delete-unit/${pk}`;
        url = baseUrl+'/'+pk;
      });
    });
    confirmation.addEventListener("click", (e) => {
      e.preventDefault();
      $.ajax({
        url: url,
        method: "GET",
        success(data) {
          show.style.display = "block";
          message.textContent = `Congratulations...! ${completionMessage} successfully deleted`;
          setTimeout(() => {
            location.pathname = redirectUrl;
          }, 3000);
        },
      });
    });
  }
  