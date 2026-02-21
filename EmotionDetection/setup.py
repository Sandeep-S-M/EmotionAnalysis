from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "requests"
    ],
    author="Sandeep S M",
    description="Emotion detection package using Watson NLP",
)
