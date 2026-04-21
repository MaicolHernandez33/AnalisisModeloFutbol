from kedro.pipeline import Pipeline, node
from .nodes import saludar

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=saludar,
            inputs=None,
            outputs="mensaje"
        )
    ])