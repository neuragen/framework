from neuragens.kernel.kernel import Kernel
from neuragens.kernel.module_loader import ModuleLoader
from neuragens.ui.gradio.gradio_plugin import GradioPlugin
from neuragens.ui.gradio.gradio_listener import gradio_listener
from neuragens.ui.streamlit.streamlit_plugin import StreamlitPlugin
from neuragens.ui.streamlit.streamlit_listener import streamlit_listener

def main():
    #https://github.com/mbrav/design_patterns_python

    kernel = Kernel()
    module_loader = ModuleLoader(kernel)

    kernel.event_manager.subscribe('PluginLoadedEvent', gradio_listener)
    kernel.event_manager.subscribe('PluginLoadedEvent', streamlit_listener)

    gradio_plugin = GradioPlugin()
    streamlit_plugin = StreamlitPlugin()

    kernel.load_plugin("GradioPlugin")
    kernel.load_plugin("StreamlitPlugin")

if __name__ == "__main__":
    main()
