from django.test import Client


def test_status_code(client:Client): # Client é um objeto fornecido pelo django que simula requisições Http.
    resp = client.get('/') # Faz uma requisição na home do projeto.
    assert resp.status_code == 200 # Certifica que a resposta retornou com sucesso.