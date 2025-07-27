
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('button');
    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const nome = button.getAttribute('car') || 'Nome desconhecido';
            alert(`O carro ${nome} foi vendido!`);
        });
    });
});
