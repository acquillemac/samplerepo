import click

# Define a command using the click decorator
@click.group()
def cli():
    """A simple CLI tool."""
    pass

# Define a simple command 'greet'
@click.command()
@click.argument('name')
def greet(name):
    """Greets the user by name."""
    click.echo(f"Hello, {name}!")

# Define a command to add two numbers
@click.command()
@click.argument('num1', type=int)
@click.argument('num2', type=int)
def add(num1, num2):
    """Adds two numbers."""
    result = num1 + num2
    click.echo(f"The result of {num1} + {num2} is {result}.")

# Define a command to multiply two numbers
@click.command()
@click.argument('num1', type=int)
@click.argument('num2', type=int)
def multiply(num1, num2):
    """Multiplies two numbers."""
    result = num1 * num2
    click.echo(f"The result of {num1} * {num2} is {result}.")

# Register the commands with the CLI group
cli.add_command(greet)
cli.add_command(add)
cli.add_command(multiply)

# Entry point for the CLI
if __name__ == '__main__':
    cli()
