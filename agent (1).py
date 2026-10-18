import os
import time
from datetime import datetime, timezone, timedelta
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool

# Otak AI: Gemini lewat API gratis (kunci diambil dari GitHub Secrets)
model = LiteLLMModel(
    model_id="gemini/gemini-3.8-flash",
    api_key=os.environ["GEMINI_API_KEY"],
)

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    max_steps=6,
)

# Beri tahu agent tanggal hari ini (zona waktu WIB) supaya tidak salah tahun
wib = timezone(timedelta(hours=7))
hari_ini = datetime.now(wib).strftime("%Y-%m-%d")

tugas = (
    f"Hari ini tanggal {hari_ini}. "
    "Cari 3 berita kebakaran terbaru di Indonesia dengan alat pencarian. "
    "Gunakan HANYA informasi dari hasil pencarian, jangan mengarang. "
    "Jalankan pencarian dulu, lihat hasilnya, baru buat jawaban akhir di langkah berikutnya. "
    "Sebutkan tanggal dan sumber (URL) tiap berita, lalu rangkum singkat dalam bahasa Indonesia."
)

# Coba ulang sampai 3 kali kalau server Google sedang sibuk (error 503)
for percobaan in range(1, 4):
    try:
        hasil = agent.run(tugas)
        print("=== HASIL AGENT ===")
        print(hasil)
        break
    except Exception as e:
        print(f"Percobaan {percobaan} gagal: {e}")
        if percobaan == 3:
            raise
        time.sleep(60)
