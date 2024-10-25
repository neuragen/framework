from neuragens.kernel.events import PluginLoadedEvent

class StreamlitPlugin:
    """Streamlit plugin implementation."""
    
    def load(self):
        """Load the Streamlit plugin."""
        print("Streamlit Plugin Loaded.")
