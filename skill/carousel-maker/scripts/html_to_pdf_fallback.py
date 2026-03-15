#!/usr/bin/env python3
"""
Fallback HTML-to-PDF converter using WeasyPrint.
Use when Playwright/Chromium cannot be installed due to network restrictions.

Works well with pure inline CSS (no external CDNs needed).

Usage:
    python html_to_pdf_fallback.py input.html output.pdf [--width 1080] [--height 1350]
"""

import argparse
import sys
import os


def convert_html_to_pdf(input_html: str, output_pdf: str, width: int = 1080, height: int = 1350):
    """Convert carousel HTML to PDF using WeasyPrint."""
    try:
        import weasyprint
    except ImportError:
        print("Installing weasyprint...")
        os.system("pip install weasyprint --break-system-packages -q")
        import weasyprint

    input_path = os.path.abspath(input_html)
    output_path = os.path.abspath(output_pdf)

    if not os.path.exists(input_path):
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    # Convert px dimensions to mm for @page size (assuming 96 DPI)
    width_mm = width * 25.4 / 96
    height_mm = height * 25.4 / 96

    # Read the HTML and inject @page CSS if not already present
    with open(input_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Ensure @page directive uses correct dimensions
    page_css = f"""
    @page {{
        size: {width_mm:.1f}mm {height_mm:.1f}mm;
        margin: 0;
    }}
    """

    # Inject the page CSS into the HTML
    if '@page' not in html_content:
        html_content = html_content.replace('</style>', page_css + '\n</style>', 1)
        if '</style>' not in html_content:
            html_content = html_content.replace('</head>',
                f'<style>{page_css}</style>\n</head>', 1)

    # Write modified HTML to temp file
    temp_path = input_path + '.tmp.html'
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    try:
        doc = weasyprint.HTML(filename=temp_path)
        doc.write_pdf(output_path)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

    file_size = os.path.getsize(output_path)
    print(f"PDF created: {output_path} ({file_size:,} bytes)")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Convert carousel HTML to PDF (WeasyPrint)")
    parser.add_argument("input", help="Path to input HTML file")
    parser.add_argument("output", help="Path to output PDF file")
    parser.add_argument("--width", type=int, default=1080, help="Slide width in pixels (default: 1080)")
    parser.add_argument("--height", type=int, default=1350, help="Slide height in pixels (default: 1350)")

    args = parser.parse_args()
    convert_html_to_pdf(args.input, args.output, args.width, args.height)


if __name__ == "__main__":
    main()
