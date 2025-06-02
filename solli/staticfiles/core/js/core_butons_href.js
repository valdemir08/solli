document.addEventListener('DOMContentLoaded', () => {
    const btn_create_acount = document.getElementById('btn_create_acount');
    if (btn_create_acount) {
        const url = btn_create_acount.dataset.url;
        btn_create_acount.addEventListener('click', () => {
            window.location.href = url;
        });
    }
});
