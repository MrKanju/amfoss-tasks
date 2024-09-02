import click
import requests
from bs4 import BeautifulSoup
import os
import hashlib

BASE_URL = "https://www.opensubtitles.org"
IMDB_API_URL = "https://www.omdbapi.com/"
API_KEY = "2d774856"  # OMDb API key

def fetch_imdb_id(movie_name):
    """Fetch IMDb ID for a given movie name."""
    response = requests.get(f"{IMDB_API_URL}?t={movie_name}&apikey={API_KEY}")
    if response.status_code == 200:
        return response.json().get("imdbID")
    return None

def calculate_file_hash_and_size(url):
    """Calculate MD5 hash and size of a movie file."""
    response = requests.head(url)
    file_size = int(response.headers.get('Content-Length', 0))

    hash_md5 = hashlib.md5()
    with requests.get(url, stream=True) as r:
        for chunk in r.iter_content(chunk_size=8192):
            hash_md5.update(chunk)
    
    return file_size, hash_md5.hexdigest()

def find_subtitles(imdb_id, language=None):
    """Find subtitles based on IMDb ID and language."""
    query = f"{BASE_URL}/en/search2/sublanguageid-{language}/imdbid-{imdb_id}" if language else f"{BASE_URL}/en/search2/imdbid-{imdb_id}"
<<<<<<< HEAD
=======
    print(f"Search query: {query}") 
>>>>>>> a23064482bcd110d7f42d1be69f4cab3dabad4b0
    response = requests.get(query)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("a", class_="bnone")

def download_and_save_subtitle(url, output_folder):
    """Download subtitle from URL and save to specified folder."""
    response = requests.get(url)
    subtitle_file_path = os.path.join(output_folder, url.split('/')[-1])
    with open(subtitle_file_path, "wb") as f:
        f.write(response.content)
    return subtitle_file_path

def process_single_file(url, language, output_folder, filter_by_size, filter_by_hash):
    """Process a single movie file or URL."""
    movie_name = url.split('/')[-1].replace('.mpeg4', '').replace('-', ' ')
    imdb_id = fetch_imdb_id(movie_name)
    
    if not imdb_id:
        click.echo(f"IMDb ID could not be found for the URL: {url}")
        return

    click.echo(f"IMDb ID for the given URL: {imdb_id}")

    if filter_by_size or filter_by_hash:
        file_size, file_hash = calculate_file_hash_and_size(url)
        click.echo(f"File size: {file_size} bytes, File hash: {file_hash}")

    subtitles = find_subtitles(imdb_id, language)
    if not subtitles:
        click.echo(f"No subtitles found for IMDb ID: {imdb_id}")
        return

    click.echo(f"Found {len(subtitles)} subtitles for IMDb ID: {imdb_id}:")
    for i, subtitle in enumerate(subtitles):
        click.echo(f"{i + 1}: {subtitle.text}")

    choice = click.prompt("Enter the number of the subtitle to download", type=int)
    if choice < 1 or choice > len(subtitles):
        click.echo("Invalid choice.")
        return

    subtitle_url = f"{BASE_URL}{subtitles[choice - 1]['href']}"
    download_and_save_subtitle(subtitle_url, output_folder)
    click.echo(f"Subtitle downloaded to {output_folder}")

def process_batch_directory(directory_path, language, output_folder, filter_by_size, filter_by_hash):
    """Process all movie files in a directory."""
    for filename in os.listdir(directory_path):
        if filename.endswith(".mpeg4"):
            file_path = os.path.join(directory_path, filename)
            process_single_file(file_path, language, output_folder, filter_by_size, filter_by_hash)

@click.command()
@click.argument("url")
@click.option("-l", "--language", type=str, help="Filter subtitles by language (e.g., eng for English).")
@click.option("-o", "--output", type=click.Path(), help="Specify the output folder for the subtitles.", default=".")
@click.option("-s", "--file-size", is_flag=True, help="Filter subtitles by movie file size.")
@click.option("-h", "--match-by-hash", is_flag=True, help="Match subtitles by movie hash.")
@click.option("-b", "--batch-download", is_flag=True, help="Enable batch mode (process all files in a directory).")
def main(url, language, output, file_size, match_by_hash, batch_download):
    """Main function to handle command-line arguments and options."""
    if batch_download:
        if not os.path.isdir(url):
            click.echo("In batch mode, please specify a directory.")
            return
        process_batch_directory(url, language, output, file_size, match_by_hash)
    else:
        if not os.path.isfile(url) and not url.startswith("http://") and not url.startswith("https://"):
            click.echo("Please provide a valid file path or URL.")
            return
        process_single_file(url, language, output, file_size, match_by_hash)

if __name__ == "__main__":
    main()

