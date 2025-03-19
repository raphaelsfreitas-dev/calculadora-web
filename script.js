const display = document.getElementById('display');
const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        if (button.textContent === 'C') {
            display.value = '';
        } else if (button.textContent === '=') {
            // Envia o cálculo para o backend
            fetch('/calcular', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ expressao: display.value }),
            })
            .then(response => response.json())
            .then(data => {
                display.value = data.resultado;
            })
            .catch(() => {
                display.value = 'Erro';
            });
        } else {
            display.value += button.textContent;
        }
    });
});
