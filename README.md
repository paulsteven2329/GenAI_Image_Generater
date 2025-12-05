===========================================================
    Text-to-Image Generator using Stable Diffusion v1-4
===========================================================

TECHNICAL DOCUMENTATION
-----------------------

This script loads the open-source Stable Diffusion v1-4 model
(locally, no HuggingFace login required) and generates an image
from a text prompt.

DEPENDENCIES:
    - diffusers
    - transformers
    - torch
    - PIL (Pillow)

COMMAND TO RUN:
    python app.py

OUTPUT:
    Saves final generated image into:
        outputs/generated.png

WORKFLOW:
    1. load_model()
         - Downloads Stable Diffusion model (if not cached)
         - Configures FP32 (safer for CPU)
         - Sends pipeline to CUDA if available

    2. main()
         - Initializes app banner
         - Calls load_model()
         - Accepts user text prompt
         - Passes prompt to generate()

    3. generate()
         - Runs model inference
         - Saves generated image
         - Displays output to user

NOTE:
    CPU mode is slow (~2–6 minutes), GPU is fast (~3–8 seconds).

===========================================================