// Exemplo conceitual de teste de integração
test('Deve retornar a cidade correta ao consultar um CEP válido', async () => {
    const cep = '01001000';
    const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const data = await response.json();
    
    expect(response.status).toBe(200);
    expect(data.localidade).toBe('São Paulo');
});