from mflux.config.config import Config
from mflux.flux.flux import Flux1
from pathlib import Path
import argparse
import sys
from utils import create_safe_filename


def main():
    parser = argparse.ArgumentParser(description="Generate an image based on a prompt.")
    parser.add_argument(
        "--prompt",
        type=str,
        help="The prompt to generate the image.",
        required=True,
    )
    args = parser.parse_args()

    if not args.prompt:
        print("Error: The --prompt argument is required.")
        sys.exit(1)

    outPath = Path(__file__).parent.parent / "out"
    outPath.mkdir(parents=True, exist_ok=True)

    flux = Flux1.from_alias(
        alias="schnell",
        quantize=8,
    )

    prompt = args.prompt
    image = flux.generate_image(
        prompt=prompt,
        seed=0,
        config=Config(num_inference_steps=4),
    )

    fileName = create_safe_filename(prompt)
    image.save(outPath / f"{fileName}.png")


if __name__ == "__main__":
    main()
