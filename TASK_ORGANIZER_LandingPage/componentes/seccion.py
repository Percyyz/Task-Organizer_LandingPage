import reflex as rx

def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text.span("T.Organizer",color=rx.color("jade",10)),
        " te ayudara a organizarte mejor",size="9"),

      rx.container(
        rx.hstack(
          rx.text("Planifica, organiza y sigue tus tareas en una plataforma intuitiva que se adapta a tus necesidades. Desde recordatorios hasta integración con tus herramientas favoritas, ¡es todo lo que necesitas para ser más eficiente! ",margin_top="4em",weight="bold",
                size="5"),
          rx.image(src="",alt="mi imagen")
        ),
        rx.hstack(
          rx.link(rx.button("Registrate",margin_top="6em",size="4"),href="https://forms.gle/mVBJT5NJPs2Xwy8j6",is_external=True),
            justify="end",
            margin_top="4em"
        )
      ),
      padding_top="6em",
      align="center",
      text_align="center",
      height="675px",
      background=rx.color("mauve",6)
  )