from .events import EventManager, ModelLoadedEvent, PluginLoadedEvent
from datetime import datetime

class Kernel:
    """Kernel that manages plugins and models."""
    
    def __init__(self):
        self.event_manager = EventManager()
        self.plugins = []
        self.models = []

    def load_model(self, model_name: str) -> None:
        """Load a model and emit an event."""
        self.models.append(model_name)
        event = ModelLoadedEvent(model_name=model_name)
        self.event_manager.emit(event)
        print(f"[{datetime.now()}] Modelo '{model_name}' carregado.")

    def load_plugin(self, plugin_name: str) -> None:
        """Load a plugin and emit an event."""
        self.plugins.append(plugin_name)
        event = PluginLoadedEvent(plugin_name=plugin_name)
        self.event_manager.emit(event)
        print(f"[{datetime.now()}] Plugin '{plugin_name}' carregado.")
