from mflux.flux.flux import Flux1
from mflux.config.config import Config
from pathlib import Path


def main():
    outPath = Path(__file__).parent.parent / "out"
    outPath.mkdir(parents=True, exist_ok=True)

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

    image.save(outPath / "flux-schnell.png")


if __name__ == "__main__":
    main()
