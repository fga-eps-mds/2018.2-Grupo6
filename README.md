# Integra - Vendas

![license mit](https://img.shields.io/badge/license-MIT-blue.svg) 
[![Build Status](https://travis-ci.org/fga-eps-mds/2018.2-Integra-Vendas.svg?branch=master)](https://travis-ci.org/fga-eps-mds/2018.2-Integra-Vendas)
[![docusaurus](https://img.shields.io/badge/doc-Docusaurus-blue.svg)](https://fga-eps-mds.github.io/2018.2-Integra-Vendas/)
[![pipeline status](https://gitlab.com/integra-vendas/api-gateway/badges/master/pipeline.svg)](https://gitlab.com/integra-vendas/api-gateway/commits/master)
[![codecov](https://codecov.io/gh/fga-eps-mds/2018.2-Integra-Vendas/branch/master/graph/badge.svg)](https://codecov.io/gh/fga-eps-mds/2018.2-Integra-Vendas)
[![Maintainability](https://api.codeclimate.com/v1/badges/4e252a288b50c256f6f9/maintainability)](https://codeclimate.com/github/fga-eps-mds/2018.2-Integra-Vendas/maintainability)

* [Documentação do Projeto Integra Vendas](https://fga-eps-mds.github.io/2018.2-Integra-Vendas/)


Vendas é um módulo do projeto Integra, que contempla a venda e troca de produtos dentro do ambiente acadêmico da UnB Faculdade Gama.

# Requisitos
* Docker

# Instalação
Para instalar a api-gateway basta realizar **make** dentro da pasta api.

```shell
cd api
make
```

# Executando
Dentro do docker execute, o script é necessário para que execute na porta correta com ip correto do localhost.
```shell
sh run-django.sh
```


# Repositorio dos microserviços
* [Microserviço login](https://github.com/fga-eps-mds/2018.2-FGAPP-login)
* [Microserviço produto](https://github.com/fga-eps-mds/2018.2-FGAPP-produto)
* [Microserviço vendas](https://github.com/fga-eps-mds/2018.2-FGAPP-vendas)
* [Microserviço notificação](https://github.com/integra-vendas/Notification-Microservice)

* [Front End](https://github.com/fga-eps-mds/2018.2-FGAPP-FrontEnd)
