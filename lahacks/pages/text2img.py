import jax
import numpy as np
from flax.jax_utils import replicate
from flax.training.common_utils import shard
from PIL import Image  # Import PIL module for image processing

from diffusers import FlaxStableDiffusionPipeline

pipeline, params = FlaxStableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", revision="bf16", dtype=jax.numpy.bfloat16
)


def text2img(prompt, params):
    prng_seed = jax.random.PRNGKey(0)
    num_inference_steps = 50

    num_samples = jax.device_count()
    prompt = num_samples * [prompt]
    prompt_ids = pipeline.prepare_inputs(prompt)

    # shard inputs and rng
    params = replicate(params)
    prng_seed = jax.random.split(prng_seed, num_samples)
    prompt_ids = shard(prompt_ids)

    images = pipeline(prompt_ids, params, prng_seed, num_inference_steps, jit=True).images
    images = pipeline.numpy_to_pil(np.asarray(images.reshape((num_samples,) + images.shape[-3:])))

    # Save each image
    for i, image in enumerate(images):
        image_path = f"generated_image_{i}.png"  # Define the path where you want to save the image
        image.save(image_path)  # Save the image
        print(f"Image saved as {image_path}")

prompt = '''white Bread Pav: Opt for whole wheat pav or multigrain bread rolls. You could even try lettuce wraps for a low-carb option.
Excessive oil/butter: Use minimal oil for sautéing, and substitute butter with a healthier alternative like ghee (clarified butter) or olive oil. Potatoes: Reduce the quantity of potatoes and add more vegetables like cauliflower, carrots, peas, and bell peppers. 
* Heavy cream: Use low-fat yogurt or cashew cream to achieve a creamy texture without the added fat.
* Food coloring:** Skip the artificial food coloring and allow the natural colors of the vegetables to shine'''
text2img(prompt, params)