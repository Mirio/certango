import os
from collections.abc import Sequence
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
LOCAL_DOTENVS_DIR = BASE_DIR / ".envs" / ".local"
LOCAL_DOTENV_FILES = [
    LOCAL_DOTENVS_DIR / ".django",
    LOCAL_DOTENVS_DIR / ".postgres",
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


if __name__ == "__main__":
    merge(DOTENV_FILE, LOCAL_DOTENV_FILES)
