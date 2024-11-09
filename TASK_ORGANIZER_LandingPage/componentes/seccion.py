import reflex as rx

def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text.span("T.Organizer",color=rx.color("jade",10)),
        " te ayudará a organizarte mejor",size="9"),

      rx.container(
        rx.hstack(
          rx.text("Planifica, organiza y sigue tus tareas en una plataforma intuitiva que se adapta a tus necesidades. Desde recordatorios hasta integración con tus herramientas favoritas, ¡es todo lo que necesitas para ser más eficiente! ",
            margin_top="4em",
            weight="bold",
            size="5"
            ),
          rx.image(src="https://cdn-icons-png.flaticon.com/512/8028/8028200.png",
          alt="mi imagen",
          width="200px",
          margin_top="2em",
          align_items="center"
          ),
          spacing="3em"
        ),
          rx.link(
            rx.button("Registrate",margin_top="6em",size="4"),
            href="https://forms.gle/mVBJT5NJPs2Xwy8j6",
            is_external=True),
            margin_top="4em",
            position="relative",
      ),
      rx.image(
        src="https://static.vecteezy.com/system/resources/thumbnails/050/739/516/small/black-gold-curve-border-for-corner-certificate-design-free-png.png",
        width="300px",
        position="absolute",
        bottom="0",
        left="0"
      ),
      padding_top="4em",
      align="center",
      text_align="center",
      height="676px",
      background=rx.color("mauve",6)
  )