import flet as ft
from groq import Groq

# مفتاحك الحقيقي تم وضعه هنا ليرتاح بالك
client = Groq(api_key="gsk_bKj3W5Yl6t8R7pQ2mN9vL4xZ1sF0hD6gJ3kH5fC8bV1n")

def main(page: ft.Page):
    page.title = "معهد العمران"
    page.rtl = True
    page.theme_mode = "light"
    
    chat_history = ft.ListView(expand=True, spacing=10, padding=10)
    user_input = ft.TextField(hint_text="اسأل إدارة معهد العمران...", expand=True, border_radius=10)

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
                    {"role": "system", "content": "أنت مساعد ذكي لإدارة معهد العمران، ردودك مهنية، قصيرة، ومباشرة."},
                    {"role": "user", "content": user_text}
                ],
                model="llama3-8b-8192",
            )
            reply = chat_completion.choices[0].message.content
            chat_history.controls.append(ft.Text(f"الإدارة: {reply}", size=14, color="#880E4F", weight="bold"))
        except Exception as ex:
            chat_history.controls.append(ft.Text(f"خطأ في الاتصال: تأكد من الإنترنت.", size=12, color="red"))
            
        page.update()

    page.add(
        ft.Container(
            content=ft.Text("معهد العمران - مساعد الذكاء الاصطناعي", size=20, weight="bold", color="white"), 
            bgcolor="#0D47A1", 
            padding=20, 
            border_radius=15
        ),
        chat_history,
        ft.Row([user_input, ft.ElevatedButton("إرسال", on_click=send_click, bgcolor="#880E4F", color="white")])
    )

ft.app(target=main)
