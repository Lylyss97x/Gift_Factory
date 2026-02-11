# Gift Factory - Order Management System

A Python-based gift order management system demonstrating multiple design patterns including Factory, Singleton, Strategy, and Decorator patterns. The system manages gift creation, employee allocation, order customization, and delivery tracking through an interactive command-line interface.

## Features

- **Interactive Order Processing**: Command-line interface for creating gift orders with customization options
- **Multiple Gift Types**: Support for Toys, Books, and Video Games
- **Order Customization**: Add love messages and teddy bears to gifts using the Decorator pattern
- **Employee Management**: Automatic employee allocation with a maximum of 3 employees per order
- **Delivery Options**: Choose between Boat or Truck delivery methods using the Strategy pattern
- **Order Tracking**: Real-time order state updates with timestamps
- **Singleton Factory**: Ensures a single factory instance manages all employees and gifts

## Architecture Overview

The system implements several design patterns:

- **Factory Pattern**: `Factory` class creates different gift types based on order specifications
- **Singleton Pattern**: Factory instance is unique across the application
- **Strategy Pattern**: Pluggable delivery methods (Boat/Truck) through `Delivery_Context`
- **Decorator Pattern**: Dynamic gift customization via the `Custom` class

## UML Diagram

The UML diagram of the system shows class relationships and design patterns usage:

![UML Diagram](../src/UML.png)

You can also view the UML diagram [here](../src/UML.png) in the repository.

---

## Project Structure

```text
.
├── Interface.py           # Main CLI interface and entry point
├── Order.py               # Order management and workflow orchestration
├── Factory.py             # Singleton factory for gifts and employees
├── Custom.py              # Decorator for gift customizations
├── Delivery_Context.py    # Strategy context for delivery methods
├── Employee.py            # Employee model
├── Boat.py                # Boat delivery strategy
├── Truck.py               # Truck delivery strategy
├── Book.py                # Book gift type
├── Toy.py                 # Toy gift type
└── Video_Game.py          # Video game gift type
```

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd gift-factory
```

2. Ensure all Python files are in the same directory.

## Usage

Run the main interface:

```bash
python Interface.py
```

### Order Flow

1. Press `1` to create a new order.
2. Enter customer name.
3. Select gift type (1: Toy, 2: Book, 3: Video Game).
4. Choose whether to add a love message (yes/no).
5. Choose whether to add a teddy bear (yes/no).
6. Select delivery method (boat/truck).
7. The system will:
   - Assign up to 3 available employees.
   - Create the selected gift.
   - Apply customizations.
   - Simulate delivery with progress visualization.
   - Update order state with timestamps.
---

## Design Patterns Implemented

| Pattern    | Implementation              | Purpose                                                   |
|-----------|-----------------------------|-----------------------------------------------------------|
| Singleton | `Factory.__new__()`         | Ensures single factory instance managing all resources    |
| Factory   | `Factory.create_gift()`     | Encapsulates gift object creation logic                   |
| Strategy  | `Delivery_Context` + modes  | Allows runtime selection of delivery methods              |
| Decorator | `Custom.decoration()`       | Dynamically adds features (messages, bears) to gifts      |


## Contributors

- Lylyss97x