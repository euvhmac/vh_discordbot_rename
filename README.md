# 🤖 Rename Bot – Discord Nickname Reset Bot

O **Rename Bot** é um utilitário desenvolvido em Python para Discord, criado com foco em performance e segurança, ideal para servidores grandes.  
Ele percorre todos os membros de um servidor e redefine o apelido de cada um para seu nome padrão (removendo `nicknames`).

---

## 🚀 Funcionalidade

- Comando único: `!renameall`
- Redefine apelidos para todos os membros do servidor
- Logs automáticos a cada 1000 renomeações
- Total de renomeações reportado ao final
- Controle de concorrência com `asyncio.Semaphore`
- Prevenção de rate limit com `asyncio.sleep`

---

## 📁 Estrutura do Projeto

```
rename_bot/
│
├── bot.py              # Código principal do bot
├── config.py           # Carrega as variáveis do ambiente (.env)
├── requirements.txt    # Dependências do projeto
└── .env                # Token do bot (NÃO versionar)
```

---

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative um ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate    # Mac/Linux
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Crie o arquivo `.env`
```env
DISCORD_TOKEN=seu_token_aqui
```

---

## 🧪 Executando o Bot

```bash
python bot.py
```

No Discord, digite:

```
!renameall
```

---

## ⚠️ Permissões necessárias

Certifique-se de que o bot:

- Está com permissão de **Administrador**
- Está **presente no servidor**
- Está com permissão de **Gerenciar Apelidos**

---

## 🛡️ Segurança

- O token é armazenado em `.env`, nunca compartilhe publicamente
- Adicione `.env` ao seu `.gitignore`

---

## 🧩 Futuras melhorias

- Interface web com Flask ou FastAPI
- Logs por arquivo e dashboards
- Filtros por cargo ou categoria
- Cron scheduler semanal

---

Feito com 💻 por Vitão 
