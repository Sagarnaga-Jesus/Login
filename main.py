import flet as ft

def main(page: ft.Page):
    
    page.scroll="auto"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30
    
    admin="Holadmin"
    admincontra="admin"
    
    page.add(ft.Text("Inicio de sesion",size=30))
    
    page.add(ft.Icon(icon=ft.Icons.LOCK,
                color=ft.Colors.BLUE_500, 
                size=50
        ))
    
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON, color=ft.Colors.BLUE_500, ))
    contra=(ft.TextField(label="Contraseña",password=True, autofocus=True, icon=ft.Icons.PASSWORD, color=ft.Colors.BLUE_500,))
    
    page.add(correo,contra)
    
    def verifica():
        if admin==correo.value and admincontra==contra.value:
            page.show_dialog(ft.SnackBar(ft.Text("Has iniciado sesion correctamente")))
        else:
            page.show_dialog(ft.SnackBar(ft.Text("Usuario o contraseña incorrecta")))
            
    def olvidado():
        page.show_dialog(ft.SnackBar(ft.Text("Se a enviado su contraseña al correo")))
        
    
    page.add( ft.Button("Iniciar sesion",color=ft.Colors.WHITE ,bgcolor=ft.Colors.BLUE, on_click=verifica))
    page.add( ft.TextButton("¿Olvidaste la contraseña?", on_click=olvidado))
    
    page.add(
            ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOUSE, label="Inicio"),
                    ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="Nuevo"),
                    ft.NavigationBarDestination(icon=ft.Icons.MENU_BOOK, label="Perfil"),
                ],
            )
        
    )
    
ft.run(main)