# zero-bounce

👷 Under construction!

Repository holding the source code and documentation for `zero-bounce`.

## Introduction

`zero-bounce` is a web application that allows multiple players with their DMs to take pen and paper games to the next level. How often do you want to experience adventures together, but don't have the opportunity to meet in person? How many trees have you killed by printing out sheets for each character and providing cards for each?

`zero-bounce` solves these and more problems. Create dynamic maps, maintain any information about your fantasy world and make it available to your players based on events. Change character traits and let your players feel what's happening in the world.

## Technologies

The technologies used under the hood of `zero-bounce` were not chosen by our own toolboxes of stacks we already have guru experience in. Rather, we use the project idea to educate ourselves in different languages, frameworks and technologies and apply our new knowledge directly by solving problems that arise.

In some places our decision may not be the best possible technically - but it was the best possible for us to learn as much as possible.

## Repository structure

- `backend/` holds all application logic for the `data-service`.
  - The service is a RESTful API written in Python with FastAPI for HTTP handling, SQLAlchemy for database ORM actions and Pydantic for API schema validation.
- `ci/` holds files, configurations, ... to build the separate services.
- `docs/` hold several files that are more some notes than actual documentation of the project.
- `frontend/` holds the application logic for the web-applications' frontend.
  - The service is written in VueJS.
- `hacks/` include several files that are used for local testing, development and other stuff that will not be baked into a production environment.

## Authors & Contributors

- [TobiStilgenbauer](https://github.com/TobiStilgenbauer)
- [torbendury](https://github.com/torbendury)
- [maxopaul](https://github.com/maxopaul)

## Code

Here are some helpful informations on how to run, build and operate the codebase and the resulting software artifacts.

### Running locally

The easiest way to run the project in its latest state locally is to use [`docker-compose`](hacks/docker-compose/docker-compose.yml). This file will be enriched with every new joined service and also with some data to test on.

### Building locally

### Building remote

### Contributions

Contributions are **always** welcome! Just hit up on one of the [authors](#authors--contributors) or open a GitHub issue if you would like to get in touch.

You might also consider reading the [contribution guidelines](CONTRIBUTING.md) that also include a COC.

#### Adding features

#### Fixing Bugs
