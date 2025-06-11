#!/usr/bin/env python3
"""
🚀 Script de setup automático para o IBMEC MALL Bot
Execute: python setup.py
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header():
    print("🛍️ IBMEC MALL Bot - Setup Automático")
    print("="*50)
    print(f"🖥️ Sistema: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    print("="*50)

def check_python_version():
    """Verifica se o Python é 3.8+"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ é necessário!")
        print(f"   Versão atual: {sys.version}")
        print("   Baixe em: https://python.org/downloads/")
        sys.exit(1)
    print("✅ Versão do Python OK")

def create_virtual_env():
    """Cria ambiente virtual se não existir"""
    venv_path = Path("venv")
    
    if venv_path.exists():
        print("✅ Ambiente virtual já existe")
        return
    
    print("🔄 Criando ambiente virtual...")
    try:
        subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
        print("✅ Ambiente virtual criado")
    except subprocess.CalledProcessError:
        print("❌ Erro ao criar ambiente virtual")
        sys.exit(1)

def get_pip_command():
    """Retorna o comando pip correto para o SO"""
    if platform.system() == "Windows":
        return "venv\\Scripts\\pip"
    else:
        return "venv/bin/pip"

def install_dependencies():
    """Instala dependências do requirements.txt"""
    print("🔄 Instalando dependências...")
    
    pip_cmd = get_pip_command()
    
    try:
        # Upgrade pip primeiro
        subprocess.run([pip_cmd, "install", "--upgrade", "pip"], check=True)
        
        # Instalar dependências
        subprocess.run([pip_cmd, "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependências instaladas")
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências")
        print("💡 Tente executar manualmente:")
        print(f"   {pip_cmd} install -r requirements.txt")
        sys.exit(1)

def create_env_file():
    """Cria arquivo .env se não existir"""
    env_path = Path(".env")
    
    if env_path.exists():
        print("✅ Arquivo .env já existe")
        return
    
    print("🔄 Criando arquivo .env...")
    
    env_content = """# Configurações do Microsoft Bot Framework (desenvolvimento local)
MicrosoftAppId=
MicrosoftAppPassword=
MicrosoftAppType=MultiTenant
MicrosoftAppTenantId=

# URL da API no Azure
URL_PREFIX=https://ibmec-ecommerce-app-gydeg9hye0eabpbf.brazilsouth-01.azurewebsites.net

# API Management (opcional)
APIM_BASE_URL=
APIM_SUBSCRIPTION_KEY=

# Porta local
PORT=3978
"""
    
    try:
        with open(".env", "w", encoding="utf-8") as f:
            f.write(env_content)
        print("✅ Arquivo .env criado")
    except Exception as e:
        print(f"❌ Erro ao criar .env: {e}")

def test_installation():
    """Testa se a instalação funcionou"""
    print("🧪 Testando instalação...")
    
    try:
        # Testar imports principais
        sys.path.insert(0, str(Path.cwd()))
        
        import aiohttp
        print("   ✅ aiohttp")
        
        from config import DefaultConfig
        print("   ✅ config")
        
        from api.product_api import ProductAPI
        print("   ✅ product_api")
        
        # Testar conexão com API
        api = ProductAPI()
        if api.test_connection():
            print("   ✅ Conexão com API")
        else:
            print("   ⚠️ API não está respondendo (normal se estiver offline)")
        
        print("✅ Instalação testada com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro no teste: {e}")
        print("💡 Pode ser normal, tente executar o bot manualmente")

def print_next_steps():
    """Mostra próximos passos"""
    print("\n🎉 Setup concluído!")
    print("="*50)
    print("📋 PRÓXIMOS PASSOS:")
    print()
    print("1️⃣ Ativar ambiente virtual:")
    
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    
    print()
    print("2️⃣ Executar o bot:")
    print("   python run_local.py")
    print()
    print("3️⃣ Testar no Bot Framework Emulator:")
    print("   URL: http://localhost:3978/api/messages")
    print("   App ID: (vazio)")
    print("   App Password: (vazio)")
    print()
    print("🔗 Download Emulator:")
    print("   https://github.com/Microsoft/BotFramework-Emulator/releases")
    print("="*50)

def main():
    """Função principal"""
    print_header()
    
    # Verificações
    check_python_version()
    
    # Setup
    create_virtual_env()
    install_dependencies()
    create_env_file()
    
    # Teste
    test_installation()
    
    # Instruções finais
    print_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelado pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")
        print("💡 Tente o setup manual seguindo o README.md")