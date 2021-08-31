# Resume generator

## Summary

Python script which generates a resume in PDF based on a json file.

## Installation

### Prerequisites:

- This project uses `weasyprint` which requires an additional installation. See: <https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation>

### Local installation

- `pip install -r requirements.txt`

## Local Run

Script documentation:

```shell
usage: src/resume_generator.py [-h] --input_json INPUT_JSON --output_filename OUTPUT_FILENAME

Script to generate easily a resume based on an HTML template by just providing a json file

optional arguments:
  -h, --help            show this help message and exit
  --input_json INPUT_JSON
                        Absolute or relative path for the input json
  --output_filename OUTPUT_FILENAME
                        Name for the generated file
```

Example:

```shell
 python src/resume_generator.py --output_filename=my_resume.pdf --input_json=assets/example_input/resume_input_example.json
```

## Examples

- Input: `assets/example_input/resume_input_example.json`

- Output: `assets/example_output/resume_example_bulma_template.pdf`

## TODO:

A lot of things! Mainly unittest, more templates and eventually a UI.