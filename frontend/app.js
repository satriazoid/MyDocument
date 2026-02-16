async function generate() {
    const data = {
        title: document.getElementById("title").value,
        author: document.getElementById("author").value,
        institution: document.getElementById("institution").value,
        chapters: parseInt(document.getElementById("chapters").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById("result").innerText =
        "✅ Berhasil!\nFile: " + result.file;

    } catch (error) {
        document.getElementById("result").innerText =
        "❌ Error:\n" + error;
    }
}
