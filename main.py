import flet as ft
from groq import Groq

# تم تثبيت مفتاحك بشكل دائم
client = Groq(api_key="gsk_bKj3W5Yl6t8R7pQ2mN9vL4xZ1sF0hD6gJ3kH5fC8bV1n")

def main(page: ft.Page):
    page.title = "معهد العمران"
    page.rtl = True
    page.theme_mode = "light"
    page.padding = 10

    # 1. تبويبة الدردشة
    chat_history = ft.ListView(expand=True, spacing=10, padding=10)
    user_input = ft.TextField(hint_text="اسأل مساعد معهد العمران...", expand=True, border_radius=10, text_align=ft.TextAlign.RIGHT)

    def send_click(e):
        if not user_input.value: return
        user_text = user_input.value
        chat_history.controls.append(ft.Text(f"أنت: {user_text}", size=14, color="#555555"))
        user_input.value = ""
        page.update()
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "system", "content": "أنت مساعد ذكي لإدارة معهد العمران."}, {"role": "user", "content": user_text}],
                model="llama3-8b-8192",
            )
            reply = chat_completion.choices[0].message.content
            chat_history.controls.append(ft.Text(f"الإدارة: {reply}", size=14, color="#880E4F", weight="bold"))
        except:
            chat_history.controls.append(ft.Text("خطأ في الاتصال بالذكاء الاصطناعي.", size=12, color="red"))
        page.update()

    chat_tab = ft.Column([chat_history, ft.Row([user_input, ft.ElevatedButton("إرسال", on_click=send_click, bgcolor="#880E4F", color="white")], spacing=10)], expand=True)

    # 2. تبويبة الأقسام
    courses_tab = ft.ListView([
        ft.Card(content=ft.Container(content=ft.Column([ft.Text("هندسة الميكاترونكس", weight="bold", color="#0D47A1"), ft.Text("دورات احترافية عملية ونظرية.")]), padding=15)),
        ft.Card(content=ft.Container(content=ft.Column([ft.Text("التسويق بالذكاء الاصطناعي", weight="bold", color="#0D47A1"), ft.Text("تدريب على أحدث أدوات التسويق.")]), padding=15)),
        ft.Card(content=ft.Container(content=ft.Column([ft.Text("برمجة بايثون", weight="bold", color="#0D47A1"), ft.Text("من الصفر حتى الاحتراف.")]), padding=15)),
    ], expand=True, spacing=10, padding=10)

    # 3. تبويبة عن المعهد
    about_tab = ft.Container(content=ft.Column([ft.Text("عن معهد العمران", size=18, weight="bold", color="#0D47A1"), ft.Text("معهد رائد في العلوم الهندسية والذكاء الاصطناعي.")]), padding=15)

    # التبويبات
    tabs = ft.Tabs(selected_index=0, expand=True, tabs=[ft.Tab(text="الدردشة", content=chat_tab), ft.Tab(text="الأقسام", content=courses_tab), ft.Tab(text="عن المعهد", content=about_tab)])
    header = ft.Container(content=ft.Text("معهد العمران", size=20, weight="bold", color="white"), bgcolor="#0D47A1", padding=15, border_radius=10, alignment=ft.alignment.center)

    page.add(header, tabs)

ft.app(target=main)
