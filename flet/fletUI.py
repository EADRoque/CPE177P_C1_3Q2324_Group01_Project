from flet import * #TextField, ElevatedButton, Image, Icon, Text, Container, Row, Column, Dropdown, DataRow, Stack
import requests
import json

# idnum = ""

with open("queue.json", "r") as student_data:
    sdata = json.load(student_data)

with open("admit.json", "r") as admitted_data:
        adata = json.load(admitted_data)
            
students = []
for student in sdata["students"]:
        students.append(student)

admitted = []
for student in adata["students"]:
    admitted.append(student)       
        
def load_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
  
def move_top_item(source_file, destination_file):
    source_data = load_json(source_file)
    if not source_data or "students" not in source_data or not source_data["students"]:
        print("No data to move.")
        return

    top_item = source_data["students"].pop(0)

    destination_data = load_json(destination_file)
    if destination_data is None or "students" not in destination_data:
        destination_data = {"students": []}

    destination_data["students"].append(top_item)

    save_json(source_data, source_file)
    save_json(destination_data, destination_file)
    print("Item moved successfully.")
    
async def main(page:Page):
    page.padding = 0
    page.spacing = 0    
    page.theme_mode = ThemeMode.LIGHT
    page.window_resizable = False
    
    studsInQ = 0
    studsAdmitted = 0
    
    def updateQ():
        nonlocal studsInQ
        queue_data = load_json('queue.json')
        studsInQ = len(queue_data['students'])
        print(studsInQ)
        numInQ.value= str(studsInQ)
    
    def updateC():
        nonlocal studsAdmitted
        completed_data = load_json('admit.json')
        studsAdmitted = len(completed_data['students'])
        print(studsAdmitted)
        numCompleted.value = str(studsAdmitted)
        
    textUsername: TextField = TextField(label=None, text_align=TextAlign.LEFT, width=300)
    textPassword: TextField = TextField(label="#######", text_align=TextAlign.LEFT, width=300, password=True, can_reveal_password=True)
    dropDept: Dropdown = Dropdown(label="DEPT.", width=140, options=[dropdown.Option("CPE"), dropdown.Option("ECE"), dropdown.Option("EE"),])
    dropMode: Dropdown = Dropdown(label="MODE", width=140, options=[dropdown.Option("ONSITE"), dropdown.Option("ONLINE"),])
    buttonStart: ElevatedButton = ElevatedButton(text="START", width=300, disabled=True)
    buttonAdmit: ElevatedButton = ElevatedButton(text="ADMIT NEXT", style=ButtonStyle(bgcolor=colors.WHITE, color="#3c3744", shape=RoundedRectangleBorder(radius=10)),width=200,height=50)
    buttonReject: ElevatedButton = ElevatedButton(text="REJECT NEXT", style=ButtonStyle(bgcolor="#DD8F88", color="#FFFFFF", shape=RoundedRectangleBorder(radius=10)),width=200,height=50)
    
    def validate(e: ControlEvent) -> None:
        if all([textUsername.value, textPassword.value, dropDept.value, dropMode.value]):
            buttonStart.disabled = False
        else:
            buttonStart.disabled = True
        
        page.update()
    
    username = ""
    dept = ""
    mode = ""
    # reqCode = ""
    
    def login(e: ControlEvent) -> None:
        nonlocal username
        username = textUsername.value

        nonlocal dept
        dept = dropDept.value

        nonlocal mode
        mode = dropMode.value

        global idnum
        idnum = str(textPassword.value)
        page.update()
        # r = requests.get(f"http://172.20.10.4:5000/enroller/{idnum}")
        # r = r.json()
        
        # if username == r["enroller"]["name"] and idnum == r["enroller"]["enroller_number"] and dept == r["enroller"]["department_id"] and mode == r["enroller"]["assigned_mode"]:
        if username == "Admin" and idnum == "1234":
            page.clean()
            page.add(
                Stack([
                    mainbg,
                    eece,
                    sidemenu,
                    mainContentView,
			    ])
            )
            identify()
            updateQ()
            updateC()
            page.update()
        else:
            page.clean()
            page.add(
                Stack([
                    loginBG,
                    failedLogin,
                ])
            )
    
    def identify():
        USERNAME.value = username
        USERNAME.update()
        DEPARTMENT.value = dept
        DEPARTMENT.update()
        MODE.value = mode
        MODE.update()
                               
    def logout(e: ControlEvent) -> None:
        page.clean()
        page.add(
			Stack([
				loginBG,
				loginBox,
			])
		)
    
    def view_Q(e):
        mainContentView.visible=True
        page.clean()
        page.add(
                Stack([
                    mainbg,
                    eece,
                    sidemenu,
                    mainContentView,
			    ])
            )
        updateQ()
        updateC()
        page.update()
 
    def full_Q(e):
        mainContentFull.visible=True
        page.clean()
        page.add(
                Stack([
                    mainbg,
                    eece,
                    sidemenu,
                    mainContentFull,
			    ])
            )
        page.update()
   
    def accept_Stud(e):
        mainContentAccept.visible=True
        page.clean()
        page.add(
                Stack([
                    mainbg,
                    eece,
                    sidemenu,
                    mainContentAccept
			    ])
            )
        page.update()
    
    def printvar(e:ControlEvent)->None:
        # print("Username: ", username)
        # print("Password: ", idnum)
        # print("Dept: ", dept)
        # print("Mode: ", mode)
        print("In Queue: ", updateQ())
        print("Completed: ", updateC())
        page.update()
        
    def clearQueue(e: ControlEvent) -> None:
        global students
        students = []
        with open("queue.json", "w") as student_data:
            json.dump({"students": []}, student_data)
            
        global admitted
        admitted = []
        with open("admit.json","w") as admitted_data:
            json.dump({"students": []}, admitted_data)
        
        viewQueue.rows = []
        mainContentView.visible=True
        page.clean()
        page.add(
                Stack([
                    mainbg,
                    eece,
                    sidemenu,
                    mainContentView,
			    ])
            )
        updateQ()
        updateC()
        page.update()
        
    
    def admit(e: ControlEvent) -> None:
        global students
        students = students[1:]
        move_top_item("queue.json","admit.json")

        with open("queue.json", "w") as student_data:
            json.dump({"students": students}, student_data, indent=4, sort_keys=True)
        
        updateQ()
        updateC()
        viewQueue.rows.remove(viewQueue.rows[0])
        viewQueue.update()
    
    def reject(e: ControlEvent) -> None:
        global students
        students = students[1:]
        with open("queue.json", "w") as student_data:
            json.dump({"students": students}, student_data, indent=4, sort_keys=True)
        updateQ()
        updateC()
        viewQueue.rows.remove(viewQueue.rows[0])
        viewQueue.update()
            

    textUsername.on_change = validate
    textPassword.on_change = validate
    dropDept.on_change = validate
    dropMode.on_change = validate
    buttonStart.on_click = login
    buttonAdmit.on_click = admit
    buttonReject.on_click = reject
    
    loginBG = Container(
        bgcolor="#0d2650",
        width=page.window_width,
        height=page.window_height,            
    )     
    
    failedLogin = Container(
        alignment=alignment.center,
        padding=padding.all(100),
		shadow=BoxShadow(spread_radius=1,
			blur_radius=15,
			color="#3c3744",
			offset=Offset(0, 0),
			blur_style=ShadowBlurStyle.OUTER,
		),        
        content=Container(
            bgcolor="#eb4034",
            width=400,
            height=500,
            border_radius=20,
            alignment=alignment.center,
            content=Column([
            Text("Failed Login",weight=FontWeight.BOLD, color="#0d2650", size=48),
			ElevatedButton(text="RETRY",color="#3c3744", width=page.window_width/5, bgcolor=colors.WHITE, on_click=logout),#
            ])
        )
    )
    
    loginBox = Container(
        alignment=alignment.center,
        padding=padding.all(100),
		shadow=BoxShadow(spread_radius=1,
			blur_radius=15,
			color="#3c3744",
			offset=Offset(0, 0),
			blur_style=ShadowBlurStyle.OUTER,
		),
        content=Container(
            bgcolor=colors.WHITE,
            width=400,
            height=500,
            border_radius=20,
            alignment=alignment.center,
            padding=padding.all(50),
            content=Column([
                Row([
                    Container(
                        Text("ENROLLMENT\nQUEUEING\nSYSTEM", weight=FontWeight.BOLD, color="#0d2650")
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
                    alignment=alignment.center,
                    content=Column([
                        Text("Full Name", size=20, weight=FontWeight.BOLD, color="#0d2650"),
                        textUsername,
                        Text("ID", size=20, weight=FontWeight.BOLD, color="#0d2650"),
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
  
    USERNAME = Text(value="", size=20, width=page.window_width/5, color=colors.WHITE, text_align=TextAlign.CENTER)
    DEPARTMENT = Text(value="", size=20, width=page.window_width/5, color=colors.WHITE, text_align=TextAlign.CENTER)
    MODE = Text(value="", size=20, width=page.window_width/5, color=colors.WHITE, text_align=TextAlign.CENTER)

    sidemenu = Container(
		content=Column([
			Image(src="avatarIcon.png",width=500,),
            USERNAME,
            DEPARTMENT,
            MODE,
			ElevatedButton(text="VIEW QUEUE",color="#3c3744", width=page.window_width/5, bgcolor=colors.WHITE, on_click=view_Q),#
			ElevatedButton(text="CLEAR QUEUE",color="#3c3744", width=page.window_width/5, bgcolor=colors.WHITE, on_click=full_Q),#
			ElevatedButton(text="ACCEPT STUDENT",color="#3c3744", width=page.window_width/5, bgcolor=colors.WHITE, on_click=accept_Stud),#
			ElevatedButton(text="LOGOUT",color="#3c3744", width=page.window_width/5, bgcolor=colors.WHITE, on_click=logout),#
			ElevatedButton(text=".",color="#3c3744", width=page.window_width/5, bgcolor=colors.WHITE, on_click=printvar),#
		],

  		),
		padding=10,
		bgcolor="#0D2650",
		width=page.window_width/5,
		height=page.window_height*(9/10),
		border_radius=20,
		margin=margin.all(25),
	
	)
  
    mainbg = Container(
		bgcolor="#D3DEF1",
		width=page.window_width,
        height=page.window_height,           
    )

    eece = Container(
		width=page.window_width,
		height=110,
		alignment=alignment.center_right,
		border_radius=20,
		margin=margin.all(25),
  		shadow=BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=Offset(0, 0),
				blur_style=ShadowBlurStyle.OUTER,
		),
		content=Column([
			Container(
			bgcolor=colors.WHITE,
			padding=10,
			content=Row([
			Container(
       		margin=margin.only(left=(page.window_width/5) + 30),
         	content=Text("1st SEMESTER 2024-25 ENROLLMENT", size=30, weight=FontWeight.BOLD, color=colors.GREY),
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
    
    viewQueue = DataTable(
					width=page.window_width*0.7,
					columns=[
						DataColumn(Text("NAME",color="#3c3744", size=16, weight=FontWeight.BOLD)),
						DataColumn(Text("MODE",color="#3c3744", size=16, weight=FontWeight.BOLD)),
						DataColumn(Text("STUDENT NUMBER",color="#3c3744", size=16, weight=FontWeight.BOLD), numeric=True),
					],
					rows=[DataRow(cells=[
								DataCell(Text(f"{student['name']}",color="#3c3744", size=16, weight=FontWeight.BOLD)),
								DataCell(Text(f"{student['mode']}",color="#3c3744", size=16, weight=FontWeight.BOLD)),
								DataCell(Text(f"{student['student_number']}",color="#3c3744", size=16, weight=FontWeight.BOLD)),
					],) for student in students]
						
					
					
				)
    cv = Column([viewQueue],scroll=True)
    rv = Row([cv],scroll=True,expand=1,vertical_alignment=CrossAxisAlignment.START)
    
    numInQ = Text(value="",color="#3c3744", size=24, weight=FontWeight.BOLD)
    numCompleted = Text(value="",color="#3c3744", size=24, weight=FontWeight.BOLD)
    
    counters = Row([
    		Container( #in queue
			border_radius=10,
			bgcolor=colors.WHITE,
			height= 100,
			width= 400,
			alignment=alignment.center,
			shadow=BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=Offset(0, 0),
				blur_style=ShadowBlurStyle.OUTER,
			),
   			content=Row([
				Icon(name=icons.HOURGLASS_BOTTOM_ROUNDED, color="#3c3744", size=40),
          		Text(f"In Queue: ",color="#3c3744", size=24, weight=FontWeight.BOLD),
                numInQ
            	],
                alignment=MainAxisAlignment.CENTER
            ),	
			),
			Container( #completed
			border_radius=10,
			bgcolor=colors.WHITE,
			height= 100,
			width= 400,
			alignment=alignment.center,
			shadow=BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=Offset(0, 0),
				blur_style=ShadowBlurStyle.OUTER,
				),
   			content=Row([
				Icon(name=icons.CHECKLIST_ROUNDED, color="#3c3744", size=40),
          		Text(f"Completed: ",color="#3c3744", size=24, weight=FontWeight.BOLD),
                numCompleted
            	],
				alignment=MainAxisAlignment.CENTER
            )	
			)],
            spacing=90)
    
    mainContentView = Container(
		margin=margin.only(left = page.window_width/4, top = 150),
		alignment=alignment.center,
  		content = Column([
            counters,
			Container( #data table
				border_radius=10,
				bgcolor=colors.WHITE,
				shadow=BoxShadow(spread_radius=1,
					blur_radius=15,
					color="#3c3744",
					offset=Offset(0, 0),
					blur_style=ShadowBlurStyle.OUTER,
				),				
				height=400,
    			content=
					rv
			)
		],
		spacing=20) 
	)
 
    mainContentFull = Container(
		margin=margin.only(left = page.window_width/4, top = page.window_height/3),
		alignment=alignment.center,
		width=page.window_width*0.65,
		height=page.window_height*0.3,
		border_radius=10,
		visible=False,
		content=Container(
			bgcolor=colors.WHITE,
			alignment=alignment.center,
			padding=padding.all(20),
			content=Column([
   				Text("STOP CURRENT QUEUE PROCESS?", size=28, color="#3c3744", weight=FontWeight.BOLD, width=page.window_width*0.65,text_align=TextAlign.CENTER),
				Text("WARNING: THIS WILL DISABLE STUDENTS TO\n REGISTER FOR QUEUEING", size=24, color="#DD8F88", weight=FontWeight.BOLD, width=page.window_width*0.65, text_align=TextAlign.CENTER),
				Row([
					ElevatedButton("YES", style=ButtonStyle(bgcolor="#fbfff1", color="#3c3744", shape=RoundedRectangleBorder(radius=10)), on_click = clearQueue),#
					ElevatedButton("CANCEL", style=ButtonStyle(bgcolor="#DD8F88", color=colors.RED, shape=RoundedRectangleBorder(radius=10))) #on_click=cancel
				],
				width=page.window_width*0.65,
           		alignment=MainAxisAlignment.CENTER)
			])
		)
	)
    
    mainContentAccept = Container(
		margin=margin.only(left = page.window_width/4, top = page.window_height*0.25),
		alignment=alignment.center,
		visible=False,
  		content = Column([Row([
    		Container( #Search
				border_radius=10,
				bgcolor=colors.WHITE,
				alignment=alignment.center,
				shadow=BoxShadow(spread_radius=1,
					blur_radius=15,
					color="#3c3744",
					offset=Offset(0, 0),
					blur_style=ShadowBlurStyle.OUTER,
					),
				content=TextField(label="STUDENT NUMBER", color="#3c3744", width=500, height=50) #change into a control
			),
			Container(
                #add functionality
       			content=ElevatedButton(text="SEARCH QUEUE", style=ButtonStyle(bgcolor="#0D2650", color="#D3DEF1", shape=RoundedRectangleBorder(radius=10)),width=200,height=50) #on_click=search
			)],
            spacing=50),
            Container(
                content=Row([
                        buttonAdmit,
                        buttonReject
                    ])
            ),
			Container( #data table
				border_radius=10,
				bgcolor=colors.WHITE,
				height = 300,
				shadow=BoxShadow(spread_radius=1,
					blur_radius=15,
					color="#3c3744",
					offset=Offset(0, 0),
					blur_style=ShadowBlurStyle.OUTER,
				),
    			content=
                    viewQueue
					# inQueue
			)
		],
		spacing=20)
	)   
    page.add( # Login Page
        Stack([
            loginBG,
            loginBox,
        ])

    )
    
app(target=main)