import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os


def load_model():
    """
    Loads the Stable Diffusion v1-4 pipeline.

    Steps:
        - Prints loading status
        - Downloads or loads cached model
        - Sets dtype to float32 (for CPU systems)
        - Moves pipeline to CUDA if GPU is available

    Returns:
        pipe: A StableDiffusionPipeline instance ready for inference.
    """
    print("\n🔄 Loading Stable Diffusion v1-4 (no login needed)...")

    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float32
    )

    # CPU or GPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = pipe.to(device)

    print(f"✅ Model loaded on: {device.upper()}")
    return pipe


def generate(pipe, prompt):
    """
    Generates an image from a text prompt.

    Args:
        pipe: The loaded StableDiffusionPipeline object.
        prompt: String describing what to generate.

    Process:
        - Runs inference with:
              num_inference_steps=30  → affects quality and speed
              guidance_scale=7.5      → controls "creativity" vs accuracy
        - Saves output PNG
        - Displays image to user

    Output:
        outputs/generated.png
    """
    print("\n⏳ Generating... This may take a few minutes on CPU...")

    result = pipe(
        prompt,
        num_inference_steps=30,
        guidance_scale=7.5
    )

    img = result.images[0]

    os.makedirs("outputs", exist_ok=True)
    save_path = "outputs/generated.png"
    img.save(save_path)

    print(f"\n🎉 Image saved to: {save_path}")
    img.show()


def main():
    print("===============================================")
    print("     LOCAL TEXT-TO-IMAGE (Stable Diffusion)    ")
    print("       Model: CompVis/stable-diffusion-v1-4     ")
    print("===============================================")

    pipe = load_model()
    prompt = input("\nEnter your prompt: ")

    generate(pipe, prompt)


if __name__ == "__main__":
    main()
