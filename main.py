import flet as ft

def main(page: ft.Page):
    
    page.scroll="auto"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30
    
    admin="Holadmin"
    admincontra="admin"
    
    page.add(ft.Text("Inicio de sesion",size=30))
    
    page.add(ft.Icon(icon=ft.Icons.PERSON,
                color=ft.Colors.BLUE_500, 
                size=50
        ))
    
    nombre=(ft.TextField(label="Nombre"))
    apellido=(ft.TextField(label="Apellido"))
    correo=(ft.TextField(label="Correo",autofocus=True))
    contra=(ft.TextField(label="Contraseña",password=True, autofocus=True))
    
    page.add(correo,contra)
    
    def verifica():
        if admin==correo.value and admincontra==contra.value:
            page.add(ft.Text("Correcta"))
        else:
            page.add(ft.Text("Correo o contraseña incorrecta"))
    
    page.add( ft.ElevatedButton("Iniciar sesion",color=ft.Colors.WHITE ,bgcolor=ft.Colors.BLUE, on_click=verifica))
    page.add( ft.TextButton("¿Olvidaste la contraseña?"))
    
ft.run(main)