import typer

app = typer.Typer()


@app.command()
def main() -> None:
    """Olympia."""


if __name__ == "__main__":
    app(prog_name="olympia")  # pragma: no cover
