document.addEventListener('DOMContentLoaded', function () {
    const estateSelect = document.querySelector('#id_estate');
    const citySelect = document.querySelector('#id_city');

    // No começo, deixa o select de cidade desabilitado e com fundo cinza
    citySelect.disabled = true;
    citySelect.classList.add('bg-gray-100', 'cursor-not-allowed');

    estateSelect.addEventListener('change', function () {
        const estate = estateSelect.value;

        // Desabilita e estiliza o campo cidade enquanto carrega
        citySelect.disabled = true;
        citySelect.classList.add('bg-gray-100', 'cursor-not-allowed');
        citySelect.innerHTML = '<option value="">Carregando...</option>';

        fetch(`/get_cities/?estate=${estate}`)
            .then(response => response.json())
            .then(data => {
                citySelect.innerHTML = ''; // limpa o select

                // Adiciona a opção padrão, desabilitada e selecionada
                const defaultOption = document.createElement('option');
                defaultOption.value = '';
                defaultOption.textContent = 'Selecione uma cidade';
                defaultOption.disabled = true;
                defaultOption.selected = true;
                citySelect.appendChild(defaultOption);

                // Adiciona as cidades retornadas
                data.cities.forEach(city => {
                    const option = document.createElement('option');
                    option.value = city.id;
                    option.textContent = city.name;
                    citySelect.appendChild(option);
                });

                // Desbloqueia e remove a estilização cinza
                citySelect.disabled = false;
                citySelect.classList.remove('bg-gray-100', 'cursor-not-allowed');
            })
            .catch(error => {
                console.error('Erro ao buscar cidades:', error);
                citySelect.innerHTML = '<option value="">Erro ao carregar</option>';
            });
    });
});
