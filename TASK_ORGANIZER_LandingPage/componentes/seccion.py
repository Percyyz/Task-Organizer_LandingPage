import reflex as rx

def seccion()->rx.Component:
  return rx.vstack(
      rx.heading(
        rx.text.span("T.Organizer",color=rx.color("jade",7)),
        " te ayudara a organizarte mejor"),

      rx.container(
        rx.text("Ofrece una solución todo en uno que permite crear, asignar y realizar un seguimiento de tareas, integrándose con otras herramientas para facilitar la organización personal y profesional. ",),
        rx.link(rx.button("Registrate",margin_top="6em"),href="https://forms.gle/SPfxQakdfYVi8S6UA"),
      ),
      padding_top="10em",
      align="center",
      text_align="center",
      height="660px"
  )