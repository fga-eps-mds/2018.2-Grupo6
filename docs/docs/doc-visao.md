---
id: doc-visao
title: Documento de Visão
sidebar_label: Documento de Visão
---

# Documento de Visão

### Sumário

1. Introdução
* 1.1 Propósito
* 1.2 Escopo
* 1.3 Definições, acrônimos e abreviações
* 1.4 Referências
* 1.5 Visão Geral

2. Posicionamento
* 2.1 Oportunidade de Negócio
* 2.2 Descrição do Problema
* 2.3 Instrução de Posição do Produto

3. Descrições da parte interessada e dos usuários

* 3.1 Demográficos de Mercado
* 3.2 Resumo da Parte Interessada
* 3.3 Resumo de Usuários
* 3.4 Ambiente do Usuário
* 3.5 Perfil dos Envolvidos
    * 3.5.1 Equipe de Desenvolvimento
    * 3.5.2 Equipe de Gestão de Projeto
* 3.6 Perfil dos Usuários
    * 3.6.1 Compradores
    * 3.6.2 Vendedores
* 3.7 Principais Necessidades dos Usuários e dos Envolvidos

4. Visão Geral do Produto
5. Recursos do Produto
6. Restrições

* 6.1 Restrições de Design
* 6.2 Restrições de Implementação
* 6.3 Restrições de Segurança
* 6.4 Restrições de Uso

### 1. Introdução
#### 1.1 Propósito
Esse documento de visão tem como objetivo estabelecer e declarar todos os propósitos e parâmetros para o desenvolvimento do aplicativo *mobile* iFoodFGA, que será desenvolvido para o sistema Android, e as demais finalidades serão descritas a seguir.

#### 1.2 Escopo
Esse projeto tem como finalidades, fazer a conexão entre vendedores autônomos de produtos alimentícios, e os potenciais compradores. Para facilitar o contato entre ambos, e também a dinâmica de vendas utilizadas pelos vendedores.

#### 1.3 Definições, acrônimos e abreviações
* FGA - Faculdade do Gama.
* UnB - Universidade de Brasília.
* RU - Restaurante Universitário.
* MDS - Métodos de Desenvolvimento de Software.
* EPS - Engenharia de Projeto de Software.
* Vendedores - Estudantes que realizam a atividade autônoma de vendas no ambiente acadêmico como forma de renda extra.
* Compradores - Estudantes interessados em comprar tais produtos.
* Produtos - Produtos vendidos pelos vendedores, geralmente de cunho alimentício como cupcakes, bombons e etc.
* App - Aplicativo *mobile*, para o sistema Android.
* Projeto - Projeto do aplicativo iFoodFGA.
* Tag - O que divide produtos especificos em categorias.

#### 1.4 Referencias
IBM Knowledge Center - Documento de Visão: Estruturas de um Documento de Visão.
Disponível em: https://www.ibm.com/support/knowledgecenter/pt-br/SSWMEQ_4.0.6/com.ibm.rational.rrm.help.doc/topics/r_vision_doc.html
Acesso em: 30 de Agosto de 2018.

MENDES, Mariana et al. Projeto Dr. Down: Documento de Visão.
Disponível em: <https://fga-eps-mds.github.io/2018.1-Dr-Down/>
Acesso em: 28 de Agosto de 2018.

HIROSHI, Lucas et al. Projeto Receita Mais: Documento de Visão.
Disponível em: <https://github.com/fga-eps-mds/2017.2-Receita-Mais>
Acesso em: 30 de Agosto de 2018.

#### 1.5 Visão Geral
Este documento está sendo estruturado com 6 tópicos.
1. Introdução: Onde é apresentado a visão para o projeto
2. Posicionamento: Declara o problema, a descrição do produto, além da oportunidade de negócio.
3. Descrições da parte interessada e dos usuários: Quem seriam nossos possíveis usuários para o App.
4. Visão Geral do Produto: Especifica o produto como ele realmente é, de forma geral e mais ampla.
5. Recursos do Produto: Funções e capacidades do App.
6. Restrições: Restrições de design, implementação, segurança e uso.

### 2. Posicionamento
#### 2.1 Oportunidade de Negócio
Atualmente no ambiente acadêmico da FGA-UnB, muitos estudantes utilizam de atividades autônoma de venda de produtos para acrescentar como uma renda extra. Porém a forma de comunicação entre esses vendedores com os potenciais compradores se resume ao contato pessoal no horário do almoço, onde os vendedores passam de mesa em mesa no RU, oferecendo seus produtos para os outros estudantes.

Nosso projeto tem como objetivo fazer com que essa comunicação seja mais fluída e eficiente entre os vendedores e compradores, através de um App, que fará a comunicação e possibilitará o encontro de ambos, para assim agilizar e melhorar o harmonia no ambiente acadêmico, que por sua vez se depara com pessoas, às vezes, incomodadas por não estarem interessadas em comprar quaisquer produtos.

O vendedor ficará mais confortável por ter todos seus produtos exibidos no App, e o comprador terá a comodidade de poder se comunicar com o vendedor o horário mais propicio para realizar a compra.

#### 2.2 Descrição do Problema
Após uma entrevista breve com a vendedora Priscila, foram apresentadas algumas dificuldades que ela sofre no dia a dia, principalmente por essa falta de um veículo para comunicação entre ela e seus clientes. Ela expôs que além do trabalho cansativo de passar em todas as mesas do RU, algumas pessoas a tratam com certa ignorância, por ela acabar passando mais de uma vez pelas mesas. Foi dito por ela também que, os seus clientes por vezes, não vão até ela comprar seus produtos.

|Descrição do Problema|O que afeta|Impacto disso|Solução viável|
|---------------------|-----------|-------------|--------------|
|Falha na comunicação entre compradores e vendedores|Realização das vendas|Vendas prejudicadas, desgaste físico do vendedor na procura por compradores, demandando um tempo considerável para a venda|Um meio de comunicação simples para propiciar o encontro de vendedores com possiveis compradores e a criação de uma forma prática de *marketing* para os interessados|

#### 2.3 Instrução de Posição do Produto
Para que os estudantes vendedores e os compradores que sofrem com a falta de um veículo de comunicação. O iFoodFGA, vem com o objetivo de servir como uma ponte de comunicação entre essas duas entidades (compradores e vendedores) a fim de melhorar o encontro e o comércio de produtos no ambiente acadêmico. Uma solução viável para isso, seria serviços como *chat*, uma ferramenta para compartilhamento de localização, e também uma listagem de todos os produtos que são oferecidos pelos vendedores, divididos por vendedores ou *tags* no sistema de busca.

### 3. Descrições da Parte Interessada e dos Usuários
#### 3.1 Demográficos de Mercado
Atualmente a FGA comporta milhares de discentes, sendo que alguns dividem a jornada acadêmica com o comércio de produtos pela faculdade como uma forma de obter dinheiro durante esse período. Com o objetivo de estreitar a relação entre os compradores e os vendedores, esse projeto propõe-se a atingir os frequentadores da FGA e apresentar uma solução para facilitar o processo de venda de mercadorias — doces, sobremesas, marmitas, etc. — dentro da faculdade.

#### 3.2 Resumo da Parte Interessada
|Grupo|Descrição|Responsabilidade|
|-|-|-|
|Equipe de Desenvolvimento|Estudantes da disciplina de MDS, UnB-FGA.|Documentar, desenvolver, testar e implementar a aplicação.|
|Equipe de Processos de Software|Estudantes da disciplina de EPS, UnB-FGA.|Coordenar, auxiliar e orientar a equipe de desenvolvimento de software, além de fundamentar o projeto.|
|Cliente|Compradores/Vendedores de produtos na FGA.|Levantar os requisitos do software.|
|Coachs|Estudantes da UnB, monitores da matéria de GPP/MDS.|Auxiliar e retirar dúvidas das equipes de desenvolvimento e gestão.|
|Professora|Professora do curso de Engenharia de Software, UnB-FGA.|Orientar e avaliar os trabalhos realizados pelas equipe de MDS e EPS.|

#### 3.3 Resumo de Usuários
|Grupo|Descrição|Responsabilidade|
|-|-|-|
|Comprador|Pessoa interessada em realizar a compra de produtos na FGA.|Solicitar o serviço por meio da aplicação.|
|Vendedor|Pessoa que disponibiliza um menu com os itens a ser vendidos na FGA.|Cadastrar produtos e efetivar a compra em dado local junto ao comprador.|

#### 3.4 Ambiente do Usuário
Dispositivos móveis:

Sistema | Versão
:-----: | :------:
Android | >= 4.1 (API 16)
iOs | >= 9.0

A aplicação estará ativa por parte do vendedor durante o seu período de atividade na faculdade indicando sua disponibilidade.

#### 3.5 Perfil dos Envolvidos
##### 3.5.1 Equipe de Desenvolvimento
|Representantes|André Pinto, Dâmaso Pereira, Gustavo Lima, Leonardo Medeiros, Shayane Alcântara, Welison Almeida|
|-|-|
|**Descrição**|Desenvolvedores.|
|**Tipo**|Estudantes da FGA da disciplina de MDS.|
|**Responsabilidade**|Desenvolvimento, documentação, implementação e Testes do _software_.|
|**Critérios de Sucesso**|Concluir devidamente o _software_ e disponibilizá-lo ao público-alvo.|
|**Envolvimento**|Alto.|
|**Problemas/Comentários**|Inexperiência em relação às linguagens, metodologias e paradigmas que serão aplicadas ao projeto.|

##### 3.5.2 Equipe de Gestão de Projeto
|Representantes|Lucas Costa, Lucas Pereira, Ricardo Canela, Wesley Araujo|
|-|-|
|**Descrição**|Gerenciamento de projeto.|
|**Tipo**|Estudantes da FGA da disciplina de GPP.|
|**Responsabilidade**|Coordenar, auxiliar e orientar a equipe de desenvolvimento de software, além de fundamentar o projeto.|
|**Critérios de Sucesso**|Gerir adequadamente o desenvolvimento, tratar riscos e entregar o produto.|
|**Envolvimento**|Alto.|
|**Problemas/Comentários**|-|

#### 3.6 Perfil dos Usuários
##### 3.6.1 Compradores
|Representante|Compradores|
|-|-|
|**Descrição**|Pessoa interessada em comprar produtos de vendedores autônomos presentes na faculdade.|
|**Tipo**|Comprador.|
|**Responsabilidade**|Solicitar o serviço e dispor informações ao vendedor quanto à localização da realização da venda.|
|**Critérios de Sucesso**|Comunicação efetiva e entrega do produto.|
|**Envolvimento**|Alto.|
|**Problemas/Comentários**|Não possuir um _smartphone_ com os pré-requisitos elecandos ou não ter acesso à internet.|

##### 3.6.2 Vendedores
|Representante|Vendedores|
|-|-|
|**Descrição**|Pessoa que vende seus produtos na FGA.|
|**Tipo**|Vendedor.|
|**Responsabilidade**|Disponibilizar um menu de mercadorias e encaminhar-se ao comprador para firmar a venda.|
|**Critérios de Sucesso**|Comunicação efetiva e entrega do produto.|
|**Envolvimento**|Alto.|
|**Problemas/Comentários**|Não possuir um _smartphone_ com os pré-requisitos elecandos ou não ter acesso à internet.|

#### 3.7 Principais Necessidades dos Usuários e dos Envolvidos
|Necessidade|Interesse|Solução Proposta|
|-|-|-|
|**Apresentar a oferta**|Estabelecer um meio eficiente para os compradores terem informações sobre os produtos disponíveis.| Disponibilizar na aplicação um menu com os produtos associados ao vendedor.|
|**Facilitar a compra**|Apresentar a disponibilidade do vendedor para efetivar a venda, abranger a comunicação entre comprador e vendedor.|Sistema de pedidos com recurso de comuniçação que possibilitará ao comprador combinar a entrega do produto e efetivar a compra.|

### 4. Visão Geral do Produto
#### 4.1 Perspectiva do Produto
O sistema Mercadão FGA funcionará como uma ferramenta facilitadora para a comunicação com fins comerciais e a locomoção de vendedores e consumidores na Faculdade do Gama, por meio de uma plataforma mobile. Os usuários da plataforma, poderão dispor de funções como cadastro de produtos, agendamento de entregas, serviço de *chat* entre o vendedor e o cliente e divulgação de promoções.

#### 4.2 Resumo das Capacidades:
 Benefício para o cliente | Recursos
:------------------------: | :-------------:
A plataforma é clara e simples, fazendo com que o acesso seja fácil e sem complicações | *Design* simples e intuitivo
A comunicação é facilitada por um *chat* entre o vendedor e o cliente, possibilitando escolhas flexíveis | *Chat* incluso na plataforma.
O gerenciamento de produtos em estoque pode vir a melhorar o controle de vendas e possíveis estudos para demandas futuras | Funcionalidade de alteração da quantidade de produtos em estoque, visível para possíveis clientes
Garantia de entrega do produto na opção mais viável para o cliente e vendedor | Negociação na plataforma de optar pela escolha do local de entrega
Datas específicas podem receber preço promocional definidas pelo vendedor | Funcionalidade de alteração de preços na plataforma

#### 4.3 Suposições e Dependências:
Suposição | Solução
:-------: | :------:
Caso o *chat* não seja implementado | Incluir número de telefone do vendedor para comunicação por plataforma externa

#### 4.4 Licenciamento e Instalação
A aplicação *mobile* será disponibilizada por meio da plataforma *Google Play*, que disporá de download simples e intuitivo para uma boa usabilidade das funcionalidades.

### 5. Recursos do Produto
#### 5.1 Cadastro
Tanto o vendedor como o consumidor realizarão um cadastro na plataforma para acessar o serviço comercial.

#### 5.2 Login
A autenticação do usuário será realizada mediante *login*.

#### 5.3 Cadastro de produtos e descrição
O vendedor poderá cadastrar os produtos desejados, definir preços, adicionar fotos e incrementar com informações complementares, se julgar necessário.

#### 5.4 Alteração de produtos cadastrados
O vendedor poderá alterar dados, características e preços de seus produtos, como exemplo, em futuras promoções.

#### 5.5 Catálogo de produtos
O vendedor poderá contar com uma lista de seus produtos visível para os possíveis clientes, através de uma pesquisa por perfil do vendedor.

#### 5.6 Pesquisa por categoria de produto
O cliente poderá realizar uma pesquisa por categoria de produto, por meio de tags previamente definidas pelos vendedores na descrição de seus produtos.

#### 5.7 Pedido e entrega
O cliente poderá assinalar o interesse pelo produto, fazendo o pedido e logo em seguida, negociando com o vendedor o local de encontro para entrega do produto em questão.

### 6. Restrições

#### 6.1 Restrições de Design

#### 6.2 Restrições de Implementação

#### 6.3 Restrições de Segurança

#### 6.4 Restrições de Uso
