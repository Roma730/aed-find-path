<p align="center">
  <img alt="upe" src="./img/upe-logo.png"/>
</p>

---

# 🗺️ Projeto — Planejamento de Rotas

**Disciplina:** Estruturas de Dados e Algoritmos
**Curso:** Engenharia de Software / Licenciatura em Computação
**Instituição:** Universidade de Pernambuco — Campus Garanhuns

---

## 🧭 O que você vai construir?

Você vai implementar um **algoritmo de busca em grafos** capaz de encontrar um caminho entre dois pontos de uma cidade virtual.

Pense nisso como o "miolo" de um GPS: dado um ponto de partida e um destino, qual sequência de ruas leva de um ao outro?

---

## 🎯 O que você vai aprender?

Ao concluir este projeto, você será capaz de:

- **Modelar** problemas reais usando grafos
- **Percorrer** estruturas conectadas
- **Escolher** estruturas de dados adequadas para busca
- **Implementar** algoritmos de planejamento de rotas
- **Analisar** a eficiência do seu código (tempo e espaço)
- **Comparar** diferentes estratégias de busca

---

## 🌎 Entendendo o problema

### Como a cidade é representada?

A cidade é um **grafo**: um conjunto de **interseções** (nós) ligadas por **estradas** (arestas).

Cada interseção tem:
- um **identificador único** (número inteiro)
- uma **posição** no mapa (coordenadas x, y)
- uma lista de **vizinhos** (interseções diretamente conectadas)

### Exemplo

```python
# Posições das interseções no mapa
intersections = {
    0: (10, 5),   # Interseção 0 está na posição x=10, y=5
    1: (12, 8),   # Interseção 1 está na posição x=12, y=8
    2: (15, 6),   # Interseção 2 está na posição x=15, y=6
}

# Quais interseções estão conectadas por estradas?
roads = {
    0: [1],       # Da interseção 0, só dá para ir para a 1
    1: [0, 2],    # Da interseção 1, dá para ir para a 0 ou a 2
    2: [1],       # Da interseção 2, só dá para ir para a 1
}
```

Visualmente:

```
[0] ——— [1] ——— [2]
```

Se quisermos ir de `0` até `2`, o único caminho possível é: **0 → 1 → 2**

---

## ✍️ Sua tarefa

Implementar a função abaixo no arquivo `challenges/find_path.py`:

```python
def find_path(city_map, start, goal):
    ...
```

| Parâmetro  | Tipo      | Descrição                                 |
| ---------- | --------- | ----------------------------------------- |
| `city_map` | `CityMap` | O mapa da cidade (interseções + estradas) |
| `start`    | `int`     | ID da interseção de partida               |
| `goal`     | `int`     | ID da interseção de destino               |

**Retorno esperado:** uma lista com os IDs das interseções percorridas, da origem ao destino.

```python
# Exemplo de retorno válido:
[5, 16, 37, 12, 34]
```

---

## 📍 Regras do caminho retornado

O caminho retornado **deve**:

- ✅ Começar na interseção `start`
- ✅ Terminar na interseção `goal`
- ✅ Usar apenas estradas que existem no mapa
- ✅ Ser encontrado de forma eficiente (veja seção de eficiência)

---

## 💡 Perguntas para guiar o raciocínio

Antes de escrever qualquer código, discuta com o grupo:

- Estando em `start`, o que você pode fazer imediatamente?
- Como garantir que não vai ficar preso em um ciclo?
- Como saber qual caminho você percorreu ao chegar no `goal`?
- E se não houver caminho possível?

> 📖 **Consulte os slides** sobre travessia de grafos — os algoritmos que vimos em aula são o ponto de partida natural para esse problema.

---

## 📈 Atenção: eficiência importa!

Os testes incluem mapas de **tamanhos muito diferentes** — desde pequenos até instâncias grandes.

Uma solução funcionalmente correta pode não ser aprovada caso seja lenta demais para os cenários maiores.

Ao finalizar uma solução que passa nos testes básicos, reflita com o grupo:

- O que acontece com o tempo de execução conforme o mapa cresce?
- Existe alguma operação no seu código que se torna cara à medida que a fronteira de busca aumenta?
- Há alguma estrutura de dados, vista em aula, que tornaria essa operação mais eficiente?

---

## 🗂️ Estrutura do projeto

```
.
├── README.md
├── dev-requirements.txt
│
├── challenges/
│   └── find_path.py               ← ✏️  VOCÊ IMPLEMENTA AQUI
│
├── data_structures/
│   ├── city_map.py                ← Estrutura do mapa
│   └── map_examples.py           ← Exemplos de mapas
│
└── tests/
    ├── test_find_path.py          ← Correção básica
    ├── test_find_path_optimality.py  ← Qualidade do caminho
    ├── test_find_path_complexity.py  ← Eficiência
    ├── generators.py
    └── complexities.py
```

> 📖 **Recomendação:** leia `data_structures/city_map.py` antes de começar. Entender como o mapa está estruturado vai deixar a implementação mais clara.

---

## 🚫 Regras do projeto

|     | Regra                                                          |
| --- | -------------------------------------------------------------- |
| ❌   | Não modifique os arquivos de teste                             |
| ❌   | Não altere a assinatura da função `find_path`                  |
| ❌   | Não use bibliotecas externas além das fornecidas               |
| ✅   | Implemente sua solução **apenas** em `challenges/find_path.py` |
| ✅   | Seu código deve passar em **todos** os testes                  |
| ✅   | Seu código deve seguir o padrão **Flake8**                     |

---

## ⚙️ Configurando o ambiente

```bash
# Crie e ative o ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
python3 -m pip install -r dev-requirements.txt
```

---

## 🔄 Testando sua solução

**Rodar todos os testes:**
```bash
python3 -m pytest
```

**Ver detalhes de cada teste:**
```bash
python3 -m pytest -s -vv
```

**Rodar apenas um arquivo de testes:**
```bash
python3 -m pytest tests/test_find_path.py -s -vv
```

---

## 📚 Referências

- Slides da disciplina
- *Entendendo Algoritmos* — Aditya Bhargava

---
