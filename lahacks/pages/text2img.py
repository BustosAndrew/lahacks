import jax
import numpy as np
from flax.jax_utils import replicate
from flax.training.common_utils import shard

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

    images = pipeline(prompt_ids, params, prng_seed,
                      num_inference_steps, jit=True).images
    images = pipeline.numpy_to_pil(np.asarray(
        images.reshape((num_samples,) + images.shape[-3:])))

    # Save each image
    for i, image in enumerate(images):
        # Define the path where you want to save the image
        image_path = f"/assets/meal{i}.png"
        image.save(image_path)  # Save the image
        print(f"Image saved as {image_path}")


# text2img(prompt, params)
