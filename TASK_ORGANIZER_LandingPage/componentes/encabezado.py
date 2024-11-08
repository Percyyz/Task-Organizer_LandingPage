import reflex as rx

def encabezado()->rx.Component:
  return rx.hstack(
      rx.hstack(
        rx.icon(tag="notebook-pen"),
        rx.heading("Task Organizer...",size="6",weight="bold"),
        align_items="center"
      ),
      justify="between",
      align_items="center",
      padding="1em",
      width="100%",
      bg=rx.color("sky",7)
    )