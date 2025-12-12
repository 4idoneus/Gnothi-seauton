# Snack Ver (Give Snack)
# 🤖 Smart Vending Machine (Automata Theory Project)

> A Cyber-Physical System (CPS) simulation modeled using Non-Deterministic Finite Automata (NFA).

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Educational-orange)
![Course](https://img.shields.io/badge/Course-Automata_Theory-green)

## 📖 Overview
This project models the operation of a **Smart Vending Machine** that integrates stock sensors and a refund mechanism to prevent user money loss. Unlike traditional machines that accept money blindly, this system uses a **Post-Select NFA** approach: it validates stock availability *before* accepting payment.

The project was developed as a term assignment for the **Automata Theory** course at **Manisa Celal Bayar University**.

## 🚀 Features
* **State-Aware Logging:** The console outputs the current Automata State (e.g., `[State: q_check]`, `[State: q_dispense]`) in real-time.
* **Cyber-Physical Simulation:** Models physical hardware components (Sensors, Cash Acceptor, Dispenser) as software objects.
* **Refund Mechanism:** Automatically cancels transactions and returns funds if stock runs out or the user cancels.
* **Recursive Payment Logic:** Handles partial payments and calculates change using recursive state transitions ($q_{owe}$).
* **Admin Panel:** Includes a maintenance mode to restock items and view financial reports.

## 📂 Project Structure

The codebase is modular, separating the Control Logic (Automata) from the Physical Logic (Hardware):

| File | Role | Description |
| :--- | :--- | :--- |
| `main.py` | **Controller** | The central processing unit. Manages the global state transitions ($q_0 \to q_{check} \to \dots$). |
| `money_handler.py` | **Validator** | Simulates the bill acceptor. Manages the "Owe" states and calculates change. |
| `snackbar.py` | **Actuator** | Represents the physical dispensing hardware and sensor checks. |
| `snacks.py` | **Database** | Stores product attributes (Price, Stock, Name). |

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.x installed on your machine.

### Running the Simulation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/4iodenus/Gnothi-seauton./snack-ver-project.git](https://github.com/4iodenus/Gnothi-seauton./snack-ver-project.git)
    cd smart-vending-machine
    ```
2.  Run the main controller:
    ```bash
    python main.py
    ```
3.  **Follow the on-screen instructions:**
    * Select an item (e.g., `water`, `protein bar`).
    * Watch the console logs to see the Automata States change.
    * Insert money (5, 10, 20, 50 TL) to complete the purchase.

## 🧠 Theoretical Model (NFA)

This software implements a **Post-Select Non-Deterministic Finite Automaton (NFA)**.

### Formal Definition
* **States ($Q$):**
    * `q0`: Idle / Selection State.
    * `q_check`: Sensor Verification State (checking stock).
    * `q_owe{X}`: Recursive Payment State (waiting for remaining amount $X$).
    * `q_dispense`: Final Acceptance State (giving item).
    * `q_cancel`: Refund / Rejection State.
* **Alphabet ($\Sigma$):** `{ Sel_Water, Sel_Cola, 5TL, 10TL, 20TL, 50TL, Sensor_OK, Sensor_Empty, ... }`

### Logic Flow
1.  **Selection:** User selects an item $\rightarrow$ Transition to `q_check`.
2.  **Sensing:** Machine checks `is_in_stock()`.
    * If `True` ($\text{Sensor\_OK}$) $\rightarrow$ Transition to `q_owe`.
    * If `False` ($\text{Sensor\_Empty}$) $\rightarrow$ Transition to `q_cancel`.
3.  **Payment:** Machine loops in `q_owe` until `balance >= cost`.
4.  **Completion:** Transition to `q_dispense`.

## 👥 Authors
* **[Aidoneus]** - ME

## 📜 License
This project is for educational purposes.