import time
from urllib.parse import quote

import requests
from flask import Blueprint, current_app
from flask import request
from flask.views import View
from bs4 import BeautifulSoup

from main.models import Response, Metrics

scrap_google = Blueprint('scrap_google', __name__)

metrics = []


def get_search_data(search: str) -> dict:
    """
    Função que retorna os 5 primeiros links da pesquisa do Google

    :param search: Texto a ser buscado na pesquisa do Google
    :return: Um dicionário com o termo pesquisado e os primeiros 5 links da pesquisa do Google
    """
    links = []
    url = current_app.config['GOOGLE_URL'] + f"/search?q={quote(search)}"
    headers = current_app.config['BROWSER_HEADER']
    s = requests.Session()
    response = s.get(url, allow_redirects=True, timeout=30, headers=headers)
    body = response.text
    soup = BeautifulSoup(body, 'html.parser')
    for result in soup.select('.tF2Cxc', limit=5):
        links.append(result.select_one('.yuRUbf a')['href'])
    return Response(search_text=search, links=links)


class ScrapGoogleSearchView(View):
    """
    View que faz uma busca no Google,
    e retorna os 5 primeiros links que o Google respondeu.
    Possui suporte para multiplas pesquisas simultâneas.
    Ex: search=teste1&search=teste2&...
    """
    def dispatch_request(self):
        global metrics
        search = request.args.getlist("search")
        if not search:
            return {"error": "Parâmetros obrigatórios não informados!"}
        start = time.time()
        data = [get_search_data(x) for x in search]
        end = time.time()
        metrics.append(Metrics(search_text=search, response_time=end-start))
        return data


class GetMetricsView(View):
    """
    Metricas das requisições da view `ScrapGoogleSearchView`
    """
    def dispatch_request(self):
        global metrics
        return metrics


scrap_google.add_url_rule(
    "/scrap-google-search",
    view_func=ScrapGoogleSearchView.as_view("scrap_list")
)
scrap_google.add_url_rule(
    "/metrics",
    view_func=GetMetricsView.as_view("metrics_list")
)
