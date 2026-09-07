# ⚡ Calculadora de Consumo de Energia

## 📌 Sobre o projeto

Este projeto é um programa desenvolvido em **Python** para calcular o consumo mensal de energia elétrica de um aparelho.

O sistema solicita o nome do aparelho, sua potência em watts (W) e o tempo médio de utilização diária. Em seguida, calcula o consumo mensal em **kWh** e apresenta uma estimativa do custo da energia.

## 🎯 Objetivo

O objetivo é praticar conceitos básicos de **Lógica de Programação** e **Python**, como:

* 📥 Entrada de dados
* 📦 Variáveis
* 🔢 Operações matemáticas
* 🧮 Fórmulas
* 📤 Exibição de resultados

## 🐍 Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-Reposit%C3%B3rio-black?logo=github)

![Energia](https://img.shields.io/badge/Energia-Consumo-yellow)

## 📐 Fórmula utilizada

O consumo mensal é calculado utilizando a seguinte fórmula:

```text
consumoMensal = (potencia × horasDia × 30) / 1000
```

Para calcular o custo estimado:

```text
custoMensal = consumoMensal × valorKWh
```

Neste projeto, foi utilizado o valor de **R$ 0,75 por kWh** como exemplo.

> 💡 O valor de R$ 0,75 é apenas uma referência para o exercício. O preço real do kWh pode variar de acordo com a tarifa de energia.

## ▶️ Como executar

### 1. Instale o Python

Verifique se o Python está instalado no computador:

```bash
python --version
```

### 2. Baixe ou clone o projeto

Abra o terminal na pasta do projeto.

### 3. Execute o programa

Digite:

```bash
python consumo.py
```

### 4. Informe os dados

O programa solicitará:

* 🏠 Nome do aparelho
* ⚡ Potência em watts
* ⏱️ Horas de uso por dia

Depois, o sistema apresentará:

* 📊 Consumo mensal em kWh
* 💰 Custo mensal estimado

## 🧪 Exemplo

```text
Digite o nome do aparelho: Geladeira
Digite a potencia do aparelho em watts (W): 150
Digite o tempo medio de uso diario em horas: 10

--- Resultado ---
Aparelho: Geladeira
Potencia: 150.0 W
Uso diario: 10.0 horas
Consumo mensal: 45.00 kWh
Custo mensal estimado: R$ 33.75
```

## 📁 Estrutura do projeto

```text
📦 calculadora-consumo-energia
 ├── 🐍 consumo.py
 └── 📖 README.md
```

## 👩‍💻 Projeto de estudo

Este projeto foi desenvolvido como exercício de aprendizado em **Python e Lógica de Programação**.

⚡🐍 **Aprender programação é transformar problemas em soluções!**

