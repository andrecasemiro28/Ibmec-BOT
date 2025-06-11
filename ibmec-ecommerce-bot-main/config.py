#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

class DefaultConfig:
    """ Configurações do Bot """

    # Porta onde o bot vai rodar (padrão do Bot Framework)
    PORT = int(os.environ.get("PORT", 3978))
    
    # Configuração para desenvolvimento local (sem autenticação)
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_TENANT_ID = os.environ.get("MicrosoftAppTenantId", "")
    
    # URL da sua API no Azure (direto)
    URL_PREFIX = os.environ.get("URL_PREFIX", "https://ibmec-ecommerce-app-gydeg9hye0eabpbf.brazilsouth-01.azurewebsites.net")
    
    # NOVO: Configurações do API Management
    APIM_BASE_URL = os.environ.get("APIM_BASE_URL", "")
    APIM_SUBSCRIPTION_KEY = os.environ.get("APIM_SUBSCRIPTION_KEY", "")
    
    @staticmethod
    def print_config():
        """Método para debug - mostra as configurações carregadas"""
        print("🔧 Configurações carregadas:")
        print(f"   PORT: {DefaultConfig.PORT}")
        print(f"   APP_ID: {'***' if DefaultConfig.APP_ID else 'Vazio (desenvolvimento local)'}")
        print(f"   URL_PREFIX: {DefaultConfig.URL_PREFIX}")
        print(f"   APIM_BASE_URL: {DefaultConfig.APIM_BASE_URL or 'Não configurado'}")
        print(f"   APIM_SUBSCRIPTION_KEY: {'***' if DefaultConfig.APIM_SUBSCRIPTION_KEY else 'Não configurado'}")
        print("="*50)