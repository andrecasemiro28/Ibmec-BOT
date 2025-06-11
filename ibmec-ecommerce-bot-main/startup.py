#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# Garantir que encontra os módulos
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

print("🚀 Iniciando IBMEC MALL Bot...")
print(f"📁 Diretório: {current_dir}")

try:
    # Importa diretamente (Azure já instalou via Oryx)
    from aiohttp import web
    print("✅ aiohttp importado!")
    
    from app import APP
    print("✅ app importado!")
    
    # Configurar porta do Azure
    port = int(os.environ.get("PORT", 3978))
    print(f"🌐 Porta: {port}")
    
    # Verificar configurações essenciais
    app_id = os.environ.get("MicrosoftAppId", "")
    if not app_id:
        print("⚠️  MicrosoftAppId não configurado (modo desenvolvimento)")
    else:
        print(f"✅ Bot ID configurado: {app_id[:8]}...")
    
    print("🚀 Iniciando servidor...")
    web.run_app(APP, host="0.0.0.0", port=port)
    
except ImportError as e:
    print(f"❌ Erro de importação: {e}")
    sys.exit(1)
    
except Exception as error:
    print(f"❌ Erro crítico: {error}")
    import traceback
    traceback.print_exc()
    sys.exit(1)