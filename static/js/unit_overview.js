// OPERATIONS

addColorToButtons();
calculateDueAmount();
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

      case "user verification pending":
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
    if(!isNaN(nums)){
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

function calculateAmountCollected() {
  let totalAmounts = [];
  const amounts = document.querySelectorAll(".amount");
  const totalDueAmounts = document.getElementById("totalDueAmounts");

  amounts.forEach((amount) => {
    let nums = amount.innerText.trim().replace(",", "").split(" ");
    totalAmounts.push(nums);
    console.log(totalAmounts);

    // remainDues.push(nums);
  });

  // // Calculate Sum
  function sum(arr) {
    return arr.reduce(function (a, b) {
      return parseInt(a) + parseInt(b);
    }, 0);
  }
  totalAmounts.forEach((val, index) => {
    console.log(sum(val));
    for (let i = 0; i < totalAmounts.length; i++) {
      amounts[i].textContent = sum(val);
    }
  });
}
// function calculateTotalEarning(){
//   let amounts = []
//   const totalEarnings = document.querySelectorAll('.total_earning')
//   totalEarnings.forEach((totalEarning)=>{
//     totalEarning.innerText.replace('$','').replace("$",'').split(' ')
//     console.log(totalEarning.innerText.replace('$','').replace("$",''));
//   })
// }
