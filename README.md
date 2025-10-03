# Introdução ao versionamento com Git/GitHub
## ⚙️ Instalando o Git
1. Acesse [git-scm.com/downloads](https://git-scm.com/downloads)  
2. Abra o PowerShell  
3. Verifique a instalação:  
   ```bash
   git --version
   ```

---

## 🔧 Configurações básicas
Definir nome de usuário (aparece nos commits):  
```bash
git config --global user.name "Seu Nome"
```

Definir e-mail (mesmo usado no GitHub):  
```bash
git config --global user.email "seuemail@gmail.com"
```

Definir branch principal padrão como `main`:  
```bash
git config --global init.defaultBranch main
```

---

## 📂 Criando um projeto
No PowerShell:  
```bash
mkdir minicurso
cd minicurso
code .
```

---

## 🚀 Git Setup
Iniciar o repositório Git:  
```bash
git init
```

Adicionar arquivos ao versionamento:  
```bash
git add .
```

Fazer o primeiro commit:  
```bash
git commit -m "primeiro commit"
```

---

## 🔄 Trocando de versões
Mostrar histórico de commits:  
```bash
git log
```

Voltar para commits anteriores:  
```bash
git checkout <commit-hash>
```

Voltar para a versão mais atual (branch principal):  
```bash
git checkout main
```

---

## ☁️ Salvando o repositório na nuvem
### GitHub Setup
1. Acesse [GitHub](https://github.com/) e crie um repositório  
2. No terminal (dentro da pasta do projeto):  
   ```bash
   git remote add origin https://github.com/user/minicurso.git
   ```

Enviar commits para o GitHub:  
```bash
git push -u origin main
```

---

## 🔑 Configurando Token no GitHub
1. Acesse [Configurações de Tokens](https://github.com/settings/tokens)  
2. Clique em **Generate new token (classic)**  
3. Clique em **Generate token** e copie o valor gerado  
4. Use o token como senha quando fizer `git push`
