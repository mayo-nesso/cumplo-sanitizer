# Cumplo sanitizer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Simple jupyter notebook to clean and organize cumplo.cl flows and investments.

## What is cumplo.cl?

Cumplo is a chilean per-to-per financing platform. Connects companies that need financing with investors with capital.

## What is this cumplo_sanitizer thing?

From the investor's perspective, Cumplo has an information panel about investments and their statuses. However, in my opinion, this information is erratic, incomplete, and confusing.
In order to carry out an analysis it is necessary to have a clean and reliable data source. This is an attempt to achieve this goal.

Using the 'Resumen de flujos' and 'Resumen de movimientos' files, we will apply operations to clean, correct, and group the different investments.
These files can be downloaded from the investor's profile.
Specifically in 'Historial Cuenta Personal' in the 'Flujos' section, and in the 'Movimientos' section.

Then we are going to classify the investments in four categories: Unexecuted, Completed, Active, and Uncollectible.

## Usage

- Install requirements: We are using poetry, so `poetry install` will do the trick!
- Download `Resumen de flujos` and `Resumen de movimientos`, and place them in `./data_in/` folder
- Go through the notebook, the results will be saved on a `sanitized_and_classified.feather`

## Notes

- Some investments (especially old ones, 2013, 2014) don't have a RemateID, we will use the 'Actor' name as ID. (Since there are just a few of these special cases, we think it is 'safe' to use this approach)
- **Some investments don't have all the movements registered!** One way to spot those is by reviewing all the investments that have a negative balance. Some of these are just active, late or uncollectable investments, but a few are just wrong! It seems like if there was more than one movement on the same date it could have been registered just once (For example, if you invested in the same investment_id but two times this could lead to some issues). For this, we have to manually append some 'dirty and quick' fixes.

## Author

- [Mayo Nesso](https://github.com/mayofunk)

## License

This project is open source and available under the [MIT License](LICENSE.md).
