from neuragens.kernel.events import PluginLoadedEvent

class GradioPlugin:
    """Gradio plugin implementation."""
    
    def load(self):
        """Load the Gradio plugin."""
        print("Gradio Plugin Loaded.")
