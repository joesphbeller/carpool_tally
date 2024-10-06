# carpool_tally
An object-oriented Python code that takes in a tab separated file that logs a monthly carpool and outputs the money that each participant owes/is owed.

## Requirements
- Python 3.x
- pandas
- numpy

Currently, this code worked in my Conda environment running Python 3.12.2, pandas 2.2.2, and numpy 1.26.4.

## Usage

syntax: 
```
python3 carpool_tally.py filename trip_cost
```
float trip_cost: Cost of the daily commute
string filename: The name of the tab delimited file that has the carpool logs  

## Output
Should output a statement for each person of what each person owes/is owed

## Example
Your .txt file that you use for input should be in the following format for each line
Driver  Passenger1  Passenger2  ... PassengerN

For example (same example file found in repository):
John    Jane    Richard
John    Richard
Jane    Richard

(If you select cells from an Excel spreadsheet, then copy and paste into a .txt editor, it sometimes does tab delimited automatically)

In this example, John drove on the first two days while Jane drove the third day.
The calculation logic is as follows:
- John owns a car with 20 mpg while Jane owns a car with 30 mpg.
- The carpool roundtrip is 25 miles.
- John and Jane decide to calculate the trip cost by averaging their vehicle mileage and adding + $2 for wear and tear.
- If gas is $4 a gallon, this means our total trip cost is $6 per trip.
- On day 1, the trip costs $6 which is split evenly between the carpool, so Jane and Richard owe John $2.
- On day 2, the trip costs $6 which is split between only the two passengers for this day, so Richard owes John $2 more.
- On day 3, the trip costs $6 which is split only between Jane and Richard, so Richard now owes Jane $2.
Code will output:
```
John has a balance of -7
Jane has a balance of -1
Richard has a balance of 8
```
Negative balance means that the person is owed money. (People who drive the most often will have negative balances)

## Error handling
- Check the sample .txt file to make sure data entry is correct. There should be no header.
## Limitations
- Expects the trip cost to be the same for all drivers (assuming everyones car has the same mpg)
- Expects trip cost to already be known/calculated

## License
This project is licensed under the MIT License - see the LICENSE file for details.

