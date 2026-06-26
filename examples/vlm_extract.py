"""Structured extraction from an image with a vision-language model (Qwen2.5-VL).

Setup:
    pip install transformers accelerate qwen-vl-utils pillow torch
"""
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration
from qwen_vl_utils import process_vision_info

model_id = "Qwen/Qwen2.5-VL-7B-Instruct"
model = Qwen2_5_VLForConditionalGeneration.from_pretrained(model_id, device_map="auto")
processor = AutoProcessor.from_pretrained(model_id)

messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "receipt.jpg"},
            {"type": "text", "text": "Extract vendor, date, and total as JSON."},
        ],
    }
]

text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
images, videos = process_vision_info(messages)
inputs = processor(text=[text], images=images, videos=videos, return_tensors="pt").to(model.device)

out = model.generate(**inputs, max_new_tokens=256)
print(processor.batch_decode(out, skip_special_tokens=True)[0])
