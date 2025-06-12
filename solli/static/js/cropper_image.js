document.addEventListener('DOMContentLoaded', function () {
    var image = document.getElementById('image_preview');
    var input = document.getElementById('id_image');
    var form = input.closest('form');
    var cropper;

    if (!image || !input) return;

    input.addEventListener('change', function (e) {
        var files = e.target.files;
        if (files && files.length > 0) {
            var url = URL.createObjectURL(files[0]);
            image.src = url;

            if (cropper) {
                cropper.destroy();
            }

            cropper = new Cropper(image, {
                aspectRatio: 1,
                viewMode: 1,
                autoCropArea: 1,
            });
        }
    });

    // Listener do submit FORA do evento 'change'
    form.addEventListener('submit', function (e) {
        if (cropper) {
            e.preventDefault();  // para garantir que damos tempo de setar os hidden

            const cropData = cropper.getData();

            document.getElementById('crop_x').value = Math.round(cropData.x) || 0;
            document.getElementById('crop_y').value = Math.round(cropData.y) || 0;
            document.getElementById('crop_width').value = Math.round(cropData.width) || 300;
            document.getElementById('crop_height').value = Math.round(cropData.height) || 300;
            /**
            alert("Dados do crop:\n" +
                "x: " + Math.round(cropData.x) + "\n" +
                "y: " + Math.round(cropData.y) + "\n" +
                "width: " + Math.round(cropData.width) + "\n" +
                "height: " + Math.round(cropData.height));
            */

            form.submit();  // após setar os valores, envia o formulário
        }
    });

});
