#!/usr/bin/env python3
"""
Convert a carousel HTML file to a multi-page PDF.

Each .slide div becomes one PDF page at the exact pixel dimensions.
Uses Playwright for accurate CSS/Tailwind/Google Fonts rendering.

Usage:
    python html_to_pdf.py input.html output.pdf [--width 1080] [--height 1350]
"""

import argparse
import sys
import os
import time


def convert_html_to_pdf(input_html: str, output_pdf: str, width: int = 1080, height: int = 1350):
    """Convert carousel HTML to multi-page PDF using Playwright."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Installing playwright...")
        os.system("pip install playwright --break-system-packages -q")
        os.system("playwright install chromium")
        from playwright.sync_api import sync_playwright

    input_path = os.path.abspath(input_html)
    output_path = os.path.abspath(output_pdf)

    if not os.path.exists(input_path):
        print(f"Error: Input file not found: {input_path}")
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Load the HTML file
        page.goto(f"file://{input_path}", wait_until="networkidle")

        # Wait for fonts to load
        page.wait_for_timeout(2000)

        # Count slides
        slide_count = page.eval_on_selector_all(".slide", "els => els.length")
        if slide_count == 0:
            # Try without .slide class — look for direct children of body
            slide_count = page.eval_on_selector_all("body > div", "els => els.length")

        print(f"Found {slide_count} slides")

        # Use CSS @page printing for proper multi-page PDF
        # The HTML already has print media styles, so we just need to generate the PDF
        page.pdf(
            path=output_path,
            width=f"{width}px",
            height=f"{height}px",
            margin={"top": "0px", "right": "0px", "bottom": "0px", "left": "0px"},
            print_background=True,
            prefer_css_page_size=True,
        )

        browser.close()

    file_size = os.path.getsize(output_path)
    print(f"PDF created: {output_path} ({file_size:,} bytes, {slide_count} pages)")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Convert carousel HTML to PDF")
    parser.add_argument("input", help="Path to input HTML file")
    parser.add_argument("output", help="Path to output PDF file")
    parser.add_argument("--width", type=int, default=1080, help="Slide width in pixels (default: 1080)")
    parser.add_argument("--height", type=int, default=1350, help="Slide height in pixels (default: 1350)")

    args = parser.parse_args()
    convert_html_to_pdf(args.input, args.output, args.width, args.height)


if __name__ == "__main__":
    main()
