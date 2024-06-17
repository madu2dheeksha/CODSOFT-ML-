<!DOCTYPE html>
<html>
<head>
    <title> Movie Genre Classification</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .movie-container {
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .movie-info {
            margin-top: 20px;
        }
        .genre-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .genre-list li {
            display: inline-block;
            margin-right: 20px;
        }
    </style>
</head>
<body>
    <h1>Movie Genre Classification</h1>
    <form id="movie-form">
        <label for="movie-title">Movie Title:</label>
        <input type="text" id="movie-title" name="movie-title"><br><br>
        <label for="movie-poster">Movie Poster:</label>
        <input type="file" id="movie-poster" name="movie-poster"><br><br>
        <button type="submit">Classify Genre</button>
    </form>
    <div id="movie-container"></div>

    <script>
        const movieForm = document.getElementById('movie-form');
        const movieContainer = document.getElementById('movie-container');

        movieForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const title = document.getElementById('movie-title').value;
            const poster = document.getElementById('movie-poster').files[0];

            // Send the movie data to the server for classification
            const response = await fetch('/classify', {
                method: 'POST',
                body: new FormData(movieForm),
            });
            const data = await response.json();

            // Display the classification results
            const movieInfo = document.createElement('div');
            movieInfo.className = 'movie-info';
            movieInfo.innerHTML = `
                <h3>${title}</h3>
                <ul class="genre-list">
                    ${data.genres.map((genre) => `<li>${genre}</li>`).join('')}
                </ul>
            `;
            movieContainer.appendChild(movieInfo);
        });
    </script>
</body>
</html>
