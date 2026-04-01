# 🎯 Simulador de Pathfinding: Benchmark Tático (A*)

![HTML5](https://img.shields.io/badge/HTML5-UI%2FUX-orange?logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-Grid_Layout-blue?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-Vanilla-yellow?logo=javascript)

Este projeto é um simulador tático interativo e de alta fidelidade visual desenvolvido para testar, visualizar e realizar o *benchmark* de diferentes algoritmos de Busca de Caminhos (*Pathfinding*).

Ele aplica conceitos teóricos de Inteligência Artificial em um ambiente de malha 2D (*grid*) com geração procedimental, onde agentes autônomos precisam calcular rotas lidando com obstáculos rígidos e terrenos de custo variável.

---

## 🚀 Funcionalidades e Simulação

O *dashboard* coloca três abordagens clássicas de busca para competir em tempo real, gerando métricas exatas de **Passos Totais** e **Custo de Terreno**:

* 🟢 **A* (A-Estrela) | Rota Ótima:**O algoritmo definitivo de *pathfinding*. Ele calcula a rota perfeita avaliando tanto o custo real do caminho percorrido `g(n)` quanto a heurística de distância `h(n)`. O A* consegue decidir matematicamente se vale a pena desviar de um terreno difícil ou atravessá-lo.
* 🟠 **Busca Gulosa (Greedy) | Rota Mediana:** Uma abordagem focada puramente na heurística `h(n)`. Por ignorar o custo real do terreno `g(n)`, o algoritmo tenta ir "direto" para o alvo, frequentemente caindo em armadilhas e gerando rotas subótimas.
* 🔴 **DFS (Busca em Profundidade) | Pior Rota:** Demonstração do comportamento de uma busca cega. Sem noção de direção ou heurística, o algoritmo explora o mapa exaustivamente, resultando em caminhos sinuosos e um enorme desperdício de passos.

## 🗺️ Mecânicas do Ambiente (Topologia)

A cada vez que o sistema gera um novo mapa, ele sorteia a posição da Origem e do Destino garantindo uma distância mínima entre eles, e popula o cenário com:

* **Chão Livre (Azul-escuro):** Custo padrão de movimento = 1.
* **Paredes (Preto):** Obstáculos sólidos e intransponíveis.
* **Zonas de Risco (Roxo):** Terrenos com penalidade de movimento (Custo = 5). Força os algoritmos a repensarem as rotas diretas.

---

## 💻 Como Executar o Projeto

A grande vantagem da arquitetura deste projeto é que ele roda 100% do lado do cliente (*client-side*), sem necessidade de instalação de bibliotecas, pacotes ou servidores locais.

1. Faça o clone deste repositório ou baixe o arquivo `index.html`.
2. Dê um duplo clique no arquivo `index.html` para abri-lo em qualquer navegador web moderno (Chrome, Edge, Firefox, Safari).
3. No painel lateral, clique em **EXECUTAR ANÁLISE COMPLETA** para assistir à varredura e compilação das rotas em tempo real.
4. Utilize o botão **GERAR NOVA TOPOLOGIA** para resetar o ambiente com um novo labirinto procedimental.

---

## 🛠️ Stack Tecnológico e Arquitetura UI/UX

* **Interface Visual:** CSS3 moderno utilizando `CSS Grid` para a renderização exata da malha matemática, variáveis globais (`:root`) para controle do *High Contrast Mode* e animações de transição.
* **Motor Lógico:** JavaScript (Vanilla). O motor realiza cálculos assíncronos (utilizando `async/await` e `Promises`) para separar a execução da matemática pesada da renderização dos *frames* no DOM, criando o efeito visual de varredura sem travar o navegador.
