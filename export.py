import json
from pathlib import Path

def extract_code_from_notebook(notebook_path):
    with notebook_path.open('r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    code_cells = [cell for cell in notebook['cells'] if cell['cell_type'] == 'code' and '#| export\n' in cell['source']]
    return [cell['source'] for cell in code_cells]

def create_python_file(notebook_path, code, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Use the notebook filename (without extension) as the Python file name
    python_file = output_dir / f"{notebook_path.stem}.py"
    
    # Join all code cells, separating them with newlines
    code_content = '\n\n'.join(''.join(cell) for cell in code)
    
    python_file.write_text(code_content, encoding='utf-8')
    print(f"Created {python_file}")

def process_notebooks(input_dir, output_dir):
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    
    for notebook_path in input_dir.glob('*.ipynb'):
        code = extract_code_from_notebook(notebook_path)
        create_python_file(notebook_path, code, output_dir)

def main(input_dir, output_dir):
    process_notebooks(input_dir, output_dir)
    print(f"All notebook code extracted to {output_dir}")

if __name__ == "__main__":
    input_dir = Path("nbs")
    output_dir = Path("out")
    main(input_dir, output_dir)
