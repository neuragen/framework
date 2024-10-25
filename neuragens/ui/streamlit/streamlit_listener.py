from neuragens.kernel.events import PluginLoadedEvent

def streamlit_listener(event: PluginLoadedEvent):
    """Listener for the Streamlit plugin loaded event."""
    print(f"Streamlit listener: {event.plugin_name} foi carregado.")
