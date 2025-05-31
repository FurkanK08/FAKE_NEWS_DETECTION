async function predict() {
  const text = document.getElementById("inputText").value.trim();
  const resultBox = document.getElementById("resultBox");

  if (!text) {
    resultBox.innerText = "Lütfen bir metin girin!";
    resultBox.className = "red";
    resultBox.classList.remove("hidden");
    return;
  }

  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text }),
  });

  const data = await response.json();
  const colorClass = data.label === "Fake" ? "red" : "green";
  resultBox.innerText = `${data.label.toUpperCase()} News\nFake: %${data.fake_prob} | Real: %${data.real_prob}`;
  resultBox.className = colorClass;
  resultBox.classList.remove("hidden");
}
