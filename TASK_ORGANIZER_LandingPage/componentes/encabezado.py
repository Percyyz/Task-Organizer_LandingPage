import reflex as rx

def encabezado()->rx.Component:
  return rx.hstack(
      rx.hstack(
        rx.icon(tag="notebook-pen"),
        rx.heading("Task Organizer",size="6",weight="bold"),
        align_items="center"
      ),
      rx.hstack(
        rx.link("Inicio",href="/#",size="3",weight="bold"),
        justify="end",
        spacing="5"
      ),
      justify="between",
      align_items="center",
      padding="1em",
      width="100%",
      bg=rx.color("jade",6)
    )