# 📚 Sistema de Chamada Escolar Automatizada

Este é um projeto de automação de chamadas escolares usando **Python** e **MySQL**. Criado com o objetivo de estudar back-end, manipulação de banco de dados, e construir uma aplicação real e útil para ambientes escolares.

---

## ✨ Funcionalidades

✅ Consulta automática das **aulas do dia** com base no calendário escolar   
✅ Registro de presença (`P`) e falta (`F`) diretamente no banco de dados  
✅ Organização das presenças por **aluno**, **data** e **matéria**

---

## 🚀 Tecnologias Utilizadas

| Ferramenta          | Descrição                                  |
|---------------------|---------------------------------------------|
| Python              | Linguagem principal do projeto 🐍           |
| Pandas              | Manipulação de dados com DataFrames 📊      |
| SQLAlchemy          | Conexão com banco de dados relacional 🔌    |
| MySQL               | Armazenamento das tabelas escolares 💄️      |
| Locale              | Para detectar o **dia da semana** em PT-BR 🗖️

---

## 🧠 Conteúdos Estudados

- 🔁 Loops e condicionais em Python  
- 🗓️ Manipulação de datas e horários  
- 📂 CRUD com bancos relacionais (MySQL) usando SQLAlchemy  
- 🧮 LabelEncoder para organizar IDs (Scikit-Learn)  
- 🧱 Modelagem de tabelas com chaves e `CHECK CONSTRAINTS` no MySQL

---

## 🏧 Estrutura do Projeto

```
📁 chamada-escolar/
🗋 main.py              # Código principal da aplicação
🗋 README.md            # Este arquivo ❤️
📓 banco de dados
   💄 alunos_dados        # Tabela com alunos
   📅 calendario          # Datas letivas
   📘 aulas               # Aulas por dia da semana
   📆 presencas           # Tabela final de presenças e faltas
```

---

## 🧪 Como usar

1. Clone este repositório
2. Instale as dependências com:
   ```bash
   pip install pandas sqlalchemy mysql-connector-python
   ```
3. Configure seu banco de dados MySQL com as tabelas:
   - `alunos_dados`
   - `calendario`
   - `aulas`
   - `presencas`
4. Execute o script:
   ```bash
   python main.py
   ```
5. Digite os alunos que faltaram no terminal 📝

---

## 💡 Futuras Melhorias

- [ ] Interface Versão Web com **FastAPI + React**
- [ ] Geração de relatórios em PDF ou Excel
- [ ] Exportação de estatísticas por aluno, turma ou matéria
- [ ] Sistema de login para professores

---

## 👩‍💼 Feito por

**Tuany Alves Farias**  
Professora migrando para o mundo do desenvolvimento back-end com muito 💖 e curiosidade.
