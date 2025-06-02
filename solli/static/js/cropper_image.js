document.addEventListener('DOMContentLoaded', function () {
    var image = document.getElementById('imagePreview');
    var input = document.getElementById('id_image');
    var cropper;

    if (!image || !input) return; // evita erros se os elementos não existirem

    input.addEventListener('change', function (e) {
        var files = e.target.files;
        if (files && files.length > 0) {
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
