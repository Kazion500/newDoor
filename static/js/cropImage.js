

let fileInput = document.getElementById("imageUpload");
  let stagedDocs = document.querySelector(".staged-docs");
  let stagedDocsToUpload = document.querySelectorAll(".staged-docs");
  let docNames = document.querySelectorAll(".doc-name");
  let imagePreviewIcon = document.querySelector(".imagePreviewIcon");
  const url = `/upload-documents/{{ tenant.user.username }}`;


  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === name + "=") {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  const csrftoken = getCookie("csrftoken");
 

  uploadFile();

  function removeOperation(div,input){
    let closeBtns = document.querySelectorAll(".fa-times");
    let upload = document.querySelector(".fa-check-circle");
    
    closeBtns.forEach((closeBtn)=>{
      closeBtn.addEventListener('click',()=>{
        // file.remove
        div.remove()
        
        console.log(stagedDocs.children);
      
      })
    })
  }


  function uploadFile() {
    // Multiple images preview in browser
    var imagesPreview = function (input, placeToInsertImagePreview) {
      if (input.files) {
        var filesAmount = input.files.length;

        if (stagedDocs.children.length > 1) {
          alert("Only two(2) document allowed front and back are required");
          return false;
        }

        if (input.files.length > 2) {
          alert("Only two(2) document allowed front and back are required");
          return false;
        }

        for (i = 0; i < filesAmount; i++) {
          switch(input.files[i].type){
            case "application/pdf":
              alert("Document should be type of Png, Jpeg, Jpg only");
              return false;
            break

            case "video/x-ms-wmv":
              alert("Document should be type of Png, Jpeg, Jpg only");
              return false;
            break
            case "video/mp4":
              alert("Document should be type of Png, Jpeg, Jpg only");
              return false;
            break
            case !"image/jpeg":
              alert("Document should be type of Png, Jpeg, Jpg only");
              return false;
            break
            case !"image/png":
              alert("Document should be type of Png, Jpeg, Jpg only");
              return false;
            break
            case !"image/jpg":
              alert("Document should be type of Png, Jpeg, Jpg only");
              return false;
            break
            case "video/x-matroska":
              alert("Document should be type of Png, Jpeg, Jpg only");
              return false;
            break   
          }


          let reader = new FileReader();

          reader.onload = function (event) {
            imagePreviewIcon.style.display = "block";
            let div = document.createElement("div");
            div.classList.add("col-md-3", "gallery");
            let img = document.createElement("img");
            let iconWrapper = document.createElement("div");
            let iconClose = document.createElement("span");
            let iconUpload = document.createElement("span");
            let closeIcon = document.createElement("i");
            let uploadIcon = document.createElement("i");
            iconWrapper.classList.add("icon-wrapper");
            iconClose.setAttribute("id", "close");
            iconUpload.setAttribute("id", "upload");
            closeIcon.classList.add("fas", "fa-times", "text-danger");
            uploadIcon.classList.add("fas", "fa-check-circle", "text-success");
            // uploadIcon.setAttribute('data-file-name','');
            iconWrapper.appendChild(iconClose);
            iconWrapper.appendChild(iconUpload);
            iconClose.appendChild(closeIcon);
            iconUpload.appendChild(uploadIcon);
            img.setAttribute("src", event.target.result);
            img.setAttribute("alt", "imagePreview");
            img.setAttribute("id", "image");
            div.appendChild(img);
            div.appendChild(iconWrapper);
            placeToInsertImagePreview.appendChild(div);

            
            removeOperation(div,input)
            
          };
          
          reader.readAsDataURL(input.files[i]);
        }
      }
    };

    fileInput.addEventListener("change", () => {
      imagesPreview(fileInput, stagedDocs);      
    });

  }
  

(()=>{
  docNames.forEach((docName)=>{
    let start = docName.textContent.replace('MEDIA/DOCUMENTS/','').indexOf('_')
    docName.textContent = docName.textContent.replace('MEDIA/DOCUMENTS/','').slice(0,start)
  })
  
})() 