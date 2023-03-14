## Installation

### Creating Virtual Environment
```env
python -m venv myenv
```

### Activate Environment
```env
myenv\Scripts\activate
```

### Deactivate Environment
```env
deactivate
```
### RASA

Refer to official [installation guide](https://rasa.com/docs/rasa/user-guide/installation/) to install RASA

Rasa Installation

   ```python
   pip install rasa
   ```

### Commands to Use on Project

- #### Add -vv to any command to enter debug mode on teminal


1. Run actions.py file (in separate terminal)
    ```
    rasa run actions
    ```

2. Train model(Open another terminal)
    ```
    rasa train
    ```
3. Run chatbot
    ```
    rasa shell

        or

    rasa shell --endpoints endpoints.yml
    ```
4. Run interactive chatbot (for training purpose)
    ```
    rasa interactive

        or

    rasa interactive --endpoints endpoints.yml