# Brick Breaker

Jogo de quebra-blocos desenvolvido em Python com a biblioteca Pygame.

Este projeto foi desenvolvido como trabalho acadêmico para a disciplina de **Linguagem de Programação Aplicada**.

---

## Sobre o projeto

O Brick Breaker é um jogo inspirado nos clássicos jogos de quebra-blocos, como Breakout e Arkanoid.

O jogador controla uma plataforma localizada na parte inferior da tela. O objetivo é rebater a bola e destruir todos os blocos posicionados na parte superior.

A partida termina quando:

- A bola toca a parte inferior da tela;
- Todos os blocos são destruídos.

Ao final da partida, o jogo informa se o jogador perdeu ou venceu e permite iniciar uma nova partida.

---

## Objetivos acadêmicos

O projeto foi desenvolvido com o objetivo de aplicar, na prática, conceitos estudados na disciplina de **Linguagem de Programação Aplicada**, incluindo:

- Estruturação de um projeto em Python;
- Divisão do código em módulos;
- Criação de funções;
- Manipulação de eventos do teclado;
- Desenvolvimento de interfaces gráficas;
- Detecção de colisões;
- Controle de movimentação;
- Manipulação de imagens;
- Reprodução de arquivos de áudio;
- Criação de um executável para Windows.

---

## Funcionalidades

- Tela inicial com nome do jogo;
- Exibição dos comandos;
- Sistema de movimentação do jogador;
- Movimento contínuo da bola;
- Colisão da bola com as paredes;
- Colisão da bola com o jogador;
- Colisão da bola com os blocos;
- Remoção dos blocos após a colisão;
- Sistema de pontuação;
- Sistema de recorde durante a execução;
- Tela de vitória;
- Tela de Game Over;
- Opção de jogar novamente;
- Opção de sair do jogo;
- Música de fundo;
- Imagens personalizadas para a bola e para o jogador;
- Possibilidade de gerar um arquivo executável para Windows.

---

## Controles

| Tecla | Ação |
|---|---|
| Seta para a esquerda | Move o jogador para a esquerda |
| Seta para a direita | Move o jogador para a direita |
| ENTER | Inicia o jogo ou começa uma nova partida |
| ESPAÇO | Inicia o jogo |
| ESC | Sai do jogo na tela final |

---

## Tecnologias utilizadas

- Python 3;
- Pygame;
- PyInstaller;
- PyCharm;
- Git e GitHub.

---

## Estrutura do projeto

```text
Brick Breaker/
│
├── main.py
├── constantes.py
├── elementos.py
├── desenho.py
├── logica.py
├── README.md
│
└── assets/
    ├── square.wav
    ├── bola.png
    └── jogador.png
```

### Descrição dos arquivos

#### `main.py`

É o arquivo principal do projeto. Ele é responsável por:

- Inicializar o Pygame;
- Criar a janela do jogo;
- Iniciar a música;
- Controlar o loop principal;
- Criar as partidas;
- Controlar a tela inicial e a tela final;
- Atualizar a pontuação.

#### `constantes.py`

Armazena as configurações gerais do jogo, como:

- Tamanho da tela;
- Tamanho da bola;
- Tamanho do jogador;
- Velocidade da bola;
- Velocidade do jogador;
- Quantidade de blocos;
- Cores;
- Caminhos das imagens e da música.

#### `elementos.py`

Responsável pela criação dos elementos do jogo:

- Bola;
- Jogador;
- Blocos;
- Imagens da bola e do jogador.

#### `desenho.py`

Contém as funções utilizadas para desenhar:

- Fundo;
- Bola;
- Jogador;
- Blocos;
- Pontuação;
- Tela inicial;
- Tela de vitória;
- Tela de Game Over.

#### `logica.py`

Contém a lógica de funcionamento do jogo:

- Movimentação do jogador;
- Movimentação da bola;
- Colisões;
- Verificação de vitória;
- Finalização da partida.

---

## Requisitos

Para executar o projeto utilizando os arquivos Python, é necessário ter:

- Python 3.8 ou superior;
- Pygame instalado;
- Os arquivos da pasta `assets`.

---

## Instalação

Clone este repositório:

```bash
git clone https://github.com/Ledsch/brick-breaker.git
```

Entre na pasta do projeto:

```bash
cd brick-breaker
```

Instale o Pygame:

```bash
pip install pygame
```

---

## Como executar

Execute o arquivo principal:

```bash
python main.py
```

Ou execute o arquivo `main.py` diretamente pelo PyCharm.

---

## Gerando o executável para Windows

Para criar um executável do jogo, instale o PyInstaller:

```bash
pip install pyinstaller
```

Depois, execute o comando abaixo na pasta principal do projeto:

```bash
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
```

O executável será criado dentro da pasta:

```text
dist/
```

O arquivo gerado estará localizado em:

```text
dist/main.exe
```

### Importante

A opção abaixo adiciona a pasta de recursos ao executável:

```bash
--add-data "assets;assets"
```

Ela permite incluir:

- Música;
- Imagens;
- Outros arquivos utilizados pelo jogo.

---

## Música e imagens

Os arquivos multimídia utilizados pelo jogo ficam dentro da pasta `assets`.

Atualmente, o projeto pode utilizar:

```text
assets/
├── square.wav
├── bola.png
└── jogador.png
```

O nome configurado no arquivo `constantes.py` deve ser exatamente igual ao nome do arquivo dentro da pasta `assets`.

Por exemplo:

```python
MUSICA_FUNDO = os.path.join(PASTA_BASE, "assets", "square.wav")
```

O nome, a extensão e as letras maiúsculas ou minúsculas devem estar corretos.

---

## Autor

Projeto desenvolvido por: **Leonardo S. (Ledsch)**
<br>
Faculdade: **Uninter**
<br>
Curso: **Analise e desenvolvimento de sistema (ADS)**
<br>
Trabalho acadêmico desenvolvido para a disciplina de: **Linguagem de Programação Aplicada**
<br>
Ano: **2026**

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos e educacionais.

O código pode ser utilizado como referência para estudos de Python, Pygame e desenvolvimento de jogos 2D.
