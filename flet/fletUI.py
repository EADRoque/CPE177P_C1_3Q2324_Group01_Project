import flet as ft
from flet import TextField, ElevatedButton, Image, Icon, Text, Container, Row, Column, Dropdown, Stack
from flet_core.control_event import ControlEvent

def main(page:ft.Page):
    page.padding = 0
    page.spacing = 0    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_resizable = False  
    
    textUsername: TextField = TextField(label="FULL NAME", text_align=ft.TextAlign.LEFT, width=300)
    textPassword: TextField = TextField(label="ID", text_align=ft.TextAlign.LEFT, width=300, password=True)
    dropDept: Dropdown = Dropdown(label="DEPT.", width=140, options=[ft.dropdown.Option("CPE"), ft.dropdown.Option("ECE"), ft.dropdown.Option("EE"),])
    dropMode: Dropdown = Dropdown(label="MODE", width=140, options=[ft.dropdown.Option("ONSITE"), ft.dropdown.Option("ONLINE"),])
    buttonStart: ElevatedButton = ElevatedButton(text="START", width=300, disabled=True)
    
    def validate(e: ControlEvent) -> None:
        if all([textUsername.value, textPassword.value, dropDept.value, dropMode.value]):
            buttonStart.disabled = False
        else:
            buttonStart.disabled = True
        
        page.update()
        
    def login(e: ControlEvent) -> None:
        print("Username: ", textUsername.value)
        print("Password: ", textPassword.value)
        print("Dept: ", dropDept.value)
        print("Mode: ", dropMode.value)

        if textUsername.value == "admin" and  textPassword.value == "1234567":
            page.clean()
            page.add(
                Stack([
                    mainbg,
                    eece,
                    sidemenu,
                    mainContentView,
                    mainContentFull,
                    mainContentAccept
			    ])
            )
        else:
            page.clean()
            page.add(
                Stack([
                    loginBG,
                    failedLogin,
                ])
            )

    def view_Q(e):
        mainContentView.visible=True
        mainContentFull.visible=False
        mainContentAccept.visible=False
        page.update()
 
    def full_Q(e):
        mainContentView.visible=False
        mainContentFull.visible=True
        mainContentAccept.visible=False
        page.update()
   
    def accept_Stud(e):
        mainContentView.visible=False
        mainContentFull.visible=False
        mainContentAccept.visible=True
        page.update()
          
    textUsername.on_change = validate
    textPassword.on_change = validate
    dropDept.on_change = validate
    dropMode.on_change = validate
    buttonStart.on_click = login

    loginBG = ft.Container(
        bgcolor="#0d2650",
        width=page.window_width,
        height=page.window_height,
        border_radius=20,             
    )     
    
    failedLogin = Container(
        alignment=ft.alignment.center,
        padding=ft.padding.all(100),
		shadow=ft.BoxShadow(spread_radius=1,
			blur_radius=15,
			color="#3c3744",
			offset=ft.Offset(0, 0),
			blur_style=ft.ShadowBlurStyle.OUTER,
		),        
        content=Container(
            bgcolor="#eb4034",
            width=400,
            height=500,
            border_radius=20,
            alignment=ft.alignment.center,
            content=Text("Failed Login",weight=ft.FontWeight.BOLD, color="#0d2650", size=48)
        )
    )
    
    loginBox = Container(
        alignment=ft.alignment.center,
        padding=ft.padding.all(100),
		shadow=ft.BoxShadow(spread_radius=1,
			blur_radius=15,
			color="#3c3744",
			offset=ft.Offset(0, 0),
			blur_style=ft.ShadowBlurStyle.OUTER,
		),
        content=Container(
            bgcolor=ft.colors.WHITE,
            width=400,
            height=500,
            border_radius=20,
            alignment=ft.alignment.center,
            padding=ft.padding.all(50),
            content=Column([
                Row([
                    Container(
                        Text("ENROLLMENT\nQUEUEING\nSYSTEM", weight=ft.FontWeight.BOLD, color="#0d2650")
                    ),
                    Container(
                        content=Image(
                            src="eece.png",
                            height=90,
                        ),
                    )
                ],
                spacing=70,
                ),
                Container(
                    alignment=ft.alignment.center,
                    content=Column([
                        Text("Full Name", size=20, weight=ft.FontWeight.BOLD, color="#0d2650"),
                        textUsername,
                        Text("ID", size=20, weight=ft.FontWeight.BOLD, color="#0d2650"),
                        textPassword,
                        Row([
                            dropDept,
                            dropMode
                        ],
                        spacing=20),
                        buttonStart
                    ])
                )
                
            ])
            
        )      
    )
  
    sidemenu = Container(
		content=Column([
			Image(src="avatarIcon.png",width=500,),
			Text("{textUsername.value}",width=page.window_width/5, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
			Text("{dropDept.value}",width=page.window_width/5, size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE, text_align=ft.TextAlign.CENTER),
			ElevatedButton(text="VIEW QUEUE",color="#3c3744", width=page.window_width/5, bgcolor=ft.colors.WHITE, on_click=view_Q),#
			ElevatedButton(text="FULL QUEUE",color="#3c3744", width=page.window_width/5, bgcolor=ft.colors.WHITE, on_click=full_Q),#
			ElevatedButton(text="ACCEPT STUDENT",color="#3c3744", width=page.window_width/5, bgcolor=ft.colors.WHITE, on_click=accept_Stud),#	
		],

  		),
		padding=10,
		bgcolor="#0D2650",
		width=page.window_width/5,
		height=page.window_height*(9/10),
		border_radius=10,
		margin=ft.margin.all(25),
	
	)
  
    mainbg = Container(
		bgcolor="#D3DEF1",
		width=page.window_width,
        height=page.window_height,
        border_radius=20,             
    )

    eece = Container(
		width=page.window_width,
		height=110,
		alignment=ft.alignment.center_right,
		border_radius=20,
		margin=ft.margin.all(25),
		content=Column([
			Container(
			bgcolor=ft.colors.WHITE,
			padding=10,
			content=Row([
			Container(
       		margin=ft.margin.only(left=(page.window_width/5) + 30),
         	content=Text("1st SEMESTER 2024-25 ENROLLMENT", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.GREY),
         	),
			Container(
				content=Image(
					src="eece.png",
					height=100,
					),
				)
 
				],
                spacing=100,
                )
 
			)
 
		])
	)
 
    mainContentView = Container(
		margin=ft.margin.only(left = page.window_width/4, top = page.window_height/3),
		alignment=ft.alignment.center,
  		content = Column([ft.Row([
    		Container( #in queue
			border_radius=10,
			bgcolor=ft.colors.WHITE,
			height= 100,
			width= 400,
			alignment=ft.alignment.center,
			shadow=ft.BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=ft.Offset(0, 0),
				blur_style=ft.ShadowBlurStyle.OUTER,
			),
   			content=Row([
				Icon(name=ft.icons.HOURGLASS_BOTTOM_ROUNDED, color="#3c3744", size=40),
          		Text("In Queue: 0",color="#3c3744", size=24, weight=ft.FontWeight.BOLD)
            	],
                alignment=ft.MainAxisAlignment.CENTER
            ),	
			),
			Container( #completed
			border_radius=10,
			bgcolor=ft.colors.WHITE,
			height= 100,
			width= 400,
			alignment=ft.alignment.center,
			shadow=ft.BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=ft.Offset(0, 0),
				blur_style=ft.ShadowBlurStyle.OUTER,
				),
   			content=Row([
				Icon(name=ft.icons.CHECKLIST_ROUNDED, color="#3c3744", size=40),
          		Text("Completed: 0",color="#3c3744", size=24, weight=ft.FontWeight.BOLD),
            	],
				alignment=ft.MainAxisAlignment.CENTER
            )	
			)],
            spacing=90),
			Container( #data table
				border_radius=10,
				bgcolor=ft.colors.WHITE,
				shadow=ft.BoxShadow(spread_radius=1,
					blur_radius=15,
					color="#3c3744",
					offset=ft.Offset(0, 0),
					blur_style=ft.ShadowBlurStyle.OUTER,
				),				
    			content=ft.DataTable(
					width=page.window_width*0.7,

					columns=[
						ft.DataColumn(ft.Text("NAME",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
						ft.DataColumn(ft.Text("MODE",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
						ft.DataColumn(ft.Text("STUDENT NUMBER",color="#3c3744", size=16, weight=ft.FontWeight.BOLD), numeric=True),
						ft.DataColumn(ft.Text("")),
						ft.DataColumn(ft.Text(""))
					],
					rows=[
						ft.DataRow(
							cells=[
								ft.DataCell(ft.Text("GUEVARRA, DOMINIC S.",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("F2F",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("2021105049",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.ElevatedButton(text="ADMIT", style=ft.ButtonStyle(bgcolor=ft.colors.WHITE, color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10)))), #on_click=admit
								ft.DataCell(ft.ElevatedButton(text="X", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10)))) #on_click=deny
							],
						),
						ft.DataRow(
							cells=[
								ft.DataCell(ft.Text("GUEVARRA, DOMINIC S.",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("F2F",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("2021105049",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.ElevatedButton(text="ADMIT", style=ft.ButtonStyle(bgcolor=ft.colors.WHITE, color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10)))),
								ft.DataCell(ft.ElevatedButton(text="X", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10))))  
							],
						),
						ft.DataRow(
							cells=[
								ft.DataCell(ft.Text("GUEVARRA, DOMINIC S.",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("F2F",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("2021105049",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.ElevatedButton(text="ADMIT", style=ft.ButtonStyle(bgcolor=ft.colors.WHITE, color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10)))),
								ft.DataCell(ft.ElevatedButton(text="X", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10))))    
							],
						),
					],
					
				)
			)
		],
		spacing=50) 
	)
 
    mainContentFull = Container(
		margin=ft.margin.only(left = page.window_width/4, top = page.window_height/3),
		alignment=ft.alignment.center,
		width=page.window_width*0.65,
		height=page.window_height*0.3,
		border_radius=10,
		visible=False,
		content=Container(
			bgcolor=ft.colors.WHITE,
			alignment=ft.alignment.center,
			padding=ft.padding.all(20),
			content=Column([
   				Text("STOP CURRENT QUEUE PROCESS?", size=28, color="#3c3744", weight=ft.FontWeight.BOLD, width=page.window_width*0.65,text_align=ft.TextAlign.CENTER),
				Text("WARNING: THIS WILL DISABLE STUDENTS TO\n REGISTER FOR QUEUEING", size=24, color="#DD8F88", weight=ft.FontWeight.BOLD, width=page.window_width*0.65, text_align=ft.TextAlign.CENTER),
				Row([
					ElevatedButton("YES", style=ft.ButtonStyle(bgcolor="#fbfff1", color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10))), #on_click=stop_Q
					ElevatedButton("CANCEL", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10))) #on_click=cancel
				],
				width=page.window_width*0.65,
           		alignment=ft.MainAxisAlignment.CENTER)
			])
		)
	)
 
    mainContentAccept = Container(
		margin=ft.margin.only(left = page.window_width/4, top = page.window_height/3),
		alignment=ft.alignment.center,
		visible=False,
  		content = Column([Row([
    		Container( #Search
				border_radius=10,
				bgcolor=ft.colors.WHITE,
				alignment=ft.alignment.center,
				shadow=ft.BoxShadow(spread_radius=1,
					blur_radius=15,
					color="#3c3744",
					offset=ft.Offset(0, 0),
					blur_style=ft.ShadowBlurStyle.OUTER,
					),
				content=TextField(label="STUDENT NUMBER", color="#3c3744", width=500, height=50) #change into a control
			),
			Container(
                #add functionality
       			content=ElevatedButton(text="SEARCH QUEUE", style=ft.ButtonStyle(bgcolor="#0D2650", color="#D3DEF1", shape=ft.RoundedRectangleBorder(radius=10))) #on_click=search
			)],
            spacing=90),
			Container( #data table
				border_radius=10,
				bgcolor=ft.colors.WHITE,
				shadow=ft.BoxShadow(spread_radius=1,
					blur_radius=15,
					color="#3c3744",
					offset=ft.Offset(0, 0),
					blur_style=ft.ShadowBlurStyle.OUTER,
				),				
    			content=ft.DataTable(
					width=page.window_width*0.7,

					columns=[
						ft.DataColumn(ft.Text("NAME",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
						ft.DataColumn(ft.Text("MODE",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
						ft.DataColumn(ft.Text("STUDENT NUMBER",color="#3c3744", size=16, weight=ft.FontWeight.BOLD), numeric=True),
						ft.DataColumn(ft.Text("")),
						ft.DataColumn(ft.Text(""))
					],
					rows=[
						ft.DataRow(
							cells=[
								ft.DataCell(ft.Text("GUEVARRA, DOMINIC S.",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("F2F",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("2021105049",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.ElevatedButton(text="ADMIT", style=ft.ButtonStyle(bgcolor=ft.colors.WHITE, color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10)))), #on_click=admit
								ft.DataCell(ft.ElevatedButton(text="X", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10))))  #on_click=deny
							],
						),
						ft.DataRow(
							cells=[
								ft.DataCell(ft.Text("GUEVARRA, DOMINIC S.",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("F2F",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("2021105049",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.ElevatedButton(text="ADMIT", style=ft.ButtonStyle(bgcolor=ft.colors.WHITE, color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10)))),
								ft.DataCell(ft.ElevatedButton(text="X", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10))))  
							],
						),
						ft.DataRow(
							cells=[
								ft.DataCell(ft.Text("GUEVARRA, DOMINIC S.",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("F2F",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.Text("2021105049",color="#3c3744", size=16, weight=ft.FontWeight.BOLD)),
								ft.DataCell(ft.ElevatedButton(text="ADMIT", style=ft.ButtonStyle(bgcolor=ft.colors.WHITE, color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10)))),
								ft.DataCell(ft.ElevatedButton(text="X", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10))))    
							],
						),
					],
					
				)
			)
		],
		spacing=50)
	)   
    page.add( # Login Page
        Stack([
            loginBG,
            loginBox,
        ]),
    )
    
ft.app(target=main)
