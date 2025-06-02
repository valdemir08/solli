document.addEventListener('DOMContentLoaded', function () {
  const btn_pj = document.getElementById('btn_pj');
  const btn_pf = document.getElementById('btn_pf');
  const cnpj_field = document.getElementById('cnpj_field');
  const is_company_input = document.getElementById('id_is_company');

  btn_pj.addEventListener('click', function (e) {
    e.preventDefault();
    cnpj_field.style.display = 'block';
    is_company_input.value = 'True';

    btn_pj.classList.add('bg-emerald-100');
    btn_pf.classList.remove('bg-emerald-100');
  });

  btn_pf.addEventListener('click', function (e) {
    e.preventDefault();
    cnpj_field.style.display = 'none';
    is_company_input.value = 'False';
    cnpj_field.querySelector('input').value = '';

    btn_pf.classList.add('bg-emerald-100');
    btn_pj.classList.remove('bg-emerald-100');
  });

  // Inicializa o estado correto ao carregar a página
  if (is_company_input.value === 'True') {
    cnpj_field.style.display = 'block';
    btn_pj.classList.add('bg-emerald-100');
  } else {
    cnpj_field.style.display = 'none';
    btn_pf.classList.add('bg-emerald-100');
  }
});
