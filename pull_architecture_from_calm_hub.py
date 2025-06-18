import requests
import click
import json

def get_pattern_from_namespace_by_id_and_version(namespace, id, version):
    res = requests.get(f"http://localhost:8080/calm/namespaces/{namespace}/patterns/{id}/versions/{version}")
    return res.json()

def save_pattern_to_file(pattern, filename):
    with open(filename, "w") as file:
        json.dump(pattern, file, indent=2)

@click.command()
@click.option('--namespace', help="Namespace holding the pattern")
@click.option('--id', help="Id of pattern")
@click.option('--version', help="Pattern version")
@click.option('--output', help="Filename to save pattern as")
def main(namespace, id, version, output):
    pattern = get_pattern_from_namespace_by_id_and_version(namespace, id, version)
    save_pattern_to_file(pattern, output)


if __name__ == "__main__":
    main()