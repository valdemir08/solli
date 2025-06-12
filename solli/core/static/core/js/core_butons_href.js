document.addEventListener('DOMContentLoaded', () => {
    const setupRedirectButton = (buttonId) => {
        const button = document.getElementById(buttonId);
        if (button) {
            const url = button.dataset.url;
            if (url) {
                button.addEventListener('click', () => {
                    window.location.href = url;
                });
            }
        }
    };

    setupRedirectButton('btn_create_acount');
    setupRedirectButton('btn_login_acount');
});
