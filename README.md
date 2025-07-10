Disclaimer: README.md written and translated by AI (gpt-4o), but manually proofread.
# 📚 UDC Tagger — Prova de Conceito

Este é um projeto de prova de conceito que demonstra o uso de modelos de aprendizado de máquina para atribuição automática de códigos da Classificação Decimal Universal (CDU) a títulos e descrições de livros.

Foi desenvolvido como projeto final para uma disciplina universitária.

## 🚀 O Que Ele Faz

Uma aplicação leve em Flask que expõe quatro modelos de classificação (não incluídos neste repositório). Usuários podem enviar um título ou descrição de livro e receber um número CDU previsto como resposta.

## 🧪 Funcionalidades

- Aceita entrada do usuário via interface web (Flask)
- - Prediz códigos de classificação da CDU
- Inclui scripts e notebooks para:
  - Criação do conjunto de dados
  - Treinamento e avaliação dos modelos

⚠️ Atualmente, suporta apenas categorias da CDU que começam com a letra **A**.

## 🛠️ Stack Tecnológico

- **Linguagem:** Python  
- **Framework:** Flask (para servir os modelos)  
- **Ferramentas:** Jupyter Notebooks para preparação de dados e treinamento  
- **Deploy:** Docker

## 🐳 Como Executar

Você pode executar a aplicação usando Docker:

```bash
cd Docker/Flask
docker build -t udc-tagger .
docker run -p 5000:5000 udc-tagger
```

> **Nota:** Os modelos não estão incluídos neste repositório. Você deve fornecer seus próprios modelos treinados e colocá-los no caminho esperado pela aplicação Flask.

## 🧭 Planos Futuros

A versão atual inclui apenas categorias da CDU que começam com "A". Expandir para toda a gama da CDU é incentivado para futuros desenvolvedores ou pesquisadores interessados em estender este trabalho.

## ⚠️ Aviso sobre o Uso da CDU

Este projeto faz referência ao sistema de Classificação Decimal Universal (CDU) apenas para fins de pesquisa e demonstração.

- O sistema CDU é protegido por direitos autorais do **Consórcio CDU**.  
- Este projeto **não é afiliado nem endossado** pelo Consórcio CDU.  
- Quaisquer trechos ou referências ao conteúdo da CDU são limitados e utilizados exclusivamente para fins acadêmicos.  
- Os usuários são responsáveis por garantir conformidade com os termos de licenciamento da CDU caso optem por reutilizar, distribuir ou expandir este trabalho.


# 📚 UDC Tagger Proof of Concept - English

This is a proof-of-concept project that demonstrates the use of machine learning models to automatically assign Universal Decimal Classification (UDC) codes to book titles and descriptions.

It was developed as a final project for a college class.
## 🚀 What It Does

A lightweight Flask application that exposes four classification models (not included in this repo). Users can submit a book title or description and receive a predicted UDC number in return.
## 🧪 Features

- Accepts user input via web interface (Flask)

- Predicts UDC classification codes

 - Includes scripts and notebooks for:

     - Dataset creation

     - Model training and evaluation

⚠️ Currently supports only UDC categories starting with the letter A.

## 🛠️ Tech Stack

- **Language:** Python

- **Framework:** Flask (for serving the models)

- **Tools:** Jupyter Notebooks for data prep and training

- **Pre-trained models:** Bert and T5

- **Deployment:** Docker

## 🐳 How to Run

You can run the application using Docker:
```
cd Docker/Flask
docker build -t udc-tagger .
docker run -p 5000:5000 udc-tagger
```
    Note: The models themselves are not included in the repository. You must provide your own trained models and place them in the expected path used by the Flask app. (`Docker/Flask/models`)

## 🧭 Future Plans

The current version only includes UDC categories starting with "A". Expanding to the full UDC range is encouraged for future developers or researchers interested in extending this work.

## ⚠️ Disclaimer on UDC Use
>**Disclaimer**
>This project references the Universal Decimal Classification (UDC) system for research and demonstration purposes only.  
>This project references the Universal Decimal Classification (UDC) system only for academic and demonstration purposes.  
>No UDC tables or classification structures are included or redistributed.  
>Example UDC predictions may appear in this project solely to illustrate model behavior, including failures.  
>The UDC system is copyrighted by the UDC Consortium.  
>This project is not affiliated with or endorsed by the UDC Consortium.  
>Users are responsible for ensuring their own compliance with UDC licensing terms.  
