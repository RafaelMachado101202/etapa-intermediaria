const fetchMock = require('jest-fetch-mock');
fetchMock.enableMocks();

async function testarIntegracaoCEP(cep) {
    try {
        const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
        const data = await response.json();
        return data;
    } catch (error) {
        return null;
    }
}

describe('Integração com API ViaCEP', () => {
    beforeEach(() => {
        fetch.resetMocks();
    });

    test('Deve retornar a localidade correta (São Paulo) ao consultar um CEP válido', async () => {
        
        fetch.mockResponseOnce(JSON.stringify({
            localidade: 'São Paulo',
            uf: 'SP',
            erro: false
        }));

        const resultado = await testarIntegracaoCEP('01001000');

        expect(resultado.localidade).toEqual('São Paulo');
        expect(resultado.uf).toEqual('SP');
        expect(fetch).toHaveBeenCalledWith('https://viacep.com.br/ws/01001000/json/');
    });

    test('Deve identificar quando um CEP não existe', async () => {
        fetch.mockResponseOnce(JSON.stringify({ erro: true }));

        const resultado = await testarIntegracaoCEP('99999999');
        expect(resultado.erro).toBe(true);
    });
});