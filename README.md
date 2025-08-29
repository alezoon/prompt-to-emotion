# Prompt-to-Emotion Classifier (Test Project)

This is a small test project that demonstrates how to classify emotions from natural language prompts using a pretrained model from Hugging Face. It serves as a prototype for a larger application that will incorporate emotion classification into more complex workflows.

---

## Information

This project takes a text prompt as input, processes it through a transformer model, and returns a set of probable emotions with confidence scores. It also visualizes the emotion distribution using interactive charts via [Streamlit](https://streamlit.io).

---

## Model Info

The project uses the following pretrained model from Hugging Face:

**[`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base)**

- Based on **DistilRoBERTa**
- Trained for multi-class emotion classification
- Outputs emotions such as: `joy`, `sadness`, `anger`, `fear`, `surprise`, `disgust`, `neutral`

---
# Example Output

Heres an example of the emotion classfication result from a prompt:
![Example Output](imgs/image.png)

---
## Purpose

This project is intended as a **test run** for a larger application.

The main goals are to:

- Experiment with Hugging Face model integration
- Test prompt-based emotion classification
- Visualize results clearly and interactively
- Prepare for future scalability and feature expansion

---
