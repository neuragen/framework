from .kernel import Kernel

class ModuleLoader:
    """Loads modules into the kernel."""
    
    def __init__(self, kernel: Kernel):
        self.kernel = kernel

    def load_module(self, module_name: str):
        """Load a module in the kernel (placeholder for actual implementation)."""
        self.kernel.load_plugin(module_name)
