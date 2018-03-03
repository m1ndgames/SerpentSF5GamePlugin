import offshoot


class SerpentSF5GamePlugin(offshoot.Plugin):
    name = "SerpentSF5GamePlugin"
    version = "0.1.0"

    libraries = []

    files = [
        {"path": "serpent_SF5_game.py", "pluggable": "Game"}
    ]

    config = {
        "fps": 2
    }

    @classmethod
    def on_install(cls):
        print("\n\n%s was installed successfully!" % cls.__name__)

    @classmethod
    def on_uninstall(cls):
        print("\n\n%s was uninstalled successfully!" % cls.__name__)


if __name__ == "__main__":
    offshoot.executable_hook(SerpentSF5GamePlugin)

    plugin_path = offshoot.config["file_paths"]["plugins"]

    context_classifier_path = f"{plugin_path}/SerpentBlankaGameAgentPlugin/files/ml_models/context_classifier.model"

    from serpent.machine_learning.context_classification.context_classifiers.cnn_inception_v3_context_classifier import CNNInceptionV3ContextClassifier
    context_classifier = CNNInceptionV3ContextClassifier(input_shape=(640, 360, 3))

    context_classifier.prepare_generators()
    context_classifier.load_classifier(context_classifier_path)

    self.machine_learning_models["context_classifier"] = context_classifier