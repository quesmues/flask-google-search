# Flask Google Search

Versão síncrona do projeto "Flask Google Search Async", o projeto é uma API de Web Scrapping, onde é retornado os 5 primeiros links da pesquisa do Google conforme a pesquisa informada.

## Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **Implantação** para saber como implantar o projeto.

### Pré-requisitos

Instale o Python 3.10.


### Instalação

Para rodar o projeto em seu computador, primeiro instale os depências com:

```
pip install -r flask_api/requirements.txt
```

Após isso rodar o Flask em modo de desenvolvimento:

```
python flask_api/app.py
```

Para verificar se o projeto está rodando abra no seu navegador e insira o endereço abaixo.

```
http://127.0.0.1:8000/api/v1/scrap-google-search?search=teste
```

Caso retorne os 5 links o projeto está rodando.

Exemplo:
```
["https://www.speedtest.net/pt",
"https://fast.com/pt/",
"https://www.minhaconexao.com.br/",
"https://www.nperf.com/pt/",
"https://melhorescolha.com/speedtest/"]
```

## Endpoints
O endpoint "api/v1/scrap-google-search" possui um parâmetro obrigatório que é o "search" utilizado para realizar a pesquisa no Google.
Possui suporte para múltiplas pesquisar, exemplo: "search=teste1&search=teste2&..."

```
http://127.0.0.1:8000/api/v1/scrap-google-search?search=test
```

E o endpoint das métricas do sistemas, retorna o tempo médio e o termo de pesquisa para cada requisição.
Obs: As métricas não são compartilhadas entre os processos (workers), ou seja, o resultado irá variar caso seja usado mais de um worker.
```
http://127.0.0.1:8000/api/v1/metrics
```

## Implantação

Para implementar um servidor produtivo, instalar o docker e executar o comando abaixo:

```
docker-compose up -d --build
```

A imagem será construida e o projeto estará rodando em um container.

Ou se prefir utilizar um servidor produtivo que tenha suporte para uso do Flask com WSGI.

Exemplo com o gunicorn:

```
gunicorn -w 4 -b 0.0.0.0 'flask_api/app:app'
```

Lembrando que o "flask_api/app" é o módulo em que o app WSGI do flask está.


## Tests

Os tests foram feitos utilizando o pytest, para executar apenas rodar o comando abaixo.

```
pytest
```



## Construído com

Flask, requests e BeaultifulSoap4.


## Autor

* **Eduardo Czamanski Rota** - *Trabalho Inicial* - [Eduardo C. Rota](https://github.com/quesmues)
