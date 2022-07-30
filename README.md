<div id="top"></div>

<br />

<h3 align="center">simple kv store</h3>

  <p align="center">
    A simple in memory kv store in core lib python
    <br />
    <a href="#start">Getting started</a>
    ·
    <a href="#tests">Run tests</a>
  </p>
</div>

## Abstract

An in memory kv store in core lib python. Usable as an example for implementing a in memory kv store in python, where performance is not the main consideration. Transactions are implemented using a rudimentary state machine. the cli has been implemented using CMD.

<div id="start"></div>

## Getting started

### 1. Installation

A recent python 3.8+ install is required.
No dependencies to install.

The program can be started with:
   ```sh
   python main.py
   ```

### 2. core Commands


1. SET a key value pair
   ```sh
   SET Key Value
   ```
2. GET a value related to a key.
   ```sh
   GET Key
   ```
3. UNSET (remove) a key value pair.
   ```sh
   UNSET Key
   ```
4. Return the count of values equal to a value.
   ```sh
   NUMEQUALTO Value
   ```
5. Begin a transaction.
   ```sh
   BEGIN
   ```
6. Commit a transaction, making it permanent. 
   And exit the transaction.
   ```sh
   COMMIT
   ```
7. Revert a transaction, 
   reverting back to the state at the beginning of the transaction. 
   And exit the transaction.
   ```sh
   ROLLBACK
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

### 3. helper commands
1. List commands
   ```sh
   ?
   ```
2. Help on specific command
   ```sh
   ? <command>
   ```
4. Return the total contents of the store
   ```sh
   LIST
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<div id="tests"></div>

## Tests

The tests can be started with:
   ```sh
   python tests/tests.py
   ```
<p align="right">(<a href="#top">back to top</a>)</p>