from dataclasses import dataclass


@dataclass
class DataIgestionArtifact:
    trained_file_path:str
    test_file_path:str