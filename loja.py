import flet as ft

# Base de produtos (simulando um banco de dados)
produtos = {
    "101": {"nome": "Paracetamol", "referencia": "Ref-001"},
    "102": {"nome": "Dipirona", "referencia": "Ref-002"},
    "103": {"nome": "Ibuprofeno", "referencia": "Ref-003"},
    "104": {"nome": "Omeprazol", "referencia": "Ref-004"},
}
# Função para buscar e listar todos os produtos compatíveis
def buscar_produto(e, campo_pesquisa, resultado_texto):
    termo = campo_pesquisa.value.strip().lower()
    resultados = []

    if not termo:
        resultado_texto.value = "Digite um código ou nome!"
    else:
        for codigo, dados in produtos.items():
            if termo in codigo or termo in dados["nome"].lower():
                resultados.append(f'Código: {codigo} | Nome: {dados["nome"]}')  #  Mostra tudo junto

        if resultados:
            resultado_texto.value = "\n".join(resultados)  #Junta todos os resultados em uma única string
        else:
            resultado_texto.value = "Produto não encontrado!"

    resultado_texto.update()

# Criar botões alinhados à direita
def criar_botoes():
    return ft.Row(
        [
            ft.ElevatedButton(text="Finalizar"),
            ft.ElevatedButton(text="Cancelar")
    
        ],
        alignment=ft.MainAxisAlignment.END
    )
# Interface principal
def main(page: ft.Page):
    page.title = "CARRINHO DE COMPRAS"

    # Configuração da janela fixa
    page.window_width = 350
    page.window_height = 400
    page.window_resizable = False
    page.window_always_on_top = True
    page.update()

    def add_task(e):
        print(resultado_texto.value)


    # Elementos da interface
    txt_titulo = ft.Text("PRODUTO", size=16, weight="bold")
    campo_pesquisa = ft.TextField(
        label="Digite o código ou nome do produto",
        text_align=ft.TextAlign.LEFT,
        on_change=lambda e: buscar_produto(e, campo_pesquisa, resultado_texto)  # Aciona a busca ao digitar
    )
    resultado_texto = ft.Text("", selectable=True)  # Permite copiar o resultado

    new_button =ft.FloatingActionButton(icon= ft.icons.ADD, on_click=add_task)
    # Adiciona elementos à página
    page.add(
        txt_titulo,
        campo_pesquisa,
        resultado_texto,
        new_button,
        criar_botoes()  # Botões alinhados à direita
    )



ft.app(target=main)

