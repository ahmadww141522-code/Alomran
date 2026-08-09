import flet as ft
from openai import OpenAI

# ====================== ضع مفتاح xAI هنا ======================
client = OpenAI(
    api_key="ضع_مفتاح_xAI_هنا",          # ← غيّر هذا السطر بمفتاح xAI الحقيقي
    base_url="https://api.x.ai/v1",
)
# =============================================================

def main(page: ft.Page):
    page.title = "معهد العمران - النظام الشامل"
    page.rtl = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 10

    # ========== تبويبة الدردشة ==========
    chat_history = ft.ListView(expand=True, spacing=10, padding=10, auto_scroll=True)
    
    user_input = ft.TextField(
        hint_text="اسأل إدارة معهد العمران...",
        expand=True,
        border_radius=10,
        text_align=ft.TextAlign.RIGHT,
        on_submit=lambda e: send_click(e)
    )

    def send_click(e):
        if not user_input.value or not user_input.value.strip():
            return

        user_text = user_input.value.strip()
        chat_history.controls.append(
            ft.Text(f"أنت: {user_text}", size=14, color="#555555", text_align=ft.TextAlign.RIGHT)
        )
        user_input.value = ""
        page.update()

        thinking = ft.Text("الإدارة عم تفكر...", size=12, color="grey", italic=True)
        chat_history.controls.append(thinking)
        page.update()

        try:
            completion = client.chat.completions.create(
                model="grok-3",
                messages=[
                    {
                        "role": "system",
                        "content": "أنت المساعد الرسمي لمعهد العمران. ردودك مهنية وواضحة ومفيدة للطلاب والأساتذة. جاوب دائماً بالعربية الفصحى المبسطة."
                    },
                    {"role": "user", "content": user_text}
                ],
                temperature=0.7,
            )
            reply = completion.choices[0].message.content

            chat_history.controls.remove(thinking)
            chat_history.controls.append(
                ft.Text(f"الإدارة: {reply}", size=14, color="#880E4F", weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.RIGHT)
            )
        except Exception as ex:
            chat_history.controls.remove(thinking)
            chat_history.controls.append(
                ft.Text(f"خطأ في الاتصال: تأكد من الإنترنت أو المفتاح", size=12, color="red")
            )

        page.update()

    chat_tab = ft.Column(
        [
            chat_history,
            ft.Row(
                [
                    user_input,
                    ft.ElevatedButton(
                        "إرسال",
                        icon=ft.Icons.SEND,
                        on_click=send_click,
                        bgcolor="#880E4F",
                        color="white"
                    )
                ],
                spacing=10
            )
        ],
        expand=True
    )

    # ========== تبويبة الأقسام والمناهج ==========
    courses_tab = ft.ListView(
        [
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.ENGINEERING, color="#0D47A1"),
                            ft.Text("هندسة الميكاترونكس والكهرباء", weight=ft.FontWeight.BOLD, size=16, color="#0D47A1")
                        ]),
                        ft.Text("دورات احترافية عملية ونظرية تغطي كافة الأساسيات والتطبيقات الهندسية والمشاريع المتقدمة.", size=13, color="#444444")
                    ]),
                    padding=15
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.SMART_TOY, color="#0D47A1"),
                            ft.Text("التسويق باستخدام الذكاء الاصطناعي", weight=ft.FontWeight.BOLD, size=16, color="#0D47A1")
                        ]),
                        ft.Text("كورس متكامل لتدريب الطلاب على أحدث أدوات الذكاء الاصطناعي في التسويق وبناء الحملات الرقمية.", size=13, color="#444444")
                    ]),
                    padding=15
                )
            ),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Icon(ft.Icons.CODE, color="#0D47A1"),
                            ft.Text("برمجة بايثون", weight=ft.FontWeight.BOLD, size=16, color="#0D47A1")
                        ]),
                        ft.Text("منهج مخصص للانتقال من الصفر وحتى الاحتراف البرمجي وتطوير التطبيقات.", size=13, color="#444444")
                    ]),
                    padding=15
                )
            ),
        ],
        expand=True,
        spacing=10,
        padding=10
    )

    # ========== تبويبة عن المعهد ==========
    about_tab = ft.Container(
        content=ft.Column(
            [
                ft.Row([
                    ft.Icon(ft.Icons.INFO, color="#0D47A1"),
                    ft.Text("عن معهد العمران", size=18, weight=ft.FontWeight.BOLD, color="#0D47A1")
                ]),
                ft.Text("معهد خاص رائد يهدف إلى تقديم أحدث العلوم الهندسية وبرامج الذكاء الاصطناعي بخبرات احترافية عالية.", size=14, color="#333333"),
                ft.Divider(),
                ft.Text("إشراف هندسي وتعليمي متطور لخدمة الطلاب والمتدربين نحو المستقبل.", size=13, color="#666666")
            ],
            spacing=10
        ),
        padding=15
    )

    # ========== التبويبات ==========
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        expand=True,
        tabs=[
            ft.Tab(label="الدردشة الذكية", content=chat_tab, icon=ft.Icons.CHAT),
            ft.Tab(label="الأقسام والمناهج", content=courses_tab, icon=ft.Icons.BOOK),
            ft.Tab(label="عن المعهد", content=about_tab, icon=ft.Icons.INFO),
        ],
    )

    # ========== الرأس ==========
    header = ft.Container(
        content=ft.Row(
            [
                ft.Icon(ft.Icons.SCHOOL, color="white"),
                ft.Text("معهد العمران - النظام الشامل", size=18, weight=ft.FontWeight.BOLD, color="white")
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        bgcolor="#0D47A1",
        padding=15,
        border_radius=10,
    )

    page.add(header, tabs)

ft.app(target=main)
