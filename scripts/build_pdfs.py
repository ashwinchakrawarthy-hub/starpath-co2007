"""
Build publication-grade academic PDFs for CO2007 coursework submission using Chrome Headless.
Generates:
  1. STARPath_Minutes_of_Meetings.pdf
  2. STARPath_Project_Guide_and_Brief.pdf
  3. STARPath_Presentation_Slides.pdf
  4. STARPath_AI_Usage_and_Academic_Integrity.pdf
  5. STARPath_Architecture_and_Deployment.pdf
"""

import os
import re
import subprocess
import tempfile
import markdown

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
WORKSPACE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DOCS_DIR = os.path.join(WORKSPACE_DIR, "docs")
SRC_DIR = os.path.join(WORKSPACE_DIR, "scripts", ".archive_md")

CSS_STYLES = """
@page {
    size: A4 portrait;
    margin: 20mm 16mm 20mm 16mm;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a202c;
    background-color: #ffffff;
    line-height: 1.6;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
}

/* Header Banner */
.academic-header {
    border-bottom: 3px solid #BA0C2F;
    padding-bottom: 14px;
    margin-bottom: 22px;
}

.uclan-badge {
    display: inline-block;
    background-color: #0B1B3D;
    color: #ffffff;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 8px;
}

.sub-badge {
    display: inline-block;
    background-color: #F1F5F9;
    color: #475569;
    font-size: 8.5pt;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 4px;
    margin-left: 6px;
    border: 1px solid #E2E8F0;
}

h1 {
    color: #0B1B3D;
    font-size: 20pt;
    font-weight: 800;
    line-height: 1.25;
    margin-top: 8px;
    margin-bottom: 6px;
}

h2 {
    color: #0B1B3D;
    font-size: 14pt;
    font-weight: 700;
    border-bottom: 1.5px solid #E2E8F0;
    padding-bottom: 6px;
    margin-top: 24px;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h3 {
    color: #BA0C2F;
    font-size: 11.5pt;
    font-weight: 700;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
}

h4 {
    color: #2D3748;
    font-size: 10.5pt;
    font-weight: 600;
    margin-top: 14px;
    margin-bottom: 6px;
    page-break-after: avoid;
}

p {
    margin-top: 0;
    margin-bottom: 10px;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 12px;
    margin-bottom: 18px;
    font-size: 9.5pt;
    page-break-inside: avoid;
}

th {
    background-color: #0B1B3D;
    color: #ffffff;
    font-weight: 700;
    text-align: left;
    padding: 8px 10px;
    border: 1px solid #0B1B3D;
    font-size: 9pt;
    letter-spacing: 0.3px;
}

td {
    padding: 7px 10px;
    border: 1px solid #CBD5E1;
    vertical-align: top;
}

tr:nth-child(even) td {
    background-color: #F8FAFC;
}

/* Code Blocks */
pre {
    background-color: #F1F5F9;
    border: 1px solid #E2E8F0;
    border-radius: 5px;
    padding: 10px 14px;
    font-family: Consolas, "Liberation Mono", Courier, monospace;
    font-size: 9pt;
    line-height: 1.45;
    overflow-x: auto;
    page-break-inside: avoid;
}

code {
    font-family: Consolas, "Liberation Mono", Courier, monospace;
    font-size: 9pt;
    background-color: #F1F5F9;
    padding: 2px 5px;
    border-radius: 3px;
    color: #0B1B3D;
}

pre code {
    background: none;
    padding: 0;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #BA0C2F;
    background-color: #FFF5F5;
    margin: 12px 0;
    padding: 10px 16px;
    font-size: 10pt;
    color: #2D3748;
    border-radius: 0 4px 4px 0;
}

/* Lists */
ul, ol {
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 22px;
}

li {
    margin-bottom: 4px;
}

/* Horizontal Rule */
hr {
    border: none;
    border-top: 1px solid #E2E8F0;
    margin: 22px 0;
}

/* Footer note */
.document-footer {
    margin-top: 30px;
    padding-top: 12px;
    border-top: 1px solid #E2E8F0;
    font-size: 8.5pt;
    color: #718096;
    display: flex;
    justify-content: space-between;
}

.meeting-card {
    page-break-inside: avoid;
    margin-bottom: 18px;
}
"""

def markdown_to_html(md_text, title="STARPath Coursework Document"):
    html_content = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "nl2br", "sane_lists"]
    )
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>{CSS_STYLES}</style>
</head>
<body>
    <div class="academic-header">
        <span class="uclan-badge">University of Central Lancashire</span>
        <span class="sub-badge">School of Engineering &amp; Computing</span>
        <span class="sub-badge">CO2007 The Agile Professional</span>
        <span class="sub-badge">Group 4 — STARPath</span>
    </div>
    
    {html_content}
    
    <div class="document-footer">
        <div><strong>STARPath</strong> — BSc (Hons) AI &amp; Data Science (2026/27)</div>
        <div>UCLan CO2007 Coursework Assessment Deliverable</div>
    </div>
</body>
</html>
"""
    return full_html


def render_pdf(html_text, output_pdf_path):
    with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as f:
        f.write(html_text)
        temp_html_path = f.name

    try:
        cmd = [
            CHROME_PATH,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={output_pdf_path}",
            temp_html_path
        ]
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=45)
        if res.returncode != 0:
            print(f"Error rendering {output_pdf_path}: {res.stderr.decode()}")
            return False
        
        size_kb = os.path.getsize(output_pdf_path) / 1024
        print(f"Successfully generated: {os.path.basename(output_pdf_path)} ({size_kb:.1f} KB)")
        return True
    finally:
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)


def main():
    print("=== STARPath PDF Builder: Compiling Coursework Deliverables ===")
    os.makedirs(DOCS_DIR, exist_ok=True)
    
    documents = [
        {
            "src": os.path.join(SRC_DIR, "MINUTES_OF_MEETINGS.md"),
            "dest": os.path.join(DOCS_DIR, "STARPath_Minutes_of_Meetings.pdf"),
            "title": "STARPath — Minutes of Meetings (MoM)"
        },
        {
            "src": os.path.join(SRC_DIR, "PROJECT_GUIDE_AND_MODULE_LEADER_BRIEF.md"),
            "dest": os.path.join(DOCS_DIR, "STARPath_Project_Guide_and_Brief.pdf"),
            "title": "STARPath — Project Guide & Module Leader Brief"
        },
        {
            "src": os.path.join(SRC_DIR, "PRESENTATION_SLIDES.md"),
            "dest": os.path.join(DOCS_DIR, "STARPath_Presentation_Slides.pdf"),
            "title": "STARPath — Module Leader Presentation Slides"
        },
        {
            "src": os.path.join(SRC_DIR, "AI_USAGE.md"),
            "dest": os.path.join(DOCS_DIR, "STARPath_AI_Usage_and_Academic_Integrity.pdf"),
            "title": "STARPath — AI Usage & Academic Integrity Report"
        }
    ]
    
    # Combined Architecture & Deployment PDF
    arch_path = os.path.join(SRC_DIR, "ARCHITECTURE.md")
    deploy_path = os.path.join(SRC_DIR, "DEPLOYMENT.md")
    combined_arch_deploy = ""
    if os.path.exists(arch_path):
        with open(arch_path, "r", encoding="utf-8") as f:
            combined_arch_deploy += f.read() + "\n\n---\n\n"
    if os.path.exists(deploy_path):
        with open(deploy_path, "r", encoding="utf-8") as f:
            combined_arch_deploy += f.read()
            
    if combined_arch_deploy:
        documents.append({
            "content": combined_arch_deploy,
            "dest": os.path.join(DOCS_DIR, "STARPath_Architecture_and_Deployment.pdf"),
            "title": "STARPath — Architecture & Cloud Deployment Guide"
        })
    
    results = []
    for doc in documents:
        if "src" in doc and os.path.exists(doc["src"]):
            with open(doc["src"], "r", encoding="utf-8") as f:
                md_text = f.read()
        elif "content" in doc:
            md_text = doc["content"]
        else:
            print(f"Skipping missing source for {doc['dest']}")
            continue
            
        html = markdown_to_html(md_text, title=doc["title"])
        ok = render_pdf(html, doc["dest"])
        results.append((doc["dest"], ok))
        
    print("\n--- Summary of Generated PDFs ---")
    for dest, ok in results:
        status = "PASSED" if ok else "FAILED"
        size = f"{os.path.getsize(dest)/1024:.1f} KB" if ok and os.path.exists(dest) else "0 KB"
        print(f"[{status}] {os.path.basename(dest)} — {size}")

if __name__ == "__main__":
    main()
