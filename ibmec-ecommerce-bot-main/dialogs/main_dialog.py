# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
)
from botbuilder.dialogs.prompts import (
    ChoicePrompt,
    PromptOptions,
)
from botbuilder.dialogs.choices import Choice
from botbuilder.core import MessageFactory, UserState

# FUNCIONALIDADES COMPLETAS HABILITADAS
from dialogs.consultar_produtos_dialog import ConsultarProdutosDialog
from dialogs.consultar_pedidos_dialog import ConsultarPedidosDialog
from dialogs.extrato_compra_dialog import ExtratoCompraDialog

class MainDialog(ComponentDialog):
    """
    Diálogo principal com todas as funcionalidades
    """
    
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.user_state = user_state

        # ADICIONANDO TODOS OS DIÁLOGOS
        self.add_dialog(ConsultarProdutosDialog(user_state))
        self.add_dialog(ConsultarPedidosDialog())
        self.add_dialog(ExtratoCompraDialog())

        # Adiciona o diálogo principal (waterfall)
        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__,
                [
                    self.prompt_option_step,
                    self.process_option_step,
                    self.restart_step
                ],
            )
        )

        # Adiciona o prompt de escolha
        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))

        # Define o diálogo inicial
        self.initial_dialog_id = WaterfallDialog.__name__

    async def prompt_option_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """
        Apresenta o menu principal completo
        """
        return await step_context.prompt(
            ChoicePrompt.__name__,
            PromptOptions(
                prompt=MessageFactory.text(
                    "🛍️ **BEM-VINDO AO IBMEC MALL!**\n\n"
                    "Sou seu assistente virtual de compras. Como posso ajudar?\n\n"
                    "🔥 **Escolha uma opção:**"
                ),
                choices=[
                    Choice("🔍 Consultar Produtos"), 
                    Choice("📦 Consultar Pedidos"), 
                    Choice("💳 Extrato de Compras"),
                    Choice("ℹ️ Status do Sistema")
                ],
            ),
        )

    async def process_option_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """
        Processa a opção escolhida
        """
        option = step_context.result.value

        if option == "🔍 Consultar Produtos":
            return await step_context.begin_dialog("ConsultarProdutosDialog")
            
        elif option == "📦 Consultar Pedidos":
            return await step_context.begin_dialog("ConsultarPedidosDialog")
            
        elif option == "💳 Extrato de Compras":
            return await step_context.begin_dialog("ExtratoCompraDialog")
            
        elif option == "ℹ️ Status do Sistema":
            await step_context.context.send_activity(
                MessageFactory.text("🔄 Testando conexão com a API...")
            )
            
            try:
                from api.product_api import ProductAPI
                api = ProductAPI()
                
                # Testa a conexão
                if api.test_connection():
                    await step_context.context.send_activity(
                        MessageFactory.text(
                            "✅ **SISTEMA ONLINE!**\n\n"
                            "🔗 **API:** Conectada\n"
                            "🌐 **Status:** Funcionando\n"
                            "📡 **Comunicação:** OK\n\n"
                            "🎯 Todas as funcionalidades disponíveis!"
                        )
                    )
                else:
                    await step_context.context.send_activity(
                        MessageFactory.text(
                            "⚠️ **PROBLEMA NA API**\n\n"
                            "🔧 Verifique a configuração da URL\n"
                            "📡 Teste manual: abra a URL da API no navegador\n\n"
                            "💡 **Dica:** Certifique-se que a API está online no Azure"
                        )
                    )
            except Exception as e:
                await step_context.context.send_activity(
                    MessageFactory.text(
                        f"❌ **ERRO TÉCNICO:**\n\n"
                        f"```\n{str(e)}\n```\n\n"
                        f"🔧 Verifique o arquivo de configuração"
                    )
                )

        return await step_context.end_dialog()

    async def restart_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        """
        Finaliza e oferece voltar ao menu
        """
        await step_context.context.send_activity(
            MessageFactory.text(
                "✅ **Operação concluída!**\n\n"
                "💬 Digite qualquer mensagem para voltar ao menu principal."
            )
        )
        
        return await step_context.end_dialog()