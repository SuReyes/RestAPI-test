import pytest

from util import rest_client
from util.models import Poem


def get_authors():
    status_code, response = rest_client.get_request("author")
    return response.get("authors")


def get_titles():
    status_code, response = rest_client.get_request("title")
    return response.get("titles")


test_authors = get_authors()
test_titles = get_titles()


@pytest.mark.parametrize(
    "author",
    test_authors,
)
def test_authors(author: str):
    author_status_code, author_response = rest_client.get_request(f"author/{author}")
    assert author_status_code == 200, f"{author_status_code=} {author_response=}"
    for poem_json in author_response:
        poem = Poem(**poem_json)
        assert poem.author == author, f"Author mismatch {poem.author} != {author}"
        #validate_poem_lines(poem)
        # we need to remove empty lines from the count
        poem_non_empty_lines = [line for line in poem.lines if line]
        assert poem.linecount == len(poem_non_empty_lines), f"{poem.author} poem {poem.title} length mismatch {poem.linecount} != {len(poem_non_empty_lines)}"


@pytest.mark.parametrize(
    "title",
    test_titles,
)
def test_titles(title: str):
    author_status_code, author_response = rest_client.get_request(f"title/{title}")
    assert author_status_code == 200, f"{author_status_code=} {author_response=}"
    clean_title = title.replace(".", "").upper()
    for poem_json in author_response:
        try:
            poem = Poem(**poem_json)
            title_check = poem.title.replace(".", "").upper()
            assert clean_title in title_check, f"Author mismatch {title} in {poem.title}"
            # we need to remove empty lines from the count
            poem_non_empty_lines = [line for line in poem.lines if line]
            assert poem.linecount == len(
                poem_non_empty_lines), f"{poem.author} poem {poem.title} length mismatch {poem.linecount} != {len(poem_non_empty_lines)}"
        except TypeError as e:
            print(f"ERROR: {e}, \n{poem_json}")
            assert False, f"{e}, {poem_json}"
