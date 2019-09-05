# INVASÃO ALIENÍGENA

Na Invasão Alienígena, o jogador controla uma espaçonave que aparece na parte inferior central da tela. O jogador pode mover a espaçonave para a direita e para a esquerda usando as teclas de direção e atirar usando a barra a esquerda usando as teclas de direção e atirar usando a barra de espaço. Quando o jogo começa, uma frota de alienígenas enche o cé e se desloca na tela para os ladaos e para baixo. O jogador atira nos alienígenas e os destrói. Se o jogador atingir todos os alienígenas, uma nova frota, que se moverá mais rapidamente que a frota anterior, aparecerá. Se algum alienígena atingir a espaçonave do jogador ou alcançar a parte inferior da tela, o jogador perderá uma nave. Se o jogador perder três espaçonaves, o jogo terminará.

O jogo foi criado com base nas instruções do livro [Curso Intensivo de Python](https://www.amazon.com.br/Curso-Intensivo-Python-Introdu%C3%A7%C3%A3o-Programa%C3%A7%C3%A3o/dp/8575225030).

## Começando

O presente projeto foi desenvolvido em Linux/Ubuntu, e todas as suas instruções serão baseadas nesse sistema operacional. Siga as descrições para rodar o programa.

### Pré-requisitos

Primeiramente será necessário ter instalado em sua máquina:
- Python 3.7+
- [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)

### Instalando

Crie um ambiente virtual:
```bash
virtualenv -p python3.7 ENV
```

Entre no ambiente virtual:
```bash
source ENV/bin/activate
```

Dentro do ambiente virtual, instale as dependências:
```bash
pip install -r requirements/base.txt
```

### Rodando o programa

Com o ambiente preparado, execute o código principal:
```bash
python main.py
```

E pronto! O jogo funcionará.
