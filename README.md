# AutoClicker em Python

Este é um script simples e eficiente de AutoClicker desenvolvido em Python. Ele permite automatizar cliques do mouse com controles fáceis via teclado.

## 🚀 Funcionalidades

- **Controle por Teclado**: Inicie, pause ou encerre o programa instantaneamente usando teclas de atalho.
- **Multithreading**: O script utiliza threads para garantir que a interface de escuta do teclado e o loop de cliques funcionem simultaneamente sem travamentos.
- **Variação de Delay**: Inclui uma pequena variação aleatória no intervalo entre cliques para simular um comportamento mais humano.

## 🛠️ Pré-requisitos

Antes de começar, você precisará ter o **Python 3.x** instalado em sua máquina.

## 📦 Instalação

1. Clone este repositório ou baixe os arquivos.
2. Abra o terminal na pasta do projeto.
3. (Opcional) Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
   # No Linux/Mac:
   source venv/bin/activate
   ```
4. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Como Usar

Para iniciar o AutoClicker, execute o seguinte comando no terminal:

```bash
python main.py
```

### Atalhos Padrão:

- **`S`**: Alternar entre **Iniciar** e **Parar** os cliques.
- **`E`**: **Encerrar** o programa completamente.

## ⚙️ Configuração

Você pode ajustar as seguintes configurações diretamente no topo do arquivo `main.py`:

- `DELAY`: Intervalo base entre os cliques (em segundos).
- `BUTTON`: Qual botão do mouse será clicado (`Button.left`, `Button.right`, etc).
- `TOGGLE_KEY`: Tecla para iniciar/parar.
- `EXIT_KEY`: Tecla para fechar o programa.

---
Desenvolvido para fins educacionais e de produtividade.
