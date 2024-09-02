import click
import requests
from bs4 import BeautifulSoup
import os
import hashlib

BASE_URL = "https://www.opensubtitles.org"
IMDB_API_URL = "https://www.omdbapi.com/"
API_KEY = "2d774856"  # OMDb API key

def get_imdb_id_from_url(url):

    movie_name = url.split('/')[-1].replace('.mpeg4', '').replace('-', ' ')
    response = requests.get(f"{IMDB_API_URL}?t={movie_name}&apikey={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        return data.get("imdbID")
    return None

def get_movie_file_info_from_url(url):

    response = requests.head(url)
    file_size = int(response.headers.get('Content-Length', 0))
    
    hash_md5 = hashlib.md5()
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:  
                hash_md5.update(chunk)
    
    file_hash = hash_md5.hexdigest()
    return file_size, file_hash

def search_subtitles_by_imdb_id(imdb_id, language=None):

    query = f"{BASE_URL}/en/search2/sublanguageid-{language}/imdbid-{imdb_id}" if language else f"{BASE_URL}/en/search2/imdbid-{imdb_id}"
    print(f"Search query: {query}") 
    response = requests.get(query)
    soup = BeautifulSoup(response.text, "html.parser")
    subtitles = soup.find_all("a", class_="bnone")
    return subtitles

@click.command()
@click.argument("url")
@click.option("-l", "--language", type=str, help="Filter subtitles by language (e.g., eng for English).")
@click.option("-o", "--output", type=click.Path(), help="Specify the output folder for the subtitles.", default=".")
@click.option("-s", "--file-size", is_flag=True, help="Filter subtitles by movie file size.")
@click.option("-h", "--match-by-hash", is_flag=True, help="Match subtitles by movie hash.")
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

        imdb_id = get_imdb_id_from_url(url)
        if not imdb_id:
            click.echo(f"IMDb ID could not be found for the URL: {url}")
            return

        click.echo(f"IMDb ID for the given URL: {imdb_id}")
        
        file_size_bytes = None
        hash_value = None
        if file_size or match_by_hash:
            file_size_bytes, hash_value = get_movie_file_info_from_url(url)
            click.echo(f"File size: {file_size_bytes} bytes")
            click.echo(f"File hash: {hash_value}")
        
        subtitles = search_subtitles_by_imdb_id(imdb_id, language)

        if not subtitles:
            click.echo(f"No subtitles found for the movie with IMDb ID: {imdb_id}")
            return

        click.echo(f"Found {len(subtitles)} subtitles for the movie with IMDb ID: {imdb_id}:")
        for i, subtitle in enumerate(subtitles):
            click.echo(f"{i + 1}: {subtitle.text}")

        choice = click.prompt("Enter the number of the subtitle to download", type=int)
        if choice < 1 or choice > len(subtitles):
            click.echo("Invalid choice.")
            return

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

