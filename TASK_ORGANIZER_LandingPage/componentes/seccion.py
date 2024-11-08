import reflex as rx

def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text.span("T.Organizer",color=rx.color("jade",10)),
        " te ayudara a organizarte mejor"),

      rx.container(
        rx.text("planifica, organiza y sigue tus tareas en una plataforma intuitiva que se adapta a tus necesidades. Desde recordatorios hasta integración con tus herramientas favoritas, ¡es todo lo que necesitas para ser más eficiente! ",margin_top="4em"),
        rx.link(rx.button("Registrate",margin_top="6em"),href="https://forms.gle/qg1UsWrgkbh15K5y9",is_external=True),
      ),
      padding_top="6em",
      align="center",
      text_align="center",
      height="675px",
      background=rx.color("mauve",6)
  )