document.addEventListener('DOMContentLoaded', () => {
  const cnpjField = document.querySelector('#id_cnpj');
  if (cnpjField) {
    Inputmask({"mask": "99.999.999/9999-99"}).mask(cnpjField);
  }
});

