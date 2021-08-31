import argparse
import json

import jinja2
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

TEMPLATE_FOLDER = 'assets/templates'
BULMA_TEMPLATE = f'{TEMPLATE_FOLDER}/html/resume_bulma_template.html'


def generate_pdf(input_context, output_filename):
    font_config = FontConfiguration()
    template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))

    # TODO: Add more templates and parametrize options on script-args
    template = template_env.get_template(BULMA_TEMPLATE)
    htmldoc = HTML(string=template.render(input_context), base_url="")
    htmldoc.write_pdf(output_filename, stylesheets=[
        CSS(string="@page { size: A4; margin: 1cm }", font_config=font_config)
    ])

    # TODO: Add logger
    print(f'Process completed, generated file {output_filename}')


def get_context(json_file):
    with open(json_file, 'r') as f:
        # TODO: Add validations to mandatory fields and expected string-length
        return json.load(f)


def init_parser():
    parser = argparse.ArgumentParser(
        description='Script to generate easily a resume based on an HTML template by just providing a json file'
    )
    parser.add_argument('--input_json', type=str, help="Absolute or relative path for the input json", required=True)
    parser.add_argument('--output_filename', type=str, help="Name for the generated file", required=True)

    return parser


def validate_args(args):
    args.output_filename = args.output_filename.lower()
    if not args.output_filename.endswith(".pdf"):
        args.output_filename = f'{args.output_filename}.pdf'


if __name__ == '__main__':
    # TODO: Add unittests
    args = init_parser().parse_args()
    validate_args(args)
    context = get_context(json_file=args.input_json)
    generate_pdf(context, output_filename=args.output_filename)
