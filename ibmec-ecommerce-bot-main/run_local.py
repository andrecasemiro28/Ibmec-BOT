#!/usr/bin/env python3
"""
Script para executar o bot localmente
"""

import os
import sys
from pathlib import Path

# Garantir que encontra os módulos
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    print("🤖 IBMEC MALL Bot - Execução Local")
    print("="*50)
    
    try:
        # Importa e mostra configurações
        from config import DefaultConfig
        DefaultConfig.print_config()
        
        # Testa imports essenciais
        print("📦 Testando imports...")
        from aiohttp import web
        print("   ✅ aiohttp")
        
        from app import APP
        print("   ✅ app")
        
        # Testa conexão com a API
        print("\n🌐 Testando conexão com API...")
        try:
            from api.product_api import ProductAPI
            api = ProductAPI()
            if api.test_connection():
                print("   ✅ API conectada com sucesso!")
            else:
                print("   ⚠️ API não está respondendo")
        except Exception as e:
            print(f"   ❌ Erro na API: {e}")
        
        # Configura porta
        config = DefaultConfig()
        port = config.PORT
        
        print(f"\n🚀 Iniciando servidor na porta {port}...")
        print(f"📍 Acesse: http://localhost:{port}")
        print(f"🔗 Endpoint: http://localhost:{port}/api/messages")
        print("\n💡 Para testar, use o Bot Framework Emulator:")
        print(f"   - URL: http://localhost:{port}/api/messages")
        print(f"   - App ID: (deixe vazio)")
        print(f"   - App Password: (deixe vazio)")
        print("\n📋 Funcionalidades disponíveis:")
        print("   🔍 Consultar Produtos")
        print("   📦 Consultar Pedidos") 
        print("   💳 Extrato de Compras")
        print("\n" + "="*50)
        print("Pressione Ctrl+C para parar o servidor")
        print("="*50 + "\n")
        
        # Inicia o servidor
        web.run_app(APP, host="localhost", port=port)
        
    except KeyboardInterrupt:
        print("\n\n👋 Bot finalizado pelo usuário")
        
    except ImportError as e:
        print(f"\n❌ Erro de importação: {e}")
        print("\n🔧 Soluções:")
        print("   1. Instale as dependências: pip install -r requirements.txt")
        print("   2. Ative o ambiente virtual")
        print("   3. Verifique se está no diretório correto")
        sys.exit(1)
        
    except Exception as error:
        print(f"\n❌ Erro crítico: {error}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()