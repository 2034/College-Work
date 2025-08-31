// Config
const imgFolder = "img/pictures/";
const imgData = {
    files: ["img1.jpg","https://www.youtube.com/embed/o1KeIrwO8wo?si=3NQy13CZjYO1kC2v", "https://www.youtube.com/embed/o1KeIrwO8wo?si=3NQy13CZjYO1kC2v", "https://www.youtube.com/embed/o1KeIrwO8wo?si=3NQy13CZjYO1kC2v"],
    names: ["Image 1","Video 1", "Video 2", "Video 3"]
};


/* 

Last Edited: 25/04/25

Explaination for this: 
extractYouTubeID function is what is used for the thumbnails of the videos.
DOM just dynamically creates images and videos from the imgData tbl.


References:
Fetched this regex from https://github.com/thanhphandev/youtube-bot/blob/a19dd262c577267354db69d8bf8886c472bf5b2a/src/common/validator.py#L12
*/

function extractYouTubeID(url) {
    const match = url.match(/(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)/);
    return match ? match[1] : "";
}

document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("image-modal");
    const modalImage = document.getElementById("modal-image");
    const modalVideo = document.getElementById("modal-video");
    const captionText = document.getElementById("caption");
    const closeBtn = document.querySelector(".close");

    const openModal = (mediaSrc, caption, isVideo) => {
        modal.style.display = "block";
        captionText.textContent = caption;

        if (isVideo) {
            modalImage.style.display = "none";
            modalVideo.style.display = "block";
            modalVideo.src = mediaSrc;
        } else {
            modalVideo.style.display = "none";
            modalImage.style.display = "block";
            modalImage.src = mediaSrc;
        }
    };

    const workPreviewContainer = document.querySelector(".work-preview-container");
    imgData.files.forEach((file, index) => {
        const collectionPreview = document.createElement("div");
        collectionPreview.className = "collection-preview";
        collectionPreview.style.animation = "500ms ease 400ms 1 normal forwards running fadeIn";
    
        const imgButton = document.createElement("button");
        imgButton.id = file.split(".")[0];
        imgButton.className = "collection-preview-button";
    
        const isVideo = file.startsWith("http");
        let imgElement;
    
        if (!isVideo) {
            imgElement = document.createElement("img");
            imgElement.src = `${imgFolder}${file}`;
            imgElement.className = "collection-image";
            imgElement.alt = `${file.split(".")[0]} Logo`;
        } else {
            imgElement = document.createElement("div");
            imgElement.className = "collection-video";
            imgElement.style.backgroundImage = `url('https://img.youtube.com/vi/${extractYouTubeID(file)}/hqdefault.jpg')`; // YouTube thumbnail
            imgElement.style.backgroundSize = "cover";
            imgElement.style.backgroundPosition = "center";
        }
    
        const infoContainer = document.createElement("div");
        infoContainer.className = "collection-preview-info";
        const nameElement = document.createElement("div");
        nameElement.className = "collection-preview-name";
        nameElement.textContent = imgData.names[index];
        infoContainer.appendChild(nameElement);
        imgButton.appendChild(imgElement);
        imgButton.appendChild(infoContainer);
        collectionPreview.appendChild(imgButton);
        workPreviewContainer.appendChild(collectionPreview);
        imgButton.addEventListener("click", () => {
            const mediaSrc = isVideo ? (file.startsWith("http") ? file : `${imgFolder}${file}`) : `${imgFolder}${file}`;
            openModal(mediaSrc, imgData.names[index], isVideo);
        });
    });

    closeBtn.addEventListener("click", () => {
        modal.style.display = "none";
        modalVideo.src = "";
    });

    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
            modalVideo.src = "";
        }
    });
});