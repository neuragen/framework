from neuragens.kernel.events import PluginLoadedEvent

def gradio_listener(event: PluginLoadedEvent):
    """Listener for the Gradio plugin loaded event."""
    print(f"Gradio listener: {event.plugin_name} foi carregado.")
