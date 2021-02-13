deleteFunc();
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
      modalBody.textContent = `Are you sure you want to delete ${name}?`;
      url = `/delete-property/${pk}`;
    });
  });
  confirmation.addEventListener("click", (e) => {
    e.preventDefault();
    $.ajax({
      url: url,
      method: "GET",
      success(data) {
        show.style.display = "block";
        message.textContent = `Congratulations...! Property successfully deleted.`;
        setTimeout(() => {
          location.pathname = "/property-overview/";
        }, 3000);
      },
    });
  });
}

// trim and replace
function trimAndReplace(str) {
  if (str.length > 4) {
    return str.trim().replace("$", "").replace(",", "");
  } else {
    return str.trim().replace("$", "");
  }
}

// Calculate totalDues

(() => {
  const totalUnitAmount = document.querySelector(".totalUnitAmounts");
  const totalDueAmount = document.querySelector(".totalDueAmount");
  const totalCollectedAmount = document.getElementById("totalCollectedAmount");
  if(parseInt(trimAndReplace(totalCollectedAmount.textContent))== 0 || parseInt(totalUnitAmount.textContent) == 0 ){
    totalDueAmount.textContent = "$"+0 ;
    return false
  }else{
    const totaldues =
    parseInt(totalUnitAmount.textContent) -
    parseInt(trimAndReplace(totalCollectedAmount.textContent));
    totalDueAmount.textContent = "$" + totaldues.toLocaleString();
  }
})();

// Calculate totalDue

(() => {
  const collectedAmounts = document.querySelectorAll('.collectedAmount')
  const dueAmounts = document.querySelectorAll('.dueAmount')
  const totalUnitAmount = document.querySelector('.totalUnitAmounts')

  function sum(arr) {
    return arr.reduce(function (a, b) {
      return a + b;
    }, 0);
  }

  collectedAmounts.forEach((collectedAmount,index)=>{
    const collectedArray = collectedAmount.innerText.trim().trim().split(' ')
    let newCollectedAmount = collectedArray.map((num,index)=>{
      
      return parseInt(num)
      
    })
    let total = sum(newCollectedAmount)

    if(!isNaN(total)){
      collectedAmounts[index].textContent = "$"+total.toLocaleString()
    }

    collectedAmounts[index].textContent.trim().replace('$','').replace(',','')
    const totalAmount = parseInt(totalUnitAmount.textContent)
    const totalDuesAmount = totalAmount - parseInt(collectedAmounts[index].textContent.trim().replace('$','').replace(',',''))

    if(!isNaN(totalDuesAmount)){
      dueAmounts[index].textContent ="$"+totalDuesAmount.toLocaleString()
    }
  })

})();
