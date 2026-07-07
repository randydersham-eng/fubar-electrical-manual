import os
import sys

# On macOS, if WeasyPrint dependencies are in Homebrew's path, we must ensure
# DYLD_FALLBACK_LIBRARY_PATH contains /opt/homebrew/lib so ctypes can load them.
if sys.platform == "darwin" and "/opt/homebrew/lib" not in os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", ""):
    fallback = os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", "")
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = f"/opt/homebrew/lib:{fallback}".strip(":")
    # Relaunch the script with the updated environment
    os.execve(sys.executable, [sys.executable] + sys.argv, os.environ)

def build_pdf():
    try:
        from weasyprint import HTML
        print("----------------------------------------")
        print("Compiling FUBAR Electrical Manual PDF...")
        print("----------------------------------------")
        
        # Resolve absolute paths
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(base_dir, "src", "index.html")
        output_dir = os.path.join(base_dir, "output")
        os.makedirs(output_dir, exist_ok=True)
        pdf_path = os.path.join(output_dir, "FUBAR electrical manual.pdf")
        
        # Compile HTML to PDF using WeasyPrint
        HTML(html_path, base_url=os.path.join(base_dir, "src")).write_pdf(pdf_path)
        
        print(f"SUCCESS! PDF has been generated successfully.")
        print(f"Output File: {pdf_path}")
        print("----------------------------------------")
    except ImportError:
        print("----------------------------------------")
        print("ERROR: 'weasyprint' package is not installed in this environment.")
        print("To compile the PDF, please run:")
        print("  pip install weasyprint")
        print("\nNote: WeasyPrint requires the 'pango' system library.")
        print("If you run into missing library errors, install it via Homebrew:")
        print("  brew install pango")
        print("----------------------------------------")
        sys.exit(1)
    except Exception as e:
        print(f"Compilation failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_pdf()
