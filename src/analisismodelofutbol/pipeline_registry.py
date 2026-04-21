from kedro.pipeline import Pipeline
from analisismodelofutbol.pipelines.data_processing import pipeline as dp

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "__default__": dp.create_pipeline(),
    }