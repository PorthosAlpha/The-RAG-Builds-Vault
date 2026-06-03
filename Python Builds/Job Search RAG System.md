--- job-search-rag/WINDOWS_SETUP.md (原始)


+++ job-search-rag/WINDOWS_SETUP.md (修改后)
# Windows Setup Guide for Job Search RAG

This guide will help you set up and run the Job Search RAG system on your Windows laptop with RTX 4050 (4GB GPU).

## Prerequisites

### 1. Install Python 3.10+

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"**
3. Verify installation:
   ```powershell
   python --version
   ```

### 2. Install NVIDIA CUDA Toolkit (for GPU acceleration)

Your RTX 4050 supports CUDA. Install:

1. Download CUDA Toolkit from [NVIDIA](https://developer.nvidia.com/cuda-downloads)
2. Select: Windows -> Your Windows version -> exe (local)
3. Follow installation wizard
4. Verify installation:
   ```powershell
   nvidia-smi
   ```

### 3. Install Ollama (Local LLM Runtime)

1. Download Ollama from [ollama.com](https://ollama.com)
2. Run the installer
3. Open PowerShell and pull the model:
   ```powershell
   ollama pull llama3:8b
   ```

   **Note**: For 4GB VRAM, use the quantized version:
   ```powershell
   ollama pull llama3:8b-instruct-q4_K_M
   ```

4. Verify Ollama is running:
   ```powershell
   ollama list
   ```

## Installation Steps

### Step 1: Clone or Download the Project

Navigate to your project directory:
```powershell
cd C:\path\to\job-search-rag
```

### Step 2: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1
```

If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 3: Install Dependencies

```powershell
# Upgrade pip
python -m pip install --upgrade pip

# Install PyTorch with CUDA support (important for GPU acceleration)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install other dependencies
pip install -r requirements.txt
```

### Step 4: Configure Environment

```powershell
# Copy environment template
copy .env.example .env
```

Edit `.env` file with your preferences (optional, defaults work fine).

### Step 5: Update Your Profile

Edit `data/user_profile.json` with your actual:
- Education background
- Skills
- Work experience
- Projects
- Job preferences

## Running the System

### Start Ollama Server

Make sure Ollama is running in the background:
```powershell
ollama serve
```

### Run the Job Search

With your virtual environment activated:

```powershell
python src/main.py
```

## Expected Output

The system will:

1. 🔍 Scrape job listings from multiple sources
2. 💾 Index jobs in the vector database
3. 🎯 Find matches based on your profile
4. 📝 Generate customized resumes and cover letters

Check the `outputs/` directory for generated documents.

## Troubleshooting

### GPU Memory Issues

If you encounter out-of-memory errors:

1. Use a smaller embedding model in `configs/settings.yaml`:
   ```yaml
   embedding:
     model: all-MiniLM-L6-v2  # Already small, but ensure it's used
     device: cpu  # Fall back to CPU if needed
   ```

2. Reduce batch size in code if processing many jobs

### Ollama Connection Errors

If you can't connect to Ollama:

1. Make sure Ollama is running: `ollama serve`
2. Check the base URL in `.env`:
   ```
   OLLAMA_BASE_URL=http://localhost:11434
   ```

### Slow Performance

To improve performance:

1. Ensure GPU is being used:
   - Check Task Manager > Performance > GPU
   - Look for CUDA activity

2. Use SSD storage for faster vector database operations

3. Limit number of jobs scraped in `configs/settings.yaml`:
   ```yaml
   scraper:
     sources:
       - name: linkedin
         max_jobs: 20  # Reduce from 50
   ```

## Customization

### Add More Job Sources

Edit `src/scraper.py` to add custom scrapers for:
- Company career pages
- Niche job boards
- RSS feeds

### Adjust Matching Threshold

In `configs/settings.yaml`:
```yaml
matching:
  threshold: 0.70  # Lower for more matches, higher for stricter matching
```

### Change LLM Model

For different models:
```powershell
# Try Mistral (smaller, faster)
ollama pull mistral:7b

# Or Phi-3 (very efficient)
ollama pull phi3:mini
```

Then update `configs/settings.yaml`:
```yaml
llm:
  model: mistral:7b  # or phi3:mini
```

## Next Steps

1. **Review Generated Documents**: Check `outputs/resumes/` and `outputs/cover_letters/`
2. **Refine Your Profile**: Update `data/user_profile.json` based on results
3. **Automate**: Set up a scheduled task to run weekly
4. **Track Applications**: Create a spreadsheet to track which jobs you applied to

## Additional Resources

- [Ollama Documentation](https://ollama.com/docs)
- [LangChain Documentation](https://python.langchain.com/docs/)
- [ChromaDB Documentation](https://docs.trychroma.com/)

## Support

If you encounter issues:

1. Check logs in `outputs/logs/`
2. Review error messages carefully
3. Ensure all prerequisites are installed correctly
4. Consider using CPU-only mode if GPU issues persist

---
--- job-search-rag/configs/settings.yaml (原始)


+++ job-search-rag/configs/settings.yaml (修改后)
llm:
  provider: ollama
  model: llama3:8b
  base_url: http://localhost:11434
  temperature: 0.7
  max_tokens: 2048

embedding:
  model: all-MiniLM-L6-v2
  device: cuda  # Use GPU for faster embeddings

scraper:
  sources:
    - name: linkedin
      enabled: true
      max_jobs: 50
    - name: indeed
      enabled: true
      max_jobs: 50
    - name: glassdoor
      enabled: true
      max_jobs: 50
  search_keywords:
    - "machine learning engineer"
    - "python developer"
    - "rag engineer"
    - "nlp engineer"
  remote_only: true

vector_store:
  type: chroma
  persist_directory: ./data/vector_db
  collection_name: job_embeddings
  distance_metric: cosine

matching:
  threshold: 0.75
  top_k: 10
  use_reranking: true

generation:
  resume_template: templates/resume_template.docx
  cover_letter_template: templates/cover_letter_template.txt
  output_format:
    resume: pdf
    cover_letter: txt

system:
  log_level: INFO
  cache_enabled: true
  cache_ttl_hours: 24
  

---
--- job-search-rag/configs/settings.yaml (原始)


+++ job-search-rag/configs/settings.yaml (修改后)
llm:
  provider: ollama
  model: llama3:8b
  base_url: http://localhost:11434
  temperature: 0.7
  max_tokens: 2048

embedding:
  model: all-MiniLM-L6-v2
  device: cuda  # Use GPU for faster embeddings

scraper:
  sources:
    - name: linkedin
      enabled: true
      max_jobs: 50
    - name: indeed
      enabled: true
      max_jobs: 50
    - name: glassdoor
      enabled: true
      max_jobs: 50
  search_keywords:
    - "machine learning engineer"
    - "python developer"
    - "rag engineer"
    - "nlp engineer"
  remote_only: true

vector_store:
  type: chroma
  persist_directory: ./data/vector_db
  collection_name: job_embeddings
  distance_metric: cosine

matching:
  threshold: 0.75
  top_k: 10
  use_reranking: true

generation:
  resume_template: templates/resume_template.docx
  cover_letter_template: templates/cover_letter_template.txt
  output_format:
    resume: pdf
    cover_letter: txt

system:
  log_level: INFO
  cache_enabled: true
  cache_ttl_hours: 24
  

---
--- job-search-rag/data/user_profile.json (原始)


+++ job-search-rag/data/user_profile.json (修改后)
{
  "education": [
    {
      "degree": "Bachelor of Science",
      "field": "Computer Science",
      "institution": "Your University",
      "graduation_year": 2023,
      "gpa": "3.8",
      "relevant_coursework": [
        "Machine Learning",
        "Data Structures",
        "Algorithms",
        "Natural Language Processing",
        "Database Systems"
      ]
    }
  ],
  "skills": {
    "programming_languages": [
      "Python",
      "JavaScript",
      "SQL",
      "Java"
    ],
    "frameworks_libraries": [
      "PyTorch",
      "TensorFlow",
      "LangChain",
      "React",
      "Node.js",
      "FastAPI"
    ],
    "tools_platforms": [
      "Git",
      "Docker",
      "AWS",
      "Linux",
      "VS Code"
    ],
    "domains": [
      "Machine Learning",
      "RAG Systems",
      "NLP",
      "Web Development",
      "Data Engineering"
    ]
  },
  "experience": [
    {
      "title": "Software Developer Intern",
      "company": "Tech Company",
      "location": "Remote",
      "duration": "May 2022 - August 2022",
      "description": "Developed machine learning models for customer segmentation",
      "achievements": [
        "Improved model accuracy by 15%",
        "Built data pipeline processing 1M+ records daily",
        "Collaborated with cross-functional team of 5 engineers"
      ]
    }
  ],
  "projects": [
    {
      "name": "RAG-based Question Answering System",
      "description": "Built a retrieval-augmented generation system for domain-specific QA",
      "technologies": ["Python", "LangChain", "ChromaDB", "Llama 3"],
      "link": "https://github.com/yourusername/project"
    }
  ],
  "preferences": {
    "remote_only": true,
    "job_types": ["Full-time", "Contract"],
    "locations": ["United States", "Europe", "Remote"],
    "salary_range": {
      "min": 80000,
      "max": 150000,
      "currency": "USD"
    },
    "exclude_keywords": [
      "onsite",
      "hybrid",
      "relocation required"
    ]
  }
}

---
