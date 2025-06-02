document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('btn_create_acount');
    if (btn) {
        const url = btn.dataset.url;
        btn.addEventListener('click', () => {
            window.location.href = url;
        });
    }
});
