# DeskTest

# 🧪 Testes em Aplicações Gráficas Desktop com Python

Este repositório tem como objetivo demonstrar e explorar técnicas de **testes em aplicações gráficas desktop** desenvolvidas com **Tkinter** e **PyQt**. A proposta abrange diferentes tipos de testes, desde abordagens clássicas como **caixa branca** e **caixa preta**, 
até testes mais intensivos como **teste de pressão**, **teste de estresse** e **teste de volume**.

## Objetivos
---
- Investigar estratégias eficazes para testar aplicações com interfaces gráficas.
- Automatizar testes funcionais e não funcionais em GUIs feitas com Tkinter e PyQt.
- Validar o comportamento e a robustez da aplicação sob diferentes condições de uso.

## Tipos de Testes Aplicados
---
- **Teste de Caixa Branca**: Avaliação estrutural do código, com foco na lógica interna das funções da interface.
- **Teste de Caixa Preta**: Verificação do comportamento da interface a partir da perspectiva do usuário.
- **Teste de Pressão (Spike Testing)**: Envio repentino de grande quantidade de eventos ou dados para observar reações inesperadas.
- **Teste de Estresse**: Execução prolongada sob carga elevada para identificar falhas de desempenho ou memória.
- **Teste de Volume**: Inserção de grandes volumes de dados para testar os limites de capacidade da aplicação.

## 🛠️ Tecnologias Utilizadas
---
- Python 3.x
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PyQt5 / PyQt6](https://riverbankcomputing.com/software/pyqt/)
- `unittest`, `pytest`, `pytest-qt`
- Ferramentas de profiling e logging para análise de desempenho

