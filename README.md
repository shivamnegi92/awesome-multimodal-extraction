# Awesome Multimodal Extraction [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, LLM-era list of models, tools, and datasets for extracting entities
> and structured data from images + text: vision-language models, document AI,
> OCR-to-structured pipelines, and multimodal NER.

[![awesome-lint](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/awesome-lint.yml/badge.svg)](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/awesome-lint.yml)
[![links](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/links.yml/badge.svg)](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/links.yml)

![Multimodal extraction: image plus text in, structured entities out](assets/demo.gif)

Text-only extraction is solved enough. The hard, valuable problems now live in
**pixels + words together**: a receipt photo, a chart in a PDF, a tweet with an
image, a scanned form. The old multimodal-NER reading lists stopped at 2023 and
the academic Twitter-image setup; the field has since moved to **vision-language
models** and **document AI**. This list is practitioner-first and kept current,
with every link verified live by CI.

## Contents

- [👁️ Vision-Language Models](#-vision-language-models)
- [🤗 VLM Checkpoints (Hugging Face)](#-vlm-checkpoints-hugging-face)
- [📄 Document AI and OCR](#-document-ai-and-ocr)
- [🧩 Structured Extraction from Images](#-structured-extraction-from-images)
- [📐 Layout, Table, and Chart Extraction](#-layout-table-and-chart-extraction)
- [🔬 Multimodal NER (Research Lineage)](#-multimodal-ner-research-lineage)
- [📊 Datasets and Benchmarks](#-datasets-and-benchmarks)
- [📏 Evaluation](#-evaluation)
- [🔗 Related Awesome Lists](#-related-awesome-lists)
- [📚 Tutorials and Learning](#-tutorials-and-learning)

## 👁️ Vision-Language Models

Open multimodal LLMs you can prompt to read images and emit structured output.

- [LLaVA](https://github.com/haotian-liu/LLaVA) - The influential open visual-instruction-tuned multimodal LLM.
- [Qwen3-VL](https://github.com/QwenLM/Qwen3-VL) - Alibaba's strong open vision-language model series with document and grounding skills.
- [InternVL](https://github.com/OpenGVLab/InternVL) - High-performing open VLM family competitive with closed models.
- [CogVLM](https://github.com/zai-org/CogVLM) - Powerful open visual-language foundation model.
- [moondream](https://github.com/m87-labs/moondream) - Tiny, fast vision-language model for on-device image understanding.

## 🤗 VLM Checkpoints (Hugging Face)

Ready-to-run multimodal checkpoints.

- [🤗 Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) - Capable open VLM strong at documents, charts, and grounded extraction.
- [🤗 Florence-2-large](https://huggingface.co/microsoft/Florence-2-large) - Microsoft's compact vision foundation model for detection, OCR, and captioning.
- [🤗 idefics2-8b](https://huggingface.co/HuggingFaceM4/idefics2-8b) - Open multimodal model that handles interleaved image-text inputs.
- [🤗 olmOCR-7B](https://huggingface.co/allenai/olmOCR-7B-0225-preview) - AllenAI VLM specialized for high-fidelity document OCR.

## 📄 Document AI and OCR

Turn PDFs, scans, and photos into clean, structured text.

- [Docling](https://github.com/docling-project/docling) - Parse PDFs, DOCX, and more into structured, AI-ready document representations.
- [Marker](https://github.com/datalab-to/marker) - Convert PDFs and documents to clean Markdown/JSON with high fidelity.
- [MinerU](https://github.com/opendatalab/MinerU) - Extract high-quality structured content from PDFs, including formulas and tables.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Pre-processing that extracts text and elements from many document types.
- [Surya](https://github.com/datalab-to/surya) - OCR, layout, reading-order, and table detection across 90+ languages.
- [Nougat](https://github.com/facebookresearch/nougat) - Transformer that converts scientific PDFs (incl. math) to markup.
- [docTR](https://github.com/mindee/doctr) - End-to-end OCR with deep-learning detection and recognition.
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - Multilingual, production-grade OCR toolkit.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) - Ready-to-use OCR for 80+ languages.
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - The classic open-source OCR engine.

## 🧩 Structured Extraction from Images

Go straight from an image to typed fields and JSON.

- [Zerox](https://github.com/getomni-ai/zerox) - OCR-then-LLM pipeline that turns documents and images into structured data.
- [Instructor](https://github.com/567-labs/instructor) - Typed, schema-validated LLM outputs; supports vision models for image extraction.
- [BAML](https://github.com/BoundaryML/baml) - A language for typed LLM functions, including image inputs for extraction.
- [Donut](https://github.com/clovaai/donut) - OCR-free document understanding transformer for parsing and extraction.

## 📐 Layout, Table, and Chart Extraction

Recover structure, not just text.

- [Table Transformer](https://github.com/microsoft/table-transformer) - Detect tables and their structure in documents.
- [LayoutParser](https://github.com/Layout-Parser/layout-parser) - Deep-learning toolkit for document image layout analysis.

## 🔬 Multimodal NER (Research Lineage)

The academic line this list grew from: entity extraction from image-text pairs.

- [UMT](https://github.com/jefferyYu/UMT) - Unified multimodal transformer for NER in social media (ACL 2020).
- [RpBERT](https://github.com/Multimodal-NER/RpBERT) - Text-image relation-propagation BERT for multimodal NER (AAAI 2021).
- [multimodal_NER](https://github.com/RiTUAL-MBZUAI/multimodal_NER) - Study of the role of images for multimodal NER (EMNLP 2021).
- [MAF](https://github.com/xubodhu/MAF) - Matching-and-alignment framework for multimodal NER (WSDM 2022).
- [HVPNeT](https://github.com/zjunlp/HVPNeT) - Hierarchical visual prefix for multimodal entity and relation extraction (NAACL 2022).
- [MKGformer](https://github.com/zjunlp/MKGformer) - Hybrid transformer for multimodal knowledge-graph completion (SIGIR 2022).
- [KB-NER / ITA](https://github.com/Alibaba-NLP/KB-NER) - Image-text alignments for multimodal NER (NAACL 2022).
- [AdaSeq](https://github.com/modelscope/AdaSeq) - Sequence-understanding library including multimodal and retrieval-augmented NER.

## 📊 Datasets and Benchmarks

- [🤗 CORD-v2](https://huggingface.co/datasets/naver-clova-ix/cord-v2) - Receipt parsing dataset for structured document extraction.
- [🤗 FUNSD](https://huggingface.co/datasets/nielsr/funsd-layoutlmv3) - Form understanding in noisy scanned documents.
- [🤗 DocVQA](https://huggingface.co/datasets/lmms-lab/DocVQA) - Question answering over document images.
- [🤗 ChartQA](https://huggingface.co/datasets/HuggingFaceM4/ChartQA) - Question answering and extraction over charts.

## 📏 Evaluation

- [seqeval](https://github.com/chakki-works/seqeval) - Entity-level F1 evaluation for sequence labeling.
- [nervaluate](https://github.com/MantisAI/nervaluate) - Nuanced NER evaluation (partial, exact, type) following SemEval.

## 🔗 Related Awesome Lists

- [Awesome Entity Extraction](https://github.com/shivamnegi92/awesome-entity-extraction) - The text-only sibling: NER, relation, and structured extraction.
- [Awesome VLM Architectures](https://github.com/gokayfem/awesome-vlm-architectures) - Deep dive on vision-language model architectures.

## 📚 Tutorials and Learning

- [Transformers Tutorials](https://github.com/NielsRogge/Transformers-Tutorials) - Hands-on notebooks for Donut, LayoutLM, Florence-2, and more.
- [Runnable examples](https://github.com/shivamnegi92/awesome-multimodal-extraction/tree/main/examples) - Copy-paste starting points for VLM and document extraction (in this repo).

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.
The one hard rule: every entry must link to a real, maintained project and
include a short, factual description. No dead links, no vaporware.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and
related or neighboring rights to this work.
