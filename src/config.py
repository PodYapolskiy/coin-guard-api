import hydra

cfg = None
with hydra.initialize(version_base=None, config_path="../conf"):
    cfg = hydra.compose(config_name="config")

assert cfg is not None
