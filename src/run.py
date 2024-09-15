from mflux.flux.flux import Flux1
from mflux.config.config import Config

flux = Flux1.from_alias(
    alias="schnell",
    quantize=8,
)

prompt = "A cat holding a sign that says hello world"

image = flux.generate_image(
    prompt=prompt,
    seed=0,
    config=Config(num_inference_steps=4),
)

image.save(path="flux-schnell.png")
