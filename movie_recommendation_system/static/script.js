async function getRecommendations() {
    const select = document.getElementById("movieSelect");
    const title = select.value;
    const status = document.getElementById("status");
    const grid = document.getElementById("movieGrid");
    const resultTitle = document.getElementById("resultTitle");
    const count = document.getElementById("count");

    if (!title) {
        status.textContent = "Please select a movie first.";
        return;
    }

    status.textContent = "Finding similar movies...";
    grid.innerHTML = "";

    try {
        const response = await fetch("/recommend", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({title: title})
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        status.textContent = "";
        resultTitle.textContent = `Because you liked "${data.selected}"`;
        count.textContent = `${data.recommendations.length} recommendations`;

        data.recommendations.forEach((movie, index) => {
            const card = document.createElement("article");
            card.className = "card";
            card.innerHTML = `
                <div class="icon">🎬</div>
                <h3>${index + 1}. ${escapeHtml(movie.title)}</h3>
                <div class="genre">${escapeHtml(movie.genres)}</div>
                <p class="desc">${escapeHtml(movie.description)}</p>
                <span class="score">Similarity: ${movie.score}%</span>
            `;
            grid.appendChild(card);
        });

    } catch (error) {
        status.textContent = error.message;
        grid.innerHTML = "";
    }
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}
