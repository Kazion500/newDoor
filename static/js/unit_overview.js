// OPERATIONS

addColorToButtons();
calculateDueAmount();
deleteFunc();
// calculateTotalEarning()
// calculateAmountCollected()

// LOGIC

function addColorToButtons() {
  const occupancyTypes = document.querySelectorAll(".occupancy_type");
  occupancyTypes.forEach((occupancyType) => {
    const occupancyTypeText = occupancyType.textContent.trim().toLowerCase();

    switch (occupancyTypeText) {
      case "vacant":
        occupancyType.style.backgroundColor = "green";
        break;

      case "occupied":
        occupancyType.style.backgroundColor = "red";
        break;

      case "verification pending":
        occupancyType.style.backgroundColor = "greenyellow";
        occupancyType.style.color = "black";
        break;

      case "document pending":
        occupancyType.style.backgroundColor = "lightblue";
        occupancyType.style.color = "black";
        break;

      case "payment pending":
        occupancyType.style.backgroundColor = "#1f97c7";
        break;

      case "create contract":
        occupancyType.style.backgroundColor = "#000";
        break;

      case "document uploaded":
        occupancyType.style.backgroundColor = "#555";
        break;

      default:
        occupancyType.style.backgroundColor = "green";
        break;
    }
  });
}

function calculateDueAmount() {
  let remainDues = [];
  const remainAmounts = document.querySelectorAll(".remain_amount");
  const totalDueAmounts = document.getElementById("totalDueAmounts");
  remainAmounts.forEach((remainAmount) => {
    let nums = parseInt(
      remainAmount.innerHTML.trim().replace("$", "").replace(",", "")
    );
    if (!isNaN(nums)) {
      remainDues.push(nums);
    }
  });
  // Calculate Sum
  function sum(arr) {
    return arr.reduce(function (a, b) {
      return a + b;
    }, 0);
  }

  if (totalDueAmounts.innerText === "") {
    totalDueAmounts.innerText = "$" + sum(remainDues).toLocaleString();
  } else if (totalDueAmounts.innerText != "0") {
    totalDueAmounts.innerText = "$" + sum(remainDues).toLocaleString();
  } else {
    totalDueAmounts.innerText = "$" + 0;
  }
}

function trimAndReplace(str) {
  if (str.length > 10) {
    return str
      .trim()
      .replace("$", "")
      .replace(",", "")
      .replace(",", "")
      .replace(",", "");
  } else if (str.length > 6) {
    return str.trim().replace("$", "").replace(",", "").replace(",", "");
  } else if (str.length > 4) {
    return str.trim().replace("$", "").replace(",", "");
  } else {
    return str.trim().replace("$", "");
  }
}

// Calculate collected
(() => {
  const occupancyTypes = document.querySelectorAll(".occupancy_type");
  const rentalAmounts = document.querySelectorAll(".rental_amount");
  const remainAmounts = document.querySelectorAll(".remain_amount");
  const amounts = document.querySelectorAll(".amount");

  occupancyTypes.forEach((occupancyType, index) => {
    if (occupancyType.textContent.trim().toLowerCase() !== "occupied") {
      amounts[index].textContent = "";
    } else {
      amounts.forEach((amount, index) => {
        if (isNaN(trimAndReplace(remainAmounts[index].textContent))) {
          remainAmounts[index].textContent = "";
        }
        if (isNaN(trimAndReplace(rentalAmounts[index].textContent))) {
          rentalAmounts[index].textContent = "";
        }
        if (
          parseInt(trimAndReplace(rentalAmounts[index].textContent)) <=
          parseInt(trimAndReplace(remainAmounts[index].textContent))
        ) {
          amount.textContent =
            "$" + rentalAmounts[index].textContent.trim().toLocaleString();
        } else {
          const eachAmount =
            parseInt(trimAndReplace(rentalAmounts[index].textContent)) -
            parseInt(trimAndReplace(remainAmounts[index].textContent));
          if (!isNaN(eachAmount)) {
            amount.textContent = "$" + eachAmount.toLocaleString();
          }
        }
      });
    }
  });
})();

function deleteFunc() {
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
      modalBody.textContent = `Are you sure you want to delete unit flat number ${name}?`;
      url = `/delete-unit/${pk}`;
    });
  });
  confirmation.addEventListener("click", (e) => {
    e.preventDefault();
    $.ajax({
      url: url,
      method: "GET",
      success(data) {
        show.style.display = "block";
        message.textContent = `Congratulations...! Unit successfully deleted.`;
        setTimeout(() => {
          location.pathname = "/unit-overview/";
        }, 3000);
      },
    });
  });
}
