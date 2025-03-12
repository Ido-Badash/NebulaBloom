from . import SafePath

def add_widgets(layout, widgets):
    for widget in widgets:
        layout.add_widget(widget)

def load_builder_files(builder, safe_path: SafePath, files):
    """Loads the KV files into the Builder object, the files param is an iter of strings."""
    for file in files:
        file = safe_path.path(file, as_string=True)
        builder.load_file(file)