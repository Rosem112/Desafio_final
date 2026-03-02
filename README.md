
# 💸 FinanBot — Educador Financeiro Pessoal

> Agente de IA generativa que analisa seus gastos mensais e responde dúvidas financeiras com base nos seus próprios dados — de forma clara, acessível e 100% local.

---

## 🎯 O Problema

Muitas pessoas não sabem para onde vai seu dinheiro no fim do mês. Sem visibilidade sobre gastos e saldo, o risco de endividamento aumenta. O **FinanBot** resolve isso organizando suas finanças de forma simples e educativa.

---

## 🤖 O Agente

O FinanBot lê dados financeiros armazenados localmente (JSON/CSV), calcula automaticamente o total de gastos, saldo restante e distribuição por categoria, e responde perguntas do usuário com linguagem acessível — sem jargões, sem julgamentos.

**Ele responde apenas com base nos dados fornecidos**, evitando alucinações e garantindo confiabilidade.

```
Usuário → Interface Streamlit → Ollama (LLM local)
                                       ↑
                           data/ (JSON + CSV do usuário)
```

---

## 🧠 Persona

| Atributo | Detalhe |
|---|---|
| **Nome** | FinanBot |
| **Perfil** | Educativo, organizado, não julgador |
| **Tom** | Acessível, informal moderado, sem termos técnicos |
| **Exemplo** | *"Olá! Sou o FinanBot, vamos organizar suas finanças hoje?"* |

---

## 🗂️ Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
├── 📁 data/
│   ├── dados_usuario.json       # Perfil: nome, renda, meta de poupança
│   ├── gastos_mensais.json      # Gastos do mês atual por categoria
│   └── historico_mensal.csv     # Histórico de movimentações anteriores
├── 📁 docs/
│   ├── 01-documentacao-agente.md   # Caso de uso, persona e arquitetura
│   ├── 02-base-conhecimento.md     # Estratégia de dados e integração
│   ├── 03-prompts.md               # System prompt e exemplos few-shot
│   ├── 04-metricas.md              # Testes e avaliação do agente
│   └── 05-pitch.md                 # Roteiro do pitch de 3 minutos
├── 📁 src/
│   └── app.py                      # Aplicação Streamlit
└── README.md
```

---

## 💬 System Prompt

```
Você é o FinanBot, um assistente financeiro pessoal focado em organização de finanças.
Responda de forma clara e objetiva, utilizando apenas os dados fornecidos no contexto.

REGRAS:
- Utilize exclusivamente as informações presentes no contexto enviado.
- Nunca invente valores, categorias ou dados.
- Não faça recomendações de investimento nem previsões financeiras.
- Se a informação não estiver no contexto, responda:
  "Não possuo dados suficientes para responder com base nas informações disponíveis."
- Não julgue o usuário pelos gastos.
```

---

## 🧪 Exemplos de Interação

| Pergunta do Usuário | Resposta do FinanBot |
|---|---|
| "Quanto ainda posso gastar este mês?" | "Sua renda é R$ 3.000 e seus gastos somam R$ 1.825. Seu saldo restante é de **R$ 1.175**." |
| "Quanto gastei com lazer?" | "Você gastou **R$ 55** na categoria Lazer neste mês." |
| "Onde devo investir?" | "Não realizo recomendações de investimento. Posso ajudar a analisar seus gastos." |
| "Qual a previsão do tempo?" | "Sou especializado em finanças. Posso ajudar com algo relacionado ao seu orçamento?" |

---

## ✅ Resultados dos Testes

| Teste | Resultado |
|---|---|
| Consulta de gasto por categoria | ✅ Correto |
| Consulta de saldo restante | ✅ Correto |
| Pergunta fora do escopo | ✅ Recusou corretamente |
| Informação inexistente nos dados | ✅ Admitiu falta de dados |

---

## 🚀 Como Executar

**Pré-requisitos:** Python 3.9+ e [Ollama](https://ollama.ai/) instalado localmente.

```bash
# 1. Clone o repositório
git clone https://github.com/Rosem112/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Suba o modelo no Ollama
ollama run llama3

# 4. Execute a aplicação
streamlit run src/app.py
```

---

## 🛠️ Tecnologias

| Ferramenta | Uso |
|---|---|
| [Streamlit](https://streamlit.io/) | Interface web do chatbot |
| [Ollama](https://ollama.ai/) | Execução local do LLM (sem custo, com privacidade) |
| Python + JSON/CSV | Lógica da aplicação e base de conhecimento |

---

## 🔒 Segurança e Privacidade

- Execução **100% local** — nenhum dado sai da sua máquina
- O agente **não acessa informações externas**
- Respostas limitadas ao contexto fornecido, eliminando alucinações
- Sem integração com APIs pagas ou serviços em nuvem

---

*Desenvolvido por [Rosem112](https://github.com/Rosem112)*
