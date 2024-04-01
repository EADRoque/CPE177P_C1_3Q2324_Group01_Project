import flet as ft

def main(page:ft.Page):
    page.padding = 0
    page.spacing = 0    
    bg = ft.Container(
        bgcolor="#0d2650",
        width=page.window_width,
        height=page.window_height,
        border_radius=20,             
    )       

    def getFN(e):
        fullname = str(e.control.value)
        print(fullname)
        return fullname
    
    def getId(e):
        idnum = str(e.control.value)
        print(idnum)
        return idnum
    
    def login(e):

        if (getFN == "admin" and getId == 1234567):
            print("Logged in")
        else:
            print("out")

    loginBox = ft.Container(
        alignment=ft.alignment.center,
        padding=ft.padding.all(150),
        content=ft.Container(
            bgcolor=ft.colors.WHITE,
            width=400,
            height=500,
            border_radius=20,
            alignment=ft.alignment.center,
            padding=ft.padding.all(50),
            content=ft.Column([
                ft.Row([
                    ft.Container(
                        ft.Text("ENROLLMENT\nQUEUEING\nSYSTEM", weight=ft.FontWeight.BOLD)
                    ),
                    ft.Container(
                        content=ft.Image(
                            src="eece.png",
                            height=90,
                        ),
                    )
                ],
                spacing=70,
                ),
                ft.Container(
                    alignment=ft.alignment.center,
                    content=ft.Column([
                        ft.Text("Full Name", size=20, weight=ft.FontWeight.BOLD, color="#0d2650"),
                        ft.TextField(label=None, width=300, on_submit=getFN),
                        ft.Text("ID", size=20, weight=ft.FontWeight.BOLD, color="#0d2650"),
                        ft.TextField(label="####", width=300, on_submit=getId),
                        ft.Row([
                            ft.Dropdown( #dept
                                width=140,
                                label="DEPT.",
                                options=[
                                    ft.dropdown.Option("CPE"),
                                    ft.dropdown.Option("ECE"),
                                    ft.dropdown.Option("EE"),
                                ],),
                            ft.Dropdown(#mode
                                width=140,
                                label="MODE",
                                options=[
                                    ft.dropdown.Option("ONSITE"),
                                    ft.dropdown.Option("ONLINE"),
                                ],)
                        ],
                        spacing=20),
                        ft.ElevatedButton(
                            text="START",
                            height=40, 
                            width=300, 
                            style=ft.ButtonStyle(bgcolor="#0D2650", color="#D3DEF1", shape=ft.RoundedRectangleBorder(radius=10)),
                            on_click=login)


                    ])
                )
                
            ])
            
        )      
    )
    
    page.add(
        ft.Stack([
            bg,
            loginBox,        
            ]),

        
        
    )

ft.app(target=main)