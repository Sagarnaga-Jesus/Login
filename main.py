import flet as ft

def main(page: ft.Page):
    
    page.scroll="auto"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 30
    
    admin="Holadmin"
    admincontra="admin"
    
    aviso=""
    page.add(aviso)
    
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
            aviso=page.show_dialog(ft.SnackBar(ft.Text("Has iniciado sesion correctamente")))
        else:
            aviso=page.show_dialog(ft.SnackBar(ft.Text("Usuario o contraseña incorrecta")))
            
    def olvidado():
        page.show_dialog(ft.SnackBar(ft.Text("Se a enviado su contraseña al correo")))
        
    
    page.add( ft.ElevatedButton("Iniciar sesion",color=ft.Colors.WHITE ,bgcolor=ft.Colors.BLUE, on_click=verifica))
    page.add( ft.TextButton("¿Olvidaste la contraseña?", on_click=olvidado))
    
ft.run(main)