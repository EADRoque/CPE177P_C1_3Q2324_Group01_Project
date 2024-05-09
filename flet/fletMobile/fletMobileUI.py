from flet import *
import time
def main(page:Page):
    page.padding = 0
    page.spacing = 0    
    page.theme_mode = ThemeMode.LIGHT
    page.window_height = 932
    page.window_width = 430
    page.window_resizable = False
    
    textStudNum: TextField = TextField(label="##########", text_align=TextAlign.LEFT, width=200)
    dropDept: Dropdown = Dropdown(label="DEPT.", width=200, options=[dropdown.Option("CPE"), dropdown.Option("ECE"), dropdown.Option("EE"),])
    buttonConfirm: ElevatedButton = ElevatedButton(text="CONFIRM", color="#FFFFFF", bgcolor="#3066be", width=200, disabled=True)
    buttonJoinZoom: ElevatedButton = ElevatedButton(text="JOIN ZOOM", color="#FFFFFF", bgcolor="#2D8CFF", width=200)
    
    def sign_in(e:ControlEvent) -> None:
        page.clean()
        page.add(
            Stack([
                mobileBG,
                mobileOverlay,
                mobileMain,
            ])
        )
    
    def validate(e: ControlEvent) -> None:
        if all([len(textStudNum.value)==10, dropDept.value]):
            buttonConfirm.disabled = False
        else:
            buttonConfirm.disabled = True
        
        page.update()
        
    textStudNum.on_change = validate
    dropDept.on_change = validate
    
    
    def go_to_Queue(e:ControlEvent) -> None:
        goToQ.visible=False
        page.clean()
        page.add(
            Stack([
                mobileBG,
                mobileOverlay,
                mobileQueueF
            ])
        )
        time.sleep(300)
        page.clean()
        page.add(
            Stack([
                mobileBG,
                mobileOverlay,
                mobileNotif
            ])
        )
        
    def confirm(e:ControlEvent) -> None:
        goToQ.visible = True
        page.clean()
        page.add(
            Stack([
                mobileBG,
                mobileOverlay,
                mobileMode
            ])
        )
    
    def go_to_Zoom(e:ControlEvent) -> None:
        page.clean()
        page.add(
            Stack([
                mobileBG,
                mobileOverlay,
                mobileQueueO
            ])
        )
        time.sleep(300)
        page.clean()
        page.add(
            Stack([
                mobileBG,
                mobileOverlay,
                mobileZoom
            ])
        )
    
    def joinZoom(e: ControlEvent) -> None:
        page.launch_url("https://us05web.zoom.us/j/86267142815?pwd=jexpRRbYRpyEXU9zEB0LiRAUMxNbbb.1")#zoom link
        
    buttonConfirm.on_click = confirm
    buttonJoinZoom.on_click = joinZoom
    header = Container(
        alignment=alignment.top_center,
        padding=20,
        bgcolor="#FFFFFF",
        content=Row([
            Text("ENROLLMENT\nQUEUEING\nSYSTEM", weight=FontWeight.BOLD, color="#0d2650"),
            Image(src="eece.png",width=100,),
            ],
        spacing=190
        )
    )
    
    goToQ = Container(visible=False, content=Row([Text("QUEUE", size=16, weight=FontWeight.BOLD, color="#0d2650"),Icon(name = icons.EXIT_TO_APP_ROUNDED, color="#0d2650")],alignment=MainAxisAlignment.CENTER),on_click=go_to_Queue)
    
    footer = Container(
        alignment=alignment.bottom_center,
        padding=20,
        bgcolor="#FFFFFF",
        content=
            goToQ,
    )
    
    mobileOverlay = Column([
        header,
        footer
        ],
        spacing = 650                  
    )
     
    mobileBG = Container(
        bgcolor="#b4c5e4",
        height=page.window_height,
        width=page.window_width,
        border_radius=15     
    )     
    
    mobileLogin = Container(
        alignment=alignment.center,
        margin=margin.only(top=200),
        content=Column([
            Image(src="eece.png",width=200,),
            Text("ENROLLMENT QUEUEING\nSYSTEM", weight=FontWeight.BOLD, color="#0d2650", size = 16, width=200, text_align=TextAlign.CENTER),
            Container(
                bgcolor="#FFFFFF",
                border_radius=10,
                padding=20,
                width=200,
                content=Row([
                    Image(src="microsoft.png",height=30),
                    Text("SIGN IN", weight=FontWeight.BOLD, color="#0d2650", size=24)
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=20
                )
            )
            ],
        alignment=CrossAxisAlignment.CENTER
        ),
        on_click=sign_in
    )
    
    mobileMain = Container(
        alignment=alignment.center,
        margin=margin.only(top=page.height*0.3),
        content=Column([
            Text("CONFIRM YOUR\nINFORMATION", weight=FontWeight.BOLD, color="#0d2650", size = 24, width=200, text_align=TextAlign.CENTER),
            Text("STUDENT NUMBER", weight=FontWeight.BOLD, color="#0d2650", size = 14, width=200, text_align=TextAlign.CENTER),            
            textStudNum,
            Text("DEPARTMENT", weight=FontWeight.BOLD, color="#0d2650", size = 14, width=200, text_align=TextAlign.CENTER),            
            dropDept,
            buttonConfirm
            ],
        alignment=CrossAxisAlignment.CENTER
        ),
    )
    
    mobileQueueF = Container(
        alignment=alignment.center,
        border_radius=20,
        bgcolor="#FFFFFF",
        margin=margin.only(top=page.height*0.3,left=30,right=30),
        padding=15,
        shadow=BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=Offset(0, 0),
				blur_style=ShadowBlurStyle.OUTER,
		),
        content=Column([
            Text("MODE: F2F", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("YOU'RE ON THE\nCURRENT QUEUE", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("WAIT FOR SFA\n", weight=FontWeight.BOLD, color="#b4c5e4", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("YOUR TICKET\nNUMBER", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text(f"######", weight=FontWeight.BOLD, color="#0d2650", size = 30, width=200, text_align=TextAlign.CENTER),
            Text("CURRENT TICKET\nNUMBER", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text(f"######", weight=FontWeight.BOLD, color="#0d2650", size = 30, width=200, text_align=TextAlign.CENTER)
            ],
            alignment=CrossAxisAlignment.CENTER
        )
    )
    
    mobileQueueO = Container(
        alignment=alignment.center,
        border_radius=20,
        bgcolor="#FFFFFF",
        margin=margin.only(top=page.height*0.3,left=30,right=30),
        padding=15,
        shadow=BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=Offset(0, 0),
				blur_style=ShadowBlurStyle.OUTER,
		),
        content=Column([
            Text("MODE: ONLINE", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("YOU'RE ON THE\nCURRENT QUEUE", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("WAIT FOR SFA\n", weight=FontWeight.BOLD, color="#b4c5e4", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("YOUR TICKET\nNUMBER", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text(f"######", weight=FontWeight.BOLD, color="#0d2650", size = 30, width=200, text_align=TextAlign.CENTER),
            Text("CURRENT TICKET\nNUMBER", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text(f"######", weight=FontWeight.BOLD, color="#0d2650", size = 30, width=200, text_align=TextAlign.CENTER)
            ],
            alignment=CrossAxisAlignment.CENTER
        )
    )
    
    mobileMode = Container(
        alignment=alignment.center,
        border_radius=20,
        margin=margin.only(top=page.height*0.4,left=30,right=30),
        padding=15,
        content=Column([
            Container(
                    alignment=alignment.center,
                    border_radius=20,
                    bgcolor="#FFFFFF",
                    padding=20,
                    shadow=BoxShadow(spread_radius=1,
                            blur_radius=15,
                            color="#3c3744",
                            offset=Offset(0, 0),
                            blur_style=ShadowBlurStyle.OUTER,
                    ),
                    content=Column([
                        Text("QUEUEING ON PROCESS", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=250, text_align=TextAlign.CENTER),
                        Text("CHOOSE MODE", weight=FontWeight.BOLD, color="#b4c5e4", size = 16, width=250, text_align=TextAlign.CENTER)
                    ])
                    ),
            Row([
                Container(
                        alignment=alignment.center,
                        border_radius=20,
                        bgcolor="#FFFFFF",
                        width=150,
                        height=90,
                        shadow=BoxShadow(spread_radius=1,
                                blur_radius=15,
                                color="#3c3744",
                                offset=Offset(0, 0),
                                blur_style=ShadowBlurStyle.OUTER,
                        ),
                        content=Text("F2F", weight=FontWeight.BOLD, color="#0d2650", size = 24, width=200, text_align=TextAlign.CENTER),
                        on_click=go_to_Queue
                    ),
                Container(
                        alignment=alignment.center,
                        border_radius=20,
                        bgcolor="#FFFFFF",
                        width=150,
                        height=90,
                        shadow=BoxShadow(spread_radius=1,
                                blur_radius=15,
                                color="#3c3744",
                                offset=Offset(0, 0),
                                blur_style=ShadowBlurStyle.OUTER,
                        ),
                        content=Text("ONLINE", weight=FontWeight.BOLD, color="#0d2650", size = 24, width=200, text_align=TextAlign.CENTER),
                        on_click=go_to_Zoom
                    ),
                ],
                spacing=20
                ),
            ],
            alignment=CrossAxisAlignment.CENTER
        )
    )
    
    mobileZoom = Container(
        alignment=alignment.center,
        border_radius=20,
        bgcolor="#FFFFFF",
        margin=margin.only(top=page.height*0.3,left=30,right=30),
        padding=15,
        shadow=BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=Offset(0, 0),
				blur_style=ShadowBlurStyle.OUTER,
		),
        content=Column([
            Image(src='zoom.png',width=300),
            buttonJoinZoom
            ],
            alignment=CrossAxisAlignment.CENTER
        )        
    )
    
    mobileNotif = Container(
        alignment=alignment.center,
        border_radius=20,
        bgcolor="#FFFFFF",
        margin=margin.only(top=page.height*0.3,left=30,right=30),
        padding=15,
        shadow=BoxShadow(spread_radius=1,
				blur_radius=15,
				color="#3c3744",
				offset=Offset(0, 0),
				blur_style=ShadowBlurStyle.OUTER,
		),
        content=Column([
            Text("IT'S YOUR TURN", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("GO TO", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            Text("ADVISER", weight=FontWeight.BOLD, color="#0d2650", size = 60, width=200, text_align=TextAlign.CENTER),
            Text(f"TABLE NO. #", weight=FontWeight.BOLD, color="#0d2650", size = 20, width=200, text_align=TextAlign.CENTER),
            ],
            alignment=CrossAxisAlignment.CENTER)
    )
    page.add(
        Stack([
            mobileBG,
            mobileLogin
        ])
    )
    
app(target=main)