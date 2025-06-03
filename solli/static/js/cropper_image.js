document.addEventListener('DOMContentLoaded', function () {
    var image = document.getElementById('image_preview');
    var tips = document.getElementById('image_crop_tips');
    var title = document.getElementById('title_pvw');
    var input = document.getElementById('id_image');
    var cropper;

    if (!image || !input) return; // evita erros se os elementos não existirem

    input.addEventListener('change', function (e) {
        var files = e.target.files;
        if (files && files.length > 0) {
            tips.classList.remove('hidden');
            title.classList.remove('hidden');
            var file = files[0];
            var url = URL.createObjectURL(file);

            image.src = url;


            if (cropper) {
                cropper.destroy();
            }

            cropper = new Cropper(image, {
                aspectRatio: 1,
                viewMode: 1,
                autoCropArea: 1,
                movable: true,
                zoomable: true,
                rotatable: false,
                scalable: false,
            });
        }
    });
});
