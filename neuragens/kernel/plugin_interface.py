class PluginInterface:
    def load(self):
        """Load the plugin."""
        raise NotImplementedError("Plugins must implement the load method.")
