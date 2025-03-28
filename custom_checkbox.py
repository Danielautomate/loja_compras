import flet as ft

class CheckboxItem(ft.UserControl):
    def __init__(self, text):
        super().__init__()

        self.text = text
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(value=text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(icon=ft.icons.SAVE, on_click=self.save, visible=False)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE, on_click=self.delete)
        self.checkbox = ft.Checkbox(on_change=self.checkbox_changed)

        self.controls = ft.Row(
            [
                self.checkbox,
                self.text_view,
                self.text_edit,
                self.edit_button,
                self.save_button,
                self.delete_button,
            ]
        )

    def build(self):
        return self.controls

    def edit(self, e):
        """Ativa modo de edição"""
        self.text_view.visible = False
        self.text_edit.visible = True
        self.edit_button.visible = False
        self.save_button.visible = True
        self.delete_button.visible = False
        self.update()

    def save(self, e):
        """Salva a edição"""
        self.text_view.value = self.text_edit.value
        self.text_view.visible = True
        self.text_edit.visible = False
        self.edit_button.visible = True
        self.save_button.visible = False
        self.delete_button.visible = True
        self.update()

    def delete(self, e):
        """Remove o item"""
        self.controls.visible = False
        self.update()

    def checkbox_changed(self, e):
        """Marca ou desmarca o checkbox"""
        estado = "marcado" if self.checkbox.value else "desmarcado"
        print(f"Checkbox {estado}: {self.text_view.value}")
        self.update()

def main(page: ft.Page):
    page.title = "Exemplo de Checkbox"

    def add_task(e):
        new_item = CheckboxItem(f"Produto {len(task_list.controls) + 1}")
        task_list.controls.append(new_item)
        page.update()

    task_list = ft.Column()

    add_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_task)

    page.add(task_list, add_button)

ft.app(target=main)
