import flet as ft

def main(page:ft.Page):
	page.padding = 0
	page.spacing = 0    

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
  
	sidemenu = ft.Container(
		content=ft.Column([
			ft.Image(src="avatarIcon.png",width=500,),
			ft.Text("Name",width=page.window_width/5, text_align=ft.TextAlign.CENTER),
			ft.Text("Department",width=page.window_width/5, text_align=ft.TextAlign.CENTER),
			ft.ElevatedButton(text="VIEW QUEUE",color="#3c3744", width=page.window_width/5, bgcolor=ft.colors.WHITE, on_click=view_Q),#
			ft.ElevatedButton(text="FULL QUEUE",color="#3c3744", width=page.window_width/5, bgcolor=ft.colors.WHITE, on_click=full_Q),#
			ft.ElevatedButton(text="ACCEPT STUDENT",color="#3c3744", width=page.window_width/5, bgcolor=ft.colors.WHITE, on_click=accept_Stud),#
			# ft.TextButton(text=".", width=page.window_width/5, bgcolor=ft.colors.WHITE),
			# ft.TextButton(text=".", width=page.window_width/5, bgcolor=ft.colors.WHITE),
			# ft.TextButton(text=".", width=page.window_width/5, bgcolor=ft.colors.WHITE),	
		],

  		),
		padding=10,
		bgcolor="#0D2650",
		width=page.window_width/5,
		height=page.window_height*(9/10),
		border_radius=10,
		margin=ft.margin.all(25),
	
	)
  
	bg = ft.Container(
		bgcolor="#D3DEF1",
		width=page.window_width,
        height=page.window_height,
        border_radius=20,             
    )

	eece = ft.Container(
		width=page.window_width,
		height=110,
		alignment=ft.alignment.center_right,
		border_radius=20,
		margin=ft.margin.all(25),
		content=ft.Column([
			ft.Container(
			bgcolor=ft.colors.WHITE,
			padding=10,
			content=ft.Row([
			ft.Container(
	       		margin=ft.margin.only(left=(page.window_width/5) + 30),
	         	content=ft.Text("1st Semester 2024-25 Enrollment", size=36, weight=ft.FontWeight.BOLD, color=ft.colors.GREY),
	         	),
			ft.Container(
				content=ft.Image(
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
 
	mainContentView = ft.Container(
		margin=ft.margin.only(left = page.window_width/4, top = page.window_height/3),
		alignment=ft.alignment.center,
  		content = ft.Column([ft.Row([
    		ft.Container( #in queue
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
   			content=ft.Row([
				ft.Icon(name=ft.icons.HOURGLASS_BOTTOM_ROUNDED, color="#3c3744", size=40),
          		ft.Text("In Queue: 0",color="#3c3744", size=24, weight=ft.FontWeight.BOLD)
            	],
                alignment=ft.MainAxisAlignment.CENTER
            ),	
			),
			ft.Container( #completed
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
   			content=ft.Row([
				ft.Icon(name=ft.icons.CHECKLIST_ROUNDED, color="#3c3744", size=40),
          		ft.Text("Completed: 0",color="#3c3744", size=24, weight=ft.FontWeight.BOLD),
            	],
				alignment=ft.MainAxisAlignment.CENTER
            )	
			)],
            spacing=90),
			ft.Container( #data table
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
 
	mainContentFull = ft.Container(
		margin=ft.margin.only(left = page.window_width/4, top = page.window_height/3),
		alignment=ft.alignment.center,
		width=page.window_width*0.65,
		height=page.window_height*0.3,
		border_radius=10,
		visible=False,
		content=ft.Container(
			bgcolor=ft.colors.WHITE,
			alignment=ft.alignment.center,
			padding=ft.padding.all(20),
			content=ft.Column([
   				ft.Text("STOP CURRENT QUEUE PROCESS?", size=28, color="#3c3744", weight=ft.FontWeight.BOLD, width=page.window_width*0.65,text_align=ft.TextAlign.CENTER),
				ft.Text("WARNING: THIS WILL DISABLE STUDENTS TO\n REGISTER FOR QUEUEING", size=24, color="#DD8F88", weight=ft.FontWeight.BOLD, width=page.window_width*0.65, text_align=ft.TextAlign.CENTER),
				ft.Row([
					ft.ElevatedButton("YES", style=ft.ButtonStyle(bgcolor="#fbfff1", color="#3c3744", shape=ft.RoundedRectangleBorder(radius=10))), #on_click=stop_Q
					ft.ElevatedButton("CANCEL", style=ft.ButtonStyle(bgcolor="#DD8F88", color=ft.colors.RED, shape=ft.RoundedRectangleBorder(radius=10))) #on_click=cancel
				],
				width=page.window_width*0.65,
           		alignment=ft.MainAxisAlignment.CENTER)
			])
		)
	)
 
	mainContentAccept = ft.Container(
		margin=ft.margin.only(left = page.window_width/4, top = page.window_height/3),
		alignment=ft.alignment.center,
		visible=False,
  		content = ft.Column([ft.Row([
    		ft.Container( #Search
				border_radius=10,
				bgcolor=ft.colors.WHITE,
				alignment=ft.alignment.center,
				shadow=ft.BoxShadow(spread_radius=1,
					blur_radius=15,
					color="#3c3744",
					offset=ft.Offset(0, 0),
					blur_style=ft.ShadowBlurStyle.OUTER,
					),
				content=ft.TextField(label="STUDENT NUMBER", color="#3c3744", width=500, height=50)
			),
			ft.Container(
       			content=ft.ElevatedButton(text="SEARCH QUEUE", style=ft.ButtonStyle(bgcolor="#0D2650", color="#D3DEF1", shape=ft.RoundedRectangleBorder(radius=10))) #on_click=search
			)],
            spacing=90),
			ft.Container( #data table
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

	page.add(
		ft.Stack([
      		bg,
   			eece,
			sidemenu,
			mainContentView,
			mainContentFull,
			mainContentAccept
			])
		)
 
ft.app(target=main)
