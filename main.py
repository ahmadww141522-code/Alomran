import flet as ft

def main(page: ft.Page):
    page.title = "معهد العمران - Al-Omran Institute"
    page.padding = 0
    page.theme_mode = "light"
    page.rtl = True

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

    display_column = ft.Column([], alignment="start")
    display_container = ft.Container(
        content=display_column,
        padding=15,
        bgcolor="#FCE4EC",
        border_radius=15
    )

    def clicked(e):
        data = sections_data.get(e.control.data)
        display_column.controls.clear()
        if data:
            for line in data:
                display_column.controls.append(ft.Text(line, size=15 if "منهج" in line or "برنامج" in line else 14, weight="bold" if "منهج" in line or "برنامج" in line else "normal", color="#880E4F"))
        page.update()

    items = list(sections_data.keys())
    rows = []
    for i in range(0, len(items), 2):
        row_items = items[i:i+2]
        row_controls = []
        for title in row_items:
            row_controls.append(ft.Container(
                content=ft.Text(title, size=21, weight="bold", color="#880E4F", text_align="center"),
                bgcolor="#FFF0F5", border_radius=15, padding=20, expand=True,
                on_click=clicked, data=title
            ))
        rows.append(ft.Row(row_controls, spacing=10))

    grid_container = ft.Container(content=ft.Column(rows, spacing=10), padding=5)

    chat = ft.ListView(expand=True, spacing=8, padding=10)
    field = ft.TextField(hint_text="اكتب استفسارك هنا للإدارة...", expand=True, border_radius=10, text_size=13)

    def send(e):
        if field.value:
            user_text = field.value
            chat.controls.append(ft.Text(f"أنت: {user_text}", size=12, color="#555555"))
            q = field.value.strip().lower()
            field.value = ""
            
            # ردود ذكية تفهم الأسئلة الشائعة وتجاوب بشكل احترافي بدون أخطاء انترنت
            if "كيفك" in q or "مرحب" in q or "أهل" in q or "السلام" in q:
                reply = "أهلاً بك يا هلا! منور معهد العمران، كيف يمكنني مساعدتك اليوم بخصوص دوراتنا ومناهجنا؟"
            elif "شغل" in q or "ترتيب" in q or "وضع" in q or "شو اخبار" in q:
                reply = "الأمور تمام التمام وكل الدورات والبرامج التعليمية متوفرة وجاهزة لتسجيل الطلاب، تفضل باختيار أي قسم بالأعلى لمعرفة تفاصيله!"
            elif "سعر" in q or "تكلفة" in q or "قسط" in q or "رسوم" in q:
                reply = "يسعدنا انضمامك إلينا! يرجى التواصل مباشرة مع إدارة المعهد لمعرفة الرسوم والتفاصيل المالية الخاصة بكل كورس."
            elif "موقع" in q or "عنوان" in q or "وين" in q:
                reply = "معهد العمران يرحب بك دائماً، يمكنك زيارتنا في مقر المعهد أو مراسلتنا هنا لأي استفسار أكاديمي."
            else:
                reply = f"أهلاً بك في معهد العمران! لقد تلقينا استفسارك ( {user_text} )، ونؤكد لك أن جميع برامجنا وأقسامنا متاحة ويمكنك الضغط عليها بالأعلى للاطلاع على تفاصيلها الكاملة."

            chat.controls.append(ft.Text(f"إدارة المعهد: {reply}", size=12, color="#880E4F", weight="bold"))
            page.update()

    send_btn = ft.ElevatedButton("إرسال", on_click=send)

    header = ft.Container(
        content=ft.Column([
            ft.Row([
                ft.Image(src="icon.png", width=40, height=40),
                ft.Text("معهد العمران", size=22, weight="bold", color="white"),
                ft.Text(" | ", color="white", size=20),
                ft.Text("Al-Omran", size=20, weight="bold", color="white")
            ], alignment="center"),
            ft.Text("الدليل الشامل للدورات والخدمات التعليمية للأهالي", size=13, color="#FFEB3B", weight="bold")
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor="#0D47A1",
        height=140,
        border_radius=20,
        padding=10,
        width=float("inf")
    )

    content_area = ft.Column([
        header,
        grid_container,
        display_container,
        ft.Divider(height=5),
        ft.Container(content=chat, height=90, padding=5, bgcolor="#FAFAFA", border_radius=10),
        ft.Row([field, send_btn], spacing=8)
    ], expand=True, spacing=8, scroll=ft.ScrollMode.AUTO)

    page.add(content_area)

ft.app(target=main)
