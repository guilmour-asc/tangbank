# tangbank
ATM (cash machine) simulator made in Django, for a test completion

## What is it?
This is just a challenge/test made by an enterprise. As I write it (December 2017), I'm trying to get employed on IT area. If this test gets greened, presumedly I'm employed, so that's it.

## How to Run
- Have **PIP (pip3)** and **python3-venv** installed...

- Clone this repo...

`git clone https://github.com/guilmour-asc/tangbank.git`

- Open the **terminal** (or Windows' **cmd**) at the cloned folder...

`cd path/to/cloned/folder/`

- Execute the virtual environment's activation. After that, the virtual environment's name will appear on parentheses before the user on the terminal. Then, we can run the project...

```
. bin/activate
tangbank/manage.py runserver
```

- To deactivate the virtual environment, execute:

`deactivate`

## To-Do
| Function                              | Made? |
| :-------------------------------------| -----:|
| List accounts                         |     🗸 |
| Create accounts                       |     🗸 |
| Show one account's details            |     🗸 |
| Chnagee account's details             |     🗸 |
| Make withdrawal (sake)                |     🗸 |
| Show the cashier's stock              |     🗸 |
| Change the cashier's stock            |     🗸 |
| Input/Output is JSON                  |       |
| Stop CSRF verification                |     🗸 |
| Allow CORS for everywhere             |     🗸 |
| Show 1+ comb. of notes, on withdrawal |     🗸 |
| Show one account's history of actions |     🗸 |
| Transfer cash between accounts        |     🗸 |