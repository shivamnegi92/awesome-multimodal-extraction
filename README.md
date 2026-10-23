# Awesome Multimodal Extraction [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated, LLM-era list of models, tools, and datasets for extracting entities
> and structured data from images + text: vision-language models, document AI,
> OCR-to-structured pipelines, and multimodal NER.

[![awesome-lint](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/awesome-lint.yml/badge.svg)](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/awesome-lint.yml)
[![links](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/links.yml/badge.svg)](https://github.com/shivamnegi92/awesome-multimodal-extraction/actions/workflows/links.yml)
[![release](https://img.shields.io/github/v/release/shivamnegi92/awesome-multimodal-extraction)](https://github.com/shivamnegi92/awesome-multimodal-extraction/releases)

![Multimodal extraction: image plus text in, structured entities out](assets/demo.gif)

This list helps you turn **pixels + words into usable structure**: a receipt
photo into fields, a PDF into a table, a chart into data, or an image-text pair
into entities. It connects multimodal-NER research with current VLM and
document-AI tooling. Links are checked by CI; example scores are synthetic
demonstrations, not claims about model quality.

**Choose by task:** PDF or scan to searchable text: Document AI and OCR. Receipt
or form to fields/JSON: structured image extraction. Dense tables/layout: layout
tools. Charts: chart extraction. Audio/video: speech and video sections.
Image-text entities: multimodal NER. Quality checks: datasets and evaluation.
These are navigation hints, not rankings. See the local runnable examples and
offline evaluation; no hosted inference demo is implied.

**Not sure where to start?** This picks a tool from your constraints:

![Which multimodal tool should I pick? A decision flowchart](assets/decision.gif)

## Contents

- [👁️ Vision-Language Models](#-vision-language-models)
- [🤗 VLM Checkpoints (Hugging Face)](#-vlm-checkpoints-hugging-face)
- [📄 Document AI and OCR](#-document-ai-and-ocr)
- [🧩 Structured Extraction from Images](#-structured-extraction-from-images)
- [📐 Layout, Table, and Chart Extraction](#-layout-table-and-chart-extraction)
- [📈 Chart and Diagram Extraction](#-chart-and-diagram-extraction)
- [🎬 Video Extraction](#-video-extraction)
- [🎙️ Audio and Speech Extraction](#-audio-and-speech-extraction)
- [🔬 Multimodal NER (Research Lineage)](#-multimodal-ner-research-lineage)
- [📊 Datasets, Benchmarks, and Evaluation](#-datasets-benchmarks-and-evaluation)
- [Try It and Measure It](#try-it-and-measure-it)
- [Papers](#papers)
- [📝 Blogs and Notebooks](#-blogs-and-notebooks)
- [🔗 Related Awesome Lists](#-related-awesome-lists)
- [📚 Tutorials and Learning](#-tutorials-and-learning)

## 👁️ Vision-Language Models

Open multimodal LLMs you can prompt to read images and emit structured output.

- [LLaVA](https://github.com/haotian-liu/LLaVA) - The influential open visual-instruction-tuned multimodal LLM.
- [moondream](https://github.com/m87-labs/moondream) - Tiny, fast vision-language model for on-device image understanding.

## 🤗 VLM Checkpoints (Hugging Face)

Ready-to-run multimodal checkpoints.

- [Florence-2-large](https://huggingface.co/microsoft/Florence-2-large) - Microsoft's compact vision foundation model for detection, OCR, and captioning.
- [🤗 idefics2-8b](https://huggingface.co/HuggingFaceM4/idefics2-8b) - Open multimodal model that handles interleaved image-text inputs.
- [🤗 olmOCR-7B](https://huggingface.co/allenai/olmOCR-7B-0225-preview) - AllenAI VLM specialized for high-fidelity document OCR.
- [🤗 Pixtral-12B](https://huggingface.co/mistralai/Pixtral-12B-2409) - Mistral's open multimodal model for image + text understanding.
- [🤗 Phi-3.5-vision](https://huggingface.co/microsoft/Phi-3.5-vision-instruct) - Small, capable multimodal model good at document reasoning.
- [SmolVLM](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct) - Tiny, efficient VLM for image-text extraction.

## 📄 Document AI and OCR

Turn PDFs, scans, and photos into clean, structured text.

- [Docling](https://github.com/docling-project/docling) - Parse PDFs, DOCX, and more into structured, AI-ready document representations.
- [Marker](https://github.com/datalab-to/marker) - Convert PDFs and documents to clean Markdown/JSON with high fidelity.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - Pre-processing that extracts text and elements from many document types.
- [Surya](https://github.com/datalab-to/surya) - OCR, layout, reading-order, and table detection across 90+ languages.
- [Nougat](https://github.com/facebookresearch/nougat) - Transformer that converts scientific PDFs (incl. math) to markup.
- [docTR](https://github.com/mindee/doctr) - End-to-end OCR with deep-learning detection and recognition.
- [Tesseract](https://github.com/tesseract-ocr/tesseract) - The classic open-source OCR engine.
- [MarkItDown](https://github.com/microsoft/markitdown) - Microsoft tool that converts Office files, PDFs, and images to Markdown for LLMs.
- [olmOCR](https://github.com/allenai/olmocr) - AllenAI toolkit for high-throughput, high-fidelity document OCR with a VLM.
- [Jina Reader](https://github.com/jina-ai/reader) - Convert any URL or PDF into clean, LLM-ready text.

## 🧩 Structured Extraction from Images

Go straight from an image to typed fields and JSON.

- [Zerox](https://github.com/getomni-ai/zerox) - OCR-then-LLM pipeline that turns documents and images into structured data.
- [Instructor](https://github.com/567-labs/instructor) - Typed, schema-validated LLM outputs; supports vision models for image extraction.
- [BAML](https://github.com/BoundaryML/baml) - A language for typed LLM functions, including image inputs for extraction.
- [Donut](https://github.com/clovaai/donut) - OCR-free document understanding transformer for parsing and extraction.
- [Sparrow](https://github.com/katanaml/sparrow) - Data extraction from documents and images with VLMs and a rule engine.
- [OmniParser](https://github.com/microsoft/OmniParser) - Microsoft tool that parses UI screenshots into structured elements.

## 📐 Layout, Table, and Chart Extraction

Recover structure, not just text.

- [Table Transformer](https://github.com/microsoft/table-transformer) - Detect tables and their structure in documents.
- [LayoutParser](https://github.com/Layout-Parser/layout-parser) - Deep-learning toolkit for document image layout analysis.
- [LayoutLM (unilm)](https://github.com/microsoft/unilm) - Home of LayoutLM/LayoutLMv3 for document layout understanding and extraction.

## 📈 Chart and Diagram Extraction

Turn charts and plots back into the underlying data.

- [🤗 DePlot](https://huggingface.co/google/deplot) - One-shot chart-image-to-data-table model from Google.
- [🤗 MatCha](https://huggingface.co/google/matcha-base) - Chart and plot understanding pretrained model.
- [UniChart](https://github.com/vis-nlp/UniChart) - Universal chart understanding and reasoning model.
- [🤗 UniChart-ChartQA](https://huggingface.co/ahmed-masry/unichart-chartqa-960) - UniChart checkpoint fine-tuned for chart question answering.
- [ChartQA](https://github.com/vis-nlp/ChartQA) - Benchmark and code for question answering over charts.

## 🎬 Video Extraction

Extract entities, events, and structured info from video.

- [Video-LLaVA](https://github.com/PKU-YuanGroup/Video-LLaVA) - Unified video-and-image language model for understanding and extraction.
- [🤗 LLaVA-NeXT-Video](https://huggingface.co/llava-hf/LLaVA-NeXT-Video-7B-hf) - Open video-language checkpoint for video QA and extraction.
- [WhisperX](https://github.com/m-bain/whisperX) - Fast speech transcription with word-level timestamps for audio tracks.

## 🎙️ Audio and Speech Extraction

Transcribe speech, find who spoke, then extract entities from the transcript -- or extract directly with an audio LLM.

- [Whisper](https://github.com/openai/whisper) - OpenAI's robust multilingual speech-recognition model.
- [whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) - State-of-the-art Whisper ASR checkpoint.
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - Fast Whisper inference with CTranslate2.
- [distil-whisper](https://github.com/huggingface/distil-whisper) - Distilled Whisper that is much faster with little accuracy loss.
- [pyannote-audio](https://github.com/pyannote/pyannote-audio) - Speaker diarization (who spoke when) and other speech tasks.
- [SpeechBrain](https://github.com/speechbrain/speechbrain) - All-in-one conversational-AI and speech toolkit.
- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo) - Toolkit for ASR, speaker tasks, and speech-to-text pipelines.
- [🤗 speaker-diarization-3.1](https://huggingface.co/pyannote/speaker-diarization-3.1) - Ready-to-use speaker-diarization pipeline.

## 🔬 Multimodal NER (Research Lineage)

The academic line this list grew from: entity extraction from image-text pairs.

- [UMT](https://github.com/jefferyYu/UMT) - Unified multimodal transformer for NER in social media (ACL 2020).
- [RpBERT](https://github.com/Multimodal-NER/RpBERT) - Text-image relation-propagation BERT for multimodal NER (AAAI 2021).
- [multimodal_NER](https://github.com/RiTUAL-MBZUAI/multimodal_NER) - Study of the role of images for multimodal NER (EMNLP 2021).
- [MAF](https://github.com/xubodhu/MAF) - Matching-and-alignment framework for multimodal NER (WSDM 2022).
- [HVPNeT](https://github.com/zjunlp/HVPNeT) - Hierarchical visual prefix for multimodal entity and relation extraction (NAACL 2022).

## 📊 Datasets, Benchmarks, and Evaluation

These resources serve different roles:

- **Datasets** provide examples and annotations.
- **Benchmark suites** define an evaluation task, protocol, and sometimes reference code.
- **Metrics and evaluation tools** score outputs; a metric by itself is not a model ranking.

A listed model or tool is not implied to have been evaluated on any dataset below.

### Datasets

- [🤗 CORD-v2](https://huggingface.co/datasets/naver-clova-ix/cord-v2) - Receipt parsing dataset for structured document extraction.
- [🤗 FUNSD](https://huggingface.co/datasets/nielsr/funsd-layoutlmv3) - Form understanding in noisy scanned documents.
- [DocVQA dataset](https://huggingface.co/datasets/lmms-lab/DocVQA) - Question answering over document images.
- [ChartQA dataset](https://huggingface.co/datasets/HuggingFaceM4/ChartQA) - Question answering and extraction over charts.
- [XFUND](https://github.com/doc-analysis/XFUND) - Multilingual form-understanding dataset spanning seven languages.
- [SROIE](https://github.com/zzzDavid/ICDAR-2019-SROIE) - Receipt OCR and key-information extraction dataset (ICDAR 2019).

### Benchmark suites and code

- [ChartQA](https://github.com/vis-nlp/ChartQA) - Benchmark and code for chart question answering; see the [original paper](https://aclanthology.org/2022.findings-acl.177/).
- [OmniDocBench](https://github.com/opendatalab/OmniDocBench) - Benchmark for diverse PDF document parsing; see the [original paper](https://arxiv.org/abs/2412.07626).

### Metrics and evaluation tools

- [seqeval](https://github.com/chakki-works/seqeval) - Entity-level F1 evaluation for sequence labeling.
- [Nervaluate](https://github.com/MantisAI/nervaluate) - Nuanced NER evaluation (partial, exact, type) following SemEval.

A useful extraction evaluation separates **what was returned** from **whether it is grounded and usable**. Match metrics to the task: OCR text error, field exact match, table-cell/structure quality, reading-order accuracy, chart-value accuracy, JSON/schema validity, and source-region localization when evidence is returned. For deployment comparisons, report latency, memory, cost, and failure rate separately from quality. State dataset/version, split, metric, normalization, model revision, hardware, and sample count; include failures and limitations. Do not compare unlike metrics or treat the synthetic receipt rows in this repository as a benchmark.

When reporting a benchmark result, link the original paper or an official leaderboard and name the model revision, dataset version and split, metric, and normalization. This README currently reports no leaderboard rankings or model performance claims.

**Evidence matters:** a value without its source location is hard to audit. When supported, preserve page/frame, bounding box with coordinate convention, source text/crop, and calibrated confidence only where measured. Confidence scales are not comparable across models unless calibrated and tested.

**Privacy and security matter too:** check dataset/model licenses, local vs remote processing, retention, and upload terms before using real documents. Treat files and extracted text as untrusted input; consider redaction, prompt-injection exposure, and malformed or hostile files within an appropriate sandbox. Never add private documents or extracted personal data here.

For release scope and limitations, see the changelog. Cite a version using the `CITATION.cff` file and its Git tag.

## Try It and Measure It

Start with the [local VLM example](examples/vlm_extract.py),
[offline receipt-field evaluator](examples/README.md), and the
[Gradio Space source and deployment guide](spaces/receipt-eval/DEPLOY.md).
[Plan for a separate image-to-fields Space](task_plan.md) documents the next
step, including model feasibility, privacy, measurement and launch gates.
A [local image-to-fields prototype](spaces/receipt-inference/DEPLOY.md) is now
checked in; its model download and real inference are **not yet verified**.
The existing Space is an interactive scorer, not a hosted VLM; publish and verify it
before advertising a live demo. The evaluator measures
exact receipt matches and per-field accuracy on your own labeled JSONL; the
checked-in synthetic example demonstrates the format only. No benchmark result
is claimed without a labeled dataset, defined split, and measured run.

## Papers

Foundational and current reading (Hugging Face Papers pages link to PDF + code).

- [LLaVA](https://huggingface.co/papers/2304.08485) - Visual instruction tuning; the open multimodal-LLM blueprint.
- [Florence-2](https://huggingface.co/papers/2311.06242) - Unified vision foundation model for detection, OCR, and grounding.
- [Donut](https://huggingface.co/papers/2111.15664) - OCR-free document understanding transformer.
- [LayoutLMv3](https://huggingface.co/papers/2204.08387) - Unified text-and-image masking for document AI.
- [Nougat](https://huggingface.co/papers/2308.13418) - Neural optical understanding for academic documents.
- [MLLM Survey](https://huggingface.co/papers/2306.13549) - A survey on multimodal large language models.

## 📝 Blogs and Notebooks

Hands-on walkthroughs and runnable notebooks.

- [HF: Document AI](https://huggingface.co/blog/document-ai) - Overview of document-AI models and how to use them.
- [HF: IDEFICS2](https://huggingface.co/blog/idefics2) - Building and using an open multimodal model.
- [HF: SmolVLM](https://huggingface.co/blog/smolvlm) - A small, efficient VLM and how to apply it.
- [roboflow/notebooks](https://github.com/roboflow/notebooks) - Notebooks for VLMs, Florence-2, and vision models.
- [Gemini Cookbook](https://github.com/google-gemini/cookbook) - Official recipes including multimodal extraction with Gemini.

## 🔗 Related Awesome Lists

- [Awesome Entity Extraction](https://github.com/shivamnegi92/awesome-entity-extraction) - The text-only sibling: NER, relation, and structured extraction.
- [Awesome VLM Architectures](https://github.com/gokayfem/awesome-vlm-architectures) - Deep dive on vision-language model architectures.

## 📚 Tutorials and Learning

- [Transformers Tutorials](https://github.com/NielsRogge/Transformers-Tutorials) - Hands-on notebooks for Donut, LayoutLM, Florence-2, and more.
- [Runnable examples](https://github.com/shivamnegi92/awesome-multimodal-extraction/tree/main/examples) - Copy-paste starting points for VLM and document extraction (in this repo).

## Contributing

Want to help make this a genuinely useful field guide? **Pick one small task and
open a PR**—a single verified entry, dead-link fix, clearer description, or
example/test improvement all count. First-time contributors are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) for the rules and steps; open help-wanted
issues are linked there. The [discovery and community plan](VISIBILITY.md) explains
how to grow reach without spam or vanity metrics. Please comment before taking a
larger task so work does not collide.

Every catalog entry must link to a real project, model, or dataset and include a
short, factual description. No dead links, vaporware, or unsupported “best”
claims. CI checks reachability; maintainers review relevance and accuracy.

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](LICENSE)

To the extent possible under law, the contributors have waived all copyright and
related or neighboring rights to this work.
