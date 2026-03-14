import flet as ft

def main(page: ft.Page):
    
    page.scroll="auto"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30
    page.window.width = 400
    page.window.height = 650
    page.bgcolor = ft.Colors.PURPLE_800
    
    admin="Holadmin"
    admincontra="admin"
    
    def ver_contra():
        contra.password = not contra.password
        contra.update()
        
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON ))
    contra=(ft.TextField(label="Contraseña",suffix=ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=ver_contra) ,password=True, autofocus=True, icon=ft.Icons.PASSWORD))
    
    def verifica():
            if admin==correo.value and admincontra==contra.value:
                page.show_dialog(ft.SnackBar(ft.Text("Has iniciado sesion correctamente")))
                inicio()
            else:
                page.show_dialog(ft.SnackBar(ft.Text("Usuario o contraseña incorrecta")))
                

    def olvidado():
            page.show_dialog(ft.SnackBar(ft.Text("Se a enviado su contraseña al correo")))
            
    
            
    iniciar=( ft.Button("Iniciar sesion",color=ft.Colors.WHITE ,bgcolor=ft.Colors.BLUE, on_click=verifica))
    olvidada =( ft.TextButton("¿Olvidaste la contraseña?", on_click=olvidado))
        
    def login ():
        page.controls.clear
        page.title="Login"
        
        page.add(ft.Column(
            controls=[
                ft.Text("Inicio de sesion",size=30, weight=ft.FontWeight.BOLD),
                ft.Icon(icon=ft.Icons.LOCK, color=ft.Colors.BLUE_700, size=60),
                correo,
                contra,
                iniciar,
                olvidada
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ))
    
    def cambio_pantalla():
        
        page.controls.clear()
        
        if page.navigation_bar.selected_index == 0:
            inicio()
            
        elif page.navigation_bar.selected_index == 1:
            nuevo()
            
        elif page.navigation_bar.selected_index == 2:
            perfil()
            
        
        
    navegador =  ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(icon=ft.Icons.HOUSE, label="Inicio"),
                    ft.NavigationBarDestination(icon=ft.Icons.BOOK, label="Nuevo", ),
                    ft.NavigationBarDestination(icon=ft.Icons.MENU_BOOK, label="Perfil"),
                ],
                on_change=cambio_pantalla
            )
        
    
    def inicio():
        page.controls.clear()
        page.title="Inicio"
        
        page.add(ft.Text("Inicio",size=30, weight=ft.FontWeight.BOLD),)
        page.add(ft.Text("Has iniciado secion correctamente bienvenido",size=15, weight=ft.FontWeight.BOLD),)
        page.navigation_bar = (navegador)
        page.update()
        
    def nuevo():
        page.controls.clear()
        page.title="Nuevo"
        
        page.add(ft.Text("Nuevo",size=30, weight=ft.FontWeight.BOLD),)
        page.add(ft.Text("Nuevo se convertira en cerrar aplicacion",size=50, weight=ft.FontWeight.BOLD),)
        page.navigation_bar = (navegador)
        page.update()
        
    def perfil():
        page.controls.clear()
        page.title="Perfil"
        
        page.add(ft.Text("Perfil",size=30, weight=ft.FontWeight.BOLD),)
        page.navigation_bar = (navegador)
        page.update()
    
    login()
    
    
ft.run(main)