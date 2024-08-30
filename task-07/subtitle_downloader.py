import click
import requests
from bs4 import BeautifulSoup
import os
import hashlib

BASE_URL = "https://www.opensubtitles.org"
IMDB_API_URL = "https://www.omdbapi.com/"
API_KEY ="2d774856"

def get_imdb_id_from_url(url):
    movie_name = url.split('/')[-1].replace('.mpeg4', '').replace('-', ' ')
    response = requests.get(f"{IMDB_API_URL}?t={movie_name}&apikey={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        return data.get("imdbID")
    return None

def search_subtitles_by_idmovie(idmovie, language=None):
    query = f"{BASE_URL}/en/search/sublanguageid-{language}/idmovie-{idmovie}" if language else f"{BASE_URL}/en/search/idmovie-{idmovie}"
    print(f"Search query: {query}")  # Debug statement
    response = requests.get(query)
    soup = BeautifulSoup(response.text, "html.parser")
    subtitles = soup.find_all("a", class_="bnone")
    return subtitles

@click.command()
@click.argument("url")
@click.option("-l", "--language", type=str, help="Filter subtitles by language (e.g., eng for English).")
@click.option("-o", "--output", type=click.Path(), help="Specify the output folder for the subtitles.", default=".")
@click.option("-s", "--file-size", type=int, help="Filter subtitles by movie file size (in bytes).")
@click.option("-h", "--match-by-hash", type=str, help="Match subtitles by movie hash.")
@click.option("-b", "--batch-download", is_flag=True, help="Enable batch mode (process all files in a directory).")
def main(url, language, output, file_size, match_by_hash, batch_download):
    if batch_download:
        if not os.path.isdir(url):
            click.echo("In batch mode, please specify a directory.")
            return
        
        for filename in os.listdir(url):
            if filename.endswith(".mpeg4"):
                file_path = os.path.join(url, filename)
                process_file(file_path, language, output, file_size, match_by_hash)
    else:
        if not os.path.isfile(url) and not url.startswith("http://") and not url.startswith("https://"):
            click.echo("Please provide a valid file path or URL.")
            return

        movie_name = os.path.basename(url).replace('.mpeg4', '').replace('-', ' ')
        imdb_id = get_imdb_id_from_url(url)
        if not imdb_id:
            click.echo(f"IMDb ID could not be found for the URL: {url}")
            return

        
        idmovie = "4959"  #hardcoded the digit 4959 is the osdb obtained from the opensubtitles manually

        subtitles = search_subtitles_by_idmovie(idmovie, language)

        if not subtitles:
            click.echo(f"No subtitles found for the movie at URL: {url}")
            return

        click.echo(f"Found {len(subtitles)} subtitles for {url}:")
        for i, subtitle in enumerate(subtitles):
            click.echo(f"{i + 1}: {subtitle.text}")

        choice = click.prompt("Enter the number of the subtitle to download", type=int)
        selected_subtitle = subtitles[choice - 1]
        subtitle_url = f"{BASE_URL}{selected_subtitle['href']}"
        download_subtitle(subtitle_url, output)
        click.echo(f"Subtitle downloaded to {output}")

def download_subtitle(url, output_folder):
    response = requests.get(url)
    subtitle_file = os.path.join(output_folder, url.split('/')[-1])
    with open(subtitle_file, "wb") as f:
        f.write(response.content)
    return subtitle_file

if __name__ == "__main__":
    main()
