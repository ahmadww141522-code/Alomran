import flet as ft
from groq import Groq

client = Groq(api_key="gsk_bKj3W5Yl6t8R7pQ2mN9vL4xZ1sF0hD6gJ3kH5fC8bV1n")

def main(page: ft.Page):
    page.title = "معهد العمران - النظام الشامل"
    page.rtl = True
    page.theme_mode = "light"
    page.padding = 10

    # 1. محتوى تبويبة الدردشة الذكية
    chat_history = ft.ListView(expand=True, spacing=10, padding=10)
    user_input = ft.TextField(
        hint_text="اسأل إدارة معهد العمران...", 
        expand=True, 
        border_radius=10,
        text_align=ft.TextAlign.RIGHT
    )

    def send_click(e):
        if not user_input.value: 
            return
        
        user_text = user_input.value
        chat_history.controls.append(ft.Text(f"أنت: {user_text}", size=14, color="#555555"))
        user_input.value = ""
        page.update()
        
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "أنت مساعد ذكي لإدارة معهد العمران، ردودك مهنية، دقيقة، ومفيدة للطلاب والأساتذة."},
                    {"role": "user", "content": user_text}
                ],
                model="llama3-8b-8192",
            )
            reply = chat_completion.choices[0].message.content
            chat_history.controls.append(ft.Text(f"الإدارة: {reply}", size=14, color="#880E4F", weight="bold"))
        except Exception as ex:
            chat_history.controls.append(ft.Text(f"خطأ في الاتصال: تأكد من الإنترنت.", size=12, color="red"))
            
        page.update()

    chat_tab = ft.Column([
        chat_history,
        ft.Row([
            user_input, 
            ft.ElevatedButton("إرسال", icon=ft.icons.SEND, on_click=send_click, bgcolor="#880E4F", color="white")
        ], spacing=10)
    ], expand=True)

    # 2. محتوى تبويبة الأقسام والمناهج الكاملة
    courses_tab = ft.ListView([
        ft.Card(content=ft.Container(content=ft.Column([
            ft.Row([ft.Icon(ft.icons.ENGINEERING, color="#0D47A1"), ft.Text("هندسة الميكاترونكس والكهرباء", weight="bold", size=16, color="#0D47A1")]),
            ft.Text("دورات احترافية عملية ونظرية تغطي كافة الأساسيات والتطبيقات الهندسية والمشاريع المتقدمة.", size=13, color="#444444")
        ]), padding=15)),
        ft.Card(content=ft.Container(content=ft.Column([
            ft.Row([ft.Icon(ft.icons.SMART_TOY, color="#0D47A1"), ft.Text("التسويق باستخدام الذكاء الاصطناعي", weight="bold", size=16, color="#0D47A1")]),
            ft.Text("كورس متكامل لتدريب الطلاب على أحدث أدوات الذكاء الاصطناعي في التسويق وبناء الحملات الرقمية.", size=13, color="#444444")
        ]), padding=15)),
        ft.Card(content=ft.Container(content=ft.Column([
            ft.Row([ft.Icon(ft.icons.CODE, color="#0D47A1"), ft.Text("برمجة بايثون", weight="bold", size=16, color="#0D47A1")]),
            ft.Text("منهج مخصص للانتقال من الصفر وحتى الاحتراف البرمجي وتطوير التطبيقات.", size=13, color="#444444")
        ]), padding=15)),
    ], expand=True, spacing=10, padding=10)

    # 3. محتوى تبويبة عن المعهد
    about_tab = ft.Container(
        content=ft.Column([
            ft.Row([ft.Icon(ft.icons.INFO, color="#0D47A1"), ft.Text("عن معهد العمران", size=18, weight="bold", color="#0D47A1")]),
            ft.Text("معهد خاص رائد يهدف إلى تقديم أحدث العلوم الهندسية وبرامج الذكاء الاصطناعي بخبرات احترافية عالية.", size=14, color="#333333"),
            ft.Divider(),
            ft.Text("إشراف هندسي وتعليمي متطور لخدمة الطلاب والمتدربين نحو المستقبل.", size=13, color="#666666")
        ], spacing=10),
        padding=15
    )

    # هيكل التبويبات الرئيسي (متوافق 100% مع الإصدارات الحالية باستخدام label)
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        expand=True,
        tabs=[
            ft.Tab(label="الدردشة الذكية", content=chat_tab, icon=ft.icons.CHAT),
            ft.Tab(label="الأقسام والمناهج", content=courses_tab, icon=ft.icons.BOOK),
            ft.Tab(label="عن المعهد", content=about_tab, icon=ft.icons.INFO),
        ],
    )

    # رأس التطبيق الثابت والمرتب
    header = ft.Container(
        content=ft.Row([
            ft.Icon(ft.icons.SCHOOL, color="white"),
            ft.Text("معهد العمران - النظام الشامل", size=18, weight="bold", color="white")
        ], alignment=ft.MainAxisAlignment.CENTER), 
        bgcolor="#0D47A1", 
        padding=15, 
        border_radius=10,
    )

    page.add(header, tabs)

ft.app(target=main)
