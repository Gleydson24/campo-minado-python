# campo-minado-python
Campo Minado em Python

# 1. Visão Geral

- **Tecnologia Utilizada**: Python (puro, sem bibliotecas gráficas)  
- **Descrição**: Implementação simplificada do clássico jogo Campo Minado no terminal, com geração aleatória de minas, contagem de minas adjacentes e condição de vitória/derrota.  
- **Objetivo**: Criar uma versão jogável de Campo Minado no console, com foco em lógica de programação e interação básica com o usuário.

---

# 2. Descrição Detalhada do Projeto

# O que é Campo Minado?

Campo Minado (Minesweeper) é um jogo de raciocínio lógico no qual o jogador precisa abrir todas as células que **não contenham minas**, com base em dicas numéricas que indicam o número de minas ao redor de cada célula.

---

# 2.1 Funcionalidades Principais

# Motor do Jogo:
- Geração aleatória de minas em um tabuleiro 5x5.
- Cálculo das quantidades de minas adjacentes para cada célula.
- Detecção de clique em mina (fim de jogo).
- Contagem de jogadas corretas até a vitória.

# Interface (Terminal):
- Campo visível representado com `"-"` para células não reveladas.
- Exibição numérica de minas próximas ao revelar células.
- Input do usuário para coordenadas de linha e coluna.
- Exibição final do campo real (com minas e números).

---

# 3. Etapas de Desenvolvimento

# Etapa 1: Estrutura Base
- Definição do tamanho do tabuleiro (5x5) e quantidade de minas (3).
- Criação das matrizes `campo_real` e `campo_visivel`.

# Etapa 2: Geração do Campo
- Colocação aleatória de minas (`X`) no campo real.
- Cálculo da quantidade de minas ao redor para cada célula.

# Etapa 3: Lógica do Jogo
- Leitura de entradas do jogador (`linha`, `coluna`).
- Verificação de clique em mina ou célula segura.
- Atualização da célula visível com o número correspondente.
- Verificação de vitória com base nas jogadas realizadas.

# Etapa 4: Finalização
- Exibição do campo completo após fim do jogo.
- Mensagens de vitória ou derrota.
- Código 100% funcional no terminal.

---

# 4. Requisitos Técnicos

# 4.1 Dependências

Este projeto **não requer bibliotecas externas** além do Python padrão.

- Requisitos:
  - Python 3.6 ou superior
  - Terminal ou console para execução

---

# 5. Melhorias Futuras (Sugeridas)

- Sistema de **bandeiras** (marcar minas).
- **Modo de dificuldade** (campo 9x9, 16x16, etc.).
- **Interface gráfica** com Pygame.
- **Abertura automática** de células vazias (flood fill).
- Sistema de **tempo** para medir desempenho.

---

# 6. Como Executar

1. Tenha o Python 3 instalado.
2. Salve o código do jogo em um arquivo chamado `campo_minado_terminal.py`.
3. No terminal, navegue até a pasta onde o arquivo está salvo.
4. Execute com o comando:

```bash
python campo_minado_terminal.py
