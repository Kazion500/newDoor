uploadFile();
function uploadFile() {
const imgHulgFile = document.querySelector(".imgHulgFile");
const imgFileToChange = document.getElementById("imgFileToChange");
const imageUpload = document.getElementById("image_upload");
// Multiple images preview in browser
var imagesPreview = function (input, placeToInsertImagePreview) {
    if (input.files) {
        switch(input.files[0].type){
        case "application/pdf":
            alert("Document should be type of Png, Jpeg, Jpg only");
            return false;

        case "video/x-ms-wmv":
            alert("Document should be type of Png, Jpeg, Jpg only");
            return false;

        case "video/mp4":
            alert("Document should be type of Png, Jpeg, Jpg only");
            return false;

        case !"image/jpeg":
            alert("Document should be type of Png, Jpeg, Jpg only");
            return false;

        case !"image/png":
            alert("Document should be type of Png, Jpeg, Jpg only");
            return false;

        case !"image/jpg":
            alert("Document should be type of Png, Jpeg, Jpg only");
            return false;

        case "video/x-matroska":
            alert("Document should be type of Png, Jpeg, Jpg only");
            return false;
        }

    let reader = new FileReader();

    reader.onload = function (event) {
        imgFileToChange.src = event.target.result;
        imgFileToChange.style.borderRadius = "6px";
        imgHulgFile.style.width = "250px";
        imgHulgFile.style.marginBottom = "7rem";
    };

    reader.readAsDataURL(input.files[0]);

    }
};

imageUpload.addEventListener("change", () => {
    imagesPreview(imageUpload, imgHulgFile);
});
}