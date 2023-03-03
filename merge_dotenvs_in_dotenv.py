import argparse
import os
from collections.abc import Sequence
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
LOCAL_DOTENVS_DIR = BASE_DIR / ".envs" / ".local"
LOCAL_DOTENV_FILES = [
    LOCAL_DOTENVS_DIR / ".django",
    LOCAL_DOTENVS_DIR / ".postgres",
]
PRODUCTION_DOTENVS_DIR = BASE_DIR / ".envs" / ".production"
PRODUCTION_DOTENV_FILES = [
    PRODUCTION_DOTENVS_DIR / ".django",
    PRODUCTION_DOTENVS_DIR / ".postgres",
]
DOTENV_FILE = BASE_DIR / ".env"


def merge(
    output_file: Path,
    files_to_merge: Sequence[Path],
) -> None:
    merged_content = ""
    for merge_file in files_to_merge:
        merged_content += merge_file.read_text()
        merged_content += os.linesep
    # Replace postgres host for local debug
    merged_content = merged_content.replace(
        'POSTGRES_HOST="postgres"', 'POSTGRES_HOST="127.0.0.1"'
    )
    output_file.write_text(merged_content)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-e",
        dest="env",
        required=True,
        choices=["local", "prod"],
        help="Select the environment to configure (local/prod)",
    )
    args = parser.parse_args(argv)
    print("Generating '%s' env file" % args.env)
    if args.env == "local":
        merge(DOTENV_FILE, LOCAL_DOTENV_FILES)
    elif args.env == "prod":
        merge(DOTENV_FILE, PRODUCTION_DOTENV_FILES)


if __name__ == "__main__":
    main()
