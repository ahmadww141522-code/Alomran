import flet as ft
from openai import OpenAI

# ====================== ضع مفتاح Groq هنا ======================
client = OpenAI(
    api_key="gsk_bKj3W5Yl6t8R7pQ2mN9vL4xZ1sF0hD6gJ3kH5fC8bV1n",
    base_url="https://api.groq.com/openai/v1",
)
# =============================================================

def main(page: ft.Page):
    page.title = "معهد العمران - Al-Omran Institute"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.scroll = ft.ScrollMode.ALWAYS  # ← حل مشكلة الكيبورد

    page.window_width = 380
    page.window_height = 780
    page.window_resizable = False

    sections_data = {
        "الحروف والكتابة | Letters & Writing 📚": [
            "منهج الحروف والكتابة (الأطفال والأساسيات)",
            "• النظرة العامة: برنامج تأسيسي متكامل يهدف إلى بناء قاعدة صلبة وواضحة في القراءة والكتابة السليمة.",
            "• التفاصيل: يركز المنهج على تدريب الطفل على مخارج الحروف الصحيحة، وعمل ربط بصري وسمعي بين شكل الحرف وصوته، مع تدريبات مكثفة على مسكة القلم."
        ],
        "الرسم الفني | Fine Arts 🎨": [
            "منهج الرسم الفني والتعبير البصري",
            "• النظرة العامة: مساحة إبداعية لتطوير الذائقة الفنية وصقل المواهب الكامنة.",
            "• التفاصيل: يعتمد البرنامج على دراسة أساسيات دمج الألوان، فهم درجات الظل والضوء، ونظريات التكوين الفني باستخدام خامات متعددة."
        ],
        "تصميم الأزياء | Fashion Design 👗": [
            "منهج تصميم الأزياء وعالم الموضة",
            "• النظرة العامة: كورس احترافي مبسط لعشاق الفن والابتكار في عالم الألبسة.",
            "• التفاصيل: يتناول الكورس دراسة خطوط الموضة، رسم الباترونات المسطحة، وتنسيق الألوان والأقمشة لتحويل الأفكار إلى قطع أزياء حقيقية."
        ],
        "تصميم مجوهرات | Jewelry Design 💍": [
            "منهج تصميم الإكسسوارات والمجوهرات",
            "• النظرة العامة: فن دقيق يدمج بين الأصالة والابتكار لصناعة قطع فريدة ومميزة.",
            "• التفاصيل: يتعلم الطالب أساسيات تصميم الحلي، دراسة توازن الأشكال، دمج الخامات، والأسس النظرية للتصميم الهندسي الفاخر."
        ],
        "الأنشطة والكروشيه | Crafts & Crochet 🧶": [
            "منهج الأنشطة والمهارات اليدوية",
            "• النظرة العامة: تدريبات عملية وذهنية تهدف لتنمية التنسيق الدقيق والمهارات الحركية.",
            "• التفاصيل: يركز المنهج على تعلم غرز الكروشيه، قراءة الباترون اليدوي، وإنتاج مشغولات نافذة تعزز التركيز والصبر."
        ],
        "فنون الميك أب | Makeup Art 💄": [
            "منهج فنون التجميل والعناية الشخصية",
            "• النظرة العامة: كورس تجميلي شامل يغطي أصول المكياج الاحترافي والعناية الذاتية.",
            "• التفاصيل: يشمل دراسة أنواع البشرة، نظريات الألوان، تحديد شكل الوجه، وتقنيات المكياج (النهاري والسهرة) بمعايير احترافية."
        ],
        "تعديل السلوك | Behavior Modification ☀️": [
            "برنامج تعديل السلوك والإرشاد التربوي",
            "• النظرة العامة: برنامج إرشادي علمي لبناء عادات حياتية إيجابية ومستقرة.",
            "• التفاصيل: يعتمد على نظريات نفسية لفهم السلوكيات وتعديلها بالتعزيز الإيجابي، إدارة الغضب، وتعزيز الثقة بالنفس."
        ],
        "تحسين النطق | Speech Improvement 🗣️": [
            "برنامج تحسين النطق والتواصل اللفظي",
            "• النظرة العامة: جلسات لمعالجة عيوب النطق ومخارج الحروف وتحقيق الطلاقة.",
            "• التفاصيل: يرتكز على تقييم مخارج الأصوات، تقوية عضلات اللسان، وتمارين التنفس لعلاج التلعثم والتحدث بوضوح."
        ],
        "الحساب الذهني | Mental Math 🔢": [
            "منهج الحساب الذهني وتطوير الذكاء",
            "• النظرة العامة: برنامج لتنشيط فصوص الدماغ والسرعة الفائقة في العمليات الحسابية.",
            "• التفاصيل: يعتمد على تقنيات الذاكرة البصرية والعد التخيلي لحل المسائل المعقدة بسرعة تفوق الآلة الحاسبة."
        ],
        "المتابعة المدرسية | School Follow-up 📖": [
            "برنامج المتابعة المدرسية الأكاديمية",
            "• النظرة العامة: مرافقة تعليمية يومية لضمان التفوق الدراسي وحل المعضلات.",
            "• التفاصيل: إشراف على مراجعة الدروس، المساعدة في الواجبات، وتبسيط المواد العلمية المعقدة لضمان أعلى الدرجات."
        ]
    }

    # ====== منطقة الشرح الثابتة ======
    display_column = ft.Column([], alignment=ft.MainAxisAlignment.START)
    display_container = ft.Container(
        content=display_column,
        padding=10,
        bgcolor="#FCE4EC",
        border_radius=15,
        visible=False,
    )

    def clicked(e):
        title = e.control.data
        data = sections_data.get(title)

        if display_container.visible and display_column.controls and display_column.controls[0].value == title:
            display_container.visible = False
            display_column.controls.clear()
            page.update()
            return

        display_column.controls.clear()
        if data:
            display_column.controls.append(ft.Text(title, size=14, weight=ft.FontWeight.BOLD, color="#880E4F"))
            for line in data:
                is_title = "منهج" in line or "برنامج" in line
                display_column.controls.append(
                    ft.Text(
                        line,
                        size=14 if is_title else 13,
                        weight=ft.FontWeight.BOLD if is_title else ft.FontWeight.NORMAL,
                        color="#880E4F"
                    )
                )
        display_container.visible = True
        page.update()

    items = list(sections_data.keys())
    rows = []
    for i in range(0, len(items), 2):
        row_items = items[i:i+2]
        row_controls = []
        for title in row_items:
            row_controls.append(
                ft.Container(
                    content=ft.Text(title, size=13, weight=ft.FontWeight.BOLD, color="#880E4F", text_align=ft.TextAlign.CENTER),
                    bgcolor="#FFF0F5",
                    border_radius=12,
                    padding=10,
                    expand=True,
                    on_click=clicked,
                    data=title
                )
            )
        rows.append(ft.Row(row_controls, spacing=8))

    grid_container = ft.Container(content=ft.Column(rows, spacing=6), padding=5)

    # ========== الشات التفاعلي ==========
    chat = ft.ListView(expand=True, spacing=8, padding=10, auto_scroll=True)
    
    # ====== حل مشكلة الكيبورد ======
    field = ft.TextField(
        hint_text="اكتب استفسارك هنا للإدارة...",
        expand=True,
        border_radius=10,
        text_size=13,
        on_submit=lambda e: send(e),
    )

    def send(e):
        if not field.value or not field.value.strip():
            return

        user_text = field.value.strip()
        chat.controls.append(ft.Text(f"أنت: {user_text}", size=13, color="#555555"))
        field.value = ""
        page.update()

        thinking = ft.Text("الإدارة عم تفكر...", size=12, color="grey", italic=True)
        chat.controls.append(thinking)
        page.update()

        try:
            sections_info = "\n".join([f"- {k}: {v[1]}" for k, v in sections_data.items()])

            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": f"""أنت المساعد الرسمي لمعهد العمران.
ردودك مهنية، واضحة، ومفيدة للأهالي والطلاب.
جاوب دائماً بالعربية الفصحى المبسطة.
هذه هي الأقسام المتوفرة في المعهد:
{sections_info}

إذا سأل عن قسم معين، أعطِ تفاصيل مفيدة.
إذا السؤال عام، رحب به ووجهه للأقسام المناسبة."""
                    },
                    {"role": "user", "content": user_text}
                ],
                temperature=0.7,
            )
            reply = completion.choices[0].message.content

            if thinking in chat.controls:
                chat.controls.remove(thinking)

            chat.controls.append(
                ft.Text(f"إدارة المعهد: {reply}", size=13, color="#880E4F", weight=ft.FontWeight.BOLD)
            )
        except Exception as ex:
            if thinking in chat.controls:
                chat.controls.remove(thinking)
            chat.controls.append(
                ft.Text("خطأ في الاتصال. تأكد من الإنترنت أو المفتاح.", size=12, color="red")
            )

        page.update()

    send_btn = ft.ElevatedButton("إرسال", on_click=send, bgcolor="#880E4F", color="white")

    # ========== الهيدر ==========
    header = ft.Container(
        content=ft.Stack([
            ft.Image(
                src="icon.png",
                width=float("inf"),
                height=160,
                fit="cover",
                repeat=ft.ImageRepeat.NO_REPEAT
            ),
            ft.Container(bgcolor="#E1F5FE", opacity=0.88, width=float("inf"), height=160),
            ft.Column([
                ft.Row([
                    ft.Text("معهد العمران", size=22, weight=ft.FontWeight.BOLD, color="black"),
                    ft.Text(" | ", color="black", size=20),
                    ft.Text("Al-Omran Institute", size=18, weight=ft.FontWeight.BOLD, color="black")
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Text("الدليل الشامل للدورات والخدمات التعليمية للأهالي", size=12, color="black", weight=ft.FontWeight.BOLD)
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ]),
        height=160,
        border_radius=20,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        width=float("inf")
    )

    # ====== ترتيب العناصر ======
    content_area = ft.Column([
        header,
        grid_container,
        display_container,
        ft.Container(content=chat, expand=True, padding=5, bgcolor="#FAFAFA", border_radius=10),
        ft.Row([field, send_btn], spacing=8)
    ], expand=True, spacing=6)

    page.add(content_area)

ft.app(target=main)
