import os
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool

# Otak AI: Gemini lewat API gratis (kunci diambil dari GitHub Secrets)
model = LiteLLMModel(
    model_id="gemini/gemini-2.5-flash",  # ganti dengan model Flash gratis terbaru di AI Studio
    api_key=os.environ["GEMINI_API_KEY"],
)

# Agent: bisa mencari di web, maksimal 5 langkah supaya hemat kuota
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    max_steps=5,
)

# Tugas agent (ubah sesuai kebutuhan Anda)
tugas = "Cari 3 berita teknologi terbaru hari ini, lalu rangkum singkat dalam bahasa Indonesia."

hasil = agent.run(tugas)
print("=== HASIL AGENT ===")
print(hasil)
